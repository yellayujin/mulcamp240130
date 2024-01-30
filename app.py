# -*- coding:utf-8 -*-
# 배포

# 가상환경 구축 -> 라이브러리 txt 만들기 -> pip install -r requirements.txt -> coding:utf-8 -> streamlit식 포맷(def, if __name__)


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def main():
    
    st.title("Welcome!🧐")
    
    st.markdown("✏️This website is a space for me to apply what I've learned today. :rainbow[Feel free to explore!]✏️")

    aisles = pd.read_csv('instacart-market-basket-analysis/aisles.csv')
    departments = pd.read_csv('instacart-market-basket-analysis/departments.csv')
    products1 = pd.read_csv('instacart-market-basket-analysis/products1.csv')
    
    order_products_prior1 = pd.read_csv('instacart-market-basket-analysis/prior1.csv',)
    order_products_train1 = pd.read_csv('instacart-market-basket-analysis/train1.csv')
    
    orders1 = pd.read_csv('instacart-market-basket-analysis/orders1.csv')


    col1, col2, col3 = st.columns([1,1,1])
    col1.metric("Total Orders", "392,501,324", "2312")
    col2.metric("Today's Orders", "394", "-15")
    col3.metric("Total Sales", "1,403,291K", "23K")


    tab0, tab1, tab2, tab3, tab4 = st.tabs(['Cart Order','Eval Set','Order Hour of Day', 'Overview: aisle_id', 'Overview: department_id'])
    
    with tab0:
        st.title('Add to cart order by reorder')
        col1, col2 = st.columns([1,1])

        with col1:
            st.header('Reordered: N')
            fig, ax = plt.subplots()
            sns.histplot(x = 'add_to_cart_order', data=order_products_prior1.loc[order_products_prior1['reordered']==0], ax=ax)
            st.pyplot(fig)

        with col2:
            st.header('Reordered: Y')
            fig, ax = plt.subplots()
            sns.histplot(x = 'add_to_cart_order', data=order_products_prior1.loc[order_products_prior1['reordered']==1], ax=ax)
            st.pyplot(fig)
    

    with tab1: 
        fig, ax = plt.subplots()
        st.header("Eval Set")
        st.markdown("See which set (old, training, test) our orders mostly belong to!")
        sns.countplot(x = "eval_set", data = orders1, palette='Set3', ax=ax)
        st.pyplot(fig)

    with tab2: 
        fig, ax = plt.subplots()
        st.header("Order Hour of Day")
        st.markdown("See how long our customers' orders take!")
        sns.histplot(x = "order_hour_of_day", data = orders1, color = 'yellowgreen', ax=ax)
        st.pyplot(fig)
    

    # 아래는 사이드로 빼도 안되려나 검색 형식으로(주식쪽 참고?)
    with tab3: # aisle_id
        fig, ax = plt.subplots()
        st.header("Aisle Id")
        st.markdown('You can see all the aisle IDs at a glance!👀')
        st.table(aisles.set_index('aisle_id'))
        st.pyplot(fig)

    with tab4: # department_id
        fig, ax = plt.subplots()
        st.header("Departmend Id")
        st.markdown('You can see all the department IDs at a glance!👀')
        st.table(departments.set_index('department_id'))
        st.pyplot(fig)


    # 사이드바 구성

    st.sidebar.title('ID Search🔎')
    
    st.sidebar.markdown('## Aisle Id')
    aisle_id_input = st.sidebar.text_input("Enter an ID of the aisle (e.g. 3)", value="3")
    st.sidebar.write("Searching: ", aisle_id_input)
    st.sidebar.write(aisles.loc[aisles['aisle_id'] == int(aisle_id_input), :].set_index('aisle_id'))

    st.sidebar.markdown('## Department Id')
    department_id_input = st.sidebar.text_input("Enter an ID of the department (e.g. 6)", value="6")
    st.sidebar.write("Searching: ", department_id_input)
    st.sidebar.write(departments.loc[departments['department_id'] == int(department_id_input), :].set_index('department_id'))


if __name__ == "__main__":
    main()
