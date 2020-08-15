import pandas as pd,numpy as np,quandl as qq,math
from sklearn import preprocessing,svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = qq.get('WIKI/GOOGL')

df.head()

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/df['Adj. Low']*100.0

df['PCT_change'] = (df['Adj. Open'] - df['Adj. Close'])/df['Adj. Close']*100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

df.head()

forecast_col = 'Adj. Close'

df.fillna(-99999,inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
forecast_out

df['Label'] = df[forecast_col].shift(-forecast_out)

df.head()

df.dropna(inplace=True)

len(df)

df.head(15)

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume','Label']]

df.tail()

X = np.array(df.drop('Label',axis = 1))

X

y = np.array(df['Label'])

X = preprocessing.scale(X)

X = X[:-forecast_out]

X_lately = X[-forecast_out:]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)

clf1 = svm.SVR() #kernel = 'poly'
clf2 = LinearRegression()

clf1.fit(X_train,y_train)
clf2.fit(X_train,y_train)

clf1.score(X_test,y_test)

clf2.score(X_test,y_test)

forecast_set = clf1.predict(X_lately)
print(forecast_set,accuracy,forecast_out)

df['Forecast'] =np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix +one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
        

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()



