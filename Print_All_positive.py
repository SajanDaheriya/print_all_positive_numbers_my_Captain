numbers = input('Enter all numbers(comma seperated): ')   # taking input for list1
list1 = numbers.split(',')   # Assigning input numbers to a list
list2 = []  # output list
for num in list1:
    if int(num)>=0:
        list2.append(int(num))  # checking condition and appending to output list
    else:
        continue
print(list2)
