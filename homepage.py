import streamlit as st
st.sidebar.header('Project Designed')
st.sidebar.markdown("[Project designed: Kobe bryant Chatbot](https://kobebryantchatbot.streamlit.app/)")
st.sidebar.markdown("[Project designed: Student Performance Application ](https://studentoutcomes.streamlit.app/)")
st.sidebar.markdown("[Project designed: Student Performance Application](https://studentlogistics.streamlit.app/)")
st.sidebar.markdown("[Project designed: House prices prediction Application](https://predicthouse.streamlit.app/)")
st.sidebar.markdown("[Project Designed: Heart disease prediction Application](https://hearcheck.streamlit.app/)")
st.sidebar.markdown("[Project designed: standing and siting classification](https://teachablemachine.withgoogle.com/models/R2x8mdK4K/)")

st.header('Cole Abdulazeem')
st.header('A Senior Machine Learning Engineer')
st.subheader('Project Collection')
col1, col2, col3 = st.columns(3)


with col1:
    st.image('heart.jpeg', width=200, caption='HEART PREDICTION APP')

with col2:
    st.image('Kobe_Bryant.jpeg', width=200, caption='KOBE BRYANT CHATBOT')

with col3:
    st.image('duplex (1).jpg', width=200, caption='HOUSE PRICE')



st.write('My experience in the A.I(Artificial intelligence) summer bootcamp was interesting and it was enlightening.'
 ' I learnt alot of new things such as linear regression, logistics regression, conditional statement, how to assign a variable etc'
         ' overall, the experience was nice.  ')
