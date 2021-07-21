USE RealEstate;
GO

CREATE TABLE  TotalList
( 
Price money NOT NULL, 
Bedroom_qty INT, 
Bathroom_qty INT,
Floor_size INT, 
Land_width INT,  
Land_depth INT, 
Address varchar(100) NOT NULL, 
City_region varchar(50),
City varchar(50),
List_type varchar(50),
Date Date NOT NULL,
);


--DROP TABLE TotalList