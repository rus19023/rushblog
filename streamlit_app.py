"""A WebApp for the Rush Family
"""

import streamlit as st
import streamlit_authenticator as stauth
#import pymongo
#from pymongo import MongoClient
from pymongo import ServerApi
import streamlit.components as stc 
import pandas as pd 
import pygwalker as pyg
import pprint
import os
import sys


def main():
    
    uri = os.environ.get(['MONGO_URI'])
    st.title('The Rush Family App')
    menu = ['Home', 'About', 'Feed', 'MyInfo']
    
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == 'Home':
        st.subheader('Home')
    
    elif choice == 'About':
        st.subheader('About')
    
    elif choice == 'Feed':
        st.subheader('Feed')
    
    elif choice == 'MyInfo':
        st.subheader('MyInfo')
        
    else:
        st.subheader('')
        
        
if __name__ == '__main__':
    main()


#cache the function and map the type to the hash function
@st.cache(hash_funcs={MongoClient: id})
def mongo_connect(url):
    return MongoClient(url)




client = mongo_connect()
db = client.orders


#Display title for streamlit app
st.title("Choose your toppings and crust!")


#Multiselect widget in app
pizza_dough = st.multiselect(
    'Which crust do you love?',
    ('Thin', 'Regular', 'Thick', 'Sicilian'))


toppings = st.multiselect(
    'What toppings do you want?',
    ('Beef','Chicken','Tofu'))


#Create dict from multiselect inputs
mongo_dump = { "dough" : pizza_dough,
             "topping" : toppings
             }


#Try submitting order (inserting into MongoDB)
if st.button("Submit Order"):
        try:
            mongo_dump_result = db.orders.insert_one(mongo_dump)
       
        except:
            st.error("Sorry, looks like we ran into an error! Try hit the recommendation again :cry:")


