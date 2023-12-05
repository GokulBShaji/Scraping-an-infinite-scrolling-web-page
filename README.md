# Scraping-an-infinite-scrolling-web-page
Educational purpose project for scraping 1BHK listings in Hyderabad from magic bricks

## Objective
- Web Scrap Details of 1BHK listings of Hyderabad in magicbricks.com
- Clean the data for getting a presentable output.

## Procedure
- Install the following libraries - Selenium,Pandas,Openpyxl
- Install chromedriver[link](https://chromedriver.chromium.org/downloads) and place the chromdriver.exe file in the program folder(1BHK) here.
- First run Magic.py file to obtain the excel file 1BHK_Database.xlsx. This is the initial database obtained as the result of scraping.
- Then run removing_callforprice.py file for removing the ones listed without price. Cleaned_1BHK.xlsx is obtained as the result at this stage.
- Then run Converting_Price.py for Changing the price column from string to numeric data of single units(Both Lakhs and Crores into Lakhs).
- Then run Cleaning.py file for obtaining prefinal.xlsx with the parameters Name,Type of area,Area and price as columns.
- Then run cleaning_phase2.py file for obtaing the final result i.e final.xlsx.
