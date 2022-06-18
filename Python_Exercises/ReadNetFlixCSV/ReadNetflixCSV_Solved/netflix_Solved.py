# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file

csvpath = os.path.join('..', 'Resources', "netflix_ratings.csv")


# Open the CSV

with open(csvpath) as movie:

    file_reader = csv.reader(movie)

    # Loop through looking for the video
   
    for row in file_reader:

        if row[0] == video:

            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

    else:

        print("Sorry about this, we don't seem to have what you are looking for!")

