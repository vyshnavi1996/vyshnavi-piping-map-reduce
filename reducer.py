import sys

thisKey = ""
thisValue = 0.0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    Country_Name, count = datalist

    if Country_Name != thisKey: 
     # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = Country_Name 
      thisValue = 0.0
  
    # apply the aggregation function
    thisValue += float(count)

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)