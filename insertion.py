# CHAPTER 7 - SORTING ALGORITHMS 
# INSERTION SORT - page 90

# declaring a function to receive a list reference as input and return a sorted (by insertion) copy as output
def insertion_sort(array) :

    for index in range(1 , len(array)) :
        value = array [index]

        while array[index - 1] > value and index >= 1 :
            array[index] = array[index - 1]
            index -= 1 
            array[index] = value

        print('\tResolving elemnt[' , index , '] to' , array)
 

array = [ 5 , 3 , 1 , 2, 6, 4]
print('Insertion sort... \nArray :' , array)

insertion_sort(array)
print('Array :' , array)