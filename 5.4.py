def main():
    loan = float(input('Enter your monthly car payment: '))
    insurance = float(input('Enter your monthly insurance payment: '))
    gas = float(input('Enter monthly amount spent on gas: '))
    oil = float(input('Enter the monthly amount spent on oil: '))
    tires = int(input('Enter the monthly cost spent on tires: '))
    maintenance = float(input('Enter the monthly amount spent on maintenance: '))
    calc_monthly(loan, insurance, gas, oil, tires, maintenance)

def calc_monthly(loan, insurance, gas, oil, tires, maintenance):
    total_monthly_cost = loan + insurance + gas + oil + tires + maintenance
    print('The monthly cost of your expenses are', total_monthly_cost)
    calc_year(total_monthly_cost)

def calc_year(total_monthly_cost):
    year = total_monthly_cost * 12
    print('The yearly cost of your expenses are', year)

main()


