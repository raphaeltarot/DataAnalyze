import pandas
from pandas import Series, DataFrame
import os
from matplotlib import pyplot, rc
import numpy as np

#print("目前工作的目錄是:", os.getcwd())
#data1 = pandas.read_csv('Data/Data21.csv', skiprows=0, index_col='FIELD_3')
dataOrg = pandas.read_csv('Data/Data21_1.csv')
#print("資料維度是:", data1.shape)
#print("標題是:", data1.head())
data1 = pandas.DataFrame(dataOrg)
#print("欄位是", data1.columns)

print("**" * 20)
#data1.drop(['INSERTDATATIME','FIELD_1', 'FIELD_2', 'FIELD_5','FIELD_6','FIELD_7','FIELD_8','FIELD_9','FIELD_10','FIELD_11','FIELD_12','FIELD_13','FIELD_14',
#            'TARGETVALUE', 'DQIX', 'DQIY', 'MEASURE', 'PIECEID', 'GSIB', 'NN_PII', 'MR_PII', 'GSI_PII', 'GSIB_PII', 'RI_PII', 'CONTEXTID_PII'], axis=1)
data1.drop(data1.columns[[0, 1, 2]],axis = 1)
print("列出標題欄:", data1.columns)
#print("列出標題1:", data1.head(10))
#print("列數:",data1.shape[1], "行數：", data1.shape[0], "長度", len(data1))
ax = pyplot.gca()

print("**"*20)

#指定序號
StartNum = 3120000
EndNum = 3150000

#篩選資料
PData = data1[(data1['FIELD_3'] == "AA00")  & (data1['CONTEXTID'] > StartNum) & (data1['CONTEXTID'] < EndNum)]
# PData1 = data1[(data1['FIELD_3'] == "AA00") & (data1['FIELD_4'] == "G8") & (data1['CONTEXTID'] > StartNum) & (data1['CONTEXTID'] < EndNum)]
# PData1.plot(kind='line',x='FIELD_3',y='NN', linewidth=.5,ax=ax)

#群組代碼
Fieldr = ["G"+str(c) for c in range(8,61)]
#print(Fieldr)
LableList = []
LableListNum = []
#畫線
for i in Fieldr:
    pd = data1[(data1['FIELD_3'] == "AA00") & (data1['FIELD_4'] == i) & (data1['CONTEXTID'] > StartNum) & (data1['CONTEXTID'] < EndNum)]
    LableList.append(pd)
    LableListNum.append(len(pd))
    pd.plot(kind='line', x='FIELD_3', y='NN', linewidth=.5, label= i, ax=ax)

#找出陣列裏最大數
LableMax = np.amax(LableListNum)
print(LableMax)

def CheckList(c):
    # print(len(c))
    if len(c) == LableMax:
        return c

LableMaxList = list( filter(lambda item: item is not None,[CheckList(c) for c in LableList]))
# print(LableMaxList[0])

#x標籤
#labels = ['01:00', '02:00']
#print(labels)

labels2 = [i for i in LableMaxList[0]['INSERTDATATIME']]
#print(labels2)
#每100間隔取值
StatNum = 0;
IntervalNum = 100
labels3 = labels2[StatNum::IntervalNum]
print(labels3)
num = int(len(labels2))
Rnum = range(StatNum,num,IntervalNum)
print(Rnum )
#代入標籤內
pyplot.xticks(ticks=Rnum ,
          labels=labels3 ,
          color='#f00',
          fontsize=5,
          rotation=0)

#上下限
pyplot.axhline(y=7, xmin=0.1, xmax=0.9)
pyplot.axhline(y=1, xmin=0.1, xmax=0.9)

#x欄名
pyplot.xlabel('Time')
#圖例操作
pyplot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0, fontsize=6)
#標題
pyplot.title("AA00 Lines")
pyplot.grid()
pyplot.show()