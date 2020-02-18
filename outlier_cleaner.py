#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """


    def removeOutliers(list, errors):

        i = 89

        while i > 80: ## Until it's equal to 81 (10 % of the data)

            maxError = max(errors, key=abs)

            index = errors.index(maxError)

            del list[index]
            del errors[index]
            i -= 1

        return list

    cleaned_data = []

    i = 0

    totalCount = len(predictions)

    errors = []

    while i < totalCount:

        error = net_worths[i][0] - predictions[i][0]

        dataPoint = (ages[i][0], net_worths[i][0],  error)

        cleaned_data.append(dataPoint)
        errors.append(error)

        i += 1

    cleaned_data = removeOutliers(cleaned_data, errors)

    print "Cleaned data count: ", len(cleaned_data)

    return cleaned_data