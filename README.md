This repo explains how to scrape real estate list data using multiple spiders/crawlers, clean the collect data, and what types of analysis we can do with the cleaned data. It also explains how to set up auto task running to collect data even when you are on vacation.  Different approaches to automatically run the tasks will be provided.

Included docs:
- Python script to scrape data.ipynb
  - A Python script to scrape multiple cities' real estate lists. 
  - Each city uses one spider/ crawler. You can test how many spiders you can put in one run. The result should depend on how many lists there are.
  - The result will include some lists without price. They are advertisement lists and should be excluded to avoid duplication.
