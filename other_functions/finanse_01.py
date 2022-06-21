def avg_income(income, bonus=1.05):
    avg = sum(income) / len(income)
    next_income = avg * bonus
    return next_income


adam_income = [200, 400, 132, 34]
beata_income = [12.5, 33.6, 50]
bonus = 3.02

print(f"Next income for Adam: {avg_income(adam_income, 1.50)}")
print(f"Next income for Adam: {avg_income(adam_income, bonus)}")
