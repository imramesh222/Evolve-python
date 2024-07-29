fruits=['apple','orange','banana']
print(fruits)

# # methods
# # insert,len,append,index,pop,reverse,extend,count,clear
# # len()
# print(len(fruits))
# # index
# print(fruits.index('banana'))

# # append add from last
# fruits.append('orange')
# print(fruits)

# # insert
# fruits.insert(2,'mango')
# print(fruits)

# # pop
# print(fruits.pop())
# print(fruits.pop(2))
# print(fruits)

# # remove
# fruits.remove('banana')
# print(fruits)

# newFruits=fruits.copy()
# print(f'new fruits is {newFruits}')

# # append
# fruits.append('mango')
# fruits.append('kiwi')
# fruits.append('pineapple')
# fruits.append('grapes')

# # sort
# # fruits.sort(reverse=False)
# # print(fruits)

# fruits.reverse()
# print(fruits)

# numbers=[1,2,3,4,3,3,4]
# fruits.extend(numbers)
# print(fruits)

# # count
# print(fruits.count(3))

# print(fruits[2])
# print(fruits[1:5])
# print(fruits[-1:-8])

print(fruits)

fruits[2]=10
print(fruits)

print(fruits.index('apple'))

fruits.clear()
print(fruits)