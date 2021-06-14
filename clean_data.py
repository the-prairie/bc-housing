# importing necessary packages
import pandas as pd
import json
import os
import numpy as np

# get path to json files in directory
# grab all .json files from data folder
path_to_json = '/Users/zar/Desktop/projects/big-burt/bc-house/data-files'
files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


# initialize empty list to store loaded json files into for aggregation
data_raw = []
for file in files:
    with open(path_to_json+'/'+file) as f:
        data_raw.append(json.load(f))
        

# set list of headers for data (had to manually fill in since response did not provide header row)
header = ['mls_number',
'latitude',
'longitude',
'listing_date',
'neighborhood_profile',
'address',
'neighborhood',
'price_asking_final',
'description',
'property_type',
'architecture_style',
'age',
'bedrooms',
'bathrooms',
'house_sqft',
'lot_frontage',
'lot_depth',
'buyers_agent_name',
'buyers_agent_company',
'unknown7',
'sellers_agent_company',
'sellers_agent_name',
'sellers_agent_phone',
'sellers_agent_email',
'sellers_agent_website',
'price_asking_original',
'asking_price_date',
'property_taxes',
'price_final_asking',
'land_sqft',
'features',
'basement',
'price_final_sold',
'date_sold',
'date_reported',
'postal_code',
'city',
'unknown13',
'year_property_tax_reference',
'unknown15',
'virtual_tour_link',
'listing_timestamp',
'web_listing_number',
'price_to_assessment_ratio',
'roof_type',
'heating_type',
'water_supply',
'zoning',
'room1',
'room2',
'room3',
'room4',
'room5',
'room6',
'room7',
'room8',
'room9',
'room10',
'room11',
'room12',
'room13',
'room14',

'room15',
'room16',
'room17',
'room18',
'room19',
'room20',
'room21',
'room22',
'room23',
'room24',
'room25',
'room26',
'room27',
'room28',
'fireplaces',
'backyard_features',
'parking_total_covered',
'suite_type',     
'rear_yard_exposure',
'pet_policy',
'maintenance_fee',
'unknown20',
'construction_method',
'foundation',
'flooring',
'exterior_finish',
'sqft_area_above_ground',
'sqft_area_main_floor',
'sqft_area_below_ground',
'sqft_area_basement',
'sqft_property',
'sqft_area_unfinished',
'number_of_storeys',
'renovations',
'parking_access',
'bathroom1',
'bathroom2',
'bathroom3',
'bathroom4',
'bathroom5',
'bathroom6',
'bathroom7',
'bathroom8',
'bathroom9',
'unknown27',
'coordinates',
'unknown28',
'unknown29',
'unknown30',
'blank31',
'blank32',
'blank33',
'blank34',
'blank35',
'blank36',
'blank37',
'blank38',
'blank39',
'blank40',
'unknown31',
'blank41',
'buyers_agent_commission',
'unknown32',
'blank42',
'blank43',
'blank44',
'blank45',
'blank46',
'blank47',
'blank48',
'blank49',
'blank50',
'region',
'blank51',
'ownership_interest',
'property_id',
'image_links',
'is_sold_or_active',
'app_link',
'blank52',
'blank53',
'unknown34',
 ]


# initialize list to store dataframes
# loop through json files and convert to pandas dataframe
data = []
for d in data_raw:
    data.append(pd.DataFrame(d['rows'], columns=header))
    
# concatenate dataframes into a single dataframe    
df = pd.concat(data)


# replace blank fields with NaN for analyzing missing values
df.replace('', np.nan, inplace=True)

# drop duplicate entries (mls number should be unique)
df.drop_duplicates(subset='mls_number', inplace=True)


# save dataset to csv file
df.to_csv(str(os.getcwd())+'/'+'bc_housing_data.csv', index=False)