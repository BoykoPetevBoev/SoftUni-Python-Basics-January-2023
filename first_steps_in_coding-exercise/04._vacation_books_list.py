from math import floor

bookPages = int(input())
pagesPerHour = int(input())
days = int(input())

totalHours = (bookPages / pagesPerHour) / days

print(floor(totalHours))