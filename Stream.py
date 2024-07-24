import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide",page_title='Startup Analysis')
df=pd.read_csv('/Users/gautammehta/PycharmProjects/Startup Dashboard/startup_cleaned.csv')

def load_overall_analysis():
    st.title('Overall Analysis')
    col1, col2,col3 = st.columns(3)
    # total invested amount
    with col1:
        amount=int(df['amount'].sum())
        st.metric('Total amount',str(amount) +'Cr')

    # Max Amount
    with col2:
        max_amount=df.groupby('Startup Name')[['Startup Name','amount']].max().sort_values(by='amount',ascending=False).head(1).values[0]
        st.metric('Highest investment', str(max_amount) + ' Cr')

    # Avg Amount Invsted
    avg_amount = df.groupby('Startup Name')[['amount']].mean().sort_values(by='amount',ascending=False).head(1).values[0]
    st.metric('Average investment', str(avg_amount) + ' Cr')

    # Funded Startups
    st.metric('Total Starups Funded',str(len(df['Startup Name'].unique())))
def load_investor_details(investor):
    st.title(investor)

    # Last 5 transactions
    last5_df=df[df['Investors Name'].str.contains(investor)][['date','Startup Name','vertical','city','round_number','amount']].head(5)
    st.subheader('last 5 details')
    st.dataframe(last5_df)

    # biggest Investment
    # col1,col2,col3=st.columns(3)
    # with col1:
    big_series=df[df['Investors Name'].str.contains(investor)].groupby('Startup Name')['amount'].sum().sort_values(ascending=False).head(5)
    st.subheader('Top Investments')
    fig,ax=plt.subplots()
    ax.bar(big_series.index,big_series.values,color='green')
    st.pyplot(fig)


    # Pie chart
    st.subheader('Vertical Investments')
    vertical_series=df[df['Investors Name'].str.contains(investor)].groupby('vertical')['amount'].sum()
    fig1,ax1=plt.subplots()
    ax1.pie(vertical_series,labels=vertical_series.index,autopct='%1.1f%%',)
    st.pyplot(fig1)

    # with col3:
    st.subheader('City Investments')
    city_series = df[df['Investors Name'].str.contains(investor)].groupby('city')['amount'].sum()
    fig2, ax2 = plt.subplots()
    ax2.pie(city_series, labels=city_series.index, autopct='%1.1f%%', )
    st.pyplot(fig2)

    st.subheader('Investments time Line')
    df['year'] = df['date'].astype('datetime64[ns]').dt.year
    year_series=df[df['Investors Name'].str.contains(investor)].groupby('year')['amount'].sum()
    fig3, ax3 = plt.subplots()
    ax3.plot(year_series.index,year_series.values )
    st.pyplot(fig3)

st.sidebar.title('Startup Funidng Analysis')

option=st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option=='Overall Analysis':
    btn0=st.sidebar.button('Overall Analysis')
    if btn0:
        load_overall_analysis()
elif option=='Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['Startup Name'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    st.title('Investor Analysis')
    selected_investor=st.sidebar.selectbox('Select Startup',sorted(set(df['Investors Name'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investor Details')
    if btn2:
        st.title(load_investor_details(selected_investor))







