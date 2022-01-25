from xgboost import XGBClassifier, XGBRegressor
from sklearn.datasets import load_boston, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score
import time
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import PowerTransformer
# import warnings
# warnings.filterwarnings('ignore')

#1. 데이터
#datasets = fetch_california_housing()
datasets = load_boston()

x = datasets.data
y = datasets['target']
#print(x.shape, y.shape) # (20640, 8) (20640,)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state=66, shuffle=True) 

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#2. 불러오기  (2.모델, 3.훈련)
import pickle
path = './_save/'
model = pickle.load(open(path + 'm23_pickle1_save.dat', 'rb')) # read

#4. 평가
results = model.score(x_test, y_test)
print("results: ",round(results,4))

y_predict = model.predict(x_test)
r2 = r2_score(y_test, y_predict)
print("r2: ", round(r2,4))

print("=========================")
hist = model.evals_result()
print(hist)

''' 
results:  0.9453
r2:  0.9453
'''
