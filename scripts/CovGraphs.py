import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import math

def Comp_DataPrepper(formatedData, country1, country2, searchedCategory):
    CombinedFrame = pd.DataFrame()
    for index, row in formatedData.iterrows():
        if (row['Country_Region'] == country1):
            if (CombinedFrame.empty):
                row['Color'] = 'crimson'
                CombinedFrame = CombinedFrame.append(row)
            else:
                if (row['Province_State'] in CombinedFrame['Province_State']):
                    CombinedFrame['Province_state'][searchedCategory] += row[searchedCategory]
                else:
                    row['Color'] = 'crimson'
                    CombinedFrame = CombinedFrame.append(row)
        if (row['Country_Region'] == country2):
            if (CombinedFrame.empty):
                row['Color'] = 'cyan'
                CombinedFrame = CombinedFrame.append(row)
            else:
                if (row['Province_State'] in CombinedFrame['Province_State']):
                    CombinedFrame['Province_state'][searchedCategory] += row[searchedCategory]
                else:
                    row['Color'] = 'cyan'
                    CombinedFrame = CombinedFrame.append(row)

    SortedFrame = CombinedFrame.sort_values([searchedCategory], ascending=True)
    
    return SortedFrame 

def Comp_IR_DataPrepper(formatedData, country1, country2):
    CombinedDict = IR_PS_DataPrepper(formatedData,country1)
    print(CombinedDict, '\n\n\n')
    tempDict = IR_PS_DataPrepper(formatedData,country2)
    
    #CombinedDict.update(tempDict)
    for key, val in zip(tempDict['Province_State'],tempDict['Infection Rate per 100k Population']):
        print(key , ' ' ,val , '\n')
        CombinedDict['Province_State'].append(key)
        CombinedDict['Infection Rate per 100k Population'].append(val)
    
    #for item in CombinedDict:
    #    if math.isnan(item[1]):
    #        CombinedDict.pop(item)
    #dict(sorted(CombinedDict.items(), key=lambda item: item[1]))
    print(CombinedDict)
    return(CombinedDict)

def CR_DataPrepper(formatedData, searchedCategory): # General Country_Region Dapa prepper. Takes in whole dataset and returns a dict that can be used with plotly.
    formatedData = formatedData.to_dict()
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

def PS_DataPrepper(formatedData, searchedCategory, searchedCountry): # General Province_State Data prepper. Takes in whole dataset, specified category, can country.
    formatedData = formatedData.to_dict()
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


def IR_PS_DataPrepper(formatedData, searchedCountry):
    formatedData = px.DataFrame(columns=['Country','Region','Infection Rate per 100k Population'])
    for x,y,z in zip(formatedData['Country_Region'].items(), formatedData['Province_State'].items(), formatedData['Incident_Rate'].items()):
        formatedData.loc['y'] = pandas.Series({'Country':x, 'Region':y, 'Infection Rate per 100k Population':z})

def IR_PS_DataPrepper(formatedData, searchedCountry): #Data prepper for Province_State with regards to Incident_Rate. Calculates average IR for State_Province in specified country and returns it as a sorted dict.
    formatedData = formatedData.to_dict()
    sortedDict = {'Province_State' : [], 'Infection Rate per 100k Population' : []}
    tempDict = {}
    tempIndexDict = {}
    for x,y in zip(formatedData['Country_Region'].items(), formatedData['Province_State'].items()):
        if (x[1] == searchedCountry):
            if formatedData['Province_State'][x[0]] in tempDict:
                if not math.isnan(formatedData['Incident_Rate'][x[0]]):
                    tempDict[y[1]] += formatedData['Incident_Rate'][x[0]]
                    tempIndexDict[y[1]] += 1
            else:
                if not math.isnan(formatedData['Incident_Rate'][x[0]]):
                    tempDict[y[1]] = formatedData['Incident_Rate'][x[0]]
                    tempIndexDict[y[1]] = 1
    
    for x in tempDict.items():
        tempDict[x[0]] = round((tempDict[x[0]])/(tempIndexDict[x[0]]), 2)
    
    tempDict = dict(sorted(tempDict.items(), key=lambda item: item[1]))

    for key, val in tempDict.items():
        sortedDict['Province_State'].append(key)
        sortedDict['Infection Rate per 100k Population'].append(val)
    
    return sortedDict

def IR_C_DataPrepper(formatedData): #Incident_Rate Data prepper for Country_Region. Returns a sorted Dict with a countries average IR that can be used with plotly.
    formatedData = formatedData.to_dict()
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

def CreateCountryBar(formatedData, searchedCategory):# Creates and dissplays a bar chart with countries and specified categorys, will only work with cumulative data like deaths, confirmed
    myDict = CR_DataPrepper(formatedData, searchedCategory)
    #print(myDict)
    fig = px.bar(myDict, x='Country_Region', y='Data')
    fig.update_layout(title_text='Graph of ' + searchedCategory)
    fig.show()

def CreateRegionBar(formatedData, searchedCategory, searchedCountry): #function creates a sorted bar chart of regions of a country, and specified data category.
    myDict = PS_DataPrepper(formatedData, searchedCategory, searchedCountry)
    #print(myDict)
    fig = px.bar(myDict, x='Province_State', y='Data')
    fig.update_layout(title_text='Graph of ' + searchedCategory + ' in ' + searchedCountry)
    fig.show()

def CreateIRCountryBar(formatedData): #function creates a sorted bar chart with countries and thier respective infection rate per 100k people.
    myDict = IR_C_DataPrepper(formatedData)
    #print(myDict)
    fig = px.bar(myDict, x='Country_Region', y='Infection Rate per 100k Population')
    fig.update_layout(title_text='Graph of Infections per Capita')
    fig.show()

def CreateIRRegionBar(formatedData, searchedCountry): #function creates a sorted bar chart with Regions of selected country and thier respective infection rates per 100k people.
    myDict = IR_PS_DataPrepper(formatedData,searchedCountry)
    #print(myDict)
    fig = px.bar(myDict, x='Province_State', y='Infection Rate per 100k Population')
    fig.update_layout(title_text='Graph of Infections per Capita in' + searchedCountry)
    fig.show()

def CompareIRCountryBar(formatedData, country1, country2):
    Combined = Comp_IR_DataPrepper(formatedData, country1, country2)
    fig = px.bar(Combined, x='Province_State', y='Infection Rate per 100k Population')
    fig.show()

def CompareCountryBar(formatedData, country1, country2, searchedCategory): #Exempel p[ hur man callar funktionen: CompareCountryBar(data,'Germany','Sweden','Confirmed')]
    Combined = Comp_DataPrepper(formatedData,country1,country2,searchedCategory)
    fig = go.Figure(data=[go.Bar( x=Combined['Province_State'], y=Combined[searchedCategory], marker_color=Combined['Color'])])
    fig.update_layout(title_text='Graph of ' + searchedCategory + ' in ' + country1 + ' and '+ country2)
    fig.show()
    
