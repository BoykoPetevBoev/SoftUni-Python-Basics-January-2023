nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylonSum = (nylon + 2) * 1.5
paintSum = (paint * 1.1) * 14.5
thinnerSum = thinner * 5
bagSum = 0.4

totalSum = nylonSum + paintSum + thinnerSum + bagSum

masterSum = totalSum * 0.3 * hours

print(totalSum + masterSum)