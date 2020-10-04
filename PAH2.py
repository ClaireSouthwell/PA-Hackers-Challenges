import sys

sample = sys.argv[1]
target = int(sys.argv[2])

# Pull integers from sample.txt into master_list
master_list = []    

with open(sample) as f:
    for x in f:
        master_list.append(int(x))


# sorted_list = sorted(master_list) // Replaced this with an insertion sort 

# Copy only numbers < target into sorted_list

sorted_list = []
for num in master_list:
    if num < target:
        sorted_list.append(num)

length = len(sorted_list) - 1 

# Use insertion sort to sort sorted_list

for i in range(1, len(sorted_list)):
    key = sorted_list[i]
    j = i - 1
    while j >= 0 and key < sorted_list[j]:
        sorted_list[j+1] = sorted_list[j]
        j -= 1
    sorted_list[j+1] = key
    

# Define binary search function

def binary_search(arr, start, end, a, b):

    if end >= start:
        mid = (end + start) // 2

        if arr[mid] == b:
            print(str(master_list.index(a))+ ', ' + str(master_list.index(b))) 
            sys.exit(0)

        elif arr[mid] > b:
            return binary_search(arr, start, mid - 1, a, b)

        else:
            return binary_search(arr, mid + 1, end, a, b)

# Loop through sorted_list 

for i in range(length):
    a = sorted_list[i]
    b = target - a
    binary_search(sorted_list, i, length, a, b)



# python3 PAH2.py sample.txt 1171827269


 #python3 PAH2.py sample.txt 1227075878 

