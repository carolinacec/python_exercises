# Can you compute the sum of all multiples of 3, 5 that are less than 100?

totlsum3 = 0

for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        totlsum3 = totlsum3 + i
print(totlsum3)