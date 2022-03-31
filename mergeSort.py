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

def mergeSort():
    return

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

size = 200
y = np.random.default_rng().uniform(0,1,size)
x = np.arange(size)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,5))
axes[0].bar(x,y, align='edge', width=1)

steps = [[0, size-1]]
mergeSortSteps(0, size-1)
steps.reverse()
for step in steps:
    merge(step[0], step[1])

axes[1].bar(x,y, align='edge', width=1)

# plt.figure()
# plt.bar(x,y, align='edge', width=1)
# plt.title('Random numbers')
# plt.ylabel('values')
fig.tight_layout()
plt.show()




# plt.figure()
# plt.boxplot(index_stack, whis=1, showfliers=False, widths=1, medianprops=dict(linewidth=0), boxprops=dict(color="red"))
# plt.title('Merge Sort steps')
# plt.ylabel('ranges')
# plt.xticks(np.arange(0,len(index_stack),max(1,len(index_stack)/20)))
# plt.xlabel('step')
# plt.show()