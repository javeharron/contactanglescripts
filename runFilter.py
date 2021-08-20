import numpy as np
import pandas as pd



import os, glob
#import dir

tag='.xls'
folder='.'

results=list()
results += [each for each in os.listdir(folder) if each.endswith(tag)]

y_list_of_items=results

element = 'ing'
for item in y_list_of_items:
    if element in item:
        y_list_of_items.remove(item)

print(y_list_of_items)
       
results=y_list_of_items

element = 'Graph'
for item in y_list_of_items:
    if element in item:
        y_list_of_items.remove(item)

print(y_list_of_items)
       
results=y_list_of_items

y_list_of_items=results

element = 'graph'
for item in y_list_of_items:
    if element in item:
        y_list_of_items.remove(item)

print(y_list_of_items)
       
results=y_list_of_items

print(results)
for i in range(0,len(results)):
        nameFile=results[i]
#nameFile='testFiles.xls'
        xl = pd.ExcelFile(nameFile)
        first=xl.sheet_names[0]
        df = xl.parse(0)
        #dfbk=xl.parse(0)
        column = df.iloc[:,3]
        values=np.real(np.asarray(column))

        lenVec=len(values)

        realz=np.argwhere(np.isnan(values)==False)
        nr=values[realz]
        meanVal=np.mean(nr)

        #rl=np.argwhere(np.isnan(values)==True)
        #loc1=rl[-2]
        #loc2=rl[-1]
        try:
            df.loc[(lenVec+1)] = ['','','','Average:','','']
            df.loc[(lenVec+2)] = ['','','',meanVal,'','']
        except:
            df = df.drop(df.columns[[0]], axis=1)
            #del df['Unnamed']
            df.loc[(lenVec+1)] = ['','','','Average:','','']
            df.loc[(lenVec+2)] = ['','','',meanVal,'','']
       # df.loc[(lenVec+3)] = ['','','','Stand Dev:','','']
       # df.loc[(lenVec+4)] = ['','','',np.std(nr),'','']

#writer = pd.ExcelWriter('.', engine = 'xlsxwriter')
#dfbk.to_excel("testFiles.xls",sheet_name=first)
        df.to_excel(nameFile,sheet_name=first)

print('Done')








