#def getting_mad(arr):
    
mad = 10000

t = 10000

arr = [-10, -3, 0, 1] 

for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            if arr[i] - arr[j] >= 0:
                t = arr[i] - arr[j]
            if t < mad:
                mad = t

print(mad) 
                    
#    return mad
