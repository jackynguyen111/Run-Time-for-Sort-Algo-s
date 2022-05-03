# Analysis of Algorithms - CSCI 323
# Assignment #2
# Jacky Nguyen
# Tim Sort (https://www.geeksforgeeks.org/timsort/)
# Bubble Sort (https://www.geeksforgeeks.org/bubble-sort/)
# Selection Sort (https://www.geeksforgeeks.org/selection-sort/) 
# Insertion Sort (https://www.geeksforgeeks.org/insertion-sort/)
# Cocktail Sort (https://www.geeksforgeeks.org/cocktail-sort) 
# Shell Sort (https://www.geeksforgeeks.org/shellsort/) 
# Merge Sort (https://www.geeksforgeeks.org/merge-sort/) 
# Quick Sort (https://www.geeksforgeeks.org/quick-sort/) 
# Heap Sort (https://www.geeksforgeeks.org/heap-sort/) 
# Counting Sort (https://www.geeksforgeeks.org/counting-sort/) 
# Bucket Sort (https://www.geeksforgeeks.org/bucket-sort-2/)
# Radix Sort (https://www.geeksforgeeks.org/radix-sort/) 
# https://www.geeksforgeeks.org/python-check-if-list-is-sorted-or-not/
import math
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import sys
import copy
from numpy import *  

def random_list(range_max, size):
  arr = [random.randint(1, range_max) for i in range(size)]
  return arr


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        
        for j in range(0, n-i-1):
          
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
            
       
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertionSort(arr):
  for i in range(1, len(arr)):
        key = arr[i]
       
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def cocktailSort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1

def shellSort(arr):
    gap = len(arr) // 2 
    while gap > 0:
        i = 0
        j = gap
         
        while j < len(arr):
            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
             
            i += 1
            j += 1
            k = i
            while k - gap > -1:
                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                k -= 1
        gap //= 2
        

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def partition(start, end, array):
    
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
    
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
            
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            end -= 1
        
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
    
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
   
    # Returning end pointer to divide the array into 2
    return end
    
def quick_sort_rec(start, end, array):

    if start < end:

        p = partition(start, end, array)

        quick_sort_rec(start, p - 1, array)
        quick_sort_rec(p + 1, end, array)


def quick_sort(arr):
    quick_sort_rec(0, len(arr) - 1, arr)
        



def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2     
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)




def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
        
        
        

def countSort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr


def insertionSo(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    

def bucketSort(arr):
    noOfBuckets = 10
    max_ele = max(arr)
    min_ele = min(arr)
 
    # range(for buckets)
    rnge = (max_ele - min_ele) / noOfBuckets
 
    temp = []
 
    # create empty buckets
    for i in range(noOfBuckets):
        temp.append([])
 
    # scatter the array elements
    # into the correct bucket
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)
 
        # append the boundary elements to the lower array
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
 
        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])
 
    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
 
    # Gather sorted elements
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1


 
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10

def nativeSort(arr):
  return arr.sort()

def sortedList(test_list):
# using sort() to 
# check sorted list 
  flag = 0
  test_list1 = test_list[:]
  test_list1.sort()
  if (test_list1 == test_list):
    flag = 1

def plot_times_line_graph(dict_sorting):
    for sort in dict_sorting:
        x = dict_sorting[sort].keys()
        y = dict_sorting[sort].values()
        plt.plot(x, y, label=sort)
    plt.legend()
    plt.title("Run Time of sort Algorithms")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time for 100 Trials")
    plt.savefig("sort_graph.png")
    plt.show()


def plot_times_bar_graph(dict_sorting, sizes, sorting):
    sort_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])

    for sort in sorting:
        sort_num += 1
        d = dict_sorting[sort.__name__]
        x_axis = [j + 0.05 * sort_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        plt.bar(x_axis, y_axis, width= 0.05, alpha=0.25, label=sort.__name__)
    plt.legend()
    plt.title("Run Time of Sorting Algorithms")
    plt.xlabel("Different Sizes")
    plt.ylabel("Time for # Trials")
    plt.savefig("sorting_graph.png")
    plt.show()


def main():
    range_max = 100
    trials = 3
    dict_sorting = {}
    sorting = [nativeSort, bubbleSort, selectionSort, insertionSort, cocktailSort, shellSort, mergeSort, quick_sort, heapSort, countSort, bucketSort, radixSort]
    for sort in sorting:
        dict_sorting[sort.__name__] = {}
    sizes = [10, 100, 1000]
    for size in sizes:
        for sort in sorting:
            dict_sorting[sort.__name__][size] = 0
        for trial in range(1, trials):
            arr = random_list(range_max, size)

            for sort in sorting:
                arr2 = arr.copy()
                start_time = time.time()
                idx = sort(arr2)
                end_time = time.time()
                net_time = end_time - start_time
                dict_sorting[sort.__name__][size] += net_time * 1000
                #print(sort.__name__, sort(arr), "in time", net_time)
                #error check
                #if (sortedList != idx):
                 # print("Error in sort", sort.__name__, sortedList , idx)
                #if arr != idx:
                 # print("Error in sort", sort.__name__, idx, arr)
    # print(dict_sorting)
    # print("{:<20} {:<20}".format('sort', 'Time'))
    # for n, t in dict_sorting.items():
    # print("{:<20} {:<20}".format(n, round(1000 * t/trials, 4)))
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    df = pd.DataFrame.from_dict(dict_sorting).T
    print(df)
    # plot_times_line_graph(dict_sorting)
    plot_times_bar_graph(dict_sorting, sizes, sorting)


if __name__ == '__main__':
    main()