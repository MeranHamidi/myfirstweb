import streamlit as st
import finpy_tse as fpy

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
with left_column:
    option = st.selectbox('Inter your stock name?',['وبملت', 'دفارا', 'دکپسول', 'دپارس' ,'درهآور','غمینو'])
    st.write('You Inter :', option)
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    #aa = fpy.Get_Price_History(stock=option,start_date='1402-01-01',end_date='1402-03-23',ignore_date=False, adjust_price=False,show_weekday=False, double_date=False)
    #aa = aa.drop(columns=['Ticker', 'Name', 'Market'])
    #st.dataframe(aa)
    #st.line_chart( aa , y =['Close'], use_container_width = True)
    #st.bar_chart(aa['Value'], use_container_width = True)
    #ast = st.dataframe(aa.style.highlight_max(axis=0, color='red'))
    #st.write(aa.keys())
    #st.write(aa.index)
    st.write('hello')

