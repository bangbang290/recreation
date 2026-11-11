from pathlib import Path
import json
import re
import uuid
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='응답하라! 우리 오락실', page_icon='📺', layout='wide', initial_sidebar_state='collapsed')
st.markdown('<style>[data-testid="stAppViewContainer"]{background:#f4e5ca}.block-container{padding:0.5rem 1rem}header[data-testid="stHeader"]{display:none}</style>', unsafe_allow_html=True)
html = Path(__file__).with_name('index.html').read_text(encoding='utf-8')
operator = st.query_params.get('operator') == '1'
channel = st.query_params.get('channel', '')
if not re.fullmatch(r'[a-zA-Z0-9-]{1,80}', channel):
    channel = ''
if not operator:
    if 'workshop_channel' not in st.session_state:
        st.session_state.workshop_channel = uuid.uuid4().hex
    channel = st.session_state.workshop_channel
    st.link_button('진행요원 창 열기 ↗', '?operator=1&channel=' + channel)
else:
    st.caption('진행요원 전용 · 이 창은 노트북에 두세요.')
if operator:
    html = html.replace('<body>', '<body class="operator">', 1)
config = json.dumps({'streamlit': True, 'channel': channel})
html = html.replace('<script>', '<script>const APP_CONFIG=' + config + ';\n', 1)
components.html(html, height=1100, scrolling=True)
