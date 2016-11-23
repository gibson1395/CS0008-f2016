def main():
    # Obtain all the information.
    loan = float(input('Enter your car payment: '))
    insurance = float(input('Insurance amount: '))
    gas = float(input('Enter monthly gas amount: '))
    oil = float(input('Enter monthly amount used on oil: '))
    tire = float(input('Enter amount spent on tires for the year: '))
    maintenance = float(input('Enter monthly maintenance cost: '))
    calc_monthly (loan, insurance, gas, oil, tire, maintenance)

def calc_monthly(loan, insurance, gas, oil, tire, maintenance):
    #calculate and print monthly cost.
    total_monthly_cost = loan + insurance + gas + oil + tire + maintenance
    print('This is the monthly cost: $',format(total_monthly_cost, ',.2f'), sep='')
    calc_annual(total_monthly_cost)

def calc_annual(monthly):
    #calculate and print annual cost.
    total_annual = monthly * 12
    print('This is the annual cost: $',format(total_annual, ',.2f'), sep='')

main()
