
#Meet Robo: your friend

#import necessary libraries
import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer #Импортируйте векторизатор TFidf из библиотеки, чтобы преобразовать набор необработанных текстов в матрицу свойств TF-IDF
from sklearn.metrics.pairwise import cosine_similarity #Кроме того, импортируйте модуль коэффициента Отиаи из библиотеки scikit. Этот модуль будет использоваться для поиска в запросе пользователя ключевых слов.
import warnings
warnings.filterwarnings('ignore')
#NLTK (Natural Language Toolkit) is a platform for creating Python programs for working with natural speech.
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only
'''
Предварительная обработка текста с помощью NLTK
Основная проблема с данными заключается в том, что они представлены в текстовом формате. Для решения задач алгоритмами машинного обучения требуется некий вектор свойств. Поэтому прежде чем начать создавать проект по NLP, нужно предварительно обработать его. Предварительная обработка текста включает в себя:
Преобразование букв в заглавные или строчные, чтобы алгоритм не обрабатывал одни и те же слова повторно.
Токенизация. Токенизация — термин, используемый для описания процесса преобразования обычных текстовых строк в список токенов, то есть слов. Токенизатор предложений используется для составления списка предложений. Токенизатор слов составляет список слов.
Пакет NLTK включает в себя предварительно обученный токенизатор Punkt для английского языка.
Удаление шума, то есть всего, что не является цифрой или буквой;
Удаление стоп-слов. Иногда из словаря полностью исключаются некоторые крайне распространенные слова, которые, как считается, не имеют большого значения для формирования ответа на вопрос пользователя. Эти слова называются стоп-словами (междометия, артикли, некоторые вводные слова);
Cтемминг: приведение слова к коренному значению. Например, если нам нужно провести стемминг слов «стемы», «стемминг», «стемированный» и «стемизация», результатом будет одно слово — «стем».
Лемматизация. Лемматизация — немного отличающийся от стемминга метод. Основное различие между ними заключается в том, что стемминг часто создает несуществующие слова, тогда как лемма — это реально существующее слово. 
Таким образом, ваш исходный стем, то есть слово, которое получается после стемминга, не всегда можно найти в словаре, а лемму — можно. Пример лемматизации: «run» — основа для слов «running» или «ran», а «better» и «good» находятся в одной и той же лемме и потому считаются одинаковыми.
'''
#Reading in the corpus
with open('chatbot.txt','r', encoding='utf8', errors ='ignore') as fin: #Выполним чтение файла corpus.txt и преобразуем весь текст в список предложений и список слов для дальнейшей предварительной обработки.
    raw = fin.read().lower()

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer() #Теперь определим функцию LemTokens, которая примет в качестве входных параметров токены и выдаст нормированные токены.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
'''
Набор слов
После первого этапа предварительной обработки нужно преобразовать текст в вектор (или массив) чисел. «Набор слов» — это представление текста, описывающего наличие слов в тексте. «Набор слов» состоит из:
- словаря известных слов;
- частот, с которыми каждое слово встречается в тексте.
Почему используется слово «набор»? Это связано с тем, что информация о порядке или структуре слов в тексте отбрасывается, и модель учитывает только то, как часто определенные слова встречаются в тексте, но не то, где именно они находятся.
Идея «набора слов» состоит в том, что тексты похожи по содержанию, если включают в себя похожие слова. Кроме того, кое-что узнать о содержании текста можно лишь по набору слов.
Например, если словарь содержит слова {Learning, is, the, not, great} и мы хотим составить вектор предложения “Learning is great”, получится вектор (1, 1, 0, 0, 1).
'''
# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
'''
Метод TF-IDF
Проблема «набора слов» заключается в том, что в тексте могут доминировать часто встречающиеся слова, которые не содержат ценную для нас информацию. Также «набор слов» присваивает большую важность длинным текстам по сравнению с короткими.
Один из подходов к решению этих проблем состоит в том, чтобы вычислять частоту появления слова не в одном тексте, а во всех сразу. За счет этого вклад, например, артиклей «a» и «the» будет нивелирован. Такой подход называется TF-IDF (Term Frequency-Inverse Document Frequency) и состоит из двух этапов:
TF — вычисление частоты появления слова в одном тексте
TF = (Число раз, когда слово "t" встречается в тексте)/(Количество слов в тексте)
IDF — вычисление того, на сколько редко слово встречается во всех текстах
IDF = 1+log(N/n), где N - общее количество текстов, n - во скольких текстах встречается "t"
Коэффициент TF-IDF — это вес, часто используемый для обработки информации и интеллектуального анализа текста. Он является статистической мерой, используемой для оценки важности слова для текста в некотором наборе текстов.
Пример
Рассмотрим текст, содержащий 100 слов, в котором слово «телефон» появляется 5 раз. Параметр TF для слова «телефон» равен (5/100) = 0,05.
Теперь предположим, что у нас 10 миллионов документов, и слово телефон появляется в тысяче из них. Коэффициент вычисляется как 1+log(10 000 000/1000) = 4. Таким образом, TD-IDF равен 0,05 * 4 = 0,20.
TF-IDF может быть реализован в scikit так:
from sklearn.feature_extraction.text import TfidfVectorizer

Коэффициент Отиаи
TF-IDF — это преобразование, применяемое к текстам для получения двух вещественных векторов в векторном пространстве. Тогда мы можем получить коэффициент Отиаи любой пары векторов, вычислив их поэлементное произведение и разделив его на произведение их норм. Таким образом, получается косинус угла между векторами. Коэффициент Отиаи является мерой сходства между двумя ненулевыми векторами. Используя эту формулу, можно вычислить схожесть между любыми двумя текстами d1 и d2.
Cosine Similarity (d1, d2) =  Dot product(d1, d2) / ||d1|| * ||d2||
Здесь d1, d2 — два ненулевых вектора.
'''
# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")    
        
        

