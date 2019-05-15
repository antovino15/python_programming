# #Getting Input
# num = int(input("Enter The number: "))
# #Defing Factor
# Factor = 1
# for fact in range(1, num+1):
#     # print(num)
#     Factor *= fact
#     # print (Factor)
# print (f'Factorial of {num} is {Factor}')

#using function
def Factorial(num):
    if num == 0:
        return 1
    return num*Factorial(num -1)
# print('Enter the numer: ')
num = int(input('Enter the numer: '))

print (Factorial(num))
