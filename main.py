import json_lines
import json
import collections
import itertools
from operator import itemgetter

def readFile():
    result = []
    with json_lines.open ('items.jl', broken=True) as file:
        for item in file:
            result.append(item)
    return result

def sortCarsByMakeName(cars):
    sorted_cars = sorted(cars, key= lambda i: i['make_name']['value'])
    return sorted_cars

def groupCarsByMakeName(sortCars):
    grouped_cars = collections.defaultdict(list)
    for item in sortCars:
        grouped_cars[item['make_name']['value']].append(item)
    return grouped_cars

def writeToJson(grouped_cars):
    with open ('data.json', 'w') as output:
        json.dump(grouped_cars, output, indent=1)

cars = readFile()
sorted_cars = sortCarsByMakeName(cars)
grouped_cars = groupCarsByMakeName(sorted_cars)

writeToJson(grouped_cars)






