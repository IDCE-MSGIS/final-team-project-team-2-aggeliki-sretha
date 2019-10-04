# Final Project Write Up
## By Team 2 (Aggeliki and Surendra)

> October 4th 2019
> IDCE 302-Intro to Python Programming

## SCRIPT 1: WEB-SCRAPING WEATHER FORECAST INFORMATION

This script is a modified version of the web scraping script we worked previously. It uses beautiful soup, a python library which parses html and xml documents to “grab” information from a given website and “spit” the information on the screen in a formatted style. It is commonly used for web scraping to convert complicated scripts that make up a webpage into a number of python elements that are easier to handle.

I was totally unaware of this library of python prior to taking this class because I did not need to use it before. Therefore, being introduced to BeautifoulSoup was actually good and I found it quite interesting. Since we already had something to work with, it was easier to work with that and modify it. Isn't this after all kind of the way to go about programming? I did not have major issues although at some point I was wondering if there was a quicker and/or more efficient way of cleaning text that needs formatting or when words are stuck together and you need spacing in between. For the capitalization of letters I had to do google search which directed me in a page by stackoverflow: https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase

As I said above I am very glad we were introduced in class of this library as I can see few uses as obtaining publically available data for natural hazards such as seismicity etc which most of the times is provided as tabular data that needs to be copied pasted from a webpage.

## SCRIPT 2: CALCULATING WATER RUNOFF

The second script we chose as part of our final project work is an improvement of an early script we wrote in class. The original script was a very basic script that calculated runoff for a small area. Everything was provided and no function was defined.

It is not unusual that coders start with existing code that at least partially does the job. The original runoff program is not very flexible and numbers have to be changed every time one has to calculate runoff. This is not very efficient way of working neither very practical. For this project, we have improved the runoff code to calculate streamflow by accommodating other variables like precipitation and evapotranspiration and make it more flexible to accept variable input without restrictions on the size of land where runoff is calculated. The input for the variables is provided by user at prompt. The goal was to produce a cleaner, more efficient code that has flexibility.

Both scripts were written in Python 2.7
