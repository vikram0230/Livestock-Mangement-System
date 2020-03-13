import pandas as pd
from backend import DataBase
from datetime import datetime, date
import view 

db = DataBase()
data = db.getGoatRecords()
dataColumns = db.getColumnNames()
df = pd.DataFrame(data,columns=dataColumns)

breed = df['breed']	

gender = df['gender']

dob = df['date_of_birth']

kidCount = db.getKidCount()
maleKidCount = 0
femaleKidCount = 0

if len(kidCount)>1:
	if kidCount[0][1] == 'm':
		maleKidCount = kidCount[0][0]
		femaleKidCount = kidCount[1][0]
	else:
		maleKidCount = kidCount[1][0]
		femaleKidCount = kidCount[0][0]
else:
	if kidCount[0][1] == 'm':
		maleKidCount = kidCount[0][0]
	else:
		femaleKidCount = kidCount[0][0]

deadCount = db.getDeadCount()
maleDeadCount = 0
femaleDeadCount = 0

if len(deadCount)>1:
	if deadCount[0][1] == 'm':
		maleDeadCount = deadCount[0][0]
		femaleDeadCount = deadCount[1][0]
	else:
		maleDeadCount = deadCount[1][0]
		femaleDeadCount = deadCount[0][0]
else:
	if deadCount[0][1] == 'm':
		maleDeadCount = deadCount[0][0]
	else:
		femaleDeadCount = deadCount[0][0]

print(deadCount)

income = db.getTotalLivestockNetworth()
expense = db.getTotalLabourCost()+db.getTotalFeedCost()+db.getTotalHealthExpenditure()+db.getTotalMiscCost()
