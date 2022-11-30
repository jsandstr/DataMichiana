import pandas as pd
import matplotlib.pyplot as mp
import plotly.express as px
import geopandas
import plotly.figure_factory as ff

# Read Stata file of Parent Incomes
data3 = pd.read_stata('ArcGISData/mrc_table3.dta')

# class of 2001 to 2012 (estimated off of birth years)
years = list(data3.cohort[data3.name == "University Of Notre Dame"])


# Attempt at Geo plot, but library does not support census tracts FIPS
"""
geo_df = geopandas.read_file("ArcGISData/StJoseph2019.csv")

 print(geo_df.geometry.y, geo_df.geometry.x)
fig = px.scatter_geo(geo_df,
                    lat=geo_df.geometry.y,
                    lon=geo_df.geometry.x,
                    hover_name="Geo_NAME"
                    )
fig.show() """

# Normalize Years to Graduating Class
for i in range(len(years)):
    years[i] += 21

# Take median and mean parent data from dataframe
par_median = list(data3.par_median[data3.name == "University Of Notre Dame"])
par_mean = list(data3.par_mean[data3.name == "University Of Notre Dame"])

# Take South Bend Median Income 2 mi radius of ND (Hardcoded) -- Potentially change in future
sb_med_income = [[n for n in range(2009, 2021, 1)]]
sb_med_income.append([41081, 36028, 38673, 39401, 39548, 38372, 39558, 40371, 41380, 45769, 46753, 51908])

# Plot ND mean household income, median household income, and SB median income
mp.plot(years, par_mean, label = 'ND Parent Household Income Mean')
mp.plot(years, par_median, label='ND Parent Household Income Median')
mp.plot(sb_med_income[0], sb_med_income[1], label = "South Bend Median Income (2 mile radius of ND)")

# Label x and y axis and title
mp.xlabel('Years')
mp.ylabel('US Dollars ($)')
mp.title('University of Notre Dame Household Income Mean and Median vs Kid\'s Graduation Year')

mp.legend()
mp.show()