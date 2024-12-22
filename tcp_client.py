import socket
import time
import random
from datetime import datetime


def send_data():
    # Создаем TCP-сокет
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаемся к серверу
    client.connect(('localhost', 12345))

    while True:
        # Генерируем случайное значение
        sensor_value = random.uniform(0, 100)

        # Получаем текущее время
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Формируем данные для отправки
        data = f"{current_time}, {sensor_value}"

        # Отправляем данные на сервер
        client.send(data.encode('utf-8'))
        print(f"Sent data: {data}")

        # Ждем 1 минуту
        time.sleep(60)


if __name__ == "__main__":
    send_data()