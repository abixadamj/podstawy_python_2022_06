def avg_income(income, bonus=1.05, yearly_bonus=1.10):
    """Our function compute next payment based on some criteria"""
    avg = sum(income) / len(income)
    next_income = avg * bonus
    if len(income) >= 5:
        next_income = next_income * yearly_bonus
    return next_income


adam_income = [200, 400, 132, 34, 300, 230]
beata_income = [12.5, 33.6, 50]
bonus = 3.02

print(f"Next income for Adam: {avg_income(adam_income, 1.50)}")
print(f"Next income for Adam: {avg_income(beata_income, bonus)}")
