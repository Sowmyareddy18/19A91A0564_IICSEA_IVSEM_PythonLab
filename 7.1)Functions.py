'''
7.1) Write a function ball_collide that takes two balls as parameters and computes if they
are colliding. Your function should return a Boolean representing whether or not the
balls are colliding. Hint: Represent a ball on a plane as a tuple of (x, y, r), r being the
radius If (distance between two balls centers) <= (sum of their radii) then (they are
colliding).
'''

def ballcollide(x1,y1,r1,x2,y2,r2):
    d=dist(x1,y1,x2,y2)
    sum_of_radius=r1+r2
    if d==sum_of_radius:
        print("colliding")
    else:
        print("not colloding")
def dist(x1,y1,x2,y2):
    return (((x2-x1)+(y2-y1))**0.5)
    
ballcollide(2,2,1,4,4,1)#colliding
ballcollide(2,3,4,5,6,7)#not colloding
