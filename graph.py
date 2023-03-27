import matplotlib.pyplot as plt
import numpy as np

red_theme = ["indianred", "coral", "khaki", "orange", "bisque", "salmon", "firebrick", "red"]
blue_theme = ["powderblue", "cadetblue", "dodgerblue", "lightskyblue", "thistle", "mediumorchid", "plum", "royalblue"]


def transform(point, tMatrix):
    return [point[0] * tMatrix[0] + point[1] * tMatrix[1],
            point[0] * tMatrix[2] + point[1] * tMatrix[3]]


def is_invariant(pointA, pointB):
    return pointA[0] == pointB[0] and pointA[1] == pointB[1]


def create_plot(transformation, clarity, markerRanges, darkMode, colorChoice):
    if colorChoice == "b" or colorChoice == "blue":
        theme = blue_theme
    else:
        theme = red_theme

    clarity = 300
    markerRanges = 10
    darkMode = True

    color = 0

    if darkMode:
        plt.style.use('dark_background')

    plt.rcParams["figure.autolayout"] = True
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(10, 10), dpi=clarity)

    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.xticks(np.arange(-20, 21, step=1), fontsize='x-small')
    plt.yticks(np.arange(-20, 21, step=1), fontsize='x-small')

    if darkMode:
        plt.axvline(x=0, c="white", label="x=0", lw=1)
        plt.axhline(y=0, c="white", label="y=0", lw=1)
    else:
        plt.axvline(x=0, c="black", label="x=0", lw=1)
        plt.axhline(y=0, c="black", label="y=0", lw=1)

    plt.grid()

    for i in range(len(transformation)):
        transformation[i] = int(transformation[i])

    for x in range(-markerRanges, markerRanges + 1):
        for y in range(-markerRanges, markerRanges + 1):

            new_point = transform([x, y], transformation)
            xrange = [x, new_point[0]]
            yrange = [y, new_point[1]]
            dx = new_point[0] - x
            dy = new_point[1] - y

            if is_invariant([x, y], new_point):
                plt.plot(x, y, marker="x", markersize=7, markeredgecolor="red")
                continue

            color = (color + 1) % len(theme)

            plt.plot(x, y, marker="x", markersize=7, markeredgecolor="darkgrey")
            plt.arrow(x, y, dx, dy, color=theme[color], lw=0.5, head_width=0.1, head_length=0.1)

    plt.show()
