import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 9) : 
    Country_Name,Covid_19Deaths,Cardiovascular_diseases,Respiratory_diseases ,Kidney_diseases,Neonatal_disorders ,Meningitis ,Malaria ,Interpersonal_violence , = datalist

    # print intermediate key-value pairs to standard output
    print(Country_Name,"\t",Covid_19Deaths)