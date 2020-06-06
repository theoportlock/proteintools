from Bio import SeqIO
import matplotlib.pyplot as plt
from collections import defaultdict

record = SeqIO.read('LspCPER_GST1.ab1', 'abi')
record.annotations.keys()
channels = ['DATA9', 'DATA10', 'DATA11', 'DATA12']
trace = defaultdict(list)
for c in channels:
    trace[c] = record.annotations['abif_raw'][c]

plt.plot(trace['DATA9'][2000:], color='blue')
#plt.plot(trace['DATA10'][2000:], color='red')
#plt.plot(trace['DATA11'][2000:], color='green')
#plt.plot(trace['DATA12'][2000:], color='yellow')
plt.show()
