from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn import metrics

#Текстовые и числовые классы, использующие базовые библиотеки sklearn
class TextTransformer(BaseEstimator, TransformerMixin):
    """
    Transform text features
    """
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None, *parg, **kwarg):
        return self

    def transform(self, X):
        return X[self.key]
    
class NumberTransformer(BaseEstimator, TransformerMixin):
    """
    Transform numeric features
    """
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[[self.key]]


#Использовать обратный векторизатор частоты документа term-frequency для преобразования количества текста 36 
#Во взвешенную матрицу важности термина
vec_tdidf = TfidfVectorizer(ngram_range=(1,1), analyzer='word', norm='l2')

#Компилирую TextTransformer и TfidfVectorizer
#К тексту 'text_sentence'
text_sentence = Pipeline([
                ('transformer', TextTransformer(key='text_attribute')),
                ('vectorizer', vec_tdidf)
                ])

#Компилирую NumberTransformer в 'text_numeric'
#И 'text_numeric2' числовые функции
text_numeric = Pipeline([
                ('transformer', NumberTransformer(key='num_attrib')),
                ])

text_numeric2 = Pipeline([
                ('transformer', NumberTransformer(key='num_attrib2')),
                ])



#объединить все функции, текстовые и числовые вместе
features = FeatureUnion([('text_attribute', text_sentence),
                      ('text_numeric', text_numeric),
                      ('text_numeric2', text_numeric2),
                      ])


text_numeric_features = ['text_attribute', 'num_attrib', 'num_attrib2']
predictor = 'target attribute'

X_train, X_test, y_train, y_test = train_test_split(df[text_numeric_features], df[predictor], 
                                                    test_size=0.25, random_state=42)







#RandomForestClassifier

#Минимальное количество образцов на лист
n_estimators = [99, 200]

#Минимальное количество выборок для разделения узла
max_depth = [25, 50]

hyperparameter_grid = {'n_estimators': n_estimators,
                       'max_depth': max_depth}





from sklearn.ensemble import RandomForestClassifier
#Создание модели для настройки гиперпараметров
model = RandomForestClassifier()

#Настройка RandomizedSearchCV с 3-кратной перекрестной проверкой
clf = RandomizedSearchCV(estimator=model,
                               param_distributions=hyperparameter_grid,
                               cv=3, n_iter=20, 
                               scoring = 'neg_mean_absolute_error',
                               n_jobs = -1, verbose = 1, 
                               return_train_score = True,
                               random_state=42)

#Обьединение функции и классификация вместе
pipe = Pipeline([('features', features),
                 ('clf',clf)
                 ])






#Обучение модели
pipe.fit(X_train, y_train)

#Обьединение функции и классификация вместе
pipe2 = Pipeline([('features', features),
                 ('clf',clf.best_estimator_)
                 ])

#Обучение лучшей модели
pipe2.fit(X_train, y_train)

#Предсказание для тестового надбора данных у лучшей модели
preds = pipe2.predict(X_test)

#Оценка точности классификации
from sklearn.metrics import classification_report
print("best was - ", clf.best_estimator_)
print(classification_report(y_test, preds))
