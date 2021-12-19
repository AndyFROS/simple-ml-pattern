#Разделение данных на обучающую и тестовую выборки
from sklearn.model_selection import train_test_split
#stratify означает что данные из указаного в этот параметр столбца будут во всех выборках распределены равномерно
X_train, X_test, y_train, y_test = train_test_split(df, df['name'], test_size=0.33, random_state=42, stratify=df['importantCol'])

#При помощи train_test_split можно сокращать количество оббектов в выборке, если та слишком большая
X_train, y_train = train_test_split(df, df['name'], test_size=0.33, random_state=42, stratify=df['importantCol'])
#Таким образом можно скоратить выборку до 67% от оригинальной, этот процент можно менять, указав другое соотношение в test_size
df = X_train
