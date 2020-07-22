# Philly Neighborhood Food Access Exploration
Galvanize DSI Capstone #1: An Analysis on Food Access in Philadelphia

## Overview
This project will explore whether poverty levels impact access to healthy food stores in the city of Philadelphia.  The dataset for this evaluation comes from OpenDataPhilly.org, and the details of the collection methodology can be found in the Technical Appendix.

## Background 


1. Dataset: https://www.opendataphilly.org/dataset/showcases/neighborhood-food-retail

1. Technical Appendix:
http://foodfitphilly.org/wp-content/uploads/2019/08/Technical-Appendix.pdf

Food access data was collected at each unique census GEOID10 within the Greater Philadlephia area, where the most specific unit was the Block Group.  Each Block Group represents a certain number of residents within a geographic location.  The data collected for each Block Group is shown in the list below: 

* GeoID: census id (unique identifier)
* Non Residential (Y/N): indicates non-residential areas
* Total Low Produce Supply Stores
* Low Produce Supply Stores per 1000 Residents
* Supermarket Access (Y/N): based on 0.5 mile radius
* Total Restaurants: within GeoID
* Percent Poverty: percent of residents that fall below the Federal Poverty Line
* Percent Vehicle Availability
* Area: of GeoID

### Definitions:  
* **High Produce Supply Store (HPSS)**: Stores that carry a certain amount of fresh fruits and vegetables   
   * *Ex: typical supermarkets*
* **Low Produce Supply stores (LPSS)**: stores that carry little to no fresh fruits or vegetables.  
  * *Ex: gas stations and corner stores* 

## Questions to Explore

* Is there a difference in poverty levels between areas that have access to a supermarket and areas that do not have access to a supermarket? 
    * "Access" means there is a supermarket within 0.5 miles walking distance.

* Is there a difference in vehicle availability between areas that have access to supermarkets and those that do not? 

* Is there a difference in the number of high produce supply stores based on poverty classification? 
    * High poverty classified as >20% of the residents falling below the Federal Poverty Line

* Is there a difference in the number of low produce supply stores based on poverty classification? 

## Exploratory Data Analysis

### Initial Exploration: 
The dataset I will be using has 1336 entries and 17 columns. 

![Dataframe Info](/images/exp1.jpeg)

There were 11 null values across all variables relating to produce access and supermarkets. These null values were consistent within their respective rows, indicating the data was not collected at those specific census geoIDs.  There are two additional rows where vehicle availability and poverty information were missing.  These rows add little value to the analysis, as they were mostly null.  Because they accounted for a very small percentage of the sample size, these 13 rows have been excluded from further analysis. Raw data and snapshots of the 13 rows that have been excluded can be found in the initial_exploration.ipynb file.  

![Exploration1](/images/exp2.jpeg)

![Exploration2](/images/exp3.jpeg)

![Exploration3](/images/exp4.jpeg)

![Exploration4](/images/exp5.jpeg)