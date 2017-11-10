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
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data["SKILLING JEFFREY K"]))
print("terron n: " + str(len(enron_data)))

counter = 0
salaryCounter = 0
emailCounter = 0
totPayCounter = 0


for option in enron_data.itervalues():
	if option["poi"] == 1:
		counter += 1
	if not option["salary"] == 'NaN':
		salaryCounter += 1
	if not option["email_address"] == 'NaN':
		emailCounter += 1
	if option["total_payments"] == 'NaN':
		totPayCounter += 1

print("pois: " + str(counter))


print("stock value:" + str(enron_data["PRENTICE JAMES"]["total_stock_value"]))
print("mails to poi:" + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])) 

print("exer. stock options:" + str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]))

moneyJeff = enron_data["SKILLING JEFFREY K"]["total_payments"]
moneyKenn = enron_data["LAY KENNETH L"]["total_payments"]
moneyAndr = enron_data["FASTOW ANDREW S"]["total_payments"]

print("Payments:" + str(moneyJeff) + " " + str(moneyKenn) + " " + str(moneyAndr))

print("Salaries:" + str(salaryCounter))

print("Emails:" + str(emailCounter))

print("totPayCounter:" + str(totPayCounter))
