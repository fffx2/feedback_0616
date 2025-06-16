import streamlit as st
from pathlib import Path
import importlib.util

st.set_page_config(page_title="WCAG 디자이너 도구", layout="wide")

# Pretendard + Montserrat + 내비 디자인
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
[data-testid="stSidebar"] label {
    padding: 14px 18px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 500;
    transition: background 0.2s;
    color: #333333;
}
[data-testid="stSidebar"] input:checked + div > label {
    background-color: #cbe7ff !important;
    color: #0d47a1 !important;
    font-weight: 600;
}
header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 좌측 내비게이션
st.sidebar.title("🧭 WCAG 검사 메뉴")
menu = st.sidebar.radio("페이지 선택", [
    "🏠 홈 안내",
    "📁 HTML 업로드",
    "🧱 시맨틱 구조 분석",
    "🎨 색상 & 폰트 분석"
])

# 페이지 매핑
page_dir = Path(__file__).parent / "pages"
page_map = {
    "📁 HTML 업로드": "page1",
    "🧱 시맨틱 구조 분석": "page2",
    "🎨 색상 & 폰트 분석": "page3"
}

if menu == "🏠 홈 안내":
    st.title("🔎 WCAG 기반 웹 접근성 디자인 검토 도구")
    st.markdown("""
이 도구는 **웹 디자이너의 시각에서 HTML 콘텐츠의 웹 접근성**을  
WCAG 2.1 가이드라인에 따라 분석할 수 있도록 설계되었습니다.
""")
else:
    module_name = page_map[menu]
    file_path = page_dir / f"{module_name}.py"
    if file_path.exists():
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        st.error(f"❌ 파일을 찾을 수 없습니다: {file_path}")
