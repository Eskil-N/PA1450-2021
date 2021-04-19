import pandas as pd
import datetime as dt

def FormatData():

    """Gets yesterdays data from John Hopkins University Covid-19 Data Repository and converts it into a dictionary"""

    time = (dt.date.today() - dt.timedelta(1)).strftime('%m-%d-%Y') # Get yesterdays date: month-day-year
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + time + ".csv" # Finds correct url for yesterdays stats
        
    data = pd.read_csv(url, sep=",", header=[0]) # Gets all information from selected url

    return data.to_dict() # Converts Dataframe into Dictionary
