import pandas as pd
df = pd.read_excel('Cleaned_1BHK.xlsx')
sf = pd.DataFrame()
a = df['Detail'].to_list()
b = df['Price'].to_list()
l = len(a)

data =[]

for i in range(l):
    temp = a[i].split('\n')
    result = temp + [b[i]]
    data.append(result)

area_set =['CARPET AREA','SUPER AREA']
Type_Area=[]
Area = []
name = []
price = []
for r in data:
    l1 = len(r)
    for i in range(l1):
        if r[i] in area_set:
            Type_Area.append(r[i])
            Area.append(r[i+1])
            name.append(r[0])
            price.append(r[-1])


sf['Name']=name
sf['Type_Area']=Type_Area
sf['Area']=Area
sf['Price in Lakhs']=price

sf.to_excel('prefinal.xlsx',sheet_name='Sheet1',index=False)

