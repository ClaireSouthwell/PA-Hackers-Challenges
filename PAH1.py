import sys

sample = sys.argv[1]
target = int(sys.argv[2])


# Pull integers from sample.txt into master list
master_list = []    
f = open(sample, "r")
for x in f:
    master_list.append(int(x))
f.close()

# Sort the list 
sorted_list = sorted(master_list)

# Use a for loop to test each number (a) for its corresponding addend (b)
for a in sorted_list:
    b = target - a
#    print("Testing number " + str(a) + " and looking for " + str(b))
    counter = 1
    testing_sample = sorted_list

# Use a binary search to narrow down b's location 
    while counter < 18:
        midpoint = len(testing_sample) // 2
        if testing_sample[midpoint] > b:
            testing_sample = testing_sample[:midpoint]
        else:
            testing_sample = testing_sample[midpoint:]
        counter += 1

# Check sample of ~4 numbers to see if b is there
# If it is, return a and b's indices from the master list 
    for item in testing_sample:
        if item == b:
            # print("I found " + str(b) + "!")
            print("The indices are " + str(master_list.index(a))
                    + " and " + str(master_list.index(b))) 
            sys.exit(0)
