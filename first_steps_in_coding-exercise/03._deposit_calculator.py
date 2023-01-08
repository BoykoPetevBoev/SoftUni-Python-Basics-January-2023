investedSum = float(input())
monts = int(input())
interestRates = float(input())

interestRatesProfit = investedSum * interestRates / 100
interestRatesMonthlyProfit = interestRatesProfit / 12
totalSum = investedSum + interestRatesMonthlyProfit * monts

print(totalSum)