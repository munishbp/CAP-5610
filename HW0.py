import numpy as num
import matplotlib.pyplot as plt




def g_distribution(samples:int):
    data: num.ndarray=num.random.multivariate_normal([0,0],[[1,0],[0,1]],samples)

    plt.scatter(data[:,0],data[:,1])

    plt.show()









def main():
    g_distribution(100)


if __name__ == "__main__":
    main()