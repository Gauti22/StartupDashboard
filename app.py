import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('Im learning Streamlit')
st.subheader('Im loving it')

st.write('The world is kind the good people find good people.\n' 
         'Beliefe in this logic Keep builing the stuff you like. keep doing great analysis.\n' 
         'Agree it will take some time but one day you will be able to do that.')

st.markdown("""
### My Favorite movies
- Race 3
- Humshakals
- Housefull

""")

st.code("""
def foo(input):
return foo**2

x=foo(3)
""")

st.latex('((x^2)+4+5-1-2)/4')


# Display Elements

df=pd.DataFrame({
    'name':['Golu','Monu','shonu'],
    'age':[22,23,24],
    'package':[6,7,8]
})

st.dataframe(df)

st.metric('Revenue','Rs 3 lac','-3%')

st.json({
    'name':['Golu','Monu','shonu'],
    'age':[22,23,24],
    'package':[6,7,8]
})


st.image('/Users/gautammehta/Desktop/Screenshot 2024-05-28 at 1.08.49 PM.png')

# st.video('address of video')
# st.audio('audio file')

st.sidebar.title('Sidebar ka title')
col1,col2=st.columns(2)

with col1:
    st.image('/Users/gautammehta/Desktop/Screenshot 2024-05-28 at 1.08.49 PM.png')

with col2:
    st.image('/Users/gautammehta/Desktop/Screenshot 2024-05-28 at 1.08.49 PM.png')

st.error('Heelo login failed')

st.info('tunutn')

st.success('yuppeee')

st.warning('wait stop')


# Showing Status
bar=st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)


# User Input
email=st.text_input('Enter Email')
number=st.number_input('Enter Number')
date=st.date_input('Enter the date')


# Buttons

email=st.text_input(label='Email')
password=st.text_input(label='Password')

btn=st.button('Login')



# if button is clicked
if btn:
    if (email=='nitish@gmail.com') and (password=='1234'):
        st.success('Login Successful')

    else:
        st.error('Login Failed')



# DropDown

gender=st.selectbox('Select Gender',['male','female','others'])
st.write(gender)


# File Uploader

file=st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())