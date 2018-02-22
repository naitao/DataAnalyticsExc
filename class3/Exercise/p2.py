import pandas as pd
import os
path = 'data'
vehicles = pd.read_csv(os.path.join(path, 'vehicles.csv'))

select_columns = ['make', 'model', 'year', 'displ', 'cylinders', 'trany', 'drive', 'VClass', 'fuelType', 'barrels08', 'city08', 'highway08', 'comb08', 'co2TailpipeGpm', 'fuelCost08']

vehicles = vehicles[select_columns][vehicles.year <= 2-16].drop_duplicates().dropna()

vehicles = vehicles.sort_values(['make', 'model', 'year'])

vehicles.columns = ['Make','Model','Year','Engine Displacement','Cylinders',
                    'Transmission','Drivetrain','Vehicle Class','Fuel Type',
                    'Fuel Barrels/Year','City MPG','Highway MPG','Combined MPG',
                    'CO2 Emission Grams/Mile','Fuel Cost/Year']

def unique_col_values(df):
    for column in df:
        print("{} | {} | {}".format(
            df[column].name, len(df[column].unique()), df[column].dtype))

unique_col_values(vehicles)

#Let's create a new Transmission Type column in our data frame and, with the help of the loc method in pandas, assign it a value of Automatic where the first character of Transmission is the letter A and a value of Manual where the first character is the letter M.

AUTOMATIC = "Automatic"
MANUAL = "Manual"

print('Display vehicles:', vehicles)
vehicles.loc[vehicles]
#vehicles.loc[vehicles['Transmission'].str.startswith('A'), 'Transmission Type'] = AUTOMATIC
#vehicles.loc[vehicles['Transmission'].str.startswith('M'), 'Transmission Type'] = MANUAL
