DEFAULT_PORT = 5050


def ask_port():
    while True:
        answer = input('Введите порт сервера, def для значения по умолчанию: ')
        if answer != 'def':
            try:
                port = int(answer)
            except ValueError:
                print('Некорректное значение у Вашего порта.')
            else:
                return port
        else:
            return DEFAULT_PORT
