# CHAPTER 7 - SORTING ALGORITHMS 
# SELECTION  SORT - page 88

# declaring a function to receive a list reference as input and return a sorted copy as output
def selection_sort(array) :

    for index in range(0 , len(array)-1) :

        value = array [index]
        current = index

        for element in range()

        for index in range ((len(array)-1) -index) :
            if array[element] > array[element+1] :
                array[element] , array[element+1] = array[element+1], array[element]

                print('\tResolving element[' , element , '] to' , array)

array = [5,3,1,2,6,4]
print('Bubble Sort \n Array :')

bubble_sort(array)

print('Array :' , array)

