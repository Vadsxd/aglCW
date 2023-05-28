import matplotlib.pyplot as plt
from numpy import log2


def create_graphic(elements, times, structure, method, y_label="Time process"):
    plt.title(structure + " " + method + " Graphic")
    plt.xlabel("Number of elements")
    plt.ylabel(y_label)
    plt.scatter(elements, times, s=0.1)
    if structure == "RBT":
        a = (times[-1]+times[-2])/2/elements[-1]/log2(elements[-1])
        plt.scatter(elements, [a*x*log2(x) for x in elements], s=0.2)
        plt.plot(elements, [a*x*log2(x) for x in elements], color='orange')
    else:
        a = times[-1]/elements[-1]
        plt.scatter(elements, [a*x for x in elements], s=0.2)
        plt.plot(elements, [a*x for x in elements], color='orange')
    plt.savefig("Graphics/" + structure + "_" + method + ".png")
    plt.show()
