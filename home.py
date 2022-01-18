from copy import copy
from math import floor
#importing math module
def Gohome(list, count, start):
    """function to determine the number of people to home 
    it takes three argument a list of people, the number to stop count, what position to start.
    it returns the set of people to go home
    """
    start-=1
    off_list = []
    ordered_list = list.copy()
    #copying the list into another 
    ordered_list.sort()
    #sorting the new list
    r = floor(len(ordered_list)/2)
    #calculating the number of pple going home to nearest smallest number
    for i in range(r):
        if count+start < len(ordered_list):
            off_list.append(ordered_list.pop(count+start))
        else: 
            off_list.append(ordered_list.pop((count+start)-len(ordered_list)))
        #condition for who get appended to off_list
        start=count+start
        #incrementing the start to the next person in the circle
    return(off_list)
 
r= Gohome([1, 2, 3, 4, 5], 2, 1)
#test sample
print(r)