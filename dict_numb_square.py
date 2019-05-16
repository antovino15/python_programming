# Creating dictory with number as key and square of it as value
num = int(input('Enter the number: '))
dict_num = {}
for i in range(1, num+1):
    dict_num[i] = i*i
    #dict[key] = value
print(dict_num)
