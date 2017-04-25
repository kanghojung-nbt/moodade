from xlrd import open_workbook
from mood.models import Mood

fname='./excelData.xlsx'
wb = open_workbook(fname)

sheets = wb.sheets()
sheet=sheets[0]


for i ,data in enumerate(sheet.col(0,3,105)):
    fb=Mood(color='red',emotion='angry',mood_Verb=data.value,mood_Amount=float(sheet.cell(i+2,1).value))    
    data=sheet.cell(i+1,1).value
    data=str(data)
    print((data))
    print((sheet.cell(i+2,1).value))
    fb.save()



for i ,data in enumerate(sheet.col(0,1,18)):
    fb=Mood(color='orange',emotion='interesting',mood_Verb=data.value,mood_Amount=(sheet.cell(i+2,3).value))
    fb.save()

for i ,data in enumerate(sheet.col(0,1,94)):
    fb=Mood(color='yellow',emotion='happy',mood_Verb=data.value,mood_Amount=(sheet.cell(i+2,5).value))
    fb.save()

for i ,data in enumerate(sheet.col(0,1,40)):
    fb=Mood(color='green',emotion='fear',mood_Verb=data.value,mood_Amount=(sheet.cell(i+2,7).value))
    fb.save()

for i ,data in enumerate(sheet.col(0,1,45)):
    fb=Mood(color='skyblue',emotion='surprise',mood_Verb=data.value,mood_Amount=(sheet.cell(i+1,9).value))
    fb.save()

for i ,data in enumerate(sheet.col(0,1,136)):
    fb=Mood(color='blue',emotion='sadness',mood_Verb=data.value,mood_Amount=(sheet.cell(i+1,11).value))
    fb.save()

for i ,data in enumerate(sheet.col(0,1,18)):
    fb=Mood(color='purple',emotion='boring',mood_Verb=data.value,mood_Amount=(sheet.cell(i+1,13).value))
    fb.save()

for i ,data in enumerate(sheet.col(0,1,51)):
    fb=Mood(color='magenta',emotion='disgust',mood_Verb=data.value,mood_Amount=(sheet.cell(i+1,15).value))
    fb.save()
