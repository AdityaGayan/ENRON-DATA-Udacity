#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#no of people
print(len(enron_data))
#no of features for each person
print(len(enron_data.values()[0]))

#no of person of interest in the dataset
count = 0
for i in range(len(enron_data)):
    a = enron_data.values()
    if a[i]['poi'] == True:
        count = count + 1        
print count

#no of person of interest according to katie
poi_names = open('../final_project/poi_names.txt', 'r')
fr = poi_names.readlines()
print(len(fr[2:]))
#poi_names.close()


#total value of person
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])


print(enron_data['SKILLING JEFFREY K']['total_payments'])



count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1
print count_salary
print count_email


total_payments_NaN_no = 0
for key in enron_data.keys():
	if enron_data[key]['total_payments'] == 'NaN' :
		total_payments_NaN_no+=1

print total_payments_NaN_no

print total_payments_NaN_no*100/146



total_payments_NaN_no_poi = 0
for key in enron_data.keys():
	if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi']=="true" :
		total_payments_NaN_no_poi+=1

print total_payments_NaN_no_poi

print total_payments_NaN_no_poi*100/146




