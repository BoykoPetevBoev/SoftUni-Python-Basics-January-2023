pencils = int(input())
markers = int(input())
preparation = int(input())
discount = int(input())

totalSum = pencils * 5.8 + markers * 7.2 + preparation * 1.2
discountPercentage = 1 - discount / 100

total = totalSum * discountPercentage

print(total)