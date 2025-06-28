
import streamlit as st

st.title("ワンピースキャラ診断 × あなたに向いてる職業")

st.markdown("以下の質問に答えて、あなたに似たワンピースキャラと向いてる職業を診断しよう！")

q1 = st.radio("Q1. 困っている仲間がいたら？", ["A: すぐに動く", "B: 作戦を立てる", "C: とにかく励ます"])
q2 = st.radio("Q2. 目標に向かって努力できる？", ["A: コツコツやれる", "B: 無理せず工夫する"])
q3 = st.radio("Q3. 人前で話すのは？", ["A: 得意", "B: 苦手"])
q4 = st.radio("Q4. あなたの強みは？", ["A: 情熱と行動力", "B: 頭の良さと分析力", "C: 優しさと気配り", "D: 表現力"])

if st.button("診断する"):
    if q1.startswith("A") and q4 == "A: 情熱と行動力":
        character = "ルフィ"
        job = "営業職・起業家・店舗マネージャー"
    elif q1.startswith("B") and q4 == "B: 頭の良さと分析力":
        character = "ナミ"
        job = "経理・事務職・マーケティング"
    elif q4 == "C: 優しさと気配り":
        character = "チョッパー"
        job = "看護助手・医療福祉系・保育士"
    elif q4 == "D: 表現力":
        character = "ウソップ"
        job = "クリエイター・コピーライター・広告"
    elif q2.startswith("A") and q3.startswith("B"):
        character = "ゾロ"
        job = "職人・整備士・施工管理"
    elif q2.startswith("B") and q3.startswith("A"):
        character = "ブルック"
        job = "アーティスト・音楽・舞台系"
    else:
        character = "ロビン"
        job = "研究職・司書・法務"

    st.subheader("🎉 診断結果 🎉")
    st.markdown(f"あなたは **{character} タイプ**！")
    st.markdown(f"向いている職業は：**{job}**")
