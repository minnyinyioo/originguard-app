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
        "tos": """### 1. Acceptance of Terms
By accessing OriginGuard, you agree to be bound by these Terms.

### 2. Authorized Use
You affirm that you are the lawful copyright owner of uploaded content. Uploading stolen content will result in immediate ban.

### 3. Limitation
We provide blockchain evidence, not legal outcomes.""",
        "refund": """### NO REFUND POLICY (STRICT)
**Gas fees are paid instantly to the Solana network.**

**ALL SALES ARE FINAL.**
Once a transaction is initiated, it cannot be canceled, reversed, or refunded.
By using this service, you waive your right to a cooling-off period.""",
        "privacy": """### Data Privacy
1. **Data Minimization:** We only hash files.
2. **No Storage:** We do not store original images.
3. **Ownership:** Your data remains yours.""",
        "sla": """### Enterprise SLA
We guarantee **99.9%** API Uptime for Enterprise subscribers.
Credits are issued for downtime exceeding limits.""",
        "disclaimer": """### Legal Disclaimer
OriginGuard is a technology provider, **not a law firm**.
The "Legal Hammer" tools are for reference only."""
    },
    "中文": {
        "tos": """### 1. 服务条款
访问即表示同意本条款。如果您不同意，请立即停止使用。

### 2. 授权使用
严禁上传盗版内容。一旦发现，我们将立即封禁账号。

### 3. 责任限制
我们提供区块链技术证据，但不承诺特定的法庭判决结果。""",
        "refund": """### 🚫 无退款政策 (No Refund)
**Gas 费已实时支付给区块链网络。**

**所有交易均为最终交易。**
OriginGuard 不支持任何形式的退款、撤销或回滚操作。
请在支付前仔细确认。""",
        "privacy": """### 🔒 隐私政策
1. **数据最小化**：我们只存储文件的数字哈希值。
2. **不存原图**：您的原始高清图片从未上传到我们的服务器。
3. **数据主权**：数据归您所有。""",
        "sla": """### ⚡ SLA 服务承诺
对于企业版订阅用户，我们承诺 **99.9%** 的 API 在线率。
如未达标，我们将按照合同约定进行赔偿。""",
        "disclaimer": """### ⚠️ 免责声明
OriginGuard 是一家技术提供商，而**非律师事务所**。
我们提供的“自动律师函”仅供参考，不构成法律建议。"""
    },
    "Myanmar": {
        "tos": """### စည်းမျဉ်းများ
ဤဝန်ဆောင်မှုကို အသုံးပြုခြင်းဖြင့် စည်းကမ်းများကို လိုက်နာရန် သဘောတူပါသည်။""",
        "refund": """### ငွေပြန်မအမ်းပါ (No Refund)
Blockchain ငွေပေးချေမှုများသည် ပြင်ဆင်၍မရပါ။
**ငွေပြန်အမ်းခြင်း မပြုလုပ်နိုင်ပါ။**""",
        "privacy": """### လုံခြုံရေး
သင့်ပုံများကို ကျွန်ုပ်တို့ သိမ်းဆည်းမထားပါ။""",
        "sla": """### SLA အာမခံချက်
၉၉.၉% အချိန်ပြည့် အလုပ်လုပ်မည်။""",
        "disclaimer": """### ငြင်းဆိုချက်
ကျွန်ုပ်တို့သည် နည်းပညာကိုသာ ပံ့ပိုးပေးသည်။"""
    }
}

