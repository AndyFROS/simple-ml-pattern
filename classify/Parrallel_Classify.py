## Custom converter
from sklearn import base
from sklearn.pipeline import make_pipeline
## feature selection
from sklearn.feature_selection import SelectFromModel

# preprocss Algorithms(预处理算法)
from sklearn.preprocessing import StandardScaler,MinMaxScaler
# feature dimension reduction(特征降维)
from sklearn.decomposition import PCA
# Regression algorithms(回归算法)
from sklearn.ensemble import RandomForestRegressor


class NoPreprocessing(base.BaseEstimator,base.TransformerMixin):
    def __init__(self):
        self.preprocessor=None
    def fit(self, X, Y=None):
        self.preprocessor=0
        return self
    def transform(self,X):
        if self.preprocessor is None:
            raise NotImplementedError()
        return X
    
def evaluate(estimator,X,y,scoring='accuracy_score', cv=3):
    import datetime as dt
    from sklearn.model_selection import cross_val_score 
    start=dt.datetime.now()
    #estimator сама модель
    preprocessors_names=' '.join(list(estimator.named_steps.keys())[:-1])
    regressors_names=list(estimator.named_steps.keys())[-1]
    score=-cross_val_score(estimator,X,y,scoring=scoring,cv=cv).mean() # MSE score
    duration=str(dt.datetime.now()-start) # Consumption of time
    return dict(preprocessor=preprocessors_names,regressor=regressors_names,score=score,duration=duration)

def score(X,y):
    no,ms,ss=NoPreprocessing(),MinMaxScaler(),StandardScaler()
    preprocessors=[[no],[ms],[ss]]
    
    random_state=42

    regressors=[
            RandomForestRegressor(n_estimators=100,random_state=random_state),
    ]  
    
    # evaluation 
    estimators=[make_pipeline(*preprocessor,regressor) for preprocessor in preprocessors for regressor in regressors]
    
    # parallel
    from joblib import parallel_backend,Parallel,delayed
    with parallel_backend('loky'):
        _=Parallel(n_jobs=-1,verbose=1)(
        delayed(evaluate)(estimator,X,y) for estimator in estimators)
    return pd.DataFrame(_).sort_values('score').reset_index(drop=True)
  
  
  
res = score(X_train,y_train)
res
