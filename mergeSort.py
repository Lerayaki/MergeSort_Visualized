import matplotlib.animation as ani
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np

def mergeSortSteps(a,b):
    global steps

    if (a == b):
        return
    
    mid = (b - a) // 2 + a
    steps.append([mid+1,b])
    mergeSortSteps(mid+1,b)
    steps.append([a,mid])
    mergeSortSteps(a,mid)

def merge(a,b):
    global y

    mid = (b - a) // 2 + a
    aux = []
    
    i = a
    j = mid+1

    while (i <= mid or j <= b):
        if i > mid:
            aux.append(y[j])
            j = j+1
            continue
        if j > b:
            aux.append(y[i])
            i = i+1
            continue
        if y[i] < y[j]:
            aux.append(y[i])
            i = i+1
        else:
            aux.append(y[j])
            j = j+1

    y[a:b+1] = np.array(aux)

def mergeSort(i=int):
    merge(steps[i][0], steps[i][1])
    fig.clear()
    p = plt.bar(x,y, align='edge', width=1.01)
    
#######################################

size = 1024
y = np.random.default_rng().uniform(0,1,size)
x = np.arange(size)

steps = [[0, size-1]]
mergeSortSteps(0, size-1)
steps.reverse()
print('size: ', len(steps))

fig = plt.figure()
animator = ani.FuncAnimation(fig, mergeSort, frames=len(steps), interval=0.2)

# plt.show()
animator.save(r'mergeSort-{}.gif'.format(size))