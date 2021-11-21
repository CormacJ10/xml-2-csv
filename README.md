# xml-2-csv
An xml to csv converter using Python.

This is my solution to the problem introduced by the people over at Gentrack. The problem was to parse the contents for any XML file and export them to a CSV file.

The rules were as follows:

Read in an XML file
Extract out the data found in the CSVIntervalData element with the following conditions,
Create a separate CSV file for each block of data within the CSVIntervalData element that starts with "200"

A single block of data is the "200" row of data, followed by the repeating rows after, until the next "200", or you hit the "900" trailing line
Each CSV file should have the "100" row as a header, and the "900" row as the trailer
Each CSV file should be named from the second field in the "200" row

Valid rows within the CSVIntervalData element can only start with "100", "200", "300","900"
The CSVIntervalData element should contain at least 1 row for each of "100", "200", "300","900"
"100", "900" rows should only appear once inside the CSVIntervalData element

"200" and "300" can repeat and will be within the header and trailer rows 
"200" row must be followed by at least 1 "300" row
Remove leading and trailing white spaces, tabs, additional newlines.

1) what was done, 2) what wasn't done, 3) what would be done with more time

The solution I created is a Python script that takes any XML file and spits out a CSV file called 'output.csv' and satisfies most of the conditions except for:
"Remove any trailing white spaces, tabs" as will be explained on the challenges faced.

What was Done: (Please note: You would need to install Jupyter Notebook to run the solution as Python has issues with the panda library being called outside of Anaconda or the Pycharm IDE)
The following were done via the python script:
Extract out the data found in the CSVIntervalData element with the following conditions,
Create a separate CSV file for each block of data within the CSVIntervalData element that starts with "200"
Remove leading and trailing white spaces, tabs, additional newlines.
Checks the pattern of the CSVInternalData file

What wasn't done:
-remove any tabs or whitespaces for rows starting with "200" and checking as well if the CSVInterval has an EOF call.
-Do further checks for any dummy data that is not rows starting with "100", "200", "300", "900"

What would have been done if there was more time:
-I have designed a template to match the rows starting with "100" as columns for rows starting with "200" but realized that was out of scope and try to parse the data on rows starting with "300" as those seemed to contain important data but didn't test much further with it.
-Also, test further for data that didn't match the initial testfile.xml (i.e. what happens if one of the data starts with "Tes 1" instead of "TES") and further filtering so the data is more presentable to the end user (i.e. having columns that show what each datum means in this context).

Time taken: 4 hours with 1 hour of updating and setting up the Python environment
