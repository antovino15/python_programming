# nums = [1,2,3,4,5,6,7,8,9,10]

# my_list= []

# for i in nums:
#     my_list.append(i)
# print (my_list)


# my_list =[i for i in nums]

# print (my_list)


# #n+n each items
# my_list= []
# for i in nums:
#     my_list.append(i*i)
# print (my_list)

# ##comprehension

# my_list = [i*i for i in nums]
# print (my_list)

# # all the even numbers in list
# my_list= []
# for i in nums:
#     if i%2 == 0:
#         my_list.append(i)
# print (my_list)

# comprehension
# my_list=[]
# my_list = [(i,j) for i in nums  for j in nums if i%2==0]
# print(my_list)

name1 = ['phy', 'che', 'mat', 'bio']
name2 =[12,13 ,14, 50]


my_list= [(i, j) for i,j in zip(name1, name2)]

print(my_list)
