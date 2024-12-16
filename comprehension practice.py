#1 Find all of the numbers from 1-1000 that have a 3 in them
"""
print([n for n in range(1,1000) if '3' in str(n)])

#2 Count the number of spaces in a string

s=input(" Enter a string: ")
print(len([a for a in s if a==" "]))
"""
'''
#3 Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
# consonants vyanjan (a,e,i,o,u," ")
a= "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
print([k for k in a if k not in 'a,e,i,o,u," "'])

#4 Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)

my_list=['hi', 4, 8.99, 'apple', ('t,b','n')]
print(tuple((my_list.index(x),x) for x in my_list))

#5 Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
a=[1, 2, 3, 4]
b = [2, 3, 4, 5]
print([i for i in a if i in b ])

#6 Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
a= 'In 1984 there were 13 instances of a protest with over 1000 people attending'
print(a.split())
print([ int(i) for i in a.split() if i.isdigit()])

#7 Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
print(['Even' if i%2==0 else "Odd" for i in range(20)])

#8 Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
a = 1, 2, 3,4,5,6,7,8,9
b = 2, 7, 1, 12
print([(x,x) for x in a if x in b])

#9 Find all of the words in a string that are less than 4 letters
a=input("Enter a string: ")
print([i for i in a.split() if len(i)<4])
'''

#10 Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
print([n for n in range(1,100) if n % n == 0 if n > 9])

result = [number for number in range(1,100) if True in [True for x in range(2,10) if number % x == 0]]
print(result)
