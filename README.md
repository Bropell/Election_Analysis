# Election_Analysis

## Project Overview
A Colorado Board of Elections employee, Tom, has given a list of tasks (shown below) to complete for the election audit of a recent local congressional election. These tasks are normally done in Microsoft Excel but Tom's manager would like to automate the process using Python. If the code is successful, they would like to expand the usage for senatorial districts and local elections. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.68.1

## Election-Audit Results
https://github.com/Bropell/Election_Analysis/blob/main/PyPoll_Challenge.py 
![alt text](https://github.com/Bropell/Election_Analysis/blob/main/analysis/Election_Results.png)

The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The counties were: 
    - Jefferson
    - Denver
    - Arapahoe
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The county results were:
    - Jefferson county had 10.5% of the vote with 38,855 votes.
    - Denver county had 82.8% of the vote with 306,055 votes.
    - Arapahoe county had 6.7% of the vote with 24,801 votes.  
- The county with the largest number of votes:
    - Denver 
- The winner of the election was: 
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
This script can be used with some slight modifications for any election. The two main changes that would have to be made can be broken down into two aspects, reading/writing files and adding additional parameters. 
- Starting with the reading and writing files aspect, there are two main things to change here that are very simple, the data file to be read and the file where the output data will be placed. There would be a different file, as well as a file path that would need to be used in place of what is used here because every election would have different data to pull information from. This change can be made in the parenthesis of line 6. Once the new data file has a path, the data can be read and the script would proceed as usual. In a similar fashion, one small change to the path written in the parenthesis on line 8 will tell the script where to place the output data. Again, this path would also be different for each election.
- The second aspect, adding additional parameters, is a little more complicated in that there will be more of the script that needs to be changed. For example, if there was another parameter of interest that was listed in the provided data that should be analyzed and displayed on the output file like the other paramters, this script has the capability to do that. In the same manner as what is used here, initialize the additional variables in the beginning of the script. Then, within the first "with open(file_to_load)" block and within the FOR loop, declare your variable and its index on the file being read. Next, use this declared variable in another IF statement in the exact same way as county name and candidate name. Lastly, write a FOR loop within the second "WITH OPEN" section for the output file which cone be done in exactly the same way as the other two paramters used in this analysis. This is also where the output format can be changed if desired. If not, the output from this FOR loop should print the results in a similar format of the additional parameter to both the terminal and the output file.