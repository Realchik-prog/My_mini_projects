from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
from requests.exceptions import MissingSchema, Timeout, HTTPError, TooManyRedirects
import logging
from tkinter.filedialog import askdirectory
from tkinter import Tk
import json
from threading import Lock



while True:
    try:
        requests_count = int(input('Сколько ссылок вы хотите ввести?: '))
        if requests_count > 0:
            break
        raise ValueError
    except ValueError:
        print('Неправильный ввод')
        
urls = []
        
for index in range(1, requests_count + 1):
    url = input(f'[{index}/{requests_count}] Ссылка: ')
    urls.append(url)
    
processed = 0
Tk().withdraw()
directory = Path(askdirectory())
if not directory:
    print('Папка не выбрана. Выход')
    exit()
directory.mkdir(parents=True, exist_ok=True)
logging.basicConfig(format='%(message)s', level=logging.INFO, force=True)
processed_lock = Lock()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def get_extension(response_type: str) -> str:
    if response_type == 'text/html':
        return '.html'
    elif response_type == 'application/json':
        return '.json'
    elif response_type == 'text/plain':
        return '.txt'
    elif response_type == 'image/jpeg':
        return '.jpg'
    elif response_type == 'image/png':
        return '.png'
    elif response_type == 'image/gif':
        return '.gif'
    else:
        return '.bin'
    
def load_url(url: str) -> bool:
    global processed
    if not url.startswith(("http://", 'https://')):
        url = 'https://' + url
    logging.info(f'Загрузка {url}')
    name = url.split('://')[1].replace('/', '_').replace('.', '_').split('%')[0].strip('_')
    response = None
    message = None
    file_path = None
    success = False
    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        if response is None:
            message = 'Ответ не получен'
            return success
        response.encoding = response.encoding or 'utf-8'
        response_type = str(response.headers.get('content-type')).split(';')[0].strip()
        extension = get_extension(response_type)
        file = name + extension
        file_path = directory / file
        i = 0
        while file_path.exists():
            i += 1
            file = name + f'({i})' + extension
            file_path = directory / file
        if extension == '.json':
            with open(file_path, 'w', encoding=response.encoding) as f:
                json.dump(response.text, f)
        elif extension in ['.html', '.txt']:
            with open(file_path, 'w', encoding=response.encoding) as f:
                f.write(response.text)
        else:
            with open(file_path, 'wb') as f:
                f.write(response.content)
        success = True
    except MissingSchema:
        message = 'Некорректный URL'
    except Timeout:
        message = 'Превышено время ожидания ответа'
    except HTTPError:
        if response is not None:
            if response.status_code==403:
                message = 'Доступ запрещён (Ошибка 403)'
            elif response.status_code==404:
                message = 'Страница не найдена (Ошибка 404)'
            else:
                message = f'Статус: {response.status_code}'
    except ConnectionError:
        message = 'Ошибка соединения'
    except TooManyRedirects:
        message = 'Слишком много редиректов'
    except Exception as e:
        message = e
    finally:
        with processed_lock:
            processed += 1
            if success and file_path is not None and response is not None:
                logging.info(f'[{processed}/{requests_count}] Успешно: {url} ({response.status_code}) - ' + 
                                            f'{file_path.name} - {file_path.stat().st_size} байт')
            else:
                logging.error(f'[{processed}/{requests_count}] Ошибка: {url} - {message}')
    return success

bad_processed = 0
good_processed = 0

print(f'Загружаем {requests_count} URL...')
with ThreadPoolExecutor(max_workers=4) as executor:
    reports = list(executor.map(load_url, urls))
for is_success in reports:
    if is_success:
        good_processed += 1
    else:
        bad_processed += 1

print(f'Успешно: {good_processed}. Ошибок: {bad_processed}')
            
