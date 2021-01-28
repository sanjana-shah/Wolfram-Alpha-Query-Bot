# Python program to  
# demonstrate creation of an 
# assistant using wolf ram API 
  
import wolframalpha 
from gtts import gTTS
import os
  
# Taking input from user 
question = input('Question: ') 
  
# App id obtained by the above steps 
app_id = 'APPID'
  
# Instance of wolf ram alpha  
# client class 
client = wolframalpha.Client(app_id) 
language='en'
# Stores the response from  
# wolf ram alpha 
res = client.query(question) 
  
# Includes only text from the response 
answer=next(res.results).text
myObj=gTTS(text=question + 'is' + answer,lang=language,slow=False)
myObj.save("welcome.mp3")
os.system("welcome.mp3")
  
#print(answer) 
