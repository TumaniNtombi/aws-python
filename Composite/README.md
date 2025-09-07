## Car Fleet Inventory – Python CSV Processing 

This project demonstrates how to process structured data from a CSV file in Python using the csv module and dictionaries. The script reads vehicle data from car_fleet.csv, creates a dictionary for each car with attributes such as VIN, make, model, year, range, top speed, acceleration (0–60), and mileage, and then stores each car in an inventory list.

Features

Uses Python’s built-in csv library to read and parse CSV data.

Deep copies a template dictionary to store each vehicle's data.

Builds an myInventoryList containing multiple vehicles.

Prints out column headers, vehicle details, and the entire inventory in a clean format.
## 🛠️ Example Output

When the script is run, it first prints the CSV column headers and processed rows, then shows the inventory list in a structured format.

**Console Output:**
Column names are: vin, make, model, year, range, topSpeed, zeroSixty, mileage
vin: 12345, make: Tesla, model: Model S, year: 2022, range: 396, topSpeed: 200, zeroSixty: 2.3, mileage: 12000
Processed 11 lines.


**Inventory List (Tabular Format):**

| vin   | make  | model   | year | range | topSpeed | zeroSixty | mileage |
|-------|-------|---------|------|-------|----------|-----------|---------|
| 12345 | Tesla | Model S | 2022 | 396   | 200      | 2.3       | 12000  |

## How to run

1. Clone the repository.
2. Ensure you have Python 3 installed.
3. Place a car_fleet.csv file in the same directory as the script.
4. Run the script: python CompositeTumani.py

## Learning Objectives

This lab is part of Python practice exercises on AWS Cloud9.
It covers:
Dictionaries and nested loops.
1. Reading CSV files.
2. Using copy.deepcopy() to preserve object structure.
3. Iterating through lists of dictionaries to display formatted output.


