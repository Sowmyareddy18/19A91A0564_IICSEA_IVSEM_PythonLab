#Implement a python script to count number of words in a string and reverse each word in a string at the same location.
#Example: Input :Honesty is the best policy Output :5 ytsenoH si eht tseb ycilop.
s=input()
words=s.split(" ")
print(len(words))
revword=[word[::-1] for word in words]
reverse=" ".join(revword)
print(reverse)
'''
OUTPUT:
Honesty is the best policy
5
ytsenoH si eht tseb ycilop
'''
