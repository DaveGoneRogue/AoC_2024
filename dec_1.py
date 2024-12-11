import pandas as pd

#df = pd.read_csv('resources/two_list.txt', header = None,sep='\t', lineterminator='\r')
df = pd.read_csv('resources/two_list.txt', header = None)

print(df.head)
