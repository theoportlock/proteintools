#!/usr/bin/env python

import matplotlib.pyplot as plt

def a(arr):
    out = []
    visited = {}
    for line in arr:
        list = line.split()
        id = list[0]
        if id == 'ATOM':
            type = list[2]
            if type == 'CA':
                residue = list[3]
                type_of_chain = list[4]
                atom_count = float(list[5])
                position = list[6:8]
                if atom_count >= 0:
                    if type_of_chain not in visited:
                        visited[type_of_chain] = 1
                        resi = []
                        for i in range(6,8):
                            resi.append(float(list[i]))
                        out.append(resi)
    return out

with open(input("input filename: ")) as df:
#    for i in a(df):
#        print(i)
    result = a(df)
    print(result)
    plt.plot(result)
    plt.savefig("testplot.png")
