# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans
# from sklearn.metrics import adjusted_rand_score
#
# documents = ["This little kitty came to play when I was eating at a restaurant.",
#              "Merley has the best squooshy kitten belly.",
#              "Google Translate app is incredible.",
#              "If you open 100 tab in google you get a smiley face.",
#              "Best cat photo I've ever taken.",
#              "Climbing ninja cat.",
#              "Impressed with google map feedback.",
#              "Key promoter extension for Google Chrome."]
#
# vectorizer = TfidfVectorizer(stop_words='english')
# X = vectorizer.fit_transform(documents)
#
# true_k = 2
# model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
# model.fit(X)
#
# print("Top terms per cluster:")
# order_centroids = model.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()
#
# for i in range(true_k):
#     print("Cluster %d:" % i),
#     for ind in order_centroids[i, :10]:
#         print(' %s' % terms[ind])
#
#
# print("\n")
# print("Prediction")
#
# Y = vectorizer.transform(["chrome browser to open."])
# prediction = model.predict(Y)
# print(prediction)
#
# Y = vectorizer.transform(["My cat is hungry."])
# prediction = model.predict(Y)
# print(prediction)
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv('SMSSpamCollection', delimiter='\t',header=None)

X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1],df[0])

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_raw)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

X_test = vectorizer.transform( ['URGENT! Your Mobile No 1234 was awarded a Prize', 'Hey honey, whats up?'] )
predictions = classifier.predict(X_test)
print(predictions)
