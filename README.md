The data (obtained originally from the TfL website) consists of various files from a large number of monitoring sites across central London.
Download the excel files from 2014-2019 alongside the code (Step1, Step2, Step3, Step4) in order to run the code.
Below are the steps I took for the project:

For Step1:
->Combine multiple quarterly CSV files (2014–2019) into a single cleaned dataset
->Filter for three specific bike monitoring stations
->Standardize and label data with year and quarter
->Add a unique row ID, clean irrelevant columns, and save the final result as CycleData.xlsx

For Step2:
->Load the dataset and allow user input to filter by station, direction, cycle type (private/all), and time format
->Create scatterplots using Seaborn to visualize cycle counts across different time frames and groupings (weather, direction, mode)
->Generate four versions of plots based on user-defined filters

For Step3:
->Group the dataset by time of day, regardless of date
->Compute average cycle counts per time slot for a given station and direction
->Output a simplified scatterplot to highlight peak usage hours

For Step4:
->Focus only on private cycle data for a selected station
->Use a decision tree regressor to model and predict peak usage times based on time of day
->Visualize both actual and predicted values to suggest optimal peak charging periods for TfL

Conclusions:

Weather: Dry days sees higher cycle while rain reduces counts suggesting its more weather dependent 
Peak Times: Consistent across stations roughly around 7–9 AM and 4:30–7 PM, likely due to commuting.
Direction: More cyclists travel northbound in the morning, southbound in the evening.
Modeling: A simple decision tree (max_depth=2) accurately identified peak hours for TfL planning.
