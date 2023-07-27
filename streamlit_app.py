
import streamlit as a

a.title('My Parents New Healthy Diner')

a.header('Breakfast Favorites')
a.text('🥣 Omega 3 & Blueberry Oatmeal')
a.text('🥗 Kale, Spinach & Rocket Smoothie')
a.text('🐔 Hard-Boiled Free-Range Egg')
a.text('🥑🍞 Avacado Toast')

a.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Lets put a picklist here so that the customers can pick the fruits they would like.
a.multiselect("Pick some fruits:", list(my_fruit_list.index))
#Display in the tabular format
a.dataframe(my_fruit_list)
