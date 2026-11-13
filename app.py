from pathlib import Path
import json
import re
import uuid
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='응답하라! 우리 오락실', page_icon='🟡', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>
  [data-testid="stApp"],[data-testid="stAppViewContainer"]{background:#050817;color:#edf5ff;color-scheme:dark}
  .block-container{padding:0.5rem 1rem}
  header[data-testid="stHeader"]{display:none}
  [data-testid="stLinkButton"] a{background:#101b36;color:#d3f5ff;border:1px solid #4d9ac1;border-radius:7px;box-shadow:0 0 12px #31bdff22}
  [data-testid="stLinkButton"] a:hover{border-color:#71e4ff;background:#152944;color:#fff}
  [data-testid="stCaptionContainer"]{color:#a7bddb}
  </style>''', unsafe_allow_html=True)
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
if not operator:
    st.markdown('''<style>
    [data-testid="stMainBlockContainer"]{padding-top:0.5rem!important;padding-bottom:0!important}
    [data-testid="stVerticalBlock"]{gap:0.5rem}
    [data-testid="stElementContainer"]:has(iframe[data-testid="stIFrame"]){height:calc(100dvh - 86px)!important;min-height:0!important}
    iframe[data-testid="stIFrame"]{height:calc(100dvh - 86px)!important;}
    </style>''', unsafe_allow_html=True)
config = json.dumps({'streamlit': True, 'channel': channel, 'build': 21})
html = html.replace('<script>', '<script>const APP_CONFIG=' + config + ';\n', 1)
components.html(html, height=1100 if operator else 700, scrolling=True)
