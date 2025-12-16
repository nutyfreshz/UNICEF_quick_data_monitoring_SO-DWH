import pandas as pd

df_dwh = pd.read_csv("./dataset/DWH.csv")
df_sf = pd.read_csv("./dataset/SF.csv")

df_dwh['AMT_DWH'] = df_dwh['Amount'].astype(int)
df_sf['AMT_SF'] = df_sf['Amount'].astype(int)

df_sf['Pledge ID'] = df_sf['npe03__Recurring_Donation__r.sescore__Pledge_Id__c'].astype(str)
df_sf['Donation ID'] = df_sf['sescore__Donation_Id__c'].astype(str)

df_mapping = df_sf.merge(
                        df_dwh,
                        on=['Donation ID'],
                        how='outer',
                        indicator=True
                        )

df_mapping['flag'] = df_mapping['_merge'].map({
                                                'left_only': 'non data from df_dwh',
                                                'right_only': 'non data from df_sf',
                                                'both': 'matched'
                                              })

'''
--Overview missing Data: Matched/Total Records--
df_mapping.flag.value_counts()

--Which Donation_ID missing: Missing data by records--
df_mapping[df_mapping['flag'] == ['non data from df_dwh','non data from df_sf']]

'''

