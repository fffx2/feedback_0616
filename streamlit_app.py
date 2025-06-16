import streamlit as st
from pathlib import Path

st.set_page_config(page_title="WCAG 디자이너 도구", layout="wide")

# 스타일 재설정: 프리텐다드 + 몬세라트, 가독성 높은 좌측 내비
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500&family=Pretendard&display=swap');

html, body, [class*="css"] {
    font-family: 'Pretendard', 'Montserrat', sans-serif;
    font-size: 17px;
    line-height: 1.75;
    color: #212121;
}

section[data-testid="stSidebar"] {
    background-color: #f8fafc;
    padding: 2rem 2rem;
    border-right: 1px solid #e0e0e0;
}

[data-testid="stSidebar"] .stRadio > div {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

[data-testid="stSidebar"] label {
    padding: 14px 18px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 500;
    transition: background 0.2s;
    color: #333333;
}

[data-testid="stSidebar"] label:hover {
    background-color: #e3f2fd;
}

[data-testid="stSidebar"] input:checked + div > label {
    background-color: #cbe7ff !important;
    color: #0d47a1 !important;
    font-weight: 600;
}

header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 내비게이션 메뉴
st.sidebar.title("🧭 WCAG 검사 메뉴")
menu = st.sidebar.radio("페이지 선택", [
    "🏠 홈 안내",
    "📁 HTML 업로드",
    "🧱 시맨틱 구조 분석",
    "🎨 색상 & 폰트 분석"
])

# 서브페이지 연결
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
    page_path = page_dir / page_files[menu]
    try:
        exec(open(page_path, encoding="utf-8").read(), globals())
    except FileNotFoundError:
        st.error(f"❌ 파일을 찾을 수 없습니다: {page_path}")
    except Exception as e:
        st.error(f"⚠️ 페이지 실행 중 오류 발생: {e}")
