#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    dataset_size=len(ages)

    differences=[(m-n)**2 for m,n in zip(net_worths,predictions)]

    for i in range(0,dataset_size):
        cleaned_data.append((ages[i],net_worths[i],differences[i]))
    
    cleaned_data.sort(key=lambda x:x[2])    

    #print cleaned_data
    return cleaned_data[:int(0.9*dataset_size)]

