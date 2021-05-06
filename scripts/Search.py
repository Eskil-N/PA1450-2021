def isCountry(dataSet, searchTerm):
    if (searchTerm in dataSet['Country_Region']):
        return True
    return False

def Search(dataSet, searchTerm):
    if (isCountry(dataSet, searchTerm)):
        return dataSet[dataSet['Country_Region'] == searchTerm]
    else:
        return dataSet[dataSet['Province_State'] == searchTerm]
