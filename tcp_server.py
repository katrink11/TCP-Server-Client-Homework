import socket
import threading


# Функция для обработки клиента
def handle_client(client_socket):
    while True:
        # Принимаем данные от клиента
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received data: {data}")

        # Сохраняем данные в файл
        with open("sensor_data.txt", "a") as file:
            file.write(data + "\n")

    client_socket.close()


def start_server():
    # Создаем TCP-сокет
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Разрешаем повторное использование порта
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Привязываем сервер к порту 12345
    server.bind(('0.0.0.0', 12345))
    server.listen(5)  # Максимум 5 клиентов в очереди
    print("Server is listening on port 12345...")

    while True:
        # Принимаем соединение от клиента
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        # Создаем поток для обработки клиента
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()