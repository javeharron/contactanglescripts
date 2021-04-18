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

#nameFile='testFiles.xls' #
        print(nameFile)
        #xl = pd.ExcelFile(nameFile)
       # xl = pd.read_csv(nameFile)
       # print(xl)
        df = np.genfromtxt(nameFile, delimiter="\t")
    #
        column = df[:,1]
        columnMean = df[:,2]
        columnStdev = df[:,3]
        columnMin = df[:,4]
        columnMax = df[:,5]
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
        newrow = ['MeanValuePerArea: ',averVPS,'','','','']



              #    'TotalArea: ', areaSum, 'TotalValue: ', valueSum]
        
        A = np.vstack([df, newrow])

        newrow=['TotalArea: ', sumReg, '','','','']
        A = np.vstack([A, newrow])

        newrow=['TotalValue: ', sumPix, '','','','']
        A = np.vstack([A, newrow])
        newrow=['MeanValue: ', np.mean(cPixel), '','','','']
        A = np.vstack([A, newrow])

            
        outString='processed_'+nameFile+'.xlsx'
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
        df2.loc[(lenVec+4)] = ['','Mean Area',np.mean(cRegions),'','']
        outFile='unkS.xlsx'
        df2.to_excel(outString)
#writer = pd.ExcelWriter('.', engine = 'xlsxwriter')
#dfbk.to_excel("testFiles.xls",sheet_name=first)
 #       df.to_excel(nameFile,sheet_name=first)

print('Done')
