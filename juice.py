# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd
import numpy as np
oj=pd.read_csv("E:/python/Python Assignments/DataSets/oj.csv")
###1.	Find the dimensions of the oj data set
oj.shape
###to check the na
np.sum(pd.isna(oj))
###2.	Find the structure of the data set
oj.info()
###3.	Find out the column names in the data set
list(oj)

###4.	Describe the data set
oj.describe()
###1.	Fetch the first row 3rd column from the data set
oj.iloc[0,2]
###2.	Fetch the first, second and Third columns of the oj data frame
oj.iloc[0:,:3]
###3.	Fetch the first, second, eighth and the 456th rows of the 
###1st, third and the sixth columns of the data frame
oj.iloc[[0,1,7,455],[0,2,5]]
###4.	Fetch the top 5 rows of the brand column
oj.loc[:5,"brand"]
###5.	Fetch top 5 rows of the brand, week and feat details
oj.loc[:5,["brand","week","feat"]]
###6.	Fetch the details of all distinct stores
oj.store.unique()
###7.	Fetch all the observations for Tropicana brand
oj[oj.brand=="tropicana"]
###8.	Fetch all the observations for Tropicana brand using query function
oj.query("(brand == 'tropicana')")
###9.	Fetch bottom 5 observations for those who have bought Tropicana or dominics
oj.query("(brand=='tropicana' or brand=='dominics')").tail()
###10.	Fetch the income, brand, price observations 
###with Tropicana brand without feature advertisement
oj.query("(brand=='tropicana' and feat==0)")[["INCOME","brand","price"]]
###11.	Add a new column in the dataset: logInc which is the logarithm of the income
oj["LogInc"]=np.log(oj.INCOME)
###12.	Sort the Data in the increasing order of the week
np.sort(oj.week)
###13.	Sort the data in the decreasing order of Income
oj.INCOME.sort_values(ascending=False)
###14.	Find the mean of the juice price for each brand
oj.groupby("brand").price.mean()
###15.	Find the average income for each brand and at each store
oj.groupby('brand'and'store')["INCOME"].agg('mean')
###16.	Find:
###a.	Mean and std deviation of the income
oj["INCOME"].agg({'mean','std'})
###b.	For income greater than or equal to 10.5, find the mean income
oj[oj.INCOME>=10.5].INCOME.mean()
###c.	For each brand having price >=2.5 find the mean, median,
### sd of the log of income
oj[oj.price>=2.5].groupby("brand").LogInc.agg({'mean','median','std'})
###17.	Find the Cross tabulation of brands and feature advertisement
pd.crosstab(oj.brand,oj.feat,margins=True)
