import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
print('❌ Генератор BTC чеков')
print('❌ Скрипт написан для канала ТЕНЕВОЙ БИЗНЕС')
print('❌ Автор: t.me/resilents | Наши проекты: t.me/shadowbiznes')
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print()
print('[BTCCheckGen] Выберите для какого бота генерировать чеки:')
print()
print('1️⃣ BTC_EXCHANGE_BOT')
print('2️⃣ CHATEX_BOT')
print()
inp = input("[BTCCheckBot] Ваш выбор: ")
Print()

if inp == '1':

number = input('[BTCCheckGen] ➕ Укажите желаемое количество ссылок для генерации:'+ "\n")
print(' ')
length = input('[BTCCheckGen] ➕ Укажите длинну чека (советуем ввести 32):'+ "\n")
print(' ')
number = int(number)
length = int(length)
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
print('[BTCCheckGen] ✅ Работа скрипта успешно завершена: ', number, ' чеков сгенерировано.')
print('[BTCCheckGen] ⚠️ ВНИМАНИЕ: Скрипт генерирует рандомные чеки, проверять на валидность придется вручную.')
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print('https://t.me/BTC_CHANGE_BOT?start=b_',password)
print(' ')
print('[BTCCheckGen] ℹ Все новости и обновления скрипта в нашем телеграм канале, подпишись и не пропускай новые плюшки.')
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')

elif inp == '2':

number = input('[BTCCheckGen] ➕ Укажите желаемое количество ссылок для генерации:'+ "\n")
print(' ')
length = input('[BTCCheckGen] ➕ Укажите длинну чека (советуем ввести 32):'+ "\n")
print(' ')
number = int(number)
length = int(length)
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
print('[BTCCheckGen] ✅ Работа скрипта успешно завершена: ', number, ' чеков сгенерировано.')
print('[BTCCheckGen] ⚠️ ВНИМАНИЕ: Скрипт генерирует рандомные чеки, проверять на валидность придется вручную.')
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print('https://t.me/BTC_CHANGE_BOT?start=b_',password)
print(' ')
print('[BTCCheckGen] ℹ Все новости и обновления скрипта в нашем телеграм канале, подпишись и не пропускай новые плюшки.')
print(' ')
print('➖➖➖➖➖➖➖[ BTCCheckGen 1.1 ]➖➖➖➖➖➖➖')
print(' ')


else:
    print("[ProxyGo] ⛔ Произошла ошибка! Повторите попытку.")
toexit = input("[ProxyGo] ⚠️ Нажмите любую клавишу для завершения.")
