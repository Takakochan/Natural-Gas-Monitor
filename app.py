import pandas as pd
from matplotlib.pylab import *
import os

html = os.path.join('data', 'gas.html')
gasprice = os.path.join('data', 'NaturalGas FuturesHistoricalData.csv')

tables = pd.read_html(html)
df = tables[0]
gas = tables[0]
gas = gas.drop('Unnamed: 5', axis=1)
gas = gas.dropna()

gas['Actual'] = gas['Actual'].str.extract(r'(-?\d+)').astype(int)
gas['Forecast'] = gas['Forecast'].str.extract(r'(-?\d+)').astype(int)
gas = gas.reset_index()
gas = gas.sort_index(ascending=False)

price = pd.read_csv(gasprice)
price = price.sort_index(ascending=False)
df2 = price['Price'].tail(50)
df1 = gas.tail(50)
gas = pd.concat([df1, df2], axis=1)

fig = plt.figure()
ax = gas.tail(30).plot(x='Release Date',
                       y=['Actual', 'Forecast'],
                       title='Natural Gas EIA & Price')
gas.tail(29).plot(x='Release Date', y=['Price'], secondary_y=True, ax=ax)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, fontsize=10)
st.write('EIA Natural Gas Storage and Natural Gas Future Price')
st.pyplot(plt)
#print(gas.tail(50))
