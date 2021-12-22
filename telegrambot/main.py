"""
@author:mrsumanbiswas
gmail: dizzytechician@gmail.com
github: https://github.com/mrsumanbiswas
linkedin: https://www.linkedin.com/in/mrsumanbiswas
Bot on Telegram: @MrDizzy_Bot
"""
#################### IMPORT ########################
import os
from wikipedia.wikipedia import summary 
import data #This is my own module whare I stored API Key
import telebot
import gtts
import wikipedia
import requests
import re
import googlesearch
from bs4 import *

#################### VARIABLE ######################


####################  CLASS ########################
class Calculate():
    pass
class Wikipedia():
    def __init__(self,quary) -> None:
        """
        # Its takes quary then search on Wikipedia and provides the result #
        """
    def __new__(cls,quary:str):
        quary:str = quary.replace("quary:","")
        Summary = wikipedia.summary(quary,sentences=3)
        texts2 = re.sub("\[.*?\]", "", Summary)
        texts3 = re.sub("\(.*?\)", "", texts2)
        Summary =  texts3.replace(")","").replace("(","").replace("=","")
        return Summary
class ImgScraping():
    ImgLink = []
    # if not os.path.exists('.Photo'):
    #     os.mkdir('.Photo')
    u_agnt = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
        }
    def Google(quary):
        search_url = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q=' + quary
        # request url, without u_agnt the permission gets denied
        response = requests.get(search_url, headers=ImgScraping.u_agnt)
        html = response.text #To get actual result i.e. to read the html data in text mode
        # find all img where class='rg_i Q4LuWd'
        b_soup = BeautifulSoup(html, 'html.parser') #html.parser is used to parse/extract features from HTML files
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
        #extract the links of requested number of images with 'data-src' attribute and appended those links to a list 'imagelinks'
        #allow to continue the loop in case query fails for non-data-src attributes
        count = 0
        for res in results:
            try:
                link = res['data-src']
                ImgScraping.ImgLink.append(link)
                count = count + 1
                if (count >= 10):
                    break
            except KeyError:
                continue
        # ImgFound = f'{len(ImgLink)} Images donloading ...'
        # print(ImgFound)
        # for i, imagelink in enumerate(imagelinks):
        #     # open each image link and save the file
        #     response = requests.get(imagelink)
        #     imagename = '.Photo' + '/' + quary +"_"+ str(i+1) + '.png'
        #     with open(imagename, 'wb') as file:
        #         file.write(response.content)
class Analys():
    def __init__(self,massage,Type:bool) -> None:
        """
        
        """
    def __new__(cls,massage,Type:bool):
        if Type:
            cls.Quary(massage)
        else:
            cls.Command(massage)
    def Quary(massage):
        quary:str = (massage.text).lower()
        if "photo:" in quary:
            return SendImg(massage)
        elif "quary:" in quary:
            try:
                text = str(Wikipedia(quary))
                SendMsg(massage,text)
                SendVoic(massage,text)
            except Exception:
                bot.reply_to(massage,"Sorry! didn't mach anything ...\nTry again........")
        elif "search:" in quary:
            quary = quary.replace('search:','')
            result = googlesearch.search(quary)
            bot.reply_to(massage,"Showing result(s) ...")
            for i in result:
                SendMsg(massage,i)
    def Command(massage):
        pass
class General():
    def __init__(self,massage) -> None:
        GQ = massage.text
        if 'who are you' in GQ\
            or 'what is your name' in GQ\
                or 'your name' in GQ:
                    REPLY = "🤖🤖🤖 I, Mr Dizz a virtual assitant 🤖🤖🤖"
        elif 'who made you' in GQ\
            or 'who is your inventor' in GQ\
                or 'who is your creator' in GQ:
                    REPLY = 'I am invented by Suman  to sort out some virtual works.'
        elif 'contac' in GQ:
            REPLY = " Gmail: dizzytechnician@gmail.com \n Github: https://github.com/mrsumanbiswas \nLinkedin: https://www.linkedin.com/in/mrsumanbiswas \n📬📬📬📬📬📬📬📬📬📬"

        bot.reply_to(massage,REPLY)

#################### FUNCTION ######################
def Run():
    pass
def Del(File):
    os.system(f"rm -r {File}")
def fun1(massage):
    if ":" in massage.text and len(massage.text) > 5: 
        return True
    else :
        return False
def fun2(massage):
    if len(massage.text) > 1 and fun1==False: 
        return True
    else :
        return False
def SendImg(massage):
    quary:str = massage.text
    quary = quary.replace("photo:","").lower()
    ImgScraping.Google(quary)
    if ImgScraping.ImgLink == []:
        text="Sorry noting mach... 😑😑😑"
    else:
        text = "Showing results... 🤗🤗🤗"
    bot.reply_to(massage,text)
    for i in ImgScraping.ImgLink:
        bot.send_photo(massage.chat.id,i)
    ImgScraping.ImgLink.clear()
def SendMsg(massage,msg):
    bot.send_message(massage.chat.id,msg)
def SendVoic(massage,text):
    gtts.gTTS(text).save(".audio.mp3")
    bot.send_audio(massage.chat.id,audio=open(".audio.mp3",'rb'))
    Del(".audio.mp3")

####################### CODE #######################
bot = telebot.TeleBot(data.BOT_API_KYE)
@bot.message_handler(commands=['start'])
def welcome(massage):
    bot.send_message(massage.chat.id,"Hey there, I am Dizzy \nHow can I help you?")
@bot.message_handler(func=fun1)
def DoTask(massage):
    Analys(massage,True)
@bot.message_handler(commands=['greet'])
def DoTask(massage):
    Analys(massage,False)
@bot.message_handler(func=fun2)
def DoTask(massage):
    General(massage)
bot.polling()


