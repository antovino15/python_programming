import re
# file_to_search = open('us-500.csv', 'r')
# print(file_to_search.readlines())
with open("us-500.csv") as f:
    for line in f:
        email_search = re.search(r'([\w.-]+@+[\w.]+)', line)
        print(email_search)
# file_to_search.close()
# Ned to save this output in csv file---tomorrow
