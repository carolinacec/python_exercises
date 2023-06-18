# Can you get the sum of all the negative numbers?

given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
totalneg = 0 

for i in given_list3:
    if i <= 0:
        totalneg += i
print(totalneg)


given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
totalneg = 0 
i = -1
while True:
    totalneg += given_list3[i]
    i -= 1
    if given_list3[i] > 0:
        break
print(totalneg)


    