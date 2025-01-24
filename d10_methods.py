# Numbers=[1,2,3,4,5,6]
# # print(max(Numbers))

# # map()
# def squareNumber(x):
#   return x**2

# squareNumberList=list(map(squareNumber,Numbers))
# print(squareNumberList)


# # filter()
# def checkNumbers(y):
#   if y%2==0:
#     # print(f"{y} is Even number")
#     return y
# result=list(filter(checkNumbers,Numbers))


# lamda function (anonymous function) same as arrow function javascript


# def squareNumber(i):return i**2
# res=squareNumber(10)

# print(res)


# squareNumber=lambda x:x**2
# res=squareNumber(2)
# print(res)

# numbers=[1,2,3,4,5,6]
# res1=list(map(lambda z:z**2,numbers))
# print(res1)


# Qno3:
# 3. Given a list of integers, filter out the odd numbers and then square the remaining even numbers. Use filter and map together with lambda functions.

# integers=[1,2,3,4,5,6,7,8,9]
# res=list(filter(lambda z:z%2==0,integers))
# print(res)
# res1=list(map(lambda i:i**2,res))
# print(res1)


# 4. Write a program that filters out words from a list that are palindromes using filter and a lambda function.
# words=['level','app','manam','apple','orange']
# palindromes=list(filter(lambda word:word==word[::-1],words))
# print(palindromes)




# 5. Given a list of numbers and a divisor, use filter and a lambda function to find all numbers in the list that are divisible by the divisor.

# numbers=[1,2,3,4,5,6,7,8,9,10]
# number=2
# result=list(filter(lambda num:num%number==0,numbers))
# print(result)



# 6. Write a program that filters out all empty strings from a list of strings using filter.
# name="ramesh"
# print(name.capitalize())
# print(name.upper())
# print(name.split(','))

# lst = [3, 1, 4, 1, 5]
# lst.append(9)          
# lst.sort()             
# lst.insert(2, 7)       
# lst.pop()              
         
# lst.reverse()          
# print(len(lst))
# print(lst.remove(5) )

# text = "Python is a great language"
# print(text.split())


# slicing

# lst = [10, 20, 30, 40, 50, 60]

# Basic slicing
# print(lst[1:4])         # [20, 30, 40] (from index 1 to 3)
# print(lst[:3])          # [10, 20, 30] (first 3 elements)
# print(lst[3:])          # [40, 50, 60] (from index 3 to the end)

# # Using step
# print(lst[::2])         # [10, 30, 50] (every second element)
# print(lst[1::2])        # [20, 40, 60] (every second element starting from index 1)

# # Negative slicing
# print(lst[-3:])         # [40, 50, 60] (last 3 elements)
# print(lst[:-3])         # [10, 20, 30] (everything except the last 3 elements)
# print(lst[::-1])        # [60, 50, 40, 30, 20, 10] (reversed list)

fruits=["ram","hari","shyam","banana"]
# print(fruits.index("banana"))

# fruits.append("holi")
# print(fruits)

# fruits.insert(2,"crime")
# print(fruits)

# print(fruits.pop())

# # fruits.remove("hari")
# fruits.sort()
# # print(fruits)
# print(fruits.count("ram"))
# fruits.reverse()


# print(fruits)

# nam = "my name is Ramesh"
# nam = nam.split()

# nam.reverse()
# result = " ".join(nam)
# print(result)

nam="my name is ramesh"
nam=nam.split()
nam.reverse()
res=" ".join(nam)
print(res)

print(type(res))