# -*- coding:utf-8 -*-
# 배포

# 가상환경 구축 -> 라이브러리 txt 만들기 -> pip install -r requirements.txt -> coding:utf-8 -> streamlit식 포맷(def, if __name__)

import streamlit as st
import pandas as pd
import seaborn as sns

def main():
    st.title("Hello :heart:")
    iris = sns.load_dataset('iris')
    st.write(iris)

if __name__ == "__main__":
    main()
