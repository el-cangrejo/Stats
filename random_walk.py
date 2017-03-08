import matplotlib.pyplot as plt
from scipy.stats import uniform

def main():
    for j in range(50):
        path = [0]
        for i in range(1000):
            if uniform.rvs() > 0.5:
                path.append(path[i] + 1)
            else:
                path.append(path[i] - 1)

        plt.plot(path)
    plt.show()

if __name__ == "__main__":
    main()
