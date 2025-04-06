import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loads the file as a dataframe using pandas, sets the first column to 0
#variable my_data holds the excel file for CycleData
my_data = pd.read_excel("CycleData.xls=x", index_col=0)

#User input for station and direction, alongside appropriate format for input
station = input("Enter desired station: ").upper()
direction = input("Enter desired direction: ").title()

#Function that plots the average number of cycles holding the parameters station & direction
def average_num_cycle(station, direction):
#Temporary data based focused on the "station" and the "direction"
    tempDF = my_data[(my_data["Station"] == station) & (my_data["Direction"] == direction)]
#Grouping the date and time, alongside summing the count column to combine private and hired cycles
#reset_index() converts the index back into columns and resetting the dataframe index to original
    newDF = tempDF.groupby(["Date", "Time"])["Count"].sum().reset_index()
#Group time and calculates the mean for count whilst resetting the index 
    meanDF = newDF.groupby("Time")["Count"].mean().reset_index()
#Configures the figure size (20 for width and 5 for height)
    plt.figure(figsize=(20, 5)) 
#Creating a scatterplot inserting the x and y 
    sns.scatterplot(x=meanDF["Time"], y=meanDF["Count"])
#Rotating the x axis time so it does not make a black line
    plt.xticks(rotation=90)
#Displays/Shows the graph
    plt.show()

#Calling the function to operate
average_num_cycle(station, direction)