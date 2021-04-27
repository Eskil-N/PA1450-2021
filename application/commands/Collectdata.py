from FormatData import FormatData
def FindData(search = str):

    """Returns data from specified country"""

    data = FormatData()
    countries = data["Country_Region"]
    index = []
    result = {}

    for i in countries:

        if countries[i] == search:

            index.append(i)

    for title in list(data):

        for i in index:

            if title not in result:

                result[title] = (str(data[title][i]) + " ")

            else:

                result[title] += (str(data[title][i]) + " ")
                
    return result
