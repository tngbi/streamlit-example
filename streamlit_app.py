import streamlit as st
import pandas as pd, numpy as np
import hvplot.pandas  # Import hvPlot

# Make sure the required libraries are installed: pandas, hvplot, openpyxl

@st.cache_data  # Use the appropriate caching decorator
def load_data(year):
    excel_file = 'sample_sales_team_data.xlsx'  # Ensure this file exists in the directory
    return pd.read_excel(excel_file, sheet_name=str(year), index_col=0)

data = load_data(2022)  # Load initial data

# Team Selector
team_selector = st.sidebar.radio(
    'Team Selector',
    ['Hunter', 'Farmer', 'Channel', 'SMB']
)

# Year Slider
year_slider = st.sidebar.slider('Year', 2020, 2023, 2022)

def plot_performance(team, year):
    data = load_data(year)  # Load the appropriate year's data

    # Define colors for each type
    colors = ['blue', 'green']  # blue for Target, green for Achievement

    # Plotting Sales
    sales_plot = data.hvplot.bar(
        x='Quarter',
        y=[f'{team} Sales Target', f'{team} Sales Achievement'],
        color=colors,
        title=f'Sales Target vs Achievement for {team}, Year: {year}',
        legend='top_right'
    )

    # Plotting Revenue
    revenue_plot = data.hvplot.bar(
        x='Quarter',
        y=[f'{team} Revenue Target', f'{team} Sales Achievement'],
        color=colors,
        title=f'Revenue Target vs Achievement for {team}, Year: {year}',
        legend='top_right'
    )

    # Return both plots
    return sales_plot, revenue_plot

def main():
    st.title("Sales Dashboard")
    
    # Displaying the plots
    team = team_selector
    year = year_slider
    sales_plot, revenue_plot = plot_performance(team, year)
    
    st.write(sales_plot)
    st.write(revenue_plot)

if __name__ == "__main__":
    main()
