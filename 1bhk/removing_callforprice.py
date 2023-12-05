import pandas as pd

df = pd.read_excel('1BHK_Database.xlsx')
df = df[df['Price'] != 'Call for Price']

df.to_excel('Cleaned_1BHK.xlsx',sheet_name='Sheet1',index=False)


