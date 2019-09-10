# Ler um arquivo com Python puro

file = open('data.csv', 'r')
# content_str = file.read() # str
content_list = file.readlines() # list
file.close()

with open('data.csv', 'r') as file:
    # content_str = file.read() # str
    content_list = file.readlines() # list



# Ler um arquivo com a lib CSV

import csv

with open('data.csv', 'r') as file:
    file_csv = csv.reader(file, dialect='excel')
    # print(file_csv)

    # for row in file_csv:
    #     print(row)




# Ler um arquivo com a lib Pandas

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')

uf_list = data.uf_busca.unique()

total_list = []
for uf in uf_list:
    total_list.append(data[data['uf_busca']==uf].uf_busca.count())

# Fixing random state for reproducibility
np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
y_pos = np.arange(len(uf_list))
error = np.random.rand(len(uf_list))

ax.barh(y_pos, total_list, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(uf_list)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Total de Campi')
ax.set_title('Relação de campus por estados do Brasil')

plt.show()
