#calculat KNN
# import numpy as np
import math
ciarettes = [7,7,3,1]
wight = [70,40,40,40]
hartAttack = ["Bad", "Bad", "Good", "Good"]

c = int(input("Enter num of ciarettes: "))
w = int(input("Enter the wight: "))
D = []
# h =

for i in range(len(ciarettes)):
    d=math.sqrt((c-ciarettes[i])**2+(w-wight[i])**2)
    D.append(d)

m = min(D)
ind=D.index(m)
print("You are belong to ", hartAttack[ind])



"""
for i in range(len(ciarettes)):
#     D = math.sqrt((subtract(c,ciarettes)**2) + (subtract(w,wight)**2))
#     print(D)
    
    
    
    Distance = np.square((np.subtract(c,ciarettes)**2) + (np.subtract(w,wight)**2))
    print(Distance)

"""