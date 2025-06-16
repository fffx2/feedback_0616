import streamlit as st

st.set_page_config(page_title="WCAG 검사 도구", layout="wide")

st.title("🔎 WCAG 접근성 검사 툴 소개")

st.markdown("""
이 도구는 웹 디자이너가 HTML 콘텐츠를 **WCAG 2.1 기준으로 검사**할 수 있도록 지원합니다.  
좌측 메뉴에서 각 기능을 선택해보세요:

- 📁 HTML 업로드
- 🧱 시맨틱 구조 분석
- 🎨 색상/폰트 대비 분석
""")
