from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='응답하라! 우리 오락실', page_icon='📺', layout='wide', initial_sidebar_state='collapsed')
st.markdown('<style>[data-testid="stAppViewContainer"]{background:#f4e5ca}.block-container{padding:0.5rem 1rem}header[data-testid="stHeader"]{display:none}</style>', unsafe_allow_html=True)
components.html(Path(__file__).with_name('index.html').read_text(encoding='utf-8'), height=1000, scrolling=True)
