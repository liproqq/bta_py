import matplotlib.pyplot as plt
from pylab import randn

def makeScatter():
    x1 = randn(200)
    y1 = randn(200)
    x2 = randn(200)
    y2 = randn(200)
    plt.scatter(x1,y1, color='r',s = 100, label="dot1" )
    plt.scatter(x2,y2, color='c',s = 10, label="dot2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


def makeHisto():
    x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
    num_bins = 10
    n, bins, patches = plt.hist(x, num_bins, facecolor='blue',alpha=0.5)
    plt.show()
    print(f"n:{n}\nbins: {bins}\npatches: {patches}")

if __name__ == "__main__":
    makeHisto()