import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree

#Loads the file called CycleData using column 0 as the index column
data = pd.read_excel("CycleData.xlsx", index_col=0)

#Filters the data to only have Private cycles
data = data[data["Mode"] == "Private cycles"]

#Allows the choice of station for users
station = input("Enter desired station: ").upper()

#Defining function station_choices holding station and max_depth
def station_choices(station, max_depth=2):

#Variable holding a copy of the rows for the given station choice
    stationDataFrame = data[data["Station"] == (station)].copy()

#Converting the "Time" column from a string to datetime format and extracting the hour value
    stationDataFrame["RealTime"] = pd.to_datetime(stationDataFrame["Time"], format="%H:%M:%S")
    stationDataFrame["RealTime"] = stationDataFrame["RealTime"].dt.hour + stationDataFrame["RealTime"].dt.minute / 60

#Forming arrays x and y corresponding to RealTime and Count and reshaping them
    x2 = stationDataFrame["RealTime"].values.reshape(-1,1)
    y = stationDataFrame["Count"].values.reshape(-1,1)

#Spliting the data into training sets and test sets (also used random_state=1 to match the answer)
    training_x2, test_x2, training_y, test_y = train_test_split(x2, y, random_state=1)

#Using the DecisionTreeRegressor model with depth
    my_regressor = DecisionTreeRegressor(max_depth = 2)
#Using the training dataset for the model
    my_regressor.fit(training_x2, training_y)
#Making the structure of the decision tree 
    plt.figure(figsize=(20,5))
    plot_tree(my_regressor, filled = True, fontsize = 8)
    plt.show()

#Predicting values for the entire dataset and storing them in a new column
    stationDataFrame["Predicted"] = my_regressor.predict(x2)
#Creating a scatterplot for actual and predicted values
    plt.figure(figsize=(20,5))
    sns.scatterplot(x=stationDataFrame["RealTime"], y=stationDataFrame["Count"], label="Actual")
    sns.scatterplot(x=stationDataFrame["RealTime"], y=stationDataFrame["Predicted"], label="Predicted")
    plt.show()
#Calls the function with the parameter inside
station_choices(station, max_depth=2)
    
    
    
    