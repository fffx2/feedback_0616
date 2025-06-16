import streamlit as st

st.set_page_config(page_title="WCAG 접근성 디자이너 도구", layout="wide")
st.title("🔎 WCAG 기반 웹 접근성 디자인 검토 도구")

st.markdown("""
이 도구는 **웹 디자이너의 시각에서 HTML 콘텐츠의 웹 접근성**을  
WCAG 2.1 가이드라인에 따라 분석할 수 있도록 설계되었습니다.

---

📂 **분석 가능한 항목**
- HTML 구조 및 시맨틱 마크업
- 색상 대비 및 명도 기준
- 폰트 크기 및 가독성
- 시각적 배치와 Reflow 유무

아래 페이지에서 HTML을 업로드하여 분석을 시작하세요.
""")
