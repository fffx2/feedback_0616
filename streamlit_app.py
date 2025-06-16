import streamlit as st
from pathlib import Path

st.set_page_config(page_title="WCAG 디자이너 도구", layout="centered")

# 🌐 웹폰트 적용 (Pretendard + Montserrat)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Pretendard&display=swap');

html, body, [class*="css"]  {
    font-family: 'Pretendard', 'Montserrat', sans-serif;
    max-width: 1500px;
    margin: auto;
}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 🚀 상단 메뉴
menu = st.selectbox(
    "📂 메뉴 선택",
    ["🏠 홈 안내", "📁 HTML 업로드", "🧱 시맨틱 구조 분석", "🎨 색상 & 폰트 분석"],
    label_visibility="collapsed"
)

# ✅ 연결
page_dir = Path(__file__).parent
page_files = {
    "📁 HTML 업로드": "page1.py",
    "🧱 시맨틱 구조 분석": "page2.py",
    "🎨 색상 & 폰트 분석": "page3.py"
}

if menu == "🏠 홈 안내":
    st.title("🔎 WCAG 기반 웹 접근성 디자인 검토 도구")
    st.markdown("""
이 도구는 **웹 디자이너의 시각에서 HTML 콘텐츠의 웹 접근성**을  
WCAG 2.1 가이드라인에 따라 분석할 수 있도록 설계되었습니다.

#### 분석 항목
- HTML 구조 및 시맨틱 마크업
- 색상 대비 및 명도 기준
- 폰트 크기 및 가독성
- 시각적 배치와 Reflow 유무
    """)
else:
    exec(open(page_dir / page_files[menu], encoding="utf-8").read())
