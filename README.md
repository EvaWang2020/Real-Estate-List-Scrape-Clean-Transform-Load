This repo explains how to scrape real estate list data using multiple spiders/crawlers, and then clean and transform the collected data, and load the data into a database or an Excel file. 

Repo main documents:
- realestatelist1.py
  - It is a Python script to scrape real estate lists of multiple cities. However, the website that I used only **allows to scrape at most 25 pages for each city using the start URL**, so some lists from the cities are missing. If you want to scrape more lists of each city in Vancouver, check [my article](https://evaanalytics.wixsite.com/website/post/use-scrapy-to-real-estate-data), which uses another website as an example. However, it will **not allow you to scrape land size for houses easily**. However, it allows you to scrape list type if you change the URL format and add list type parameters inside.
  - Each city is assigned one spider/ crawler. If you want to scrape lists from more cities, you might want to create another Python script with a few new spiders/crawlers. If there are too many spiders in one script, it could be blocked by the website when running. You can test how many spiders can be included in one run. The result should depend on how many real estate lists there are.
  - The output will include some lists without bedroom and bathroom quantity and size of the land. They are advertisement lists.
  - One list can appear multiple times
  - You can adjust scrape speed. If you scrape too fast, you could be blocked. Also, some lists could be skipped, so make sure to verify whether you have scraped all the lists you want

- Compile data data _clean_transform.py
  - It is another Python script showing how to combine all the text files with the scraped data and implement ETL.
  - Each txt file records the total real estate list data of one city in Metro Vancouver for one specific day. If you run the Python script to scrape data every day, you will gradually get many files to combine.
  - The script removes the duplicated lists and advertisement lists. Also, it will add a date for each list recorded.

- Compile data data _clean_transform1.py
  - This file includes a very similar Python script as the above. Instead of combining all the files, the script uses the append approach: it will clean and transform data from the files generated today and then append the results as rows to an existing CSV file 
  - If you can run the script every day, in the long term, this script is better than the one inside the above Jupyter notebook because there will be too many files to combine using the script from the above notebook

- Compile data data _clean_transform2.py
  - If you want to save the cleaned list data into a database rather than into a CSV file, you can refer to this file.

- SQLQuery.sql
  - It is a SQL script to create a table in the target database. The table needs to be created first before running file Compile data data _clean_transform2.py


