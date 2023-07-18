import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)

    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text=y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
tfidf=pickle.load(open('vecorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))


st.title("Email/SMS spam classifier")

inputsms = st.text_area("enter the message")

if st.button('Predict'):
    #pre process
    transformed=transform_text(inputsms)
    #vectorize
    vectorInput=tfidf.transform([transformed])
    #model
    result=model.predict(vectorInput)[0]
    # Display

    if result==1:
        st.header("Spam")
    else:
        st.header("not spam")
