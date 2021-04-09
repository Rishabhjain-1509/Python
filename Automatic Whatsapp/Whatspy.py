import pywhatkit as kit
import pandas as pd
import numpy as np

Data = pd.read_csv("B:\Python\contacts.csv" )

#Dorp the row having null mobile number.
Data = Data.dropna() 

#Convert into the array.
Mobile =Data["Mobile Phone"].to_numpy()

#Model of cleaning.
for i in range(len(Mobile)):
    if ( len(Mobile[i]) < 13 ):
        if ( Mobile[i][:2] == "91" and len(Mobile[i]) == 12):
            Mobile[i] = "+"+Mobile[i][:2]+" "+Mobile[i][2:7]+" "+Mobile[i][7:]
        else:
            Mobile[i] = "+91 "+Mobile[i][:5]+" "+Mobile[i][5:]
    elif ( len(Mobile[i]) != 15 and len(Mobile[i]) > 14 ) :
            Mobile[i] = Mobile[i][:8]+Mobile[i][9]+" "+Mobile[i][10:12]+Mobile[i][13:]
    elif ( len(Mobile[i]) == 13 ):
        Mobile[i] = Mobile[i][:3]+" "+Mobile[i][3:8]+" "+Mobile[i][8:]

Data["Mobile Phone"] = Mobile

#Create new csv of updated one.
Data.to_csv("cleanfile1.csv", encoding="utf-8")

for i in range(len(Mobile)):
    kit.sendwhatmsg(Mobile[i],"Hello",22,15+i*0.4)