# Vyshnavi-piping-map-reduce
- For large python datasets using the map-reduce 
# Data Description:
- I used data from kaggle website (https://www.kaggle.com/majyhain/death-cause-by-country) Based on Death Cause Reason by Each country.
- The dataset contains 9 columns and 188 rows contains the death causes by All Countires.
# Powershell Command:
- cat Death_Reason_by_Country.csv | py 21mapper.py | sort | py 22reducer.py > swetha.txt 
# Summary Of Data
- By checking the final ouput I have reduced based on the countries and covid_19 Death casesz.
## Charts : 
- I have decided to draw a bar chart based on countries and covid19_Death cases.
- I have decide to draw an bar chart based on countries and covid19_Death cases with Highest cases in which country it is occured.
