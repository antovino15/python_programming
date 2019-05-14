s1 = {1,2,3,4,5,1,2,3,6}
print(s1)

s1.add(7)
print(s1)

s1.update([8,9,0])
s1.remove(5)
#remove items without showing error if not present in set
s1.discard(5)
print(s1)

s2={5,6}
s3={8,6,5,3}

s4= s1.intersection(s2,s3)
print(s4)


s4= list(s1.difference(s2,s3))
print(s4)

