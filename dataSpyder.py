# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:48:31 2024

@author: Moi
"""

import pandas as pd



#path= '//ad.univ-lille.fr/Etudiants/Homedir3/142068/Desktop/ProjetFinalBigData/bigdata/'
path = 'C:/Users/Moi/Desktop/Travail_Lille/bigdata/'


holidays_events = pd.read_csv("%sdata/holidays_events.csv" % path)
train = pd.read_csv("%sdata/train.csv" % path)
stores = pd.read_csv("%sdata/stores.csv" % path)



#holidays_events
holidays_events = holidays_events[holidays_events.transferred != True]
holidays_events['flagHoliday'] = 1
holidays_events = holidays_events.drop(['type','description','transferred'], axis=1)
holidays_events['datePlaceKey'] = holidays_events['date'].astype(str) + '_' + holidays_events['locale_name']


#Train
stores = stores.drop(['type','cluster'], axis=1)
trainStores = train.merge(stores, left_on='store_nbr', right_on='store_nbr')

#Merge
    #Niveau local
holidaysLocal = holidays_events[holidays_events.locale == 'Local']
holidaysLocal = holidaysLocal.drop(['locale','date','locale_name'], axis=1)
    #Niveau Regional
holidaysRegional = holidays_events[holidays_events.locale == 'Regional']
holidaysRegional = holidaysRegional.drop(['locale','date','locale_name'], axis=1)
    #Niveau National
holidaysNational = holidays_events[holidays_events.locale == 'National']
holidaysNational = holidaysNational.drop(['locale','datePlaceKey','locale_name'], axis=1)



    #Création ID
trainStores['dateCityKey'] = trainStores['date'].astype(str) + '_' + trainStores['city']
trainStores['dateStateKey'] = trainStores['date'].astype(str) + '_' + trainStores['state']

    #Niveau local
trainStoreHolidaysCity   = trainStores.merge(holidaysLocal, left_on='dateCityKey', right_on='datePlaceKey')
trainStoreHolidaysCity = trainStoreHolidaysCity.drop(['date','datePlaceKey','dateStateKey','store_nbr','family','sales','onpromotion','city','state'], axis=1)
#storesHol = trainStores.merge(trainStoreHolidaysCity, left_on='dateCityKey', right_on='dateCityKey', how='left')

    #Niveau Regional
trainStoreHolidaysRegion = trainStores.merge(holidaysRegional, left_on='dateStateKey', right_on='datePlaceKey')
trainStoreHolidaysCity = trainStoreHolidaysCity.drop(['date','datePlaceKey','dateStateKey','store_nbr','family','sales','onpromotion','city','state'], axis=1)
#storesHol = trainStores.merge(trainStoreHolidaysRegion, left_on='dateStateKey', right_on='dateStateKey', how='left')
    
    #Niveau National
trainStoreHolidaysGlobal = trainStores.merge(holidaysNational, left_on='date', right_on='date')
trainStoreHolidaysGlobal = trainStoreHolidaysGlobal.drop(['dateStateKey','store_nbr','family','sales','onpromotion','city','state'], axis=1)
trainStoreHolidaysGlobal = trainStoreHolidaysGlobal.drop_duplicates()
#storesHol = trainStores.merge(trainStoreHolidaysGlobal, left_on='date', right_on='date', how='left')




    #merge final
storesHol = trainStores.merge(dfDistinct, left_on='dateCityKey', right_on='dateCityKey', how='left')




transactions = pd.read_csv("%sdata/initial/transactions.csv" % path)
transactions.isnull().sum(axis = 0) 

oil = pd.read_csv("%sdata/initial/oil.csv" % path)




