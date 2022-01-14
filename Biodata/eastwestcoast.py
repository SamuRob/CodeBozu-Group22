from datetime import date
from bs4 import BeautifulSoup
import csv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import matplotlib.pyplot as plt

east_coast_states=["Maine", "New Hampshire", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia", "Florida"]
west_coast_states=["California","Oregon","Washington","Alaska","Hawaii"]
folder = "Biodata"

file = open(folder + "/" + 'Deliverable 1.csv')
csvreader = csv.reader(file)
birth_area=[]
all_the_people = []
east_coast=0
west_coast=0
for row in csvreader:
    all_the_people.append(row)
for birth in all_the_people:
    for cities in east_coast_states:
        if cities in birth[2]:
            east_coast+=1

for birth in all_the_people:
    for cities in west_coast_states:
        if cities in birth[2]:
            west_coast+=1

left = [1,2]
height = [west_coast , east_coast]
tick_label = ['West Coast','East Coast']
plt.bar(left,height,tick_label = tick_label,
        width = 0.8,color = ['red','green'])

plt.xlabel('Coasts')
plt.ylabel('Presidents and Vice Presidents')
plt.title('Distribution of US Vice and Presidents on West vs East Coast')

plt.show()
