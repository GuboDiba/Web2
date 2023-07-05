# write a python program to create a set of intergers and 
# then add a new element to the set use a function
def setIntergers(numbers):
    numb=list(numbers)
    numb.append(67)
    sety=set(numb)
    return sety
    
    
numbers={23,76,89,12,34,65}
print(setIntergers(numbers))