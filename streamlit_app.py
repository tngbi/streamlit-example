import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Replace st.cache_data with st.cache, as st.cache_data is not standard in Streamlit
@st.cache_data
def load_data(year):
    excel_file = 'sample_sales_team_data.xlsx'  # Ensure this file exists in the directory
    return pd.read_excel(excel_file, sheet_name=str(year), index_col=0)

# Load initial data
data = load_data(2022)

# Team Selector
team_selector = st.sidebar.radio('Team Selector', ['Hunter', 'Farmer', 'Channel', 'SMB'])

# Year Slider
year_slider = st.sidebar.slider('Year', 2020, 2023, 2022)

def plot_performance(team, year):
    data = load_data(year)  # Load the appropriate year's data

    # Creating two subplots for sales and revenue
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

    # Plotting Sales
    data[[f'{team} Sales Target', f'{team} Sales Achievement']].plot(kind='bar', ax=axes[0], color=['blue', 'green'])
    axes[0].set_title(f'Sales Target vs Achievement for {team}, Year: {year}')
    axes[0].set_xlabel('Quarter')
    axes[0].set_ylabel('Sales')

    # Plotting Revenue
    data[[f'{team} Revenue Target', f'{team} Sales Achievement']].plot(kind='bar', ax=axes[1], color=['blue', 'green'])
    axes[1].set_title(f'Revenue Target vs Achievement for {team}, Year: {year}')
    axes[1].set_xlabel('Quarter')
    axes[1].set_ylabel('Revenue')

    # Adjusting layout
    plt.tight_layout()

    return fig

def main():
    st.title("Sales Dashboard")

    # Displaying the plots
    team = team_selector
    year = year_slider
    plot_fig = plot_performance(team, year)

    st.pyplot(plot_fig)

if __name__ == "__main__":
    main()
