#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
        
        Predictions are made using ages_train data
    """
    
    cleaned_data = []
    errors = []

    ### your code goes here
    for index, pred in enumerate(predictions):
        square_of_error = (predictions[index] - ages[index]) ** 2
        print square_of_error
        errors.append(square_of_error)
        
    sorted(errors)
    
    print "Errors: ", errors
    print "Limit: ", round(int(len(errors)*0.9))
    error_limit = errors[int(round(len(errors)*0.9))]
    print "error_limit: ", error_limit
    
    for index, pred in enumerate(predictions):
        error = (predictions[index] - ages[index]) ** 2
        if error < error_limit:
            cleaned_data.append((ages[index], net_worths[index], error))
    
    return cleaned_data

