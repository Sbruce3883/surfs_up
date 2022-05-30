# surfs_up
### Exploring Weather Data with SQLAlchemy, Flask, and SQLite

# Overview of Analysis
### The purpose of this analysis was to track temperature patterns during June and December to determine whether opening a surf shack business would be pragmatic. Two separate queries were run for each month, then the recorded temperatures for June and December were converted to lists and stored in a dataframe.  Summary statistics were finally stated using the describe method. 

# Results

During the month of June, temperatures were taken 1700 different times: 
- Mean of 74.9°F 
- Min of 64.0°F 
- Max of 85.0°F
<img width="69" alt="June_temperatures" src="https://user-images.githubusercontent.com/101988047/170896190-581589b5-8045-45d8-8bc9-a315c1ebe8b6.png">

During the month of December, temperatures were taken 1517 different times: 
- Mean of 71.0°F 
- Min of 56.0°F 
- Max of 83.0°F
<img width="74" alt="December_temperatures" src="https://user-images.githubusercontent.com/101988047/170896198-3e153db7-ea5f-4387-b3b3-ba7132b91aca.png">

The Standard Deviation is 3.26 in June and 3.75 in December -- with a .5 difference between the two seasons.

# Summary

### Although the results regarding temperature would leave us to believe that the small difference in temperature deviation between the months of June and December would be reason enough to commit to starting a surf shack, more information is needed with regards to precipitation and other factors which would give better indication of unfavorable weather conditions. Luckily, SQLAlchemy and Flask can be used to visualize other climate data that would offer better preparation for opening a surf shack. 
