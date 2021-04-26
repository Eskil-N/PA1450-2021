import plotly.express as px
import math
#import DataFormater

def CRDataPrepper(formatedData, searchedCategory):
    sortedDict = {'Country_Region': [], 'Data' : []}
    tempDict = {}
    for x in formatedData['Country_Region'].items():
        if x[1] in tempDict:
            tempDict[x[1]] += formatedData[searchedCategory][x[0]]
        else:
            tempDict[x[1]] = formatedData[searchedCategory][x[0]]

    tempDict = dict(sorted(tempDict.items(), key=lambda item: item[1])) 

    for key, val in tempDict.items():
        sortedDict['Country_Region'].append(key)
        sortedDict['Data'].append(val)

    return sortedDict #Dict is structures like others produced from Dataformater with one category for province/state and another for the data but sorted.

def PSDataPrepper(formatedData, searchedCategory, searchedCountry): #Function returns a dict containing all province/states and its selected category data from selected country.
    sortedDict = {'Province_State' : [], 'Data' : []}
    tempDict = {}
    for x, y in zip(formatedData['Country_Region'].items(), formatedData['Province_State'].items()):
        if (x[1] == searchedCountry):
            if y[1] in tempDict:
                tempDict[y[1]] += formatedData[searchedCategory][y[0]]
            else:
                tempDict[y[1]] = formatedData[searchedCategory][y[0]]

    tempDict = dict(sorted(tempDict.items(), key=lambda item: item[1])) 

    for key, val in tempDict.items():
        sortedDict['Province_State'].append(key)
        sortedDict['Data'].append(val)

    return sortedDict #Dict is structures like others produced from Dataformater with one category for province/state and another for the data but sorted.

def IRCDataPrepper(formatedData):
    sortedDict = {'Country_Region' : [], 'Infection Rate per 100k Population' : []}
    tempDict = {}
    tempIndexDict = {}
    itterationsList = []
    for x in formatedData['Country_Region'].items():
        if x[1] in tempDict:
            if not math.isnan(formatedData['Incident_Rate'][x[0]]): #Need this since there are wierd fucking nan vals in the data
                tempDict[x[1]] += formatedData['Incident_Rate'][x[0]]
                tempIndexDict[x[1]] += 1
        else:
            if not math.isnan(formatedData['Incident_Rate'][x[0]]):
                tempDict[x[1]] = formatedData['Incident_Rate'][x[0]]
                tempIndexDict[x[1]] = 1
    
    for x in tempDict.items():
        tempDict[x[0]] = round((tempDict[x[0]])/(tempIndexDict[x[0]]), 2) #Calculating cumulative value from all regions / number of regions to get average across whole country.

    tempDict = dict(sorted(tempDict.items(), key=lambda item: item[1])) 
    
    for key, val in tempDict.items():
        sortedDict['Country_Region'].append(key)
        sortedDict['Infection Rate per 100k Population'].append(val)

    return sortedDict #Dict is structures like others produced from Dataformater with one category for province/state and another for the data but sorted.

def CreateCountryBar(formatedData, searchedCategory):
    myDict = CRDataPrepper(formatedData, searchedCategory)
    print(myDict)
    fig = px.bar(myDict, x='Country_Region', y='Data')
    fig.show()

def CreateRegionBar(formatedData, searchedCategory, searchedCountry): #function creates a sorted bar chart from provided Dict.
    myDict = PSDataPrepper(formatedData, searchedCategory, searchedCountry)
    #print(myDict)
    fig = px.bar(myDict, x='Province_State', y='Data')
    fig.show()

def CreateIRCountryBar(formatedData):
    myDict = IRCDataPrepper(formatedData)
    print(myDict)
    fig = px.bar(myDict, x='Country_Region', y='Infection Rate per 100k Population')
    fig.show()

#def CreateIRRegionBar(formatedData, searchedCountry):

