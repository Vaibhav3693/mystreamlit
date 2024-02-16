import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='📈')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCK7j9dbWr81kAAwChe4zq9klrKm2iLQREWWJeP8rwBw&s')
st.title('VK Trading')
st.header('By Vaibhav K')
st.text('This is a Stock Trading Company')
if(mymenu=='Home'):
    st.markdown('<center><h1>HELLO INVESTER</h1><center>',unsafe_allow_html=True)
    st.image('https://media.istockphoto.com/id/1487894858/photo/candlestick-chart-and-data-of-financial-market.webp?b=1&s=170667a&w=0&k=20&c=iwQM0ozj7upM-_7CUEjZ2veIY3ljlB8m3PbijouIyVM=')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        dob=st.date_input("Choose Date of Birth")
        income=st.slider('Choose Income')
        k=st.form_submit_button("Submit Form")
        if k:
            st.write('Name:',name,'DOB:',dob,'Income:', income)

elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','Hello this is the downloaded data','trading.txt' )
