def monthly_payment(loan, annual_rate, years):
    r = annual_rate / 12
    payment = float((loan * r/(1-(1+r)**(-(years*12)))))
    return payment


def remaining_balance(loan, annual_rate, years, months_paid):
    r = annual_rate / 12
    p = monthly_payment(loan, annual_rate, years)
    balance = float(loan*((1+r)**months_paid)-(p * ((1+r)**months_paid-1))/r)
    return balance


