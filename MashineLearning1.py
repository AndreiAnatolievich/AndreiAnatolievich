# %%
import numpy as np
import pandas as pd

# %%
data_1 = pd.read_csv(r'energy_1.csv')

# %%
data_1['timestamp'] = pd.to_datetime(data_1['timestamp'])
data_1['hour'] = data_1['timestamp'].dt.hour

# %%
data_1.to_csv('energy_2.csv', index=False)

# %%
std = np.std(data_1['meter_reading'])
print('{0: .4}'.format(std))

# %%
model = float(data_1['meter_reading'].mean())
err = np.mean(np.abs(data_1['meter_reading']-model))
print('Model: {0: .4},'.format(model),
      'Mistake of model: {0: .4}%,'.format(100*err/model),
      'Mistake of data: {0: .4}%'.format(std/model))

# %%
data_0 = data_1.loc[data_1['hour'] == 0]

# %%
model_0 = float(data_0['meter_reading'].mean())
err_0 = np.mean(np.abs(data_0['meter_reading']-model_0))
print('Model: {0: .4},'.format(model_0),
      'Mistake of model hour: {0: .4}%,'.format(100*err_0/model_0),
      'Mistake of basic model: {0: .4}%'.format(100*err/model))

# %%
print(model, err, err_0, std)

# %%
data1 = data_1.loc[data_1['hour'] == 1]

# %%
model_1 = float(data1['meter_reading'].mean())
err_1 = np.mean(np.abs(data1['meter_reading']-model_1))
print('Model: {0: .4},'.format(model_1),
      'Mistake of model hour: {0: .4}%,'.format(100*err_1/model_1))

# %%
data2 = data_1.loc[data_1['hour'] == 2]

# %%
model2 = float(data2['meter_reading'].mean())
err2 = np.mean(np.abs(data2['meter_reading']-model2))
print('Model: {0: .4},'.format(model2),
      'Mistake of model hour: {0: .4}%,'.format(100*err2/model2))

# %%
data3 = data_1.loc[data_1['hour'] == 3]
data4 = data_1.loc[data_1['hour'] == 4]
data5 = data_1.loc[data_1['hour'] == 5]
data6 = data_1.loc[data_1['hour'] == 6]
data7 = data_1.loc[data_1['hour'] == 7]
data8 = data_1.loc[data_1['hour'] == 8]
data9 = data_1.loc[data_1['hour'] == 9]
data10 = data_1.loc[data_1['hour'] == 10]
data11 = data_1.loc[data_1['hour'] == 11]

# %%
data12 = data_1.loc[data_1['hour'] == 12]
data13 = data_1.loc[data_1['hour'] == 13]
data14 = data_1.loc[data_1['hour'] == 14]
data15 = data_1.loc[data_1['hour'] == 15]
data16 = data_1.loc[data_1['hour'] == 16]
data17 = data_1.loc[data_1['hour'] == 17]
data18 = data_1.loc[data_1['hour'] == 18]
data19 = data_1.loc[data_1['hour'] == 19]
data20 = data_1.loc[data_1['hour'] == 20]
data21 = data_1.loc[data_1['hour'] == 21]
data22 = data_1.loc[data_1['hour'] == 22]
data23 = data_1.loc[data_1['hour'] == 23]

# %%
model3 = float(data3['meter_reading'].mean())
err3 = np.mean(np.abs(data3['meter_reading']-model3))
print('Model: {0: .4},'.format(model3),
      'Mistake of model hour: {0: .4}%,'.format(100*err3/model3))

# %%
model4 = float(data4['meter_reading'].mean())
err4 = np.mean(np.abs(data4['meter_reading']-model4))
print('Model: {0: .4},'.format(model4),
      'Mistake of model hour: {0: .4}%,'.format(100*err4/model4))

# %%
model10 = float(data10['meter_reading'].mean())
err10 = np.mean(np.abs(data10['meter_reading']-model10))
print('Model: {0: .4},'.format(model2),
      'Mistake of model hour: {0: .4}%,'.format(100*err10/model10))

# %%
model15 = float(data15['meter_reading'].mean())
err15 = np.mean(np.abs(data15['meter_reading']-model15))
print('Model: {0: .4},'.format(model15),
      'Mistake of model hour: {0: .4}%,'.format(100*err15/model15))

# %%
model20 = float(data20['meter_reading'].mean())
err20 = np.mean(np.abs(data20['meter_reading']-model20))
print('Model: {0: .4},'.format(model20),
      'Mistake of model hour: {0: .4}%,'.format(100*err20/model20))

# %%
model23 = float(data23['meter_reading'].mean())
err23 = np.mean(np.abs(data23['meter_reading']-model23))
print('Model: {0: .4},'.format(model23),
      'Mistake of model hour: {0: .4}%,'.format(100*err23/model23))

# %%
data_1['timestamp'] = pd.to_datetime(data_1['timestamp'])
data_1['day'] = data_1['timestamp'].dt.day

# %%
data_1.to_csv('energy_3.csv', index=False)

# %%
data014 = data_1.loc[data_1['day'] == 014]

# %%
model014 = float(data014['meter_reading'].mean())
err014 = np.mean(np.abs(data014['meter_reading']-model014))
print('Model: {0: .4},'.format(model014),
      'Mistake of model hour: {0: .4}%,'.format(100*err014/model014))

# %%
data026 = data_1.loc[data_1['day'] == 26]
data022 = data_1.loc[data_1['day'] == 22]
data018 = data_1.loc[data_1['day'] == 18]
data014 = data_1.loc[data_1['day'] == 14]
data010 = data_1.loc[data_1['day'] == 10]
data06 = data_1.loc[data_1['day'] == 6]
data02 = data_1.loc[data_1['day'] == 2]

# %%
model026 = float(data026['meter_reading'].mean())
err026 = np.mean(np.abs(data026['meter_reading']-model026))
print('Model: {0: .4},'.format(model026),
      'Mistake of model hour: {0: .4}%,'.format(100*err026/model026))

# %%
model022 = float(data022['meter_reading'].mean())
err022 = np.mean(np.abs(data022['meter_reading']-model022))
print('Model: {0: .4},'.format(model022),
      'Mistake of model hour: {0: .4}%,'.format(100*err022/model022))

# %%
model018 = float(data018['meter_reading'].mean())
err018 = np.mean(np.abs(data018['meter_reading']-model018))
print('Model: {0: .4},'.format(model018),
      'Mistake of model hour: {0: .4}%,'.format(100*err018/model018))

# %%
model014 = float(data014['meter_reading'].mean())
err014 = np.mean(np.abs(data014['meter_reading']-model014))
print('Model: {0: .4},'.format(model014),
      'Mistake of model hour: {0: .4}%,'.format(100*err014/model014))

# %%
model010 = float(data010['meter_reading'].mean())
err010 = np.mean(np.abs(data010['meter_reading']-model010))
print('Model: {0: .4},'.format(model010),
      'Mistake of model hour: {0: .4}%,'.format(100*err010/model010))

# %%
model06 = float(data06['meter_reading'].mean())
err06 = np.mean(np.abs(data06['meter_reading']-model06))
print('Model: {0: .4},'.format(model06),
      'Mistake of model hour: {0: .4}%,'.format(100*err06/model06))

# %%
model02 = float(data02['meter_reading'].mean())
err02 = np.mean(np.abs(data02['meter_reading']-model02))
print('Model: {0: .4},'.format(model02),
      'Mistake of model hour: {0: .4}%,'.format(100*err02/model02))

# %%



