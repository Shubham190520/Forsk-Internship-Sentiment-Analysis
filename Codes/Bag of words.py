#features - reviewText col
#labels - Positivity

df['reviewText'].head()

#Bag of words model

from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test = train_test_split(df['reviewtext'],df['Positivity'], random_state = 42)



list1 = [1,2,3,4,5,6,7,8,9,10]

train , test = train_test_split(list1, random state = 0)

####

from sklearn.feature_extraction.text import Count vectorizer

vect = CountVectorizer().fit(features_train)


len(vect.get_feature_names())

features_train_vectorized = vect.transform(features_train)

features_train_vectorized.toarray()

