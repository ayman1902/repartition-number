import  numpy as np
import matplotlib.pyplot as plt
def repartition(max):
    plt.axes(projection='polar')
    for j in range(0,max):
        plt.polar(j*(180/np.pi),j,'k.')
    for n in range(0,max+1):
        if n > 1:
            for i in range(2,n):
                if(n%i) == 0:
                    break
            else:
                    print(n)
                    plt.polar(n*(180/np.pi),n,'r.')
    plt.show()
repartition(18)