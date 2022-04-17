def logo():
    print(bcolors.RED + bcolors.BOLD)
    print("""
      
     ______ __                   _______                         __         ______                               __        
|   __ \__|.-----.-----.    |     __|.-----.---.-.----.----.|  |--.    |   __ \.-----.--.--.--.---.-.----.--|  |.-----.
|   __ <  ||     |  _  |    |__     ||  -__|  _  |   _|  __||     |    |      <|  -__|  |  |  |  _  |   _|  _  ||__ --|
|______/__||__|__|___  |    |_______||_____|___._|__| |____||__|__|    |___|__||_____|________|___._|__| |_____||_____|
                 |_____|                                                                                               
       
       {V} - About Time To Make Some Money

    """.format(V=VERSION))
    print(bcolors.ENDC)


import os
import time
import webbrowser
from random import randint

file = open("/home/Your UserName/Bing-Search/words.txt", "r")
words = []
for line in file:
    words.append(line)

for i in range(1, 31):

    idx = randint(0, len(words) - 1)
    search = "What does the word " + words[idx] + " mean?"

    url = 'https://www.bing.com/search?q=' + search

    # Open URL in new browser window
    webbrowser.open_new_tab(url) # opens in default browser

    time.sleep(4)

  