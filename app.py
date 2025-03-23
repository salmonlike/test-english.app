import streamlit as st
import openai
import os


# APIキーを直接文字列で設定
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


st.title("英会話練習アプリ")

user_input = st.text_input("英語で話しかけてみよう")

if st.button("送信") and user_input:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a kind English teacher. Respond in English."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        st.write("AIの返答：", reply)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
