# CHAPTER 7 - SORTING ALGORITHMS 
# BUBBLING SORT - page 87

# declaring a function to receive a list reference as input and return a sorted copy as output
def bubble_sort(array) :

    for index in range(len(array)) :

        for element in range ((len(array)-1) -index) :
            if array[element] > array[element+1] :
                array[element] , array[element+1] = array[element+1], array[element]

                print('\tResolving element[' , element , '] to' , array)

array = [5,3,1,2,6,4]
print('Bubble Sort \n Array :')

bubble_sort(array)

print('Array :' , array)

