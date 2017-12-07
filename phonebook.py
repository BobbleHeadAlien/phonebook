# The first file i sent had a bug in it. Kindly consider this file instead of the previous file.

#! Python3
# Program to store telephone data and display required contact list.
# Given data for the problem is preloaded, But additional input can be given.

# Input data
phonebook = {'Einstein' : 1234567896, 'Newton' : 2478965782, 'Alexander' : 9876543216}
n = int(input("Please enter the number of contacts to be uploaded (Ex:3): (Or enter '0' to continue)"))

# Storing values and extraction of required data                        
for i in range(n):
    print ("please enter Name " + str(i+1) +  " and Phone number seperated by a space:")
    new = input().upper().split()     #split the input text based on space & store in the list 'new'
    phonebook[new[0]] = new[1]               #assign the 1st item to key and 2nd item to value of the dictionary

# Printing the required output
while 1:
    a = input("Enter the search term for the names you are looking for: ").upper()
    if str(a) != '0':
        search = {k: v for k, v in phonebook.items() if k.startswith(str(a))} # Searching using given data
        print ("The contacts related to your search term are: " + str(search))
    elif str(a) == '0':
         print ("Successfully exited the phone book!")
         break
# Printing the required output

