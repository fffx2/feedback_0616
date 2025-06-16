import streamlit as st
from pathlib import Path

st.set_page_config(page_title="WCAG 디자이너 도구", layout="wide")

# 🌐 Pretendard + Montserrat, 좌측 내비 디자인 개선
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Pretendard&display=swap');

html, body, [class*="css"]  {
    font-family: 'Pretendard', 'Montserrat', sans-serif;
    max-width: 1500px;
    margin: auto;
}

section[data-testid="stSidebar"] {
    background-color: #f7f9fa;
    padding: 2rem 1rem;
    border-right: 1px solid #e0e0e0;
}

.css-1d391kg {  /* 사이드바 라디오 버튼 전체 */
    font-size: 16px !important;
    padding: 8px 14px !important;
    border-radius: 8px;
}

.css-1d391kg:hover {
    background-color: #e3f2fd;
}

header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 📚 사이드바 내비게이션
st.sidebar.title("🧭 WCAG 검사 메뉴")
menu = st.sidebar.radio("이동할 페이지", [
    "🏠 홈 안내",
    "📁 HTML 업로드",
    "🧱 시맨틱 구조 분석",
    "🎨 색상 & 폰트 분석"
])

# 📂 서브페이지 연결
page_dir = Path(__file__).parent / "pages"
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
