import nltk
import string
import pymorphy2
import regex as re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pymorphy2

#Тестовое предложение
sentence_example = df.iloc[0]["Вопросы"]

#Создание MorphAnalyzer для использования метода лемматизации
morph = pymorphy2.MorphAnalyzer()
#Создание списка стоп-слов
stop_words = stopwords.words("russian")

#Функция, которую буду использовать для обработки nltk
def tokinize_sentence(sentense: str, remove_stop_word: bool = True):
    #Перед использованием функции удалю все специальные символы и цифры с помощью регулярных выражений, а strip удалит лишние пробелы в начале и в конце предложения
    #Первый шаг — токенизация (у нас будет список слов)
    tokens = word_tokenize(re.compile('[^а-яА-Я ]').sub('', sentense).strip(), language="russian")
    #Второй шаг - удалить знаки препинания
    tokens = [i for i in tokens if i not in string.punctuation]
    #Затем удаляю стоп-слова, если ине это нужно.
    if remove_stop_word:
        tokens = [i for i in tokens if i not in stop_words]
    #Теперь верну слово в начальную форму
    tokens = [morph.parse(i)[0].normal_form for i in tokens]
    return tokens

#Использование функции
tokinize_sentence(sentence_example)
