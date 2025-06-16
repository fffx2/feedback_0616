import streamlit as st

st.set_page_config(page_title="WCAG 디자이너 도구", layout="centered")

# 웹폰트 설정
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

# 메뉴
menu = st.selectbox(
    "📂 메뉴 선택",
    ["🏠 홈 안내", "📁 HTML 업로드", "🧱 시맨틱 구조 분석", "🎨 색상 & 폰트 분석"],
    label_visibility="collapsed"
)

# 상태 저장용
if 'html_str' not in st.session_state:
    st.session_state['html_str'] = ""

# 홈
if menu == "🏠 홈 안내":
    st.title("🔎 WCAG 기반 웹 접근성 디자인 검토 도구")
    st.markdown("""
이 도구는 **웹 디자이너의 시각에서 HTML 콘텐츠의 웹 접근성**을  
WCAG 2.1 가이드라인에 따라 분석할 수 있도록 설계되었습니다.
""")

# HTML 업로드
elif menu == "📁 HTML 업로드":
    st.title("📁 HTML 업로드 및 미리보기")
    uploaded_file = st.file_uploader("HTML 파일을 업로드하세요", type="html")
    if uploaded_file:
        html_str = uploaded_file.read().decode("utf-8")
        st.session_state['html_str'] = html_str
        st.subheader("📌 코드 미리보기")
        st.code(html_str[:1000] + "..." if len(html_str) > 1000 else html_str, language='html')
        st.success("✅ 분석 준비 완료! 다른 탭에서 분석을 진행하세요.")
    else:
        st.info("HTML 파일을 업로드하면 다른 탭에서 분석이 가능해집니다.")

# 시맨틱 분석
elif menu == "🧱 시맨틱 구조 분석":
    st.title("🧱 시맨틱 구조 분석")
    html = st.session_state.get('html_str', None)
    if html:
        st.subheader("✅ 시맨틱 태그 점검")
        tags = ["<header", "<main", "<footer", "<nav", "<section"]
        for tag in tags:
            if tag in html:
                st.success(f"{tag} 태그가 사용되었습니다.")
            else:
                st.warning(f"{tag} 태그가 없습니다.")
        if "<h1" in html and "<h2" in html:
            st.success("헤딩 구조가 감지되었습니다 (h1~h2).")
        else:
            st.warning("헤딩 구조가 미흡하거나 누락되어 있습니다.")
    else:
        st.error("HTML 파일을 먼저 업로드해주세요.")

# 색상 분석
elif menu == "🎨 색상 & 폰트 분석":
    st.title("🎨 색상 및 폰트 분석")
    html = st.session_state.get('html_str', None)
    if html:
        st.subheader("🔠 폰트 크기 분석")
        if "font-size: 16px" in html:
            st.success("기본 텍스트가 16px 이상입니다. (접근성 기준 통과)")
        else:
            st.warning("텍스트 크기가 작을 수 있습니다.")
        st.subheader("🌗 대비 색상 분석")
        if "#fff" in html and ("#aaa" in html or "#ccc" in html):
            st.error("흰색 배경에 흐린 회색 텍스트가 감지되었습니다.")
        else:
            st.success("명도 대비 기준 위반 요소는 명확히 보이지 않습니다.")
    else:
        st.error("HTML 파일을 먼저 업로드해주세요.")
