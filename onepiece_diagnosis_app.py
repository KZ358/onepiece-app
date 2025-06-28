import streamlit as st

st.title("MBTI風 性格診断 × 向いている職業")
st.markdown("12の質問に答えて、あなたの性格タイプと向いている職業を診断しましょう！")

# 初期化（4軸 × 2タイプ）
scores = {
    "E": 0, "I": 0,
    "S": 0, "N": 0,
    "T": 0, "F": 0,
    "J": 0, "P": 0,
}

# 質問（MBTI形式）
questions = [
    ("大人数の集まりは楽しい？", "E", "I"),
    ("一人の時間が大切？", "I", "E"),
    ("事実や経験を重視する？", "S", "N"),
    ("アイデアや可能性を大切にする？", "N", "S"),
    ("論理的な説明に納得しやすい？", "T", "F"),
    ("他人の気持ちに影響されやすい？", "F", "T"),
    ("物事は計画通りに進めたい？", "J", "P"),
    ("状況に応じて柔軟に動きたい？", "P", "J"),
    ("初対面でもすぐ話せる？", "E", "I"),
    ("細かいことより全体像を重視？", "N", "S"),
    ("対立しても正しいと思えば主張する？", "T", "F"),
    ("予定よりも流れに任せたい？", "P", "J"),
]

# 質問を表示
for idx, (q, a_type, b_type) in enumerate(questions):
    answer = st.radio(f"Q{idx+1}. {q}", ["はい", "いいえ"], key=q)
    if answer == "はい":
        scores[a_type] += 1
    else:
        scores[b_type] += 1

# 診断結果表示
if st.button("診断する"):
    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"

    job_map = {
        "ESTJ": "営業・管理職・プロジェクトマネージャー",
        "INFP": "カウンセラー・ライター・福祉職",
        "ENTP": "マーケター・企画職・起業家",
        "ISFJ": "事務職・看護師・学校職員",
        "INTJ": "エンジニア・研究職・戦略系コンサル",
        "ESFP": "接客業・イベント企画・芸能系",
        "ISTJ": "会計・行政職・技術職",
        "ENFP": "教育職・人材・SNSクリエイター"
    }
    job = job_map.get(mbti, "さまざまな分野で活躍できます！")

    st.subheader("🎯 診断結果")
    st.markdown(f"あなたの性格タイプは **{mbti} タイプ** です。")
    st.markdown(f"向いている職業：**{job}**")
