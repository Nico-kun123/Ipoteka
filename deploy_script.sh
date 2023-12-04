#!/bin/bash

# Обновление кода из репозитория
git pull origin main

# Установка зависимостей (если необходимо)
python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt

# Запуск программы
python3 your_program.py