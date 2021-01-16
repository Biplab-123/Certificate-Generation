##import all required libaries
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os



#read the list of the all the name as CSV file
df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf',100)




##access the list
for index,j in df.iterrows():    
    a=len(j['Name'])    ##calculate the length of the each name
    print(a)      
    img = Image.open('certificate.jpg')     #upload the certificates
    draw = ImageDraw.Draw(img)




#according to the size or length of the name place eaach name
    if(a>17):
         draw.text(xy=(1345,880),text='{}'.format(j['Name']),fill=(255,0,0),font=font)
    elif(a<=15):
        draw.text(xy=(1500,880),text='{}'.format(j['Name']),fill=(255,0,0),font=font)
    elif(a>=21):
        draw.text(xy=(1000,880),text='{}'.format(j['Name']),fill=(255,0,0),font=font) ##exception Have huge name
    else:    
        draw.text(xy=(1600,880),text='{}'.format(j['Name']),fill=(255,0,0),font=font)



#save the certificate with .jpg extension
#create a folder name as ****certificates*** onto the same location where certificate and name list present             
    img.save('certificates/{}.jpg'.format(j['Name'])) 
