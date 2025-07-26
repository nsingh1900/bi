# Sample mock data and layout concept for "Court Resource Allocation Dashboard"
import pandas as pd
import plotly.express as px

# Sample data
court_data = pd.DataFrame({
    'Court': ['County A', 'County B', 'County C', 'County D'],
    'Judges': [12, 8, 15, 10],
    'Support Staff': [40, 25, 55, 30],
    'Cases Filed': [12000, 8500, 16000, 11000],
    'Cases Resolved': [11000, 8000, 15500, 10500],
    'Region': ['North', 'South', 'East', 'West']
})

# Calculate derived metrics
court_data['Cases Per Judge'] = court_data['Cases Filed'] / court_data['Judges']
court_data['Resolution Rate'] = court_data['Cases Resolved'] / court_data['Cases Filed']

# Visualization 1: Workload per Judge by Court
fig1 = px.bar(court_data, x='Court', y='Cases Per Judge', title='Workload Per Judge by Court')
fig1.show()

# Visualization 2: Resolution Rate by Court
fig2 = px.bar(court_data, x='Court', y='Resolution Rate', title='Resolution Rate by Court', text='Resolution Rate')
fig2.update_traces(texttemplate='%{text:.2%}', textposition='outside')
fig2.show()

# Visualization 3: Regional Resource Allocation Heatmap
fig3 = px.treemap(court_data, path=['Region', 'Court'], values='Support Staff', 
                  title='Support Staff Allocation by Region and Court')
fig3.show()
