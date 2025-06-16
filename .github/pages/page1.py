import streamlit as st

st.title("📁 HTML 업로드 및 미리보기")

uploaded_file = st.file_uploader("HTML 파일을 업로드하세요", type="html")

if uploaded_file:
    html_str = uploaded_file.read().decode("utf-8")
    st.session_state['html_str'] = html_str
    st.subheader("📌 코드 미리보기")
    st.code(html_str[:1000] + "..." if len(html_str) > 1000 else html_str, language='html')
    st.success("✅ 분석 준비 완료! 다른 탭으로 이동해 분석을 진행하세요.")
else:
    st.info("HTML 파일을 업로드하면 다른 탭에서 분석이 가능해집니다.")
