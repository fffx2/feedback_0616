import streamlit as st

st.title("🧱 시맨틱 구조 및 마크업 분석")

html = st.session_state.get('html_str', None)

if html:
    st.markdown("### ✅ 시맨틱 태그 사용 여부")
    if all(tag in html for tag in ["<header", "<main", "<footer"]):
        st.success("header/main/footer 태그가 모두 사용되었습니다.")
    else:
        st.warning("시맨틱 태그 일부가 누락되었습니다.")

    st.markdown("### ✅ 헤딩 구조")
    if "<h1" in html and "<h2" in html:
        st.success("h1, h2 계층적 구조 감지됨")
    else:
        st.error("헤딩 구조가 부족하거나 잘못된 것 같습니다.")
else:
    st.error("⚠️ 먼저 'HTML 업로드' 탭에서 파일을 업로드해주세요.")
