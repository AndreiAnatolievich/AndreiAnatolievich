# %%
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# %%
data = pd.read_csv(r'energy_1.csv')
data.head()

# %%
data['wind_direction_rad'] = data['wind_direction']*np.pi/180
data['wind_direction_sin'] = np.sin(data['wind_direction_rad'])
data['wind_direction_cos'] = np.cos(data['wind_direction_rad'])
data = data.drop(labels=['wind_direction_rad'], axis=1)

# %%
data['air_temperature_1'] = data['air_temperature'].diff()

# %%
data.at[0, 'air_temperature_1'] = data.at[1, 'air_temperature']

# %%
data['precip_depth_1_hr'] = data['precip_depth_1_hr'].apply(lambda x: x if x>0 else 0)
data_sea_level_mean = data['sea_level_pressure'].mean()
data['sea_level_pressure'] = data['sea_level_pressure'].apply(lambda x: data_sea_level_mean if x != x else 0)
data_wind_direction_mean = data['wind_direction'].mean()
data['wind_direction'] = data['wind_direction'].apply(lambda x: data_wind_direction_mean if x != x else x)
data.info()

# %%
data_temperature = data['air_temperature'].mean()
data_temperature 

# %%
data_cloud = data['cloud_coverage'].mean()
data_cloud

# %%
data_dew_temperature = data['dew_temperature'].mean()
data_dew_temperature

# %%
data['air_temperature'] = data['air_temperature'].fillna(data_temperature)

# %%
data['cloud_coverage'] = data['cloud_coverage'].fillna(data_cloud)

# %%
data['dew_temperature'] = data['dew_temperature'].fillna(data_dew_temperature)

# %%
data = data.loc[data['meter_reading'] > 0]

# %%


# %%
data = data.drop(labels=['site_id', 'building_id', 'meter', 'primary_use',
                             'square_feet', 'year_built', 'floor_count', 'wind_direction'], axis=1)
data.head()

# %%
data.head()

# %%
data_train, data_test = train_test_split(data, test_size=0.2)

# %%
model = float(data_train['meter_reading'].mean())
print('{0:.4}'.format(model))

# %%
err = np.mean(np.abs(data['meter_reading'] - model))
print('{0:.4}%'.format(100*err/model))             

# %%
data.to_csv('energy_1.csv')

# %%



