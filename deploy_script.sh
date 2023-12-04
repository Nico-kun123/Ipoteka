#!/bin/bash

# Обновление кода из репозитория
git pull origin main

# Установка зависимостей (если необходимо)
python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt

# Запуск программы с передачей аргументов
python3 ipoteka.py 100000 5 30 fixed 100