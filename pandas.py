import pandas as pd

x = {'client_id': [9002, 6722, 8799, 8737, 5208],
     'sex': [1, 1, 1, 0, 0],
     'wealth': ['medium', 'high', 'high', 'low', 'medium'],
     'age': [63, 54, 62, 54, 37]}
df = pd.DataFrame(x)

medium_35 = (df.query("wealth == 'medium' and age > 35"))
print(medium_35)