import re
# file_to_search = open('us-500.csv', 'r')
# print(file_to_search.readlines())
# newfile = open('mailist.txt', 'w')
with open("us-500.csv") as f:
    for line in f:
        email_search = re.findall(r'([\w.-]+@+[\w.]+)', line)
        print(email_search)
        # email_list.append(email_search)
        # print(email_search)
        # newfile.write(str(email_search))
# file_to_search.close()
# Ned to save this output in csv file---tomorrow
# newfile.close()
# print(email_list)
