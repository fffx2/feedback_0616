import streamlit as st

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
