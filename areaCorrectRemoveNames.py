import numpy as np
import pandas as pd



import os, glob
#import dir

tag='.xls'
folder='.'

results=list()
results += [each for each in os.listdir(folder) if each.endswith(tag)]


print(results)

noDel=['dec','int','Dec','Int','INT','DEC']


#Output = [a for a in results if not any(b in noDel for b in str(a))]

#results=Output
print(results)

results = [ele for ele in results if all(ch not in ele for ch in noDel)]


for iy in range(0,len(results)):
        nameFile=results[iy]

#nameFile='testFiles.xls' #
        print(nameFile)
        #xl = pd.ExcelFile(nameFile)
       # xl = pd.read_csv(nameFile)
       # print(xl)
        try:
                df = np.genfromtxt(nameFile, delimiter="\t")
                column = df[:,1]
                columnMean = df[:,2]
                columnStdev = df[:,3]
                columnMin = df[:,4]
                columnMax = df[:,5]
        except:
                df = pd.read_excel(nameFile)
                column = df.iloc[:,1]
               
                columnMean = df.iloc[:,2]
              #  print(columnMean)
                columnStdev = df.iloc[:,2]
                columnMin = df.iloc[:,3]
                columnMax = df.iloc[:,4]
     #   print(len(column))
       # print(len(columnMean))
## Not using Pandas so commenting out
        #xl = pd.ExcelFile(nameFile)
        #first=xl.sheet_names[0]
       # df = xl.parse(0)
        #dfbk=xl.parse(0)
      #  column = df.iloc[:,1]

      
        # area
        values=np.real(np.asarray(column))
        cRegions=column[1::]
        cPixel=columnMean[1::]
        cStd=columnStdev[1::]
        cMin=columnMin[1::]
        cMax=columnMax[1::]
        sumPix=np.sum(cPixel)
        sumReg=np.sum(cRegions)
        combinedPixReg=np.multiply(cRegions,cPixel)
        sumPixReg=np.sum(combinedPixReg)
        averVPS=sumPixReg/sumReg

        lenVec=len(values)

        print(averVPS)
        #rl=np.argwhere(np.isnan(values)==True)
        #loc1=rl[-2]
        #loc2=rl[-1]
        #newrow = ['MeanValuePerArea: ',averVPS,'','','','']



              #    'TotalArea: ', areaSum, 'TotalValue: ', valueSum]
        
            
        outString='processed '+nameFile+'.xlsx'
        print(outString)

        data={
              'Area':cRegions,
              'Mean':cPixel,
              'StdDev':cStd,
              'Min':cMin,
              'Max':cMax
              }

        df2=pd.DataFrame(data)        
        #np.savetxt(outString, A, delimiter='\t', fmt="%s")
        df2.loc[(lenVec+1)] = ['','Mean Value per Area',averVPS,'','']
        df2.loc[(lenVec+2)] = ['','Total Area',sumReg,'','']
        df2.loc[(lenVec+3)] = ['','Mean Value',np.mean(cPixel),'','']
        #df2.loc[(lenVec+4)] = ['','Mean Area',np.mean(cRegions),'','']
        outFile='unkS.xlsx'
        df2.to_excel(outString)
#writer = pd.ExcelWriter('.', engine = 'xlsxwriter')
#dfbk.to_excel("testFiles.xls",sheet_name=first)
 #       df.to_excel(nameFile,sheet_name=first)

print('Done')
