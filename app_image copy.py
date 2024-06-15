import os
from openai import OpenAI
import streamlit as st # 이 순서에 유의해 주세요!, 임포트 안되어 있으면 임포트 전까지 코드에는 안먹음

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title('슈퍼 시나리오 봇🤩')
keyword = st.text_input("키워드를 입력하세요")


    
if st.button('생성하기'):
    with st.spinner('시나리오를 열심히 만들고 있어요'):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": keyword,
                },
                {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 흥미진진한 300자 이내의 시나리오를 작성해줘.",
                }
            ],
            model="gpt-4o",
        )
    result = chat_completion.choices[0].message.content
    st.write(result)