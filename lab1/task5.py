dist = int(input('Дистанция ')) / 100
cons = float(input("Потребление "))
cost = float(input('Цена '))

total_f = dist * cons
total_c = total_f * cost

print(f'Топливо: {total_f:.2f}')
print(f'Стоимоть: {total_c:.2f}')
