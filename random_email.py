# Creating Random Doamin
import random
import string
domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'live.com']
length = random.randint(5, 10)


def new_email(length=5, char=string.ascii_lowercase):
    length = random.randint(5, 10)
    name = ''.join(random.choice(char) for x in range(length))
    email = (name + '@' + random.choice(domain))
    print(email)
    # print(length)


Number_of_email = int(input("Enter number of emails you want: "))
for i in range(1, Number_of_email+1):
    new_email()