# ==========================================
# 3. 动态 CSS (V4.2: 高对比度 + 真实组件)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 1. 背景动画：深海渐变 + 粒子下落 */
    @keyframes move-background {
        from {transform: translate3d(0px, 0px, 0px);}
        to {transform: translate3d(0px, 1000px, 0px);}
    }
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
        color: #ffffff !important; 
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
    }
    
    .stApp::before {
        content: "";
        position: absolute;
        top: -1000px;
        left: 0;
        width: 100%;
        height: 300%;
        background-image: 
            radial-gradient(2px 2px at 100px 50px, #22d3ee, transparent),
            radial-gradient(2px 2px at 300px 450px, #818cf8, transparent),
            radial-gradient(1.5px 1.5px at 600px 100px, #ffffff, transparent);
        background-size: 1000px 1000px;
        animation: move-background 40s linear infinite;
        opacity: 0.3; 
        z-index: 0;
        pointer-events: none;
    }

    /* 2. 法律条款专用容器 (黑底白字，强制覆盖) */
    .legal-box {
        background-color: #000000 !important;
        border: 1px solid #333;
        padding: 25px;
        border-radius: 12px;
        color: #ffffff !important;
        font-size: 16px;
        line-height: 1.6;
        box-shadow: 0 5px 20px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }
    .legal-box h3 {
        color: #FCD535 !important; /* 金色标题 */
        margin-top: 0;
        font-size: 20px;
    }

    /* 3. 按钮样式重构 */
    /* Primary (Binance Yellow) */
    button[kind="primary"] {
        background: linear-gradient(90deg, #FCD535 0%, #FBC100 100%) !important;
        color: #1e2329 !important;
        border: none !important;
        font-weight: 800 !important;
    }
    /* Secondary (Glass - Footer) */
    div.stButton > button:not([kind="primary"]) {
        background-color: rgba(30, 41, 59, 0.6) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(148, 163, 184, 0.3) !important;
        border-radius: 6px;
    }
    div.stButton > button:not([kind="primary"]):hover {
        border-color: #FCD535 !important;
        color: #fff !important;
        background-color: rgba(30, 41, 59, 1) !important;
    }

    /* 4. Cookie 弹窗 (Binance Style) */
    .cookie-banner {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #1e2329;
        border-top: 2px solid #FCD535;
        padding: 20px;
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
    }
    
    /* 5. 页脚标题 */
    .footer-title {
        color: #FCD535;
        font-weight: 700;
        font-size: 14px;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. 语言字典
# ==========================================
TRANS = {
    "English": {
        "slogan": "Protect What You Create.",
        "sub_slogan": "The Global Standard for Web3 Copyright Defense.",
        "btn_launch": "🚀 LAUNCH CONSOLE",
        "cookie_msg": "We use cookies to ensure asset security. By continuing, you agree to our Terms.",
        "cookie_btn": "Accept & Continue",
        "f_comm": "Community", "f_legal": "Legal", "f_prod": "Products", "f_serv": "Support",
        "login_title": "Sign In", "login_email": "Access Code", "login_btn": "Verify & Enter", "login_error": "Invalid Code.",
        "titles": ["Terms", "Refund", "Privacy", "SLA", "Disclaimer"]
    },
    "中文": {
        "slogan": "捍卫你的数字资产",
        "sub_slogan": "Web3 版权保护全球标准 | 自动确权与维权",
        "btn_launch": "🚀 启动控制台",
        "cookie_msg": "我们使用 Cookie 保障您的资产安全。继续使用即表示您同意我们的条款。",
        "cookie_btn": "接受并继续",
        "f_comm": "官方社区", "f_legal": "法律条款", "f_prod": "产品中心", "f_serv": "客户支持",
        "login_title": "登录", "login_email": "访问密钥", "login_btn": "验证并进入", "login_error": "密钥错误。",
        "titles": ["服务条款", "无退款政策", "隐私政策", "SLA承诺", "免责声明"]
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး",
        "btn_launch": "🚀 စနစ်စတင်မည်",
        "cookie_msg": "သင့်လုံခြုံရေးအတွက် Cookie အသုံးပြုပါသည်။",
        "cookie_btn": "လက်ခံမည်",
        "f_comm": "ကွန်မြူနတီ", "f_legal": "ဥပဒေ", "f_prod": "ထုတ်ကုန်များ", "f_serv": "ဝန်ဆောင်မှု",
        "login_title": "အကောင့်ဝင်ပါ", "login_email": "စကားဝှက်", "login_btn": "ဝင်မည်", "login_error": "မှားယွင်းနေသည်။",
        "titles": ["စည်းမျဉ်းများ", "ငွေပြန်မအမ်းပါ", "လုံခြုံရေး", "SLA", "ငြင်းဆိုချက်"]
    }
}

# ==========================================
# 5. 逻辑控制
# ==========================================
lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "中文", "Myanmar"], index=1)
T = TRANS[lang_choice]
L_TEXT = LEGAL_CONSTANTS[lang_choice]

if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'auth' not in st.session_state: st.session_state.auth = False
if 'cookies_accepted' not in st.session_state: st.session_state.cookies_accepted = False

def set_page(name): st.session_state.page = name

# --- 组件：大页脚 (Binance Style) ---
def render_fat_footer():
    st.write("")
    st.markdown("---")
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f"<div class='footer-title'>{T['f_comm']}</div>", unsafe_allow_html=True)
        st.button("👾 Discord", use_container_width=True)
        st.button("🐦 Twitter / X", use_container_width=True)
        st.button("✈️ Telegram", use_container_width=True)

    with c2:
        st.markdown(f"<div class='footer-title'>{T['f_legal']}</div>", unsafe_allow_html=True)
        # 点击法律按钮，跳转到 legal_view
        if st.button("Terms (ToS)", key="ft1", use_container_width=True): 
            st.session_state.view_legal = "tos"; set_page('legal_view'); st.rerun()
        if st.button("No Refunds", key="ft2", use_container_width=True):
            st.session_state.view_legal = "refund"; set_page('legal_view'); st.rerun()
        if st.button("Privacy", key="ft3", use_container_width=True):
            st.session_state.view_legal = "privacy"; set_page('legal_view'); st.rerun()

    with c3:
        st.markdown(f"<div class='footer-title'>{T['f_prod']}</div>", unsafe_allow_html=True)
        st.button("API Docs", disabled=True, use_container_width=True)
        st.button("Solana Scan", disabled=True, use_container_width=True)

    with c4:
        st.markdown(f"<div class='footer-title'>{T['f_serv']}</div>", unsafe_allow_html=True)
        st.button("SLA Guarantee", use_container_width=True)
        st.info("✉️ support@originguard.com")

    st.markdown("<div style='text-align:center; color:#64748b; font-size:12px; margin-top:30px;'>© 2026 OriginGuard Solutions Inc.</div>", unsafe_allow_html=True)
    
    # Cookie Banner
    if not st.session_state.cookies_accepted:
        st.markdown(f"""
        <div class="cookie-banner">
            <span style="color:#fff; font-size:16px; margin-right:20px;">🍪 {T['cookie_msg']}</span>
        </div>
        """, unsafe_allow_html=True)
        # 按钮在 Streamlit 布局中渲染
        c_k1, c_k2, c_k3 = st.columns([1,1,1])
        with c_k2:
             if st.button(T['cookie_btn'], type="primary", use_container_width=True, key="cookie_accept"):
                st.session_state.cookies_accepted = True
                st.rerun()

# --- 1. 官网首页 ---
if st.session_state.page == 'landing':
    st.write("")
    st.markdown(f"""
    <div style="text-align: center; padding: 60px 0;">
        <h1 style="font-size: 64px; margin-bottom: 20px;">{T['slogan']}</h1>
        <p style="font-size: 24px; color: #f8fafc; font-weight:600;">{T['sub_slogan']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    block_num = random.randint(245000000, 245999999)
    st.markdown(f"<div style='text-align: center; margin-bottom: 40px; color:#FCD535; font-weight:bold;'>🟢 Solana Mainnet Block #{block_num}</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(T['btn_launch'], use_container_width=True, type="primary"):
            set_page('login'); st.rerun()
            
    render_fat_footer()

# --- 2. 真实登录页 ---
elif st.session_state.page == 'login':
    st.write("")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown(f"## {T['login_title']}")
        pwd = st.text_input(T['login_email'], type="password")
        if st.button(T['login_btn'], type="primary", use_container_width=True):
            if pwd == "origin2026":
                with st.spinner("Connecting..."): time.sleep(1)
                st.session_state.auth = True; set_page('dashboard'); st.rerun()
            else:
                st.error(T['login_error'])
        
        st.markdown("---")
        st.button("🇬 Google", use_container_width=True)
        st.button("🍎 Apple", use_container_width=True)
        if st.button("⬅️ Back", use_container_width=True): set_page('landing'); st.rerun()
        
    render_fat_footer()

# --- 3. 控制台 ---
elif st.session_state.page == 'dashboard':
    if not st.session_state.auth: set_page('login'); st.rerun()
    
    with st.sidebar:
        st.success("🟢 CEO: MNNO")
        if st.button("Log Out"): st.session_state.auth=False; set_page('landing'); st.rerun()

    st.title("📊 Dashboard")
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
        st.button("Send Notice", type="primary")

    render_fat_footer()

# --- 4. 法律详情页 (High Contrast) ---
elif st.session_state.page == 'legal_view':
    st.button("⬅️ Back", on_click=lambda: set_page('landing'))
    st.markdown("---")
    
    key = st.session_state.get('view_legal', 'tos')
    content = L_TEXT.get(key, "Error")
    
    # 使用自定义 CSS 类 .legal-box 渲染纯黑底白字
    st.markdown(f"""
    <div class="legal-box">
        {content}
    </div>
    """, unsafe_allow_html=True)
    
    render_fat_footer()
