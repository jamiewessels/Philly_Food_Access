# Philly_Food_Access
Galvanize DSI Capstone #1: An Analysis on Food Access in Philadelphia

# Galvanize DSI Capstone 1 
## Jamie Wessels
### July 16, 2020

### Proposal: Philly Neighborhood Food Access Exploration

This project will explore whether poverty levels impact access to healthy food stores in the city of Philadelphia.  The dataset for this evaluation comes from OpenDataPhilly.org, and the details of the collection methodology can be found in the Technical Appendix.  

1. Dataset: https://www.opendataphilly.org/dataset/showcases/neighborhood-food-retail

1. Technical Appendix:
http://foodfitphilly.org/wp-content/uploads/2019/08/Technical-Appendix.pdf

Food access data was collected at each unique census GEOID within the Greater Philadlephia area, where the most specific unit was the Block Group (#TODO: add info on what a block group is and how it relates to location). The data collected for each Block Group is shown in the list below: 

* GeoID: census id (unique identifier)
* Non Residential (Y/N): indicates non-residential areas
* Total Low Produce Supply Stores
* Low Produce Supply Stores per 1000 Residents
* Supermarket Access (Y/N): based on 0.5 mile radius
* Total Restaurants: within GeoID
* Percent Poverty: based on US Census data
* Percent Vehicle Availability
* Area: of GeoID

A food store is considered a "High Produce Supply Store" if it carries a certain amount of fresh fruits and vegetables (see Technical Appendix for thresholds).  A typical supermarket is an example of a High Produce Supply Store (HPSS). These stores provide access to healthy foods. Low Produce Supply stores carry little to no fresh fruits or vegetables.  A gas station or corner store is an example of a Low Produce Supply Store.

## The Questions I'd like to Answer: 

* Is there a difference in poverty levels between areas that do have access to a supermarket and areas that do not have access to a supermarket? Note: access means within 0.5 miles (assumes walking distance).

* Is there a difference in vehicle availability between areas that have access to supermarkets and those that do not? 

* Is there a correlation between poverty levels and high produce supply stores? Note: the number of stores will be normalized both by area and by population

* Is there a correlation between poverty levels and high produce supply stores? Note: the number of stores will be normalized both by area and by population

* Is there a difference in the number of supermarkets based on poverty levels? 

* Is there a correlation between the number of restaurants within each geoid unit and poverty percentage. 

## Initial Exploration of the Data

The dataset I will be using has 1336 entries and 17 columns. 

![Dataframe Info](/images/exp1.jpeg)

There were 11 null values across all variables relating to produce access and supermarkets. These null values were consistent within their respective rows, indicating the data was not collected at those specific census geoIDs.  There are two additional rows where vehicle availability and poverty information were missing.  These rows add little value to the analysis, as they were mostly null.  Because they accounted for a very small percentage of the sample size, these 13 rows have been excluded from further analysis. Raw data and snapshots of the 13 rows that have been excluded can be found in the initial_exploration.ipynb file.  

![Exploration1](/images/exp2.jpeg)

![Exploration2](/images/exp3.jpeg)

![Exploration3](/images/exp4.jpeg)

![Exploration4](/images/exp5.jpeg)