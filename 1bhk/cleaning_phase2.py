import pandas as pd
df = pd.read_excel('prefinal.xlsx')
sf = pd.DataFrame()

a1 = df['Name'].to_list()
a2 = df['Type_Area'].to_list()
a3 = df['Area'].to_list()
a4 = df['Price in Lakhs'].to_list()
l = len(a1)

b1 = []
b2 = []
b3 = []
b4 = []

for i in range(l):
    if a1[i][0] == '1':
        b1.append(a1[i])
        b2.append(a2[i])
        b3.append(a3[i])
        b4.append(a4[i])

sf['Name']=b1
sf['Type_Area']=b2
sf['Area']=b3
sf['Price in Lakhs']=b4

sf.to_excel('final.xlsx',sheet_name='Sheet1',index=False)