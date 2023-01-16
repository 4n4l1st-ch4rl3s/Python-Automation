#!/usr/bin/env python3
import csv
import threading

#create a function that read the csv file and outputs the new_numbers to a new csv.
def process_file():
    #opens and reads the file
    with open("Copy of Farmer-Data - Sheet22.csv", "r") as csvfile:
        csvFile = csv.reader(csvfile)
        # the new_row will contain the aappended value
        new_rows = [['254'+row[0].replace(',','')] + row[1:] for row in csvFile]
    
    #creates the output csv to which the new_rows will be saved.
    with open("output.csv", "w", newline='') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerows(new_rows)

#initiaslizing the thread
t = threading.Thread(target=process_file)
#start the threads
t.start()


