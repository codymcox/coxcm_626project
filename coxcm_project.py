import csv, datetime

# creating subset of number of covid cases per date
with open('COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
outputrows = []
for sourcerow in data:
        outputrow = {'datetime':sourcerow['DATE_OF_INTEREST'],
                     'casecount':sourcerow['CASE_COUNT']}
        outputrows.append(outputrow)
outputcsv = 'covid_subset.csv'
c = open(outputcsv, 'w')
fields = ['datetime','casecount']
writer = csv.DictWriter(c, fieldnames = fields,lineterminator='\n')
writer.writeheader()
writer.writerows(outputrows)
c.close()

# creating subset of film permits for just 2020
with open('Film_Permits.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
outputrows = []
for sourcerow in data:
    datetime_str = sourcerow["StartDateTime"]
    datetime_obj = datetime.datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S %p')
    new_datetime_str = datetime_obj.strftime("%Y-%m-%d 00:00:00")
    nds = new_datetime_str.split("-")
    if nds[0] == '2020':
        outputrow = {'datetime':sourcerow["StartDateTime"],
                     'event_id':sourcerow['EventID']}
        outputrows.append(outputrow)
outputcsv = 'film_permit_subset.csv'
c = open(outputcsv, 'w')
fields = ['datetime','event_id']
writer = csv.DictWriter(c, fieldnames = fields,lineterminator='\n')
writer.writeheader()
writer.writerows(outputrows)
c.close()

# combining two subset csv files
reader = csv.reader(open("covid_subset.csv"))
reader1 = csv.reader(open("film_permit_subset.csv"))
f = open("626project.csv", "w")
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)
f.close()

# creating new csv with dictionary of dates and number of permits per date
with open('626project.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
dates = {}
for row in data:
    datetime_str = row['permit_datetime']
    obj_date = datetime.datetime.strptime((datetime_str), '%m/%d/%y %H:%M')
    nds = datetime.datetime.strftime(obj_date,'%Y-%m-%d')

    if nds in dates:
        dates[nds] += 1
    else:
        dates[nds] = 1
with open('filmpermits.csv', 'w') as f:
    fieldnames = ['permit_dates', 'number_of_permits']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    data = [dict(zip(fieldnames, [k, v])) for k, v in dates.items()]
    writer.writerows(data)

# Null data won't allow strftime change to '%Y-%m-%d'
cases = {}
for row in data:
    '''datetime_str = row['covid_datetime']
    obj_date = datetime.datetime.strptime((datetime_str),'%m/%d/%y')
    nds = datetime.datetime.strftime(obj_date,'%Y-%m-%d')'''
    cases[row['covid_datetime']] = row['casecount']
print(cases)

# csv file with number of permits and number of cases per day
reader = csv.reader(open("covid_subset.csv"))
reader1 = csv.reader(open("filmpermits.csv"))
f = open("coxcm_626project.csv", "w")
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)
f.close()

# Tried to create list of dates for dictionary. Issues making it into a list
'''date1 = '2020-01-01'
date2 = '2020-09-01'
start = datetime.datetime.strptime(date1, '%Y-%m-%d')
end = datetime.datetime.strptime(date2, '%Y-%m-%d')
step = datetime.timedelta(days=1)
while start <= end:
    #print(start.date())
    start += step
# printing out cases and permits but needed dates as key values 
with open('626project.csv') as f:
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
cases = {}
for row in data:
    datetime_str = row['covid_datetime']
    #obj_date = datetime.datetime.strptime((datetime_str),'%m/%d/%y')
    #nds = datetime.datetime.strftime(obj_date,'%Y-%m-%d')
    cases[row['covid_datetime']] = row['casecount']'''
#print(cases)
