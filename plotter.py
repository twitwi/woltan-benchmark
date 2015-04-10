import numpy as np
import matplotlib.pyplot as plt

py_data=np.genfromtxt('Test.csv',delimiter=' ',comments='#')
cpp_data=np.genfromtxt('cpp.csv',delimiter=' ',comments='#')

plt.figure()

npdata=py_data[:,0:4]
cpdata=py_data[:,4:]

npdata[:,3]=npdata[:,3]-npdata[:,1] # max error
npdata[:,2]=npdata[:,1]-npdata[:,2] # min error

cpdata[:,3]=cpdata[:,3]-cpdata[:,1] # max error
cpdata[:,2]=cpdata[:,1]-cpdata[:,2] # min error

cpp_data[:,3]=cpp_data[:,3]-cpp_data[:,1] # max error
cpp_data[:,2]=cpp_data[:,1]-cpp_data[:,2] # min error

minimum=np.min([np.min(npdata[:,1]),np.min(cpdata[:,1]),np.min(cpp_data[:,1])])
minimum = minimum - 0.5*np.abs(minimum)
maximum=np.max([np.max(npdata[:,1]),np.max(cpdata[:,1]),np.max(cpp_data[:,1])])

#plt.figure()
plt.xlabel('Matrix dimension')
plt.ylabel('Elapsed time [s]')
plt.ylim(bottom=minimum)
plt.yscale('log', nonposy="clip")
plt.errorbar(npdata[:,0],npdata[:,1],yerr=[npdata[:,2],npdata[:,3]],color='red',marker="+",label='Numpy')
plt.errorbar(cpdata[:,0],cpdata[:,1],yerr=[cpdata[:,2],cpdata[:,3]],color='green',marker="x",label='Python/BLAS')
plt.errorbar(cpp_data[:,0],cpp_data[:,1],yerr=[cpp_data[:,2],cpp_data[:,3]],color='blue',marker="*",label='c++/BLAS')
plt.legend(loc='lower right')

plt.show()