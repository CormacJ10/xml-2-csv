# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
  
#inital setup
headers =["100", "200", "300", "900"]
cols=[]
rows=[]
interval_data=""

header_count=0
interval_counter=0
trailer_count=0
  
# Parsing the XML file
xmlparse = Xet.parse('testfile.xml')
root = xmlparse.getroot()
for i in root:
    interval_data=i.find("CSVIntervalData").text

    print(interval_data)
    #rows.append()
  
#df = pd.DataFrame(rows, columns=cols)#for version 2
  
# Writing dataframe to csv
#df.to_csv('output.csv')
