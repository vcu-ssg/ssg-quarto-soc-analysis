import pandas as pd
import panel as pn
pn.extension('tabulator')

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Value1': [10, 20, 30],
        'Value2': [15, 10, 5]}
df = pd.DataFrame(data)
df['Bar'] = ''  # Placeholder column for the bar chart

# JavaScript formatter
formatter = """
function(cell, formatterParams, onRendered){
    var value1 = cell.getRow().getData().Value1;
    var value2 = cell.getRow().getData().Value2;
    var maxVal = Math.max(...cell.getTable().getData().map(row => row.Value1 + row.Value2));
    var width1 = 100 * (value1 / maxVal);
    var width2 = 100 * (value2 / maxVal);
    return '<div style="width: 100%; display: flex; height: 100%; align-items: center;">' +
           '<div style="width:' + width1 + '%; background-color: blue; height: 100%"></div>' +
           '<div style="width:' + width2 + '%; background-color: red; height: 100%"></div>' +
           '</div>';
}
"""

# Setting up the Tabulator widget
tabulator = pn.widgets.Tabulator(df, width=400, height=300, formatters={'Bar': {'type': 'html', 'formatter': formatter}})

tabulator.servable()
