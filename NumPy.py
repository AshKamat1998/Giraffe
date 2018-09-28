import numpy as np
import sys
from datetime import time

a = np.array([2, 3, 4])
print(a[0])
l=range(1000)
print(sys.getsizeof(5)*len(l))
array=np.arange(1000)
print(array.size*array.itemsize)

size=1000000
a1=np.arange(size)
a2=np.arange(size)
#start = time.time()
