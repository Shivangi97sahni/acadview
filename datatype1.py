#1
n=int(input("enter a list"))
l=[]
l.append(n)
print(l)


#2
l=[1,2,3,4]
l.append(5)
print(l)


#3
l=[1,2,2,2,4]
a=l.count(2)
print(a)


#4
l = [3,7,5,4,1]
l.sort()
print(l)

#5
a = [1,3,8]
b = [2,4]
c = a+b
c.sort()
print(c)


#6
stack = [4, 1, 6, 3]
print(stack)
stack.append(7)
stack.append(4)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

from collections import deque
queue = deque([4, 1, 6, 3])
print(queue)
queue.append(7)
print(queue)
queue.append(4)
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)