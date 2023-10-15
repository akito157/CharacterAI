import streamlit as st
import openai
from time import sleep
import os
import base64
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    layout = "wide",
    page_title = "キャラクター育成",

)

file_name = 'src/style.css'
with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

image = Image.open('static/toranpet.png')

left, mid, right =  st.columns([3,0.5, 3])

left.header("🏫 あなたのプロフィール")

# 名前
l_name = left.expander('名前の入力', expanded=True)
l_name_c1, l_name_c2 = l_name.columns(2)
name = l_name_c1.text_input("名前", value="", placeholder="山田 太郎")
nick_name = l_name_c2.text_input("あだ名", value="", placeholder="やまちゃん")

# 部活動
l_act = left.expander('部活動', expanded=True)
l_act_c1, l_act_c2 =  l_act.columns(2)
bukatu = l_act_c1.text_input("部活", value="", placeholder="吹奏楽部")
bukatu_position = l_act_c2.text_input("役割", value="", placeholder="トランペット")
bukatu_goal =  l_act_c1.text_area('目標', placeholder='コンクール金賞')
bukatu_task =  l_act_c2.text_area('課題', placeholder='毎日朝練習')

# 勉強
l_study = left.expander('勉強', expanded=True)
l_study_c1, l_study_c2 =  l_study.columns(2)
like = l_study_c1.text_input("好きな科目", value="", placeholder="数学")
hate = l_study_c2.text_input("苦手な科目", value="", placeholder="歴史")

# 進路
l_career = left.expander('進路', expanded=True)
l_career_c1, l_career_c2 =  l_career.columns(2)
sinro = l_career_c1.selectbox("進学 or 就職", options=['進学', '就職'])
sinro_name = l_career_c2.text_input("進路先名", value="", placeholder="◯◯大学 OR 〇〇会社")

# ボタンエリア
l_con = left.container()
l_con_col1, l_con_col2, *l_col = l_con.columns(5)
is_generate = l_con_col1.button("生成", type='primary')
is_reset = l_con_col2.button("やり直し")

if is_reset:
    st.experimental_rerun()  # Streamlitのセッションをリセット

if is_generate:
    with st.spinner("説明考え中..."):
        sleep(2)  # 2秒待機

        prompt = f"{name}について、{nick_name}に例えて、説明してください。"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=0.5,
            messages=[
                {"role": "user", "content": prompt}],
        )
        left.write(response.choices[0].message.content)


image_container = right.markdown(f'<div class="image_container"></div>', unsafe_allow_html=True)
right.header('「部活動」　✕　可能性！')
right.subheader('あなたの成長する可能性をキャラクターにします')
r_col1, r_col2 =  right.columns(2)
r_col1.image(image, caption="character A")
text = "やまちゃん、こんにちは！一緒に成長していこうね！"
r_col2.markdown(f'<div class="dialogue_container">{text}</div>', unsafe_allow_html=True)



