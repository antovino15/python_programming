#Getting Input
num = int(input("Enter The number: "))
#Defing Factor
Factor = 1
for fact in range(1, num+1):
    # print(num)
    Factor *= fact
    # print (Factor)
print(Factor) 