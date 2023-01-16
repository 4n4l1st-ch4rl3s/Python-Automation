import csv
import threading

def process_file():
    # Opens and reads the file
    with open("Copy of Farmer-Data - Sheet22.csv", "r") as csvfile:
        csvFile = csv.reader(csvfile)
        # The new_row will contain the appended value
        new_rows = []
        for row in csvFile:
            # Check if the first digit is '0'
            if row[0][0] == '0':
                # Replace the first digit with '254'
                new_num = '\'254' + row[0][1:]
                # new_num = row[0][1:]
            else:
                # Append '254' to the front of the number
                new_num = '\'254' + row[0]
                # new_num = row[0]
            new_rows.append([new_num])
    # Creates the output csv to which the new_rows will be saved.
    with open("output.csv", "w", newline='') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerows(new_rows)

# Initializing the thread
t = threading.Thread(target=process_file)
# Start the thread
t.start()
