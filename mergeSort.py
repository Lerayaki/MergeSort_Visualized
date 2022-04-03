import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np

class TrackedArray():
    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indexes = []
        self.values = []
        self.access_type = []
        self.full_copies = []
        self.full_copies.append(np.copy(self.arr))

    def track(self, index, access_type):
        self.indexes.append(index)
        self.values.append(self.arr[index])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))

    def getActivity(self, index=None):
        if index == None:
            return [ (i,a) for (i,a) in zip(self.indexes, self.access_type)]
        else:
            return (self.indexes[index], self.access_type[index])

    def __getitem__(self, index):
        self.track(index, 'get')
        return self.arr[index]

    def __setitem__(self, index, value):
        self.arr[index] = value
        self.track(index, 'set')
    
    def __len__(self):
        return len(self.arr)

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

    for i in range(len(aux)):
        arr[a+i] = aux[i]

def printProgressBar(iter, total, decimals = 1, prefix = '', suffix = '', length = 40, fill='█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iter / total))
    fillLength = length * iter // total
    bar = fill * fillLength + '-' * (length - fillLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    if iter == total:
        print()

def update(i=int):
    txt.set_text(f" Array accesses: {i}")
    for (rectangle, height) in zip(container.patches, arr.full_copies[i]):
        rectangle.set_height(height)
        rectangle.set_color("#b3b3b3")
    
    if i > 0:
        index, access_type = arr.getActivity(i-1)

        if access_type == 'get':
            container.patches[index].set_color("#1fa214")
        elif access_type == 'set':
            container.patches[index].set_color("#b02919")

    printProgressBar(i, total=len(arr.full_copies)-1, prefix='Progress', suffix='Completed', printEnd='')

    return (*container, txt)

#######################################

fps = 60
size = 256
arr = np.arange(1, size+1)
np.random.shuffle(arr)
arr = TrackedArray(arr)

# figure, axis = plt.subplots(1,2, figsize=(12,5))
# axis[0].bar(range(size), arr, width=1)

mergeSort(arr)

# axis[1].bar(range(size), arr, width=1)
# plt.show()


fig, ax = plt.subplots()
container = ax.bar(np.arange(len(arr)), arr, align="edge", width=1)
ax.set_xlim([-1,size])
ax.set_ylim([0,int(size*1.1)])
ax.set(xlabel="Index", ylabel="Value", title="Merge Sort")
txt = ax.text(0,int(size*1.05),"")

anim = ani.FuncAnimation(fig, update, frames=len(arr.full_copies), blit=True, interval=1000/fps, repeat=False)
# plt.show()
anim.save(f'mergeSort-{size}.gif', fps=min(50,fps))