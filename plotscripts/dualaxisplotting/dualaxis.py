#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

def plot(df):
    fig, ax1 = plt.subplots()
    color = 'tab:blue'
    ax1.set_xlabel('Volume (ml)')
    ax1.set_ylabel('Absorbance (mAU)')
    ax1.plot(df['volume (ml)'],df['Absorbance (mAU)'],color=color)
    ax1.set_xlim(xmin=0)
    ax1.set_ylim(ymin=-34)
    ax1.tick_params(axis="y",labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:green'
    ax2.set_ylabel("Conc B (%)") 
    ax2.plot(df['volume (mL)'],df['Buffer B Concentration (%)'],color=color)
    ax2.set_ylim(ymax=100)
    ax2.set_ylim(ymin=-2)
    ax2.tick_params(axis='y', labelcolor=color)
    fig.tight_layout()

    plt.show()
    #plt.savefig('results.svg')

def main():
    directory = "2019-10-09 HRCTD HisTrap 3L prep.csv"
    df = pd.read_csv(directory)
    plot(df)

if __name__ == '__main__':
    main()
