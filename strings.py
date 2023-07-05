from timeit import default_timer as timer

#ordered, immutable, text representation
my_string = "Hello World" 

#reversing a string using slices
def reverseString(a):
    reversedString = a[::-1]
    print (reversedString)
 
# reverseString(my_string)  

# reversing a string using for loops
# take input from the user
original_str = "Enter a string: "

# initialize an empty string to store the reversed string
reversed_str = ""

# loop through each character in the original string in reverse order
for i in range(len(original_str)-1, -1, -1):
    reversed_str += original_str[i]

# print the reversed string
print("Reversed string:", reversed_str)

def basicStringLoop(b):
    for i in b:
        print (i)

# basicStringLoop(my_string)

def removeWhitespace(c):
    cleaned = c.strip()
    print (len(my_string), len(cleaned))

# removeWhitespace(my_string)

def splitToList(d):
    splitted = d.split(",")
    print (splitted)

my_list = splitToList(my_string)
# my_list = my_list * 1000000

def joinList(e): #Joining a list using methods
    joined = ' '.join(e)
    # print (joined)

def joinList2(f, separator): #Joining a List without using methods
    joined = ""

    for i in range(len(f)):

        if i != 0:
            joined += separator
        # Append the current element to the joined string
        joined += str(f[i])
    # print (joined)

# joinList2(my_list, ',')

# start = timer()
# joinList(my_list)
# stop = timer()
# print(stop-start)

# start = timer()
# joinList2(my_list, ',')
# stop = timer()
# print(stop-start)