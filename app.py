# -*- coding:utf-8 -*-
# 배포

# 가상환경 구축 -> 라이브러리 txt 만들기 -> pip install -r requirements.txt -> coding:utf-8 -> streamlit식 포맷(def, if __name__)

import streamlit as st
import pandas as pd
import seaborn as sns

# 데이터 불러오기
@st.cache_data
def load_data():
    df = sns.load_dataset("iris")
    return df


def main():
    st.title("Hello :heart:")
    iris = load_data()
    st.table(iris)              # 코드 변경사항은 git add, commit, push로 업데이트


if __name__ == "__main__":
    main()
