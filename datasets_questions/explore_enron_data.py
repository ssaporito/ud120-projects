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

#print(enron_data.keys())
#print len(enron_data.keys())
#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

salary_count=0
email_count=0

# for k in enron_data.keys():
#  	salary_count+=1 if enron_data[k]['salary']!='NaN' else 0 
#  	email_count+=1 if enron_data[k]['email_address']!='NaN' else 0 
# print salary_count
# print email_count
#print len(enron_data[enron_data.keys()[0]].values())
count_payments=0
for k in enron_data.keys():
	count_payments+=1 if enron_data[k]['total_payments']=='NaN' and enron_data[k]['poi'] else 0

print count_payments
print 100*count_payments/len(enron_data)

# print sum_poi

