# CHAPTER 7 - SORTING ALGORITHMS 
# PARTITIONING SORT - page 96/97

# declaring a function to receive a list reference as input and return a sorted (by quick sort) copy as output

def quick_sort(array) :
    if len(array) > 1 :
        pivot = int(len(array) -1)
        less = [] ; more = []

        for element in range (len(array)) :
            value = array[element]
            if element != pivot :
                if value < array[pivot] :
                    less.append(value)
                else :
                    more.append(value)
    

        quick_sort(less) ; quick_sort(more)
        print('\t Less :' , less , '\t Pivot :' , array[pivot] , '\t More :', more)
        array[:] = less + [array[pivot]] + more
        print('\t\t Merged : ' , array)

array = [ 5 , 3 , 1 , 2, 6, 4]
print('Quick sort... \nArray :' , array)
quick_sort(array)
print('\nArray :' , array)