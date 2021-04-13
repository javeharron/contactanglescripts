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
        lenVec=len(values)
        realz=np.argwhere(np.isnan(values)==False)
        nr=values[realz]
        meanVal=np.mean(nr)
# mean 
        #columnMean=df.iloc[:,2]
        valuesMean=np.real(np.asarray(columnMean))
        lenVecMean=len(valuesMean)
        realzMean=np.argwhere(np.isnan(valuesMean)==False)
        nrMean=values[realzMean]
        meanMeanVal=np.mean(nrMean)
        means=np.squeeze(nrMean)
        areas=np.squeeze(nr)
        vecLenM=len(means)
        vecLenA=len(areas)
       # print(vecLenM)
      #  print(vecLenA)

        valuePerAreaArray=np.multiply(means,areas)
       # print(valuePerAreaArray)
        totalVPASum=np.sum(valuePerAreaArray)
        areaSum=np.sum(areas)
        valueSum=np.sum(means)
        averVPS=totalVPASum/areaSum
        print(averVPS)
        #rl=np.argwhere(np.isnan(values)==True)
        #loc1=rl[-2]
        #loc2=rl[-1]
        newrow = ['MeanValuePerArea: ',averVPS,'','','','']



              #    'TotalArea: ', areaSum, 'TotalValue: ', valueSum]

        A = np.vstack([df, newrow])

        newrow=['TotalArea: ', areaSum, '','','','']
        A = np.vstack([A, newrow])

        newrow=['TotalValue: ', valueSum, '','','','']
        A = np.vstack([A, newrow])
        newrow=['MeanValue: ', meanMeanVal, '','','','']
        A = np.vstack([A, newrow])
    
        outString='processed_'+nameFile
        print(outString)
        np.savetxt(outString, A, delimiter='\t', fmt="%s")
      #  df.loc[(lenVec+1)] = ['','','','Average:','','']
       # df.loc[(lenVec+2)] = ['','','',meanVal,'','']
       # df.loc[(lenVec+3)] = ['','','','Stand Dev:','','']
       # df.loc[(lenVec+4)] = ['','','',np.std(nr),'','']

#writer = pd.ExcelWriter('.', engine = 'xlsxwriter')
#dfbk.to_excel("testFiles.xls",sheet_name=first)
 #       df.to_excel(nameFile,sheet_name=first)

print('Done')
