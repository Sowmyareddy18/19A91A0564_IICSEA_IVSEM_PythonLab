'''
6.2)Implement a Python script to rotate list of elements towards right up to given number
of times. Example: Input: [23,34,9,45,19] and 2 (Hint: 2 indicates No.
of times to rotate) Output: [45,19,23,34,9]
'''
n=int(input("enter how many list of values"))
list=[]
r=int(input("enter number of times to rotate"))
for i in range(n):
    number=int(input())
    list.append(number)#appending numbers in to list DS
print(list)
list=(list[len(list)-r:len(list)]+list[0:len(list)-r])
print("list after rotating is",list)
'''
OUTPUT:
enter how many list of values5
enter number of times to rotate2
23
34
9
45
19
[23, 34, 9, 45, 19]
list after rotating is [45, 19, 23, 34, 9]
'''
      
