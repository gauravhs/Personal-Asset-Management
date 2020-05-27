#####Modules Import
from tensorflow.keras.layers import Input, LSTM, GRU, SimpleRNN, Dense, GlobalMaxPool1D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD, Adam

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

#####Stock Data Fetching
from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override()

stock = "HDFCNIFETF.NS"
df = pdr.get_data_yahoo(stock, start="2018-09-01", end="2020-02-21")

#####Pre processing

# Start by doing the WRONG thing - trying to predict the price itself
series = df['Close'].values.reshape(-1, 1)

# Normalize the data
# Note: I didn't think about where the true boundary is, this is just approx.
scaler = StandardScaler()
scaler.fit(series[:len(series) // 2])
print(series)
series = scaler.transform(series).flatten()
print(series)
### build the dataset
# let's see if we can use T past values to predict the next value
T = 40
D = 1
X = []
Y = []
for t in range(len(series) - T):
  x = series[t:t+T]
  X.append(x)
  y = series[t+T]
  Y.append(y)

X = np.array(X).reshape(-1, T, 1) # Now the data should be N x T x D
Y = np.array(Y)
N = len(X)
print("X.shape", X.shape, "Y.shape", Y.shape)

### try autoregressive RNN model
i = Input(shape=(T, 1))
x = LSTM(20)(i)
# x = Dense(, activation = 'relu')(x)
# x = Dense(16, activation = 'relu')(x)
x = Dropout(0.2)(x)
x = Dense(10, activation = 'relu')(x)
x = Dense(1)(x)

model = Model(i, x)
model.compile(
  loss='mse',
  optimizer=Adam(lr=0.1),
)

# train the RNN
r = model.fit(
  X[:-N//2], Y[:-N//2],
  epochs=80,
  validation_data=(X[-N//2:], Y[-N//2:]),
)

outputs = model.predict(X)
# print(outputs.shape)
predictions = outputs[:,0]
only_pred = np.array([])

param = X[-1:]
for i in range(10):
    out = model.predict(param)
    out = out[:,0]
    predictions = np.append(predictions, out)
    only_pred = np.append(only_pred, out)
    tmp = param[0]
    tmp = np.append(tmp, out)
    tmp = np.delete(tmp, [0])
    param = tmp.reshape(-1, T, 1)
    print(param)

pred = scaler.inverse_transform(predictions)
print(pred)

Y = scaler.inverse_transform(Y)
predictions = scaler.inverse_transform(predictions)
only_pred = scaler.inverse_transform(only_pred)

plt.plot(Y, label='targets')
plt.plot(predictions, label='predictions')
plt.legend()
plt.show()

# Plot loss per iteration
import matplotlib.pyplot as plt
plt.plot(r.history['loss'], label='loss')
plt.plot(r.history['val_loss'], label='val_loss')
plt.legend()
plt.show()

stock = stock + ".csv"
stockall = stock + "_all" + ".csv"
pd.DataFrame(only_pred).to_csv(stock)
pd.DataFrame(predictions).to_csv(stockall)
