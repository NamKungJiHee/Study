from sklearn.utils import all_estimators
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

#1. 데이터
datasets = load_iris()
x = datasets.data
y = datasets.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size= 0.8, shuffle = True, random_state = 66)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#2. 모델 구성
allAlgorithms = all_estimators(type_filter = 'classifier')  # classifier에 대한 모든 측정기
print("allAlgorithms: ", allAlgorithms)  # [('AdaBoostClassifier', <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'>), ..]
print("모델의 갯수: ", len(allAlgorithms))  # 모델의 갯수:  41

#allAlgorithms = all_estimators(type_filter = 'regressor')  # regressor에 대한 모든 측정기

#print("allAlgorithms: ", allAlgorithms)  # [('ARDRegression', <class 'sklearn.linear_model._bayes.ARDRegression'>), ..]
#print("모델의 갯수: ", len(allAlgorithms))  # 모델의 갯수: 55

for (name, algorithm) in allAlgorithms:   # [('AdaBoostClassifier', <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'>),...
    try:
        model = algorithm()
        model.fit(x_train, y_train)
        
        y_predict = model.predict(x_test)
        acc = accuracy_score(y_test, y_predict)
        print(name, '의 정답률: ', acc)
    except:                     # 에러나는 것 빼고 계속해라.
        #continue   
        print(name, '은 에러')
""" 
모델의 갯수:  41
AdaBoostClassifier 의 정답률:  0.6333333333333333
BaggingClassifier 의 정답률:  0.9666666666666667
BernoulliNB 의 정답률:  0.4
CalibratedClassifierCV 의 정답률:  0.9666666666666667
CategoricalNB 의 정답률:  0.3333333333333333
ClassifierChain 은 없습니다
ComplementNB 의 정답률:  0.6666666666666666
DecisionTreeClassifier 의 정답률:  0.9333333333333333
DummyClassifier 의 정답률:  0.3
ExtraTreeClassifier 의 정답률:  0.9333333333333333
ExtraTreesClassifier 의 정답률:  0.9666666666666667
GaussianNB 의 정답률:  0.9666666666666667
GaussianProcessClassifier 의 정답률:  0.9666666666666667
GradientBoostingClassifier 의 정답률:  0.9333333333333333
HistGradientBoostingClassifier 의 정답률:  0.8666666666666667
KNeighborsClassifier 의 정답률:  1.0
LabelPropagation 의 정답률:  0.9666666666666667
LabelSpreading 의 정답률:  0.9666666666666667
LinearDiscriminantAnalysis 의 정답률:  1.0
LinearSVC 의 정답률:  0.9666666666666667
LogisticRegression 의 정답률:  0.9666666666666667
LogisticRegressionCV 의 정답률:  1.0
MLPClassifier 의 정답률:  0.9
MultiOutputClassifier 은 없습니다
MultinomialNB 의 정답률:  0.6333333333333333
NearestCentroid 의 정답률:  0.9666666666666667
NuSVC 의 정답률:  0.9666666666666667
OneVsOneClassifier 은 없습니다
OneVsRestClassifier 은 없습니다
OutputCodeClassifier 은 없습니다
PassiveAggressiveClassifier 의 정답률:  0.7666666666666667
Perceptron 의 정답률:  0.9333333333333333
QuadraticDiscriminantAnalysis 의 정답률:  1.0
RadiusNeighborsClassifier 의 정답률:  0.4666666666666667
RandomForestClassifier 의 정답률:  0.9333333333333333
RidgeClassifier 의 정답률:  0.9333333333333333
RidgeClassifierCV 의 정답률:  0.8333333333333334
SGDClassifier 의 정답률:  0.8
SVC 의 정답률:  1.0
StackingClassifier 은 없습니다
VotingClassifier 은 없습니다
"""

