# Final Project Write Up
## By Team 2 (Aggeliki and Surendra)

> October 4th 2019
> IDCE 302-Intro to Python Programming

## SCRIPT 1: WEB-SCRAPING WEATHER FORECAST INFORMATION

This script is a modified version of the web scraping script we worked previously. It uses beautiful soup, a python library which parses html and xml documents to “grab” information from a given website and “spit” the information on the screen in a formatted style. It is commonly used for web scraping to convert complicated scripts that make up a webpage into a number of python elements that are easier to handle. Step by step the script does the following:

- It scrapes the 5-day weather forecast from the National Weather Service website. The script extracts information from multiple elements listed under the same class name using the BeautifulSoup library. 
- This script is written with Python version 2.7. 
- The script returns the 5-day forecast for a user-selected location (latitude and longitude information need to be provided). 

We were totally unaware of this library of python prior to taking this class because we did not need to use it before. Therefore, being introduced to BeautifoulSoup was actually good and we found it quite interesting. Since we already had something to work with, it was easier to work with that and modify it. Isn't this after all the way to go about programming? We did not have major issues although at some point we were wondering if there was a quicker and/or more efficient way of cleaning text that needs formatting or when words are stuck together and you need spacing in between. What if we want to web scrape a bunch of items and there are always words stuck together? The replace() command works well if there is a pattern in the way words need to be formatted, but what if there are too many cases of those?

For the capitalization of letters we had to do google search which directed us in a page by stackoverflow: https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase

As was said above we are glad we were introduced to this library and can see few uses. For example, it could be used to obtain publically available data for natural hazards such as seismicity which is most of the times provided as tabular data that needs to be copied and pasted from a webpage.

## SCRIPT 2: CALCULATING WATER RUNOFF

The second script we chose as part of our final project work is an improvement of an early script we wrote in class. The original script was a basic script that calculated runoff for a small area. Everything was provided and no function was defined at the time.

It is not unusual that coders start with existing code that at least partially does the job. The original runoff program was not very flexible and numbers would have to be changed every time one was to calculate runoff. This is not a 
very efficient way of working neither very practical. For this project, we have improved the runoff code to calculate streamflow by accommodating other variables like precipitation and evapotranspiration and make it more flexible to accept variable input without restrictions on the size of land where runoff is calculated. The input for the variables is provided by the user at the prompt. The goal was to produce a cleaner, more efficient code that has flexibility.

This script takes user input value of precipitation and assigns 60% of this precipitation to evapotranspiration and the remaining 40% to runoff. The output of the runoff function is then assigned to a variable called “Runoff” and converted from inches to meters. Similarly, we designed a function to calculate an area of watershed that accepts the user defined value of length and breadth and assign the area function output to a variable called “Area”. Finally, the streamflow is calculated by multiplying the area of watershed by the runoff depth.

While writing the script, we had an issue of multiplying the output of two different functions. For this, we had to do google search which directed us to a stackoverflow page: https://stackoverflow.com/questions/18687505/multiplying-functions-in-python. This link helped us solve our problem with a second script. The solution was simple and required assigning the output of each function to separate variables and multiply those variables to get the final output.

Both scripts were written in Python 2.7
