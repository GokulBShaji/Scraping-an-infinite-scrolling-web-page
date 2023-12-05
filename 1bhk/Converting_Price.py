import pandas as pd
df = pd.read_excel('Cleaned_1BHK.xlsx')
a = df['Price'].to_list()
l = len(a)

def numeric(a):
    l = len(a)
    if a[-3] == 'L':
        b = a[1:l-3]
        c = float(b)
    else:
        b = a[1:l-2]
        c = 100 * (float(b))
    return c

for i in range(l):
    a[i] = numeric(a[i])

print(a)
print(len(a))

df['Price']=a
df.to_excel('Cleaned_1BHK.xlsx',sheet_name='Sheet1',index=False)