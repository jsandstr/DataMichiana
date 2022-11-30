import pandas as pd
import matplotlib.pyplot as mp
import plotly.express as px
import geopandas
import plotly.figure_factory as ff


# Create Dataframes of data we found from online (ND Financial Aid Website)
on_housing_exp = pd.DataFrame({'Name': ['On-Campus Student Expenses'],
    'Cost': ['Housing'],
    'US Dollars ($)': [16710],
    })
on_food_exp = pd.DataFrame({'Name': ['On-Campus Student Expenses'],
    'Cost': ['Food'],
    'US Dollars ($)': [3227],
    })

# Create Dataframes of Off-Campus student expenses (taken from census and online avg food costs)
off_housing_exp = pd.DataFrame({'Name': ['Off-Campus Student Expenses'],
    'Cost': ['Housing'],
    'US Dollars ($)': [8880],
    })
off_food_exp = pd.DataFrame({'Name': ['Off-Campus Student Expenses'],
    'Cost': ['Food'],
    'US Dollars ($)': [2318],
    })

# Read in Census data on Indiana median rental housing costs
IN2020 = pd.read_csv("ArcGISData/IN2020.csv")

# Normalize data to 10 months instead of 12
in_10m_housing_cost = IN2020['SE_A18009_001'][0] * 10

# Create Dataframes for IN housing and IN Food costs
in_housing_exp = pd.DataFrame({'Name': ['Indiana Living Expenses'],
    'Cost': ['Housing'],
    'US Dollars ($)': [in_10m_housing_cost],
    })

in_food_exp = pd.DataFrame({'Name': ['Indiana Living Expenses'],
    'Cost': ['Food'],
    'US Dollars ($)': [(2872/12) * 10],
    })

# Concacatenate Dataframes
liv_df = pd.concat([on_food_exp, on_housing_exp, off_food_exp, off_housing_exp, in_housing_exp, in_food_exp])

# Use Plotly express to create bar charts of living expenses
fig = px.bar(liv_df, x="Name", y="US Dollars ($)", color="Cost", title = "10 Month Housing Costs" )
fig.show()