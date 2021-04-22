import plotly.express as px
import DataFormater

formatedData = DataFormater.FormatData()
for item in formatedData.items():
    print(item)

fig = px.bar(formatedData, x='Country_Region', y='Confirmed')
fig.write_html('Confirmed.html', auto_open=True)
