import csv

# challenges with each dataset:
# online_retail - 541k rows, time formats
# spam - lots of different symbols, unstructured, includes links
# students_performance - least challenging w/ 1k rows, most rows are set options, rows w/ scores have set range 0-100

# online_retail - should manage large dataset & handle time format
with open('online_retail.csv', newline='') as csvfile:
    # retail = csv.reader(csvfile, delimiter=' ', quotechar= '|' )
    retail = csv.DictReader(csvfile)
    for row in retail:
        print(row['Description'], row ['Quantity'])
    
# spam - should handle various inputs with links and symbols


# students_performance - handle size of dataset and transform input into organised table, convert values?
