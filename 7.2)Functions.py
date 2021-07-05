#Find mean, median, mode for the given set of numbers in a list
l=[1,2,3,4,5,5,6,7,7,8,9,9,1,1]
def mean(l):
    print(sum(l)/len(l))
def median(l):
    l.sort()
    n=len(l)
    if n%2==l:
        print(l[int(n-1)/2])
    else:
        s=l[int((n-1)/2)]+l[int(n/2)]
    print(s/2)
def mode(l):
    freq={}
    for i in l:
        freq.setdefault(i,0)
        freq[i]+=1
    highfreq=max(freq.values())
    highfreqlst=[]
    for i,freq2 in freq.items():
        if freq2==highfreq:
            highfreqlst.append(i)
    print(highfreqlst)
mean(l)
median(l)
mode(l)

'''
4.857142857142857
5.0
[1]
'''
