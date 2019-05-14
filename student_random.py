

name = ['vino', 'anto', 'rhema', 'shan']
marks = [50, 40, 60, 81]
sname = ['abe', 'abt', 'alo', 'bai']
# abc= [[i,j] for i, j in zip (name, marks) if j>80]
# print (abc)

# abc= [(i,j) for i, j in zip(name, marks) if j in range(50, 60)]
# print (abc)

# for i in name:
#     for j in sname:
#         print(i,j)

# abc = [(i,j) for i in name for j in sname]
# print(abc)

name_vow= 'sadfsdfasffawerwr'

# for i in name_vow:
#     if i in 'aeiou':
#         print (i)
abc= [i for i in name_vow if i in 'aeiou']
print (abc)
