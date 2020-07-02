import matplotlib.pyplot as plt

# pie-chart

def makePie():
    lang = ["Java", "Python", "PHP", "Javascript", "C#"]
    pop = [22.2, 17.6, 8.8, 7.7, 6.7]
    col = ["r", "b", "k", "pink", "grey"]

    explode = [.5, .1, 0, 0, 0]

    plt.pie(pop, labels=lang, colors=col, shadow=True,explode=explode)

    plt.show()

def makeBar():
    lang = ["Java", "Python", "PHP", "Javascript", "C#"]
    pop = [22.2, 17.6, 8.8, 7.7, 6.7]
    col = ["r", "b", "k", "pink", "grey"]

    x_pos = range(1,6)

    plt.bar(x_pos, pop)
    plt.xlabel("Languages")
    plt.xlabel("Popularity (%)")
    plt.title("Popularity of Programming Languages")

    plt.xticks(x_pos, lang)

    plt.show()

if __name__ == "__main__":
    #makePie()
    makeBar()