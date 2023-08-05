# Dmail contract sender | Dev: [@python_web3](https://t.me/python_web3)
[Dmail](https://mail.dmail.ai/): web3 почтовый сервис, а для нас +1 контракт в сети ZkSync и дешёвые транзакции.

Адрес получателя генерируется случайным образом.
Письма не отображаются в самом сервисе, но транзакции валидные и проходят успешно.

## Установка
1. [Скачиваем](https://www.python.org/downloads/) и устанавливаем Python.  
2. [Скачиваем](https://github.com/SomeWeb3/dmail_sender/archive/refs/heads/main.zip) и распаковываем проект.
3. ```pip install -r requirements.txt```

## Настройка
1. В `wallets.txt` закидываем приватники.
2. Редактируем файл `.env`.\
В `SLEEP_BETWEEN_WALLETS=` указываем границы случайной задержки между кошельками. \
В `RANDOM_WALLETS_ORDER=` `True` или `False`, отвечает за случайный порядок кошельков при выполнении.

## Запуск
1. ```python main.py```.