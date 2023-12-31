
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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a picklist here so that the customers can pick the fruits they would like.
selected_fruits = a.multiselect("Pick some fruits:", options=list(my_fruit_list.index), default=["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[selected_fruits]
#Display in the tabular format
a.dataframe(fruits_to_show)
