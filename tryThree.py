import pandas as pd
import numpy as np
df = pd.read_csv('Data/Traffic_Data_5.csv')
df.head()
print(df.describe())
df.shape
print(df.info())
df.isnull().sum()
# Data Cleaning
df['Traffic Volume'] = df['Traffic Volume'].interpolate(method='linear')
df['Weather Conditions'].fillna(df['Weather Conditions'].mode()[0], inplace=True)
df['Average Speed'].fillna(df['Average Speed'].mean(), inplace=True)
df.isnull().sum()
df['Date'].fillna(method='ffill', inplace=True)
df['Road/Intersection Name'].fillna(method='ffill', inplace=True)
df['Travel Time Index'] = df['Travel Time Index'].interpolate(method='linear')
df['Congestion Level'] = df['Congestion Level'].interpolate(method='linear')
df['Road Capacity Utilization'] = df['Road Capacity Utilization'].interpolate(method='linear')
df['Incident Reports'].fillna(df['Incident Reports'].mode()[0], inplace=True)
df['Environmental Impact'] = df['Environmental Impact'].interpolate(method='linear')
df['Public Transport Usage'] = df['Public Transport Usage'].fillna(df['Public Transport Usage'].rolling(7, min_periods=1).mean())
df['Pedestrian and Cyclist Count'] = df['Pedestrian and Cyclist Count'].interpolate(method='linear')
df['Roadwork and Construction Activity'].fillna(df['Roadwork and Construction Activity'].mode()[0], inplace=True)
df.isnull().sum()

print(df['Weather Conditions'].unique())
print(df['Road/Intersection Name'].nunique())
print(df['Road/Intersection Name'].unique()) 
import matplotlib.pyplot as plt
import seaborn as sns

# Plot distribution for each numerical feature
numerical_columns = ["Traffic Volume", "Average Speed", "Travel Time Index", "Congestion Level",
                     "Road Capacity Utilization", "Incident Reports", "Environmental Impact", 
                     "Public Transport Usage",  
                     "Pedestrian and Cyclist Count"]

plt.figure(figsize=(16, 12))
for i, col in enumerate(numerical_columns, 1):
    plt.subplot(4, 3, i)
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()
# Compute the correlation matrix
correlation_matrix = df[numerical_columns].corr()

# Plot a heatmap of correlations
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.show()
# Boxplot of 'Traffic Volume' across different 'Weather Conditions'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Weather Conditions', y='Traffic Volume', data=df)
plt.title('Traffic Volume across Weather Conditions')
plt.xticks(rotation=45)
plt.show()

# Similar plot for 'Road/Intersection Name'
plt.figure(figsize=(12, 6))
sns.boxplot(x='Road/Intersection Name', y='Traffic Volume', data=df)
plt.title('Traffic Volume across Road/Intersection Name')
plt.xticks(rotation=90)
plt.show()
# Plot Traffic Volume over time
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
plt.figure(figsize=(14, 6))
plt.plot(df['Date'], df['Traffic Volume'], label='Traffic Volume')
plt.title('Traffic Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Traffic Volume')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Average Traffic Volume by Day of Week
df['Day of Week'] = df['Date'].dt.dayofweek  
avg_traffic_by_day = df.groupby('Day of Week')['Traffic Volume'].mean()

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_traffic_by_day.index, y=avg_traffic_by_day.values)
plt.title('Average Traffic Volume by Day of Week')
plt.xlabel('Day of Week (0=Mon, 6=Sun)')
plt.ylabel('Average Traffic Volume')
plt.show()
# Compare Traffic Volume based on roadwork and construction activity
plt.figure(figsize=(10, 6))
sns.boxplot(x='Roadwork and Construction Activity', y='Traffic Volume', data=df)
plt.title('Impact of Roadwork and Construction on Traffic Volume')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()
# Use boxplot to visualize outliers in numerical features
plt.figure(figsize=(14, 10))
for i, col in enumerate(numerical_columns, 1):
    plt.subplot(4, 3, i)
    sns.boxplot(df[col])
    plt.title(f'Outliers in {col}')
