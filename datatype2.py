#tuple

#1
'''tup = ("shivangi",3.35,6)
len(tup)
print(len(tup))


#2
tup = ("zyz","to","splash","s")
a = max(tup)
b = min(tup)
print(a,b)


#3
tup = [2,4,5,6,7]
i = 0
mul = 1
for i in range (len(tup)):
    mul = mul*tup[i]
print(mul)


#set

#1
a = set([1,2,4,5])
b = set([2,3,5])
print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))'''


#dictionary

#1
import operator
for i in range (1, 11):




#2
sorted_d = sorted(d.item(),key = operator.itemgetter(0))
print('Sorted marks are : ',sorted_d)



#3
'''def count(str1):
    dict = {}
    for n in str1:
       keys = dict.keys()
       if n in keys:
           dict[n] += 1
       else:
           dict[n] = 1
    return dict
print(count('Mississippi'))'''
