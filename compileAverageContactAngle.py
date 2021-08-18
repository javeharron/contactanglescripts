import numpy as np
import pandas as pd

# add stand deviation column, overall mean contact angle and std dev

import os, glob
#import dir

tag='.xls'
folder='.'
tes='HJ'

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
        dfO = df.tail(1)

        meanVPA=dfO.iloc[0,4]
        nameList.append(nameFile)
        vpaList.append(meanVPA)

#print(vpaList)
amountCA=int(len(vpaList))
meanCA=float(np.average(vpaList))
stdevCA=float(np.std(vpaList))

        
data={
        'Name':nameList,
        'Mean Contact Angle':vpaList,
        #'Mean Value':areaList,
        #'Total Area':totalAreaList

        }

df2=pd.DataFrame(data)
df2.loc[(amountCA+1)] = ['','Mean Contact Angle:']
df2.loc[(amountCA+2)] = ['',meanCA]
df2.loc[(amountCA+3)] = ['','Standard Deviation:']
df2.loc[(amountCA+4)] = ['',stdevCA]


outFile='compiledContactAngle.xlsx'
df2.to_excel(outFile)
