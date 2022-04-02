import string
from timeit import repeat
from turtle import width
import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np

def mergeSort(arr, a=None, b=None):
    if a == None or b == None:
        a = 0
        b = len(arr)-1
    if a >= b:
        return
    
    mid = (b-a) // 2 + a

    mergeSort(arr, a, mid)
    mergeSort(arr, mid+1, b)

    i = a
    j = mid+1
    aux = []

    while (i <= mid or j <= b):
        if i > mid:
            aux.append(arr[j])
            j = j+1
        elif j > b:
            aux.append(arr[i])
            i = i+1
        elif arr[i] < arr[j]:
            aux.append(arr[i])
            i = i+1
        else:
            aux.append(arr[j])
            j = j+1

    arr[a:b+1] = np.array(aux)

    global states
    states.append(list(arr))
    
def update(i=int):
    global size
    plt.clf()
    p = plt.bar(range(size), states[i], width=1)
#######################################

size = 128
arr = np.arange(1, size+1)
np.random.shuffle(arr)
states = [list(arr)]

figure, axis = plt.subplots(1,2, figsize=(12,5))
axis[0].bar(range(size), arr, width=1)

mergeSort(arr)

axis[1].bar(range(size), arr, width=1)
plt.show()

fig = plt.figure()
animator = ani.FuncAnimation(fig, update, frames=len(states) , interval=50, repeat=False)

plt.show()
# # animator.save(r'mergeSort-{}.gif'.format(size))