plt.tight_layout()
plt.show()
# Outliers (by inter quartile range [IQR] method)
# Average Speed
sns.boxplot(df['Average Speed'])
q1 = df['Average Speed'].quantile(0.25)
q3 = df['Average Speed'].quantile(0.75)
iqr = q3-q1
q1,q3,iqr
upper_limit=  q3 + (1.5 * iqr)
lower_limit = q1 - (1.5 * iqr)
lower_limit, upper_limit
df.loc[(df['Average Speed'] > upper_limit) | (df['Average Speed'] < lower_limit)]
new_df = df.loc[(df['Average Speed'] < upper_limit) & (df['Average Speed'] > lower_limit)]
print('before removing outliers: ' , len(df))
print('after removing outliers: ', len(new_df))
print('outliers:' ,len(df) - len(new_df))
sns.boxplot(new_df['Average Speed'])
# capping - change the outlier values to upper (or) lower limit
new_df = df.copy()
new_df.loc[(new_df['Average Speed']>upper_limit), 'Average Speed'] = upper_limit
new_df.loc[(new_df['Average Speed']<lower_limit), 'Average Speed'] = lower_limit
sns.boxplot(new_df['Average Speed'])

# Environmental Impact
sns.boxplot(df['Environmental Impact'])
q1 = df['Environmental Impact'].quantile(0.25)
q3 = df['Environmental Impact'].quantile(0.75)
iqr = q3-q1
q1,q3,iqr
upper_limit=  q3 + (1.5 * iqr)
lower_limit = q1 - (1.5 * iqr)
lower_limit, upper_limit
df.loc[(df['Environmental Impact'] > upper_limit) | (df['Environmental Impact'] < lower_limit)]
new_df = df.loc[(df['Environmental Impact'] < upper_limit) & (df['Environmental Impact'] > lower_limit)]
print('before removing outliers: ' , len(df))
print('after removing outliers: ', len(new_df))
print('outliers:' ,len(df) - len(new_df))
sns.boxplot(new_df['Environmental Impact'])

# Feature Engineering
df.head()
df = df.drop('Road Capacity Utilization', axis=1)

# Categorical Variable Transformation
df = pd.get_dummies(df, columns=['Weather Conditions'], drop_first=True)

# Normalize/Standardize Numerical Features
from sklearn.preprocessing import MinMaxScaler

# List of numerical columns
numerical_columns = [
    "Traffic Volume", "Average Speed", "Travel Time Index", 
    "Congestion Level", "Incident Reports", 
    "Environmental Impact", "Public Transport Usage", 
    "Pedestrian and Cyclist Count", "Roadwork and Construction Activity"
]

# Initialize the scaler
scaler = MinMaxScaler()

# Apply scaling
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Time Series Transformation
# Create lag feature for Traffic Volume (previous day's traffic volume)
df['Traffic_Volume_Lag_1'] = df['Traffic Volume'].shift(1)

#Create Train-Test Split
from sklearn.model_selection import train_test_split

# Drop NaN values
df.dropna(inplace=True)

# Create a chronological split
train_size = int(len(df) * 0.8)  # 80% for training
train, test = df.iloc[:train_size], df.iloc[train_size:]

# Further split the training set for validation if necessary
from sklearn.model_selection import train_test_split
train, val = train_test_split(train, test_size=0.2, shuffle=False)

# Baseline Model (Linear Regression)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Define features and target variable
features = [
    "Average Speed", "Travel Time Index", "Congestion Level", 
    "Incident Reports", "Environmental Impact", 
    "Public Transport Usage", "Pedestrian and Cyclist Count", 
    "Roadwork and Construction Activity", "Day of Week", 
    "Traffic_Volume_Lag_1"  # Include lag feature
]
target = "Traffic Volume"

# Separate the features and target for training and validation sets
X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]

# Initialize the model
model = LinearRegression()

# Fit the model on the training set
model.fit(X_train, y_train)

# Make predictions on the validation set
y_pred = model.predict(X_val)

# Evaluate the model
rmse = mean_squared_error(y_val, y_pred, squared=False)
mae = mean_absolute_error(y_val, y_pred)

