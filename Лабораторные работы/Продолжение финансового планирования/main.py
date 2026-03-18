salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
spend_2= spend
for months in range(months):
     if spend_2 > salary:
         money_capital += spend_2- salary
         spend_2*= (1+increase)
         money_capital = round ( money_capital)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months+1} месяцев без долгов:", money_capital)
