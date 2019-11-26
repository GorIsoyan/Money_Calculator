def setupinitialMoney():
    money = int(input("Insert the initial balance above 0: "))
    while money<0:
        print ("Please, insert balance above 0")
        money = int(input("Insert the initial balance above 0: "))
    else:
        return(money)
    
def setupPercent():
    percentage = int(input("Insert the percentage without % sign: "))
    return(percentage)

def setupYears():
    years = int(input("Insert value of years between 0 and 20: "))
    while years < 0 or years >20:
        print("Please, insert a positive number")
        years = int(input("Insert value of years between 0 and 20: "))
    else:
        return(years)
    
def calculateTheResultMoney(initialMoney, percentage):
    i = (percentage/100)+1
    value = initialMoney *i
    return(value)

def main():
    print("This app will calculate the amount of money you will have in your account depending on the inserted data")
    initialMoney = setupinitialMoney()
    percent = setupPercent()
    years = setupYears()
    x = initialMoney
    y = years
    while (years>0):
        result = calculateTheResultMoney(initialMoney, percent)
        years=years-1 
    print ("After", y, "years, your", y, "balance turn to", result)
main()