print(f"RMSE: {rmse}")
print(f"MAE: {mae}")

r2_score(y_val,y_pred)

df.head()

# LSTM Model
# Reshape Data for LSTM
def create_dataset(data, time_steps=1):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps)])
        y.append(data[i + time_steps])
    return np.array(X), np.array(y)


traffic_volume_data = df['Traffic Volume'].values.reshape(-1, 1)
X, y = create_dataset(traffic_volume_data, time_steps=1)

# Train-Test Split
train_size = int(len(X) * 0.8)  # 80% for training
val_size = int(len(X) * 0.2)    # 20% for validation
X_train, X_val, X_test = X[:train_size], X[train_size:train_size + val_size], X[train_size + val_size:]
y_train, y_val, y_test = y[:train_size], y[train_size:train_size + val_size], y[train_size + val_size:]

# Model Definition
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))  # First LSTM layer
model.add(Dropout(0.2))  # Dropout layer to prevent overfitting
model.add(LSTM(50))  # Second LSTM layer
model.add(Dropout(0.2))  # Another Dropout layer
model.add(Dense(1))  # Output layer for regression
model.compile(optimizer='adam', loss='mean_squared_error')  # Compile the model

# Training the Model
model.fit(X_train, y_train, epochs=3, batch_size=32, validation_data=(X_val, y_val), verbose=1)

# Evaluation
from sklearn.metrics import mean_squared_error, mean_absolute_error

y_pred = model.predict(X_test)  # Predictions on the test set
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Calculate RMSE
mae = mean_absolute_error(y_test, y_pred)  # Calculate MAE
print(f'RMSE: {rmse}, MAE: {mae}')

# Hyperparameter Tuning
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.optimizers import Adam
import keras_tuner as kt

# Define model
def build_model(hp):
    model = Sequential()
    
    # Tuning number of LSTM units
    model.add(LSTM(units=hp.Int('units', min_value=32, max_value=512, step=32), 
                   return_sequences=True, 
                   input_shape=(X_train.shape[1], X_train.shape[2])))
    
    # Adding Dense layers with variable units
    model.add(Dense(units=hp.Int('dense_units', min_value=32, max_value=256, step=32), 
                    activation=hp.Choice('dense_activation', values=['relu', 'tanh'])))
    
    # Output layer
    model.add(Dense(1,activation='sigmoid'))
    
    # Tuning learning rate
    model.compile(optimizer=Adam(hp.Float('learning_rate', min_value=1e-4, max_value=1e-2, sampling='LOG')),
                  loss='mean_squared_error')
    
    return model

# Define the tuner
tuner = kt.RandomSearch(
    build_model,
    objective='val_loss',
    max_trials=5,  # Number of different hyperparameter combinations to try
    executions_per_trial=2,  # Number of models to build and average results
    directory='my_dir',  # Directory to save the tuning results
    project_name='hyperparam_tuning'  # Project name for organization
)

# RUN
tuner.search(X_train, y_train,
             epochs=3,  # Number of epochs for each model
             validation_data=(X_val, y_val),
             batch_size=32)

# Best Model

best_model = tuner.get_best_models(num_models=1)[0]

#Evaluate

best_model.evaluate(X_val, y_val)

# save the best model
best_model.save("best_tuned_model.h5")

best_model.save('my_model.keras')

from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# Evaluate on validation data
val_preds = best_model.predict(X_val)

# Reshape predictions and true values to 2D
# Assuming the shape is (num_samples, time_steps, num_outputs)
val_preds_reshaped = val_preds.reshape(val_preds.shape[0], -1)  # Combine last two dimensions
y_val_reshaped = y_val.reshape(y_val.shape[0], -1)  # Combine last two dimensions

# Compute RMSE and MAE
rmse = np.sqrt(mean_squared_error(y_val_reshaped, val_preds_reshaped))
mae = mean_absolute_error(y_val_reshaped, val_preds_reshaped)

print(f"RMSE: {rmse}, MAE: {mae}")

model.save('traffic_volume_model.h5')

