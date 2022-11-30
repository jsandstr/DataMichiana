import pandas as pd
import matplotlib.pyplot as mp
import plotly.express as px
import geopandas
import plotly.figure_factory as ff

#means1 is 2 mi ND, and means2 is SB
means1, means2 = [], []

# Read in ND 2 mile census data and take mean of census tracts and append to array of means1
nd1980 = pd.read_csv("ArcGISData/ND1980.csv")
means1.append(nd1980["SE_T167_001"].mean())
nd1990 = pd.read_csv("ArcGISData/ND1990.csv")
means1.append(nd1990["SE_T167_001"].mean())
nd2000 = pd.read_csv("ArcGISData/ND2000.csv")
means1.append(nd2000["SE_T167_001"].mean())
nd2010 = pd.read_csv("ArcGISData/ND2010.csv")
means1.append(nd2010["SE_A18009_001"].mean())
nd2020 = pd.read_csv("ArcGISData/ND2020.csv")
means1.append(nd2020["SE_A18009_001"].mean())

# Read in SB census data and take mean of census tracts and append to array of means2
sb1980 = pd.read_csv("ArcGISData/SB1980.csv")
means2.append(sb1980["SE_T167_001"].mean())
sb1990 = pd.read_csv("ArcGISData/SB1990.csv")
means2.append(sb1990["SE_T167_001"].mean())
sb2000 = pd.read_csv("ArcGISData/SB2000.csv")
means2.append(sb2000["SE_T167_001"].mean())
sb2010 = pd.read_csv("ArcGISData/SB2010.csv")
means2.append(sb2010["SE_A18009_001"].mean())
sb2020 = pd.read_csv("ArcGISData/SB2020.csv")
means2.append(sb2020["SE_A18009_001"].mean())


# Create inflation line with 41 y axis points intiialized to 1st census data point from means1
inflation = [means1[0]] * 41
# With avg inflation of 2.9%, show how inital housing price cost would translate with standard US inflation
for i in range(1, len(inflation)):
    inflation[i] = 1.0295 * inflation[i-1]
# Create 41 correlating x axis points for years 1980 to 2020
inflation_years = [*range(1980,2021,1 )]

# years is every 10 years from 1980 to 2020 for every census year
years = [*range(1980, 2021,10)]

# Create data frames for 3 lines

# Inflation Line
df1 = pd.DataFrame({'Name' : ['US dollar inflation'] * len(inflation_years),
    'Years': inflation_years,
    'US Dollars ($)': inflation})

# ND 2 mi radius median rent line
df2 = pd.DataFrame({'Name' : ['ND 2 mile radius median gross rent'] * len(means1),
    'Years': years,
    'US Dollars ($)': means1})

# SB median rent line
df3 = pd.DataFrame({'Name' : ['South Bend median gross rent'] * len(means2),
    'Years': years,
    'US Dollars ($)': means2})

# concatenate datafeames
df = pd.concat([df1,df2,df3])

# Create line graph
fig = px.line(df, x = 'Years', y = 'US Dollars ($)', color = 'Name', markers = True)
fig.show()
