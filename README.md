 # Get Reward Points For Doing Nothing Well Worth The Grind
 This Script is A Fully Automatic Web Searcher For Bing Rewards About Time to Get Some Money 
 
 Please submit an issue or pull-request if you have an idea for a feature


 
# Examples

GamePass Ultimate

12,000 points




Amazon.com Gift Card

5,250 points





Microsoft Gift Cards - buy devices,
games, and more!

1,600 points




Skype Unlimited

2,800 points


 

Dunkin’ Donuts Gift Card

5,250 points

Microsoft apparel, gifts, and more!

4,650 points


 

Xbox Game Pass for PC

6,800 points




Taco Bell eGift Card

5,250 points

# Installation 
git clone https://github.com/graven144p/Bing-Search-Rewards-

cd Bing-Search-Rewards-

chmod +x bingsearch.sh

./bingsearch.sh 

# More Info 
Now we need to tell the our computer to run our Python script every day, enter this into Terminal

crontab -e

Inside crontab, I have added the two lines seen below to run at 5:00 and 5:30 AM every morning

0 5 * * * /full/path/to/directory/bingsearch.sh

After saving this it should run at the specified times every morning. You may want to check to make sure the cron job runs correctly by first putting a time thats a minute or two after the current time and wait for it to run and make sure it works. You also need to make sure to log in to your Microsoft Rewards account in Bing for both your primary browser 
