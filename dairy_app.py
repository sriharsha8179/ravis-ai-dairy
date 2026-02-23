import streamlit as st

st.set_page_config(
    page_title="Ravi's AI Dairy Farm",
    page_icon="🐄",
    layout="wide"
)

st.markdown("""
<link rel="manifest" href="/static/manifest.json">
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/static/service-worker.js');
}
</script>
""", unsafe_allow_html=True)