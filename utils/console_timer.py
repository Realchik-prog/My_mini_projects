import threading
from time import time, sleep
import queue
from typing import Literal

class ConsoleTimer:
    def __init__(self) -> None:
        self.status: Literal['off', 'pause', 'on'] = 'off'
        self.count = 0
        
    def timer(self) -> None:
        while True:
            if self.status == 'on':
                start_time = time()
                sleep(0.05)
                self.count += time() - start_time
            elif self.status == 'off':
                self.count = 0
                break
            elif self.status == 'pause':
                resume = self.resume.get()
                if resume:
                    self.status = 'on'
        
    def setup(self):
        print('\nВы запустили приложение "Консольный таймер"\n')
        print('Для показа команд введите "commands"')

        while True:
            print()
            command = input('> ').strip().lower()
            print()
            if command == 'commands':
                print("""Команды:
        start - запуск таймера
        pause - пауза
        resume - возобновление таймера после паузы
        status - текущее состояние таймера
        stop - остановка таймера
        exit - завершение программы""")
                
            elif command == 'start':
                if self.status == 'off':
                    self.status = 'on'
                    self.timer_thread = threading.Thread(target=self.timer)
                    self.resume = queue.Queue()
                    self.timer_thread.start()
                    print('Таймер успешно запущен')
                else:
                    print('Таймер уже запущен')
                    
            elif command == 'pause':
                if self.status == 'on':
                    self.status = 'pause'
                    print('Таймер успешно остановлен')
                elif self.status == 'off':
                    print('Таймер ещё не запущен')
                elif self.status == 'pause':
                    print('Таймер уже остановлен')
                
            elif command == 'resume':
                if self.status == 'pause':
                    self.resume.put(True)
                    print('Таймер успешно возобновлён')
                elif self.status == 'off':
                    print('Таймер ещё не запущен')
                elif self.status == 'on':
                    print('Таймер ещё не остановлен')
                    
            elif command == 'status':
                if self.status == 'off':
                    print('Таймер не запущен')
                else:
                    time = round(self.count, 2)
                    minutes = round(time // 60)
                    seconds = time % 60
                    time = f'{minutes}:{seconds}'
                    if self.status == 'on':
                        print(f'Прошло: {time}')
                    elif self.status == 'pause':
                        print(f'Прошло: {time} (Приостановлен)')
                    
            elif command == 'stop':
                if self.status == 'off':
                    print('Таймер ещё не запущен')
                else:
                    self.status = 'off'
                    print('Таймер сброшен')
                    if self.status == 'pause':
                        self.resume.put(False)
                    
            elif command == 'exit' or command == '0':
                self.status = 'off'
                break
            
            else:
                print('Неизвестная команда')
            
if __name__ == "__main__":
    app = ConsoleTimer()
    app.setup()