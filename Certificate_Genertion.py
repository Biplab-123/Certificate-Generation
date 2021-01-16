from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf',100)
for index,j in df.iterrows():
    a=len(j['Name'])
    print(a)      
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    if(a>17):
         draw.text(xy=(1345,880),text='{}'.format(j['Name']),fill=(255,0,0),font=font)
    elif(a<=15):
        draw.text(xy=(1500,880),text='{}'.format(j['Name']),fill=(255,0,0),font=font)
    elif(a>=21):
        draw.text(xy=(1000,880),text='{}'.format(j['Name']),fill=(255,0,0),font=font)
    else:    
        draw.text(xy=(1600,880),text='{}'.format(j['Name']),fill=(255,0,0),font=font)
    img.save('pictures/{}.jpg'.format(j['Name']))
