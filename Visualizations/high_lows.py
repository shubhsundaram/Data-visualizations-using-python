import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
    print(highs)
    
# get some visualizations.
fig = plt.figure(dpi=128,figsize=(8,6))
plt.plot(dates,highs,c="red",alpha=0.75)
plt.plot(dates,lows,c="blue",alpha=0.75)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily high and low temperatures - 2014",fontsize=25)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()         # it will let dates to show diagonally.
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which  ='major',labelsize=16)
plt.show()