# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# show the title
st.title("Titanic App by Jingyi Guo")


# read csv and show the dataframe
df = pd.read_csv('train.csv') 
st.dataframe(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, axs = plt.subplots(1, 3, figsize=(15, 5))


axs[0].boxplot(df[df['Pclass'] == 1]['Fare'])
axs[0].set_title('Pclass 1 Fare Distribution')
axs[0].set_xlabel('Pclass 1')
axs[0].set_ylabel('Ticket Fare')


axs[1].boxplot(df[df['Pclass'] == 2]['Fare'])
axs[1].set_title('Pclass 2 Fare Distribution')
axs[1].set_xlabel('Pclass 2')
axs[1].set_ylabel('Ticket Fare')

axs[2].boxplot(df[df['Pclass'] == 3]['Fare'])
axs[2].set_title('Pclass 3 Fare Distribution')
axs[2].set_xlabel('Pclass 3')
axs[2].set_ylabel('Ticket Fare')

st.pyplot(fig)