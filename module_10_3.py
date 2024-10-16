import threading
import random
import time
from threading import Thread, Lock


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
        x = random.randint(50, 500)
        self.balance += x
        print(f'Поплнение: {x}. Баланс: {self.balance})')
        time.sleep(0.001)

    def take(self):
        for i in range(100):
            y = random.randint(50, 500)
            print(f'Запрос на {y}')
            if y <= self.balance:
                self.balance -= y
                print(f'Снятие: {y}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bank = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bank,))
th2 = threading.Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bank.balance}')
