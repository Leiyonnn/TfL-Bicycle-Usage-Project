import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#Loading file as a dataframe using pandas & using the column 0 as the index column stored as variable my_data
my_data = pd.read_excel("CycleData.xlsx", index_col=0)

#User input alongisde proper formatting
station = input("Enter desired station: ").upper()
direction = input("Enter desired direction: ").title()
private_only = input("Do you want to restrict to private cycles only (Y/N)? ").upper()
period_type = input("Do you want to display the date by time (T) or by date and time (D)?: ").upper()
shade = input("Do you want to colour code by Weather, Direction, or Mode?: ").title()

#Function contains three parameter: station, shade and period_type
def plot_data(station, shade, period_type):
#Filters the dataset to include ONLY rows where the "Station" matches users inputs "station" which is stored inside md (temp variable)
    md = my_data[(my_data["Station"]) == station] 
#if user input for period_type is "T" it sets to Time, else it would set to "Full_time"
    x_col = "Time" if period_type == "T" else "Full_time"
#Configures the figure size (20 for width and 5 for height)
    plt.figure(figsize=(20,5))
#Rotates the x-column so the lines won't overlap

    plt.xticks(rotation=90)
#Using seaborn to generate a scatter plot which uses the: temp dataset, x/y-axis and hue which contains the shade variable from users
    sns.scatterplot(data = md , x=x_col, y="Count", hue=shade)
#Shows/Displays the scatter plot 
    plt.show()    

#Similar to the plot_data function; however given the parameter private_cycle to restrict data
def plot_private_cycles(station, shade, period_type):
#This time filters the station and only items in "Mode" that matches to "Private cycles" in the excel sheet
    md = my_data[(my_data["Station"] == station) & (my_data["Mode"] == "Private cycles")]
    x_col = "Time" if period_type == "T" else "Full_time"
    plt.figure(figsize =(20, 5))
    plt.xticks(rotation=90)
    sns.scatterplot(data = md, x= x_col, y="Count", hue=shade)
    plt.show()

#Similar to the plot_data function; however given the parameter direction
def plot_direction(station, shade, period_type, direction):
#This time filters the station and only items in "Direction" that matches with the user input with directions
    md = my_data[(my_data["Station"] == station) & (my_data["Direction"] == direction)] 
    x_col = "Time" if period_type == "T" else "Full_time"
    plt.figure(figsize =(20, 5))
    plt.xticks(rotation=90)
    sns.scatterplot(data = md, x = x_col, y="Count", hue=shade)
    plt.show()

#Similarly to the plot_data function; however added the parameters private cycle and direction 
def plot_private_direction(station, shade, period_type, direction):
#This time filters the station, direction and mode 
    md = my_data[(my_data["Station"] == station) & (my_data["Direction"] == direction) & (my_data["Mode"] == "Private cycles")] 
    x_col = "Time" if period_type == "T" else "Full_time"
    plt.figure(figsize =(20, 5))
    plt.xticks(rotation=90)
    sns.scatterplot(data = md, x= x_col, y="Count", hue=shade)
    plt.show()

#If statements to determine which function will be called upon depending on what the user inputs
#For when user inputs "Y" and a direction but "Any"
if private_only == "Y" and direction != "Any":
    plot_private_direction(station, shade, period_type, direction)
#When user selects wants to use the restricted private cycles
elif private_only == "Y":
    plot_private_cycles(station, shade, period_type)
#Not private but has to be a direction i.e Northbound, Eastbound, etc
elif direction != "Any":
    plot_direction(station, shade, period_type, direction)
else:
    plot_data(station, shade, period_type)
    





    
    
    
    
