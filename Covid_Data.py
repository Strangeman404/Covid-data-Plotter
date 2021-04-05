import pandas, numpy
from matplotlib import pyplot as plt
import matplotlib.dates
from datetime import datetime

data = pandas.read_csv("/Users/Michael/Documents/Coding/Python/owid-covid-data (1).csv")

# iso_code = data['iso_code']
# continent = data['continent']
location = data['location']
day_time = data['date']
# total_cases = data['total_cases']
# new_cases = data['new_cases']

x = day_time[0]
# y = x.strftime("%d %m %y")
print(type(x))

"Takes unique Locations"
code = []
for i in location:
    if i not in code:
        code.append(i)


def fun(var):
    loca, type = var
    list = []
    y = 0
    for i in data['location']:
        if loca == i:
            list.append(data[type][y])
        y = y + 1
    return list


def plotter(var):
    loca, type = var

    y = fun([loca,type])


    fig, ax = plt.subplots()
    ax.plot(fun([loca,'date']), y)

    ax.xaxis.set_minor_locator(matplotlib.dates.MonthLocator((1,4,10)))
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())

    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("\n%Y"))
    ax.xaxis.set_minor_formatter(matplotlib.dates.DateFormatter("%b"))
    plt.setp(ax.get_xticklabels(),rotation=0, ha="center")

    plt.show()

print(day_time)

print(plotter(["Greece","total_cases"]))

# print(code)
# x = input(" " + "pick a country")
# print("Available Data: total_cases, new_cases")
# y = input(" " + "pick data type")
# plotter([x,y])