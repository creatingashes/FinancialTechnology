import requests
import re

#create textfiles for the male descriptions and female descriptions
m = open("male.txt","w+")
f = open("female.txt", "w+")

#extract the descriptions 50 times
for i in range(50):
    get_resp = requests.get('https://www.theyfightcrime.org/')
    text = get_resp.text
    x = re.search("He's(.+)\.(.+)\.", text)
    
    #test to make sure it was correctly found or try again
    if x == None:
        get_resp = requests.get('https://www.theyfightcrime.org/')
        text = get_resp.text
        x = re.search("He's(.+)\.(.+)\.", text)
        
    str = x.group()
    print(str)
   
#split the male and female descriptions and write them onto the textfiles
    y = re.split("\sShe's", str)
    m.write(y[0] + "\n")
    f.write("She's" + y[1] + "\n")
    
f.close()
