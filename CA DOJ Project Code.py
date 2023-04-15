import pandas as pd
import numpy as np
"""
data1 = pd.read_csv('1985 to 1994 crime.csv').transpose()
data1.columns = data1.iloc[0]
data1 = data1.tail(-1)
data1 = data1.reset_index(drop=False)
data1 = data1.rename(columns={'index':'Year'})
print(data1)

data2 = pd.read_csv('1993 to 2002 crime.csv').transpose()
data2.columns = data2.iloc[0]
data2 = data2.tail(-1)
data2 = data2.reset_index(drop=False)
data2 = data2.rename(columns={'index':'Year'})
print(data2)

data3 = pd.read_csv('2002 to 2010 crime.csv').transpose()
data3.columns = data3.iloc[0]
data3 = data3.tail(-1)
data3 = data3.reset_index(drop=False)
data3 = data3.rename(columns={'index':'Year'})
print(data3)

data4 = pd.read_csv('2011 to 2021 crime.csv').transpose()
data4.columns = data4.iloc[0]
data4 = data4.tail(-1)
data4 = data4.reset_index(drop=False)
data4 = data4.rename(columns={'index':'Year'})
print(data4)

data = pd.concat([data1, data2, data3, data4])
print(data)

data = data.drop_duplicates(subset='Year',keep='first')
print(data)

data.to_csv('Annual CA Crime Data.csv',index=False)
"""
"""
lfpr = pd.read_csv('CA LFPR.csv')
ann_lfpr = pd.DataFrame(data={'Year':range(1970,2023)})
index = 0
for year in ann_lfpr['Year']:
    rate = np.mean(lfpr[lfpr['DATE'].str.contains(str(year))]['LBSNSA06'])
    ann_lfpr.loc[index, 'Avg Annual LFPR'] = rate
    index += 1
ann_lfpr = ann_lfpr.dropna()
print(ann_lfpr)
ann_lfpr.to_csv('Avg Annual LFPR.csv',index=False)

snap = pd.read_csv('CA SNAP.csv')
ann_snap = pd.DataFrame(data={'Year':range(1970,2023)})
index = 0
for year in ann_snap['Year']:
    num = np.mean(snap[snap['DATE'].str.contains(str(year))]['BRCA06M647NCEN'])
    ann_snap.loc[index, 'Avg Annual SNAP'] = num
    index += 1
ann_snap = ann_snap.dropna()
print(ann_snap)
ann_snap.to_csv('Avg Annual SNAP.csv',index=False)

unemp = pd.read_csv('CA UNEMP.csv')
ann_unemp = pd.DataFrame(data={'Year':range(1970,2023)})
index = 0
for year in ann_unemp['Year']:
    rate = np.mean(unemp[unemp['DATE'].str.contains(str(year))]['CAURN'])
    ann_unemp.loc[index, 'Avg Annual UNEMP'] = rate
    index += 1
ann_unemp = ann_unemp.dropna()
print(ann_unemp)
ann_unemp.to_csv('Avg Annual UNEMP.csv',index=False)

earn = pd.read_csv('CA AVGHOUREARN.csv')
ann_earn = pd.DataFrame(data={'Year':range(1970,2023)})
index = 0
for year in ann_earn['Year']:
    rate = np.mean(earn[earn['DATE'].str.contains(str(year))]['SMU06000000500000003'])
    ann_earn.loc[index, 'Avg Annual HOUREARN'] = rate
    index += 1
ann_earn = ann_earn.dropna()
print(ann_earn)
ann_earn.to_csv('Avg Annual HOUREARN.csv',index=False)

income = pd.read_csv('CA PCPI.csv')
ann_income = pd.DataFrame(data={'Year':range(1970,2023)})
index = 0
for year in ann_income['Year']:
    rate = np.mean(income[income['DATE'].str.contains(str(year))]['CAPCPI'])
    ann_income.loc[index, 'Avg Annual PCPI'] = rate
    index += 1
ann_income = ann_income.dropna()
print(ann_income)
ann_income.to_csv('Avg Annual PCPI.csv',index=False)

pov = pd.read_csv('CA POV.csv')
ann_pov = pd.DataFrame(data={'Year':range(1970,2023)})
index = 0
for year in ann_pov['Year']:
    rate = np.mean(pov[pov['DATE'].str.contains(str(year))]['PPAACA06000A156NCEN'])
    ann_pov.loc[index, 'Avg Annual POV'] = rate
    index += 1
ann_pov = ann_pov.dropna()
print(ann_pov)
ann_pov.to_csv('Avg Annual POV.csv',index=False)
"""

data = pd.read_csv('Avg Annual LFPR.csv')

data1 = pd.read_csv('Avg Annual SNAP.csv')
data = data.merge(data1, on='Year')

data1 = pd.read_csv('Avg Annual UNEMP.csv')
data = data.merge(data1, on='Year')

data1 = pd.read_csv('Avg Annual PCPI.csv')
data = data.merge(data1, on='Year')

data1 = pd.read_csv('Avg Annual POV.csv')
data = data.merge(data1,on='Year')

data1 = pd.read_csv('Annual CA Crime Data.csv')
import re
for col in data1.columns:
    index = 0
    for element in data1[col]:
        print(element)
        if type(element) == str:
            if ',' in element:
                data1.loc[index, col] = float(re.sub(',','',element))
        index += 1
        print(element)
#data1 = data1.astype(float)
for col in data1.columns:
    print(type(data1[col][0]))
data = data.merge(data1, on='Year')

#print(data)
data.to_csv('All Annual Data.csv',index=False)
