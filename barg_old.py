from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'axes.grid' : False})
def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    
    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw legend if we need
    if legend:
        ax.legend(bars, data.keys(),fontsize = 15)


if __name__ == "__main__":
    data = {
        "South Africa": [13],
        "India": [9],
        "Germany": [8],
        "Poland, Romania": [4],
        "United States,Indonesia,Philippines":[3],
        "Hungary,Norway,France": [3],
        "Bangladesh, Denmark, Saudi Arabia":[2], 
        "Spain, Argentina, Netherlands, Canada, Brazil": [2],
        "Colombia, Azerbaijan, Austria, Chile, Estonia": [1],
        "Malaysia, Iran, Guatemala, Kosovo, Canadia, Greece":[1],
        "Czech, Moldova, Italy, Slovakia, Portugal, Russia, Yugoslavia":[1], 
        "Slovenia, England, Lithuania, Finland, Iraq, Tunisina, Hungary": [1],
        
    }    			

    #plotting the bar graph
    fig, ax = plt.subplots()
    x = np.array([0,1,2,3,4,5,6])
    bar_plot(ax, data, total_width=.8, single_width=.9)
    plt.yticks(np.arange(0, 14, step=2),fontsize=20)
    plt.xticks(fontsize = 0)
    plt.ylabel("Number of Entries",fontsize = 28)
    plt.xlabel("Countries",fontsize = 28)
    plt.title("Number of entries per country distribution", fontsize = 28)
    #plt.savefig('Bar_SMS.png')
    plt.show()