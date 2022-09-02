print('Задача 1. Конвертация')
print('-----------------------------')

# При покупках за рубежом 
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например, 
# если купить что-то в евро, 
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
# 
# Напишите программу, 
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
# 
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

e = float(input('Введите стоимость покупки в евро: '))
e_s = 1.25
s_r = 60.87

# print('Цена в $ =', e * e_s)
print('Цена в R =', round((e * e_s) * s_r, 2))

print('-----------------------------')