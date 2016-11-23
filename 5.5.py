labor = 35

def main():
    square_feet = float(input('Enter the square feet of wall space to be painted: '))
    price = float(input('Enter the price of paint per gallon: '))
    gallonsRequired = int(square_feet / 112)
    laborRequired = int((square_feet / 112) * 8)
    laborCost = format(float(laborRequired * labor), '.2f')
    costPaint = price * gallonsRequired
    totalCost(laborCost, costPaint)

def totalCost(laborCost, costPaint):
    total = float(laborCost + costPaint)
    print(total)
main()
