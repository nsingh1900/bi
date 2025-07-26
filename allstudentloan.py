Here’s a **beginner-friendly Python code** using **Plotly Dash** that you can run to create a **student loan portfolio characteristics dashboard**. It includes filters, charts for portfolio by servicer, delinquency trend, risk rating distribution, and average loan balance.

---

### ✅ Step 1: Install Dash and Plotly (only once)

```bash
pip install dash plotly pandas
```

---

### ✅ Step 2: Save and run this Python code (`student_loan_dashboard.py`)

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample Data (you can replace this with your actual dataset)
data = {
    'Servicer': ['SLMA', 'Nelnet', 'ACS', 'Great Lakes', 'SLMA', 'Nelnet', 'ACS', 'Great Lakes'],
    'Month': ['2023-01', '2023-01', '2023-01', '2023-01', '2023-02', '2023-02', '2023-02', '2023-02'],
    'Loan_Count': [10000, 8500, 6000, 9200, 10200, 8700, 6100, 9300],
    'Delinquency_Rate': [4.2, 5.1, 3.7, 4.8, 4.0, 5.3, 3.6, 4.7],
    'Average_Balance': [32000, 31000, 29500, 30000, 32500, 31200, 29700, 30200],
    'Risk_Rating': ['Medium', 'High', 'Low', 'Medium', 'Medium', 'High', 'Low', 'Medium']
}

df = pd.DataFrame(data)
df['Month'] = pd.to_datetime(df['Month'])

# Start Dash app
app = dash.Dash(__name__)
app.title = "Student Loan Portfolio Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Student Loan Portfolio Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Servicer:"),
        dcc.Dropdown(
            options=[{'label': servicer, 'value': servicer} for servicer in df['Servicer'].unique()],
            value=['SLMA', 'Nelnet', 'ACS', 'Great Lakes'],
            multi=True,
            id='servicer-filter'
        )
    ], style={'width': '50%', 'margin': 'auto'}),

    html.Br(),

    html.Div([
        dcc.Graph(id='loan-count-trend'),
        dcc.Graph(id='delinquency-trend'),
        dcc.Graph(id='risk-rating-pie'),
        dcc.Graph(id='avg-balance-bar')
    ])
])

# Callbacks
@app.callback(
    [Output('loan-count-trend', 'figure'),
     Output('delinquency-trend', 'figure'),
     Output('risk-rating-pie', 'figure'),
     Output('avg-balance-bar', 'figure')],
    [Input('servicer-filter', 'value')]
)
def update_dashboard(selected_servicers):
    filtered_df = df[df['Servicer'].isin(selected_servicers)]

    fig_loan = px.line(
        filtered_df, x='Month', y='Loan_Count', color='Servicer',
        title='Loan Count Trend'
    )

    fig_delinquency = px.line(
        filtered_df, x='Month', y='Delinquency_Rate', color='Servicer',
        title='Delinquency Rate Trend (%)'
    )

    pie_df = filtered_df.groupby('Risk_Rating').size().reset_index(name='Count')
    fig_risk = px.pie(
        pie_df, names='Risk_Rating', values='Count', title='Risk Rating Distribution'
    )

    avg_balance_df = filtered_df.groupby('Servicer')['Average_Balance'].mean().reset_index()
    fig_balance = px.bar(
        avg_balance_df, x='Servicer', y='Average_Balance',
        title='Average Loan Balance by Servicer'
    )

    return fig_loan, fig_delinquency, fig_risk, fig_balance

# Run server
if __name__ == '__main__':
    app.run_server(debug=True)
```

---

### 📊 Dashboard Features

* Dropdown to filter by loan servicer
* Line chart for:

  * Loan count trend
  * Delinquency rate
* Pie chart for risk rating
* Bar chart for average loan balance

---

### 📝 Next Steps

* Replace the dummy `data = {}` dictionary with your real loan portfolio dataset (e.g., from a CSV or database).
* Add metrics like `collateral coverage`, `cash flow waterfalls`, etc., if available.

Would you like a version that connects to Excel or loads CSV?
