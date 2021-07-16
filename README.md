This repo explains how to scrape real estate list data using multiple spiders/crawlers, clean and transform the collected data, and load the data into a database or an Excel file. 
It also explains how to run python scripts automatically every day.  Different approaches will be covered and compared.

Repo main documents:
- Python script to scrape data.ipynb
  - It is a Jupyter notebook, inside which there is code to scrape real estate lists of multiple cities 
  - Each city is assigned one spider/ crawler. If you want to scrape lists from more cities, you might want to create another python script with a few new spiders/crawlers. If there are too many spiders in one script, it could be blocked by the website when running. You can test how many spiders can include in one run. The result should depend on how many real estate lists there are.
  - The output will include some lists without bedroom and bathroom quantity and size of the land. They are advertisement lists.
  - One list can appear multiple times
  - You can adjust scrape speed. If you scrape too fast, you could be blocked. Also, some lists could be skipped, so make sure to verify whether you have scraped all the lists you want

- Compile data_clean_transform.ipynb
  - It is another Jupyter notebook that includes the script to combine all the files with the scraped data, steps to clean and transform the data, and save the result into an Excel file.
  - Each file records the real estate lists date for only one day. So if you scrape every day, you will have more and more files.
  - The script will remove the duplicated lists as well as the advertisement lists. Also, it will add a date for each list.
