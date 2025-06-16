import streamlit as st

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
