# TCP Server and Client Homework
# 5.1 Homework, задача “минимум” (5 баллов)
# Реализовать TCP server (или UDP-server)

содержит реализацию TCP-сервера и TCP-клиента для выполнения домашнего задания.

## Описание задания

- **TCP-сервер**:
  - Принимает данные от клиента.
  - Сохраняет принятые данные в файл `sensor_data.txt`.

- **TCP-клиент**:
  - Раз в минуту отправляет данные (текущее время и случайное значение) на сервер.
  -- Формат данных: `"текущее время, случайное значение"`.
---

## Структура проекта

- `tcp_server.py` — сервер, принимающий данные от клиента.
- `tcp_client.py` — клиент, отправляющий данные на сервер.
- `sensor_data.txt` — файл, в который сервер сохраняет данные.
- `README.md` — описание проекта.

---

## Как запустить

1. Запуск:
   ```bash
   python tcp_server.py
   python tcp_client.py


