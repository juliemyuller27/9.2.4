per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму, которую хотите положить под проценты ");
deposit = [float(money)*per_cent['ТКБ']*0.01,float(money)*per_cent['СКБ']*0.01,float(money)*per_cent['ВТБ']*0.01,float(money)*per_cent['СБЕР']*0.01]

print("Максимальная сумма, которую вы можете заработать — ",max(deposit))
