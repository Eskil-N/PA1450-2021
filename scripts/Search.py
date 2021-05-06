def isCountry(dataSet, searchTerm):
    for item in dataSet['Country_Region'].items():
        if (item[1] == searchTerm):
            return True
    return False

def Search(dataSet, searchTerm):
    if (isCountry(dataSet, searchTerm)):
        return dataSet[dataSet['Country_Region'] == searchTerm]
    else:
        return dataSet[dataSet['Province_State'] == searchTerm]
