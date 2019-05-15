import sys
print (sys.version)
result = []
# for number in range(2000, 30001):
#     if (number%7==0) and (number%5!=0):
#         result.append(number)
#         # print(number, end = ", ")

first_number = int(input("Enter the starting number: "))
Last_number = int(input("Enter the last Number: "))

for number  in range(first_number, Last_number+1):
        if(number%5 == 0):
                print (number)