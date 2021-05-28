#Implement a python script to count frequency of characters in a given string.
s=input('Enter a string: ')
a={} #used to define a dictionary
for i in set(s):
    a[i]=s.count(i) #number of substrings in the given string
print(a)
'''
OUTPUT:
Enter a string: aditya
{'t': 1, 'a': 2, 'y': 1, 'd': 1, 'i': 1}
'''
