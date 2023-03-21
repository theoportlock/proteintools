#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

def GenerateTimeLine(data, day_interval=5):
    ''' Makes a timeline based on a csv file with the first and second column being date and name respectively '''
    pd.plotting.register_matplotlib_converters()
    levels = [-5, 5, -3, 3, -1, 1]
    fig, ax = plt.subplots()
    start = data.index.max()
    stop = data.index.min()
    ax.plot((start, stop), (0, 0), 'k', alpha=.5)
    for ii, (idate, iname) in enumerate(data.itertuples()):
        level = levels[ii % 6]
        vert = 'top' if level < 0 else 'bottom'
        ax.scatter(idate, 0, s=100, facecolor='w', edgecolor='k', zorder=9999)
        ax.plot((idate, idate), (0, level), c='r', alpha=.7)
        ax.text(idate, level, iname, ha='right', va=vert, fontsize=14, backgroundcolor=(1., 1., 1., .3))
    plt.setp((ax.get_yticklabels() + ax.get_yticklines() + list(ax.spines.values())), visible=False)
    return ax

if __name__ == "__main__":
    df = pd.read_csv("testdata.csv", index_col="date", parse_dates=True, infer_datetime_format=True)
    GenerateTimeLine(df)
    plt.show()
