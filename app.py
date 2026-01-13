# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import random
import time

# ==========================================
# 1. 核心配置 (Core Config)
# ==========================================
st.set_page_config(
    page_title="OriginGuard Web3",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. 法律文本常量库 (IMMUTABLE LEGAL TEXTS)
# ==========================================
LEGAL_CONSTANTS = {
    "English": {
        "tos": """**1. Acceptance of Terms:** By accessing OriginGuard, you agree to be bound by these Terms.\n\n**2. Authorized Use:** You affirm that you are the lawful copyright owner of uploaded content.\n\n**3. Limitation:** We provide evidence, not legal outcomes.""",
        "refund": """**NO REFUND POLICY:**\n\nGas fees are paid instantly to the Solana network.\n\n**ALL SALES ARE FINAL.**\n\nNo cancellations or reversals allowed.""",
        "privacy": """**Data Privacy:**\nWe only hash files. We do not store original images. Your data remains yours.""",
        "sla": """**Enterprise SLA:**\n99.9% API Uptime Guarantee for Enterprise subscribers.""",
        "disclaimer": """**Disclaimer:**\nOriginGuard is a technology provider, not a law firm."""
    },
    "中文": {
        "tos": """**1. 条款接受：** 访问即表示同意。\n\n**2. 授权使用：** 严禁上传盗版内容。\n\n**3. 责任限制：** 我们提供技术证据，不承诺法庭结果。""",
        "refund": """**无退款政策：**\n\nGas 费已实时支付给区块链网络。\n\n**所有交易均为最终交易。**\n\n不支持任何形式的退款或撤销。""",
        "privacy": """**隐私政策：**\n我们只存储哈希值，不存储原图。数据归您所有。""",
        "sla": """**SLA 承诺：**\n企业版用户享受 99.9% 在线率保证。""",
        "disclaimer": """**免责声明：**\nOriginGuard 提供技术证明，非法律咨询机构。"""
    },
    "Myanmar": {
        "tos": """**စည်းမျဉ်းများ:** ဤဝန်ဆောင်မှုကို အသုံးပြုခြင်းဖြင့် စည်းကမ်းများကို လိုက်နာရန် သဘောတူပါသည်။""",
        "refund": """**ငွေပြန်မအမ်းပါ:** Blockchain ငွေပေးချေမှုများသည် ပြင်ဆင်၍မရပါ။""",
        "privacy": """**လုံခြုံရေး:** သင့်ပုံများကို ကျွန်ုပ်တို့ သိမ်းဆည်းမထားပါ။""",
        "sla": """**SLA:** ၉၉.၉% အချိန်ပြည့် အလုပ်လုပ်မည်။""",
        "disclaimer": """**ငြင်းဆိုချက်:** ကျွန်ုပ်တို့သည် နည်းပညာကိုသာ ပံ့ပိုးပေးသည်။"""
    }
}

# ==========================================
# 3. 动态 CSS (V4.0 企业级视觉重构)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 1. 全局字体与背景 */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
        color: #f8fafc !important; 
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
    }

    /* 2. 按钮样式重构 (彻底解决白底白字) */
    
    /* Primary Button (亮色渐变: Login, Launch) */
    button[kind="primary"] {
        background: linear-gradient(90deg, #FCD535 0%, #FBC100 100%) !important; /* Binance Yellow style for primary actions */
        color: #1e2329 !important; /* 黑字 */
        border: none !important;
        font-weight: 800 !important;
    }

    /* Secondary Button (深色玻璃: Footer, Legal) */
    div.stButton > button:not([kind="primary"]) {
        background-color: rgba(30, 41, 59, 0.7) !important; /* 深蓝灰背景 */
        color: #e2e8f0 !important; /* 亮灰白文字 */
        border: 1px solid rgba(148, 163, 184, 0.3) !important;
        border-radius: 8px;
        transition: all 0.3s;
    }
    div.stButton > button:not([kind="primary"]):hover {
        border-color: #FCD535 !important; /* 悬停变黄 */
        color: #ffffff !important;
        background-color: rgba(30, 41, 59, 1) !important;
    }

    /* 3. Cookie 弹窗样式 */
    .cookie-banner {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 800px;
        background: #1e2329;
        border: 1px solid #474d57;
        padding: 20px;
        border-radius: 12px;
        z-index: 9999;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    /* 4. 页脚矩阵样式 */
    .footer-header {
        color: #FCD535;
        font-weight: 700;
        margin-bottom: 10px;
        font-size: 14px;
        text-transform: uppercase;
    }

    /* 5. 标题流光 */
    h1 {
        background: linear-gradient(90deg, #FCD535, #f0fdf4, #FCD535);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientText 4s linear infinite;
    }
    @keyframes gradientText { 0% {background-position: 0% center;} 100% {background-position: 200% center;} }

</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. 语言字典 (UI 文本)
# ==========================================
TRANS = {
    "English": {
        "slogan": "Protect What You Create.",
        "sub_slogan": "The Global Standard for Web3 Copyright Defense.",
        "btn_launch": "🚀 LAUNCH CONSOLE",
        "cookie_msg": "We use cookies to ensure the security of your assets and to improve your experience. By clicking 'Accept', you agree to our cookie policy.",
        "cookie_btn": "Accept Cookies & Continue",
        # Footer Headers
        "f_comm": "Community",
        "f_legal": "Legal & Privacy",
        "f_prod": "Products",
        "f_serv": "Service",
        # Login
        "login_title": "Sign In",
        "login_email": "Access Code",
        "login_btn": "Verify & Enter",
        "login_error": "⚠️ Invalid Code.",
    },
    "中文": {
        "slogan": "捍卫你的数字资产",
        "sub_slogan": "Web3 版权保护全球标准 | 自动确权与维权",
        "btn_launch": "🚀 启动控制台",
        "cookie_msg": "我们使用 Cookie 以确保您的资产安全并提升体验。点击“接受”即表示您同意我们的 Cookie 政策。",
        "cookie_btn": "接受 Cookie 并继续",
        # Footer Headers
        "f_comm": "官方社区",
        "f_legal": "法律与隐私",
        "f_prod": "产品中心",
        "f_serv": "客户服务",
        # Login
        "login_title": "登录",
        "login_email": "访问密钥",
        "login_btn": "验证并进入",
        "login_error": "⚠️ 密钥错误。",
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး | ကမ္ဘာ့အဆင့်မီ နည်းပညာ",
        "btn_launch": "🚀 စနစ်စတင်မည်",
        "cookie_msg": "သင့်လုံခြုံရေးအတွက် ကျွန်ုပ်တို့ Cookie ကို အသုံးပြုပါသည်။",
        "cookie_btn": "လက်ခံမည်",
        # Footer Headers
        "f_comm": "ကွန်မြူနတီ",
        "f_legal": "ဥပဒေ",
        "f_prod": "ထုတ်ကုန်များ",
        "f_serv": "ဝန်ဆောင်မှု",
        # Login
        "login_title": "အကောင့်ဝင်ပါ",
        "login_email": "စကားဝှက်",
        "login_btn": "ဝင်မည်",
        "login_error": "⚠️ မှားယွင်းနေသည်။",
    }
}

# ==========================================
# 5. 逻辑控制
# ==========================================
lang_choice = st.sidebar.selectbox("🌐 Language / 语言", ["English", "中文", "Myanmar"], index=1)
T = TRANS[lang_choice]
L_TEXT = LEGAL_CONSTANTS[lang_choice]

if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'auth' not in st.session_state: st.session_state.auth = False
if 'cookies_accepted' not in st.session_state: st.session_state.cookies_accepted = False # Cookie 状态

def set_page(name): st.session_state.page = name

# --- Cookie 弹窗组件 (Binance Style) ---
def render_cookie_consent():
    if not st.session_state.cookies_accepted:
        st.markdown(f"""
        <div class="cookie-banner">
            <h4 style="color:white; margin:0;">🍪 Cookie Consent</h4>
            <p style="color:#b7bdc6; font-size:14px; margin: 10px 0;">{T['cookie_msg']}</p>
        </div>
        """, unsafe_allow_html=True)
        # 这里的按钮使用 Streamlit 原生按钮，放在容器中
        # 为了美观，我们放在页面最底部的主区域渲染逻辑里
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(T['cookie_btn'], type="primary", use_container_width=True):
                st.session_state.cookies_accepted = True
                st.rerun()

# --- 矩阵式页脚 (Fat Footer) ---
def render_fat_footer():
    st.write("")
    st.markdown("---")
    
    # 4列布局
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f"<div class='footer-header'>{T['f_comm']}</div>", unsafe_allow_html=True)
        st.button("👾 Discord", use_container_width=True)
        st.button("🐦 Twitter / X", use_container_width=True)
        st.button("✈️ Telegram", use_container_width=True)

    with c2:
        st.markdown(f"<div class='footer-header'>{T['f_legal']}</div>", unsafe_allow_html=True)
        if st.button("Terms (ToS)", use_container_width=True): 
            st.session_state.view_legal = "tos"; set_page('legal_view'); st.rerun()
        if st.button("Privacy Policy", use_container_width=True):
            st.session_state.view_legal = "privacy"; set_page('legal_view'); st.rerun()
        if st.button("No Refunds", use_container_width=True):
            st.session_state.view_legal = "refund"; set_page('legal_view'); st.rerun()

    with c3:
        st.markdown(f"<div class='footer-header'>{T['f_prod']}</div>", unsafe_allow_html=True)
        st.button("🛡️ OriginGuard API", disabled=True, use_container_width=True)
        st.button("⛓️ Solana Explorer", disabled=True, use_container_width=True)
        st.button("📱 Mobile App", disabled=True, use_container_width=True)

    with c4:
        st.markdown(f"<div class='footer-header'>{T['f_serv']}</div>", unsafe_allow_html=True)
        st.button("SLA Guarantee", use_container_width=True)
        st.button("Help Center", disabled=True, use_container_width=True)
        st.info("📧 support@originguard.com")

    st.markdown("---")
    st.markdown("<div style='text-align:center; color:#474d57; font-size:12px;'>© 2026 OriginGuard Solutions Inc. All rights reserved.</div>", unsafe_allow_html=True)

# --- 1. 官网首页 (Landing) ---
if st.session_state.page == 'landing':
    st.write("")
    st.markdown(f"""
    <div style="text-align: center; padding: 60px 0;">
        <h1 style="font-size: 64px; margin-bottom: 20px;">{T['slogan']}</h1>
        <p style="font-size: 24px; color: #e2e8f0; max-width: 800px; margin: 0 auto;">{T['sub_slogan']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    block_num = random.randint(245000000, 245999999)
    st.markdown(f"<div style='text-align: center; margin-bottom: 40px; color:#FCD535; font-weight:bold;'>🟢 Solana Mainnet Block #{block_num}</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(T['btn_launch'], use_container_width=True, type="primary"):
            set_page('login') 
            st.rerun()
    
    # 渲染 Cookie 弹窗 (如果没有接受)
    render_cookie_consent()
    
    # 渲染大页脚
    render_fat_footer()

# --- 2. 真实登录页 ---
elif st.session_state.page == 'login':
    st.write("")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown(f"## {T['login_title']}")
        password = st.text_input(T['login_email'], type="password")
        if st.button(T['login_btn'], type="primary", use_container_width=True):
            if password == "origin2026":
                with st.spinner("Connecting to Solana..."):
                    time.sleep(1)
                st.session_state.auth = True
                set_page('dashboard')
                st.rerun()
            else:
                st.error(T['login_error'])
        if st.button("⬅️ Back", use_container_width=True):
            set_page('landing'); st.rerun()
    render_fat_footer()

# --- 3. 控制台 (Dashboard) ---
elif st.session_state.page == 'dashboard':
    if not st.session_state.auth: set_page('login'); st.rerun()
    
    with st.sidebar:
        st.success("🟢 CEO: MNNO")
        if st.button("Log Out"): st.session_state.auth = False; set_page('landing'); st.rerun()

    st.title("📊 Enterprise Console")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Assets", "1,248")
    k2.metric("Threats", "53", "High", delta_color="inverse")
    k3.metric("Legal", "41")
    k4.metric("Saved", "$12,400")
    
    st.markdown("---")
    t1, t2 = st.tabs(["🛡️ Protect", "⚖️ Legal Hammer"])
    with t1:
        st.file_uploader("Upload Image", type=['png','jpg'])
        st.button("Encrypt", type="primary")
    with t2:
        st.text_input("Infringing URL")
        st.button("Send DMCA Notice", type="primary")

    render_fat_footer()

# --- 4. 法律详情页 ---
elif st.session_state.page == 'legal_view':
    st.button("⬅️ Back", on_click=lambda: set_page('landing'))
    st.markdown("---")
    key = st.session_state.get('view_legal', 'tos')
    st.info(LEGAL_CONSTANTS[lang_choice].get(key, "Error"))
    render_fat_footer()
