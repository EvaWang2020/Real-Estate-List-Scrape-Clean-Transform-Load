This repo explains how to scrape real estate list data using multiple spiders/crawlers, clean and transform the collected data, and load the data into a database or an Excel file. 

Repo main documents:
- realestatelist1.py
  - It is a Python script to scrape real estate lists of multiple cities 
  - Each city is assigned one spider/ crawler. If you want to scrape lists from more cities, you might want to create another python script with a few new spiders/crawlers. If there are too many spiders in one script, it could be blocked by the website when running. You can test how many spiders can include in one run. The result should depend on how many real estate lists there are.
  - The output will include some lists without bedroom and bathroom quantity and size of the land. They are advertisement lists.
  - One list can appear multiple times
  - You can adjust scrape speed. If you scrape too fast, you could be blocked. Also, some lists could be skipped, so make sure to verify whether you have scraped all the lists you want

- Compile data data _clean_transform.py
  - It is another Python script to combine all the text files with the scraped data, steps to clean and transform the data and save the result into an Excel file.
  - Each txt file records the total real estate lists date of those cities for one specific day. If you run the Python script to scrape data every day, you will gradually get many files to combine whenever you run the script in this note.
  - The script will remove the duplicated lists as well as advertisement lists. Also, it will add a date for each list record

- Compile data data _clean_transform1.py
  - This file includes very similar Python script as the above. Instead of combining all the files, the script uses the append approach: it will use clean and transform data from the files generated today and then append the results as rows to an existing CSV file 
  - If you can run the script every day, in long term, this script is better than the one inside the above Jupyter notebook because there will be too many files to combine using the script from the above notebook

- Compile data data _clean_transform2.py
  - If you want to save the cleaned list data into a database rather than into a CSV file, you can refer to this file.


