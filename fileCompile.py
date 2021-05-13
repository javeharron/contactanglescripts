import numpy as np
import pandas as pd



import os, glob
#import dir

tag='.xlsx'
folder='.'
tes='processed'

results=list()
results += [each for each in os.listdir(folder) if each.endswith(tag) and each.startswith(tes)]


print(results)

nameList=list()
vpaList=list()
areaList=list()
totalAreaList=list()

for iy in range(0,len(results)):
        nameFile=results[iy]

#nameFile='testFiles.xls' #
        print(nameFile)
        df = pd.read_excel(nameFile)
        dfO = df.tail(3)
       # print(dfO)
        meanVPA=dfO.iloc[0,3]
        meanArea=dfO.iloc[2,3]
        totalArea=dfO.iloc[1,3]
        nameList.append(nameFile)
        vpaList.append(meanVPA)
        areaList.append(meanArea)
        totalAreaList.append(totalArea)
#        print(meanArea)

data={
        'Name':nameList,
        'Mean VPA':vpaList,
        'Mean Value':areaList,
        'Total Area':totalAreaList

        }

df2=pd.DataFrame(data)
outFile='compiledData.xlsx'
df2.to_excel(outFile)
