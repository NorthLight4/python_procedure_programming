money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
monthsAmount = 0
while money_capital > spend:
    monthsAmount += 1
    money_capital += salary
    money_capital -= spend
    if monthsAmount != 1:
        spend *= (1+increase)
print("Количество месяцев, которое можно протянуть без долгов:", monthsAmount)
