# CHAPTER 7 - SORTING ALGORITHMS 
# COPY SORT - page 86

# declaring a function to receive a list reference as input and return a sorted copy as output
def copy_sort(array) :
    
    copy = array[:]
    # new array to store th interted elements in order 
    sorted_copy = []

    while len(copy) > 0 : 

        # each value is popped off the list copy in sequence - to build the sorted version by appending each to the empty array
        minimum = 0
        for element in range(0 , len( copy )) :
            if copy[element] < copy[minimum] :
                minimum = element
        print('\tRemoving' , copy[minimum] , 'from' , copy)
        sorted_copy.append(copy.pop(minimum))


    return sorted_copy



array = [5,3,1,2,6,4]
print('Copy Sort \n Array')

print('Copy:',copy_sort(array))
print('Array:' , array)
