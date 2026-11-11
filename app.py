from pathlib import Path
import json
import re
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='응답하라! 우리 오락실', page_icon='📺', layout='wide', initial_sidebar_state='collapsed')
st.markdown('<style>[data-testid="stAppViewContainer"]{background:#f4e5ca}.block-container{padding:0.5rem 1rem}header[data-testid="stHeader"]{display:none}</style>', unsafe_allow_html=True)
html = Path(__file__).with_name('index.html').read_text(encoding='utf-8')
operator = st.query_params.get('operator') == '1'
channel = st.query_params.get('channel', '')
if not re.fullmatch(r'[a-zA-Z0-9-]{1,80}', channel):
    channel = ''
if operator:
    html = html.replace('<body>', '<body class="operator">', 1)
config = json.dumps({'streamlit': True, 'channel': channel if operator else ''})
html = html.replace('<script>', '<script>const APP_CONFIG=' + config + ';\n', 1)
components.html(html, height=1100, scrolling=True)
