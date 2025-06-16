import streamlit as st

st.title("🎨 색상 대비 및 폰트 가독성")

html = st.session_state.get('html_str', None)

if html:
    st.markdown("### 🔠 글꼴 크기 확인")
    if "font-size: 16px" in html:
        st.success("텍스트가 WCAG 기준 16px 이상으로 설정됨")
    else:
        st.warning("일부 텍스트가 16px 미만일 수 있음")

    st.markdown("### 🌗 명도 대비 감지")
    if "#fff" in html and ("#ccc" in html or "#aaa" in html):
        st.error("흰 배경 + 흐린 회색 텍스트 조합 감지됨")
    else:
        st.success("색상 대비 기준을 위반하지 않는 것으로 보입니다.")
else:
    st.error("⚠️ HTML 파일을 먼저 업로드해주세요.")
