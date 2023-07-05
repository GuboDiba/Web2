# //Write a Python program to count the number of items in a dictionary that have a 
# value greater than a certain number.

# my-dict={"Apple":5,"mango":3,"orange":7,"banana":2}
# value=2
# count=len([x for x in my-dict.values()if x<value])
# print(count)

# No 1
# Write a program that uses a tuple to represent a person's name, age, 
# and gender, and then prints out a message that says "Hello, 
# my name is [name], I am [age] years old, and I am [gender]."
def names():
  x="Gubo"
  b=30
  c="Female"
  print(f"Hello my name is {x},i am a {c} and i am {b} years old")
names()

# No 2
#Write a program that creates a dictionary of English words 
# and their corresponding definitions, and then prompts the user to enter a word 
# and prints out its definition (if it exists in the dictionary).


# No 3
# Write a function that takes a list of numbers as input and returns
# a new list with all duplicate numbers removed.

numbers=[2,6,1,6,4,2]
def duplicate(num):
     return list(set(num)) 
print(duplicate(numbers))

# No 4
# score =int(input("Enter your score"))

# if score>=50:
#     print("You have passed the exams")
#     print("Congratulations")
# else:
#     print("failed") 
    
  # 5
  # Write a function that takes two numbers as input and returns their sum.
def sum():
  m=3
  n=4
  return(m+n)
print(sum())

# 6
# Write a function that takes a string as input and returns the length of the string.
def stringLength():
    String="AkiraChix"
    return(len(String))
print(stringLength())    

# 7
# Write a function that takes a list of numbers as input and returns the average of the numbers.
# def listNum():
  
#   list=[2,3,4,5,6,7,8]
#   average= sum(list) / len(list)
#   # return average
# print(average)

# 8
# Write a function that takes a list of numbers as input and 
# returns the maximum number in the list.
def maxNum(): 
  list=[2,3,4,5,6,7,8]
print(" max.list)