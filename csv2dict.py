import csv
from itertools import groupby
from operator import itemgetter


# def group_dict(school):
#     return school[sub_location]


with open('Schools - Kindergartens.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['Name'])

    # next(csv_reader)
    # with open("new_csv.csv")
# for key, items in groupby(csv_reader, itemgetter(0)):
#     print(key)
#     for value in items:
#         print(value)
# print('-'*20)
