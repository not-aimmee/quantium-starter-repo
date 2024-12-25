import pandas as pd
ds0=pd.read_csv('daily_sales_data_0.csv')
ds1=pd.read_csv('daily_sales_data_1.csv')
ds2=pd.read_csv('daily_sales_data_2.csv')
ds0['sales']=ds0['quantity']*ds0['price']
ds1['sales']=ds1['quantity']*ds0['price']
ds2['sales']=ds2['quantity']*ds0['price']
#pm0=ds0[ds0['product']=='pink morsel']
#pm1=ds1[ds1['product']=='pink morsel']
#pm2=ds2[ds2['product']=='pink morsel']
#all_pm= pd.concat([pm0,pm1,pm2], axis=0, ignore_index=True)
ds0.drop(ds0[ds0['product']!= 'pink morsel'].index, inplace=True)
ds1.drop(ds1[ds1['product']!= 'pink morsel'].index, inplace=True)
ds2.drop(ds2[ds2['product']!= 'pink morsel'].index, inplace=True)
all_data= pd.concat([ds0,ds1,ds2],axis=0,ignore_index=True)
print(all_data)