import subprocess
import time
# Создаем запрос в командной строке netsh wlan show profiles, декодируя его по кодировке в самом ядре
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')
# Создаем список всех названий всех профилей сети (имена сетей)
Wi_Fis = [line.split(':')[1][1:-1] for line in data if "Все профили пользователей" in line]
# Для каждого имени...
for Wi__Fi in Wi_Fis:
    # ...вводим запрос netsh wlan show profile [ИМЯ_Сети] key=clear
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', Wi__Fi, 'key=clear']).decode('cp866').split('\n')
    # Забираем ключ
    results = [line.split(':')[1][1:-1] for line in results if "Содержимое ключа" in line]
    # Пытаемся его вывести в командной строке, отсекая все ошибки
    try:
        print(f'Имя сети: {Wi__Fi}, Пароль: {results[0]}')
    except IndexError:
        print(f'Имя сети: {Wi__Fi}, Пароль не найден!')