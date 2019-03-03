#%matplotlib online
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ['python', 'c++']
performance = [5, 20]
x_pos = np.arange(len(objects))




plt.barh(x_pos, performance, align='center', alpha = 0.5)
plt.yticks(x_pos, objects)
plt.xlabel('Usage')
plt.title('Hello wold')

plt.show()
