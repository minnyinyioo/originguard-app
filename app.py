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
        "tos": """### 1. 条款接受
访问即表示同意本条款。如果您不同意，请立即停止使用。

### 2. 授权使用
严禁上传盗版内容。一旦发现，我们将立即封禁账号并保留追究法律责任的权利。

### 3. 责任限制
我们提供区块链技术证据，但不承诺特定的法庭判决结果。""",
        "refund": """### 无退款政策 (No Refund Policy)

**Gas 费已实时支付给区块链网络。**

由于区块链技术的不可逆特性，**所有交易均为最终交易**。
OriginGuard 不支持任何形式的退款、撤销或回滚操作。
请在支付前仔细确认。""",
        "privacy": """### 隐私政策 (Privacy)

1. **数据最小化**：我们只存储文件的数字哈希值。
2. **不存原图**：您的原始高清图片从未上传到我们的服务器。
3. **数据主权**：数据归您所有，我们绝不出售用户数据。""",
        "sla": """### SLA 服务承诺

对于企业版订阅用户，我们承诺 **99.9%** 的 API 在线率。
如未达标，我们将按照合同约定进行赔偿。""",
        "disclaimer": """### 免责声明 (Disclaimer)

OriginGuard 是一家技术提供商，而非律师事务所。
我们提供的“自动律师函”仅供参考，不构成法律建议。"""
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
# 3. 动态 CSS (V4.1: 星尘回归 + 真实 Logo + 清晰字体)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 1. 背景动画：深海渐变 + 粒子下落 (雪花特效回归) */
    @keyframes move-background {
        from {transform: translate3d(0px, 0px, 0px);}
        to {transform: translate3d(0px, 1000px, 0px);}
    }
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
        color: #ffffff !important; 
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
    }
    
    /* 星尘粒子层 (z-index 设为 0，防止遮挡交互) */
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
        opacity: 0.35; 
        z-index: 0;
        pointer-events: none;
    }

    /* 2. 法律条款阅读框 (解决看不清问题) */
    .legal-content-box {
        background-color: #000000 !important; /* 纯黑底 */
        border: 1px solid #333;
        padding: 30px;
        border-radius: 12px;
        color: #ffffff !important; /* 纯白字 */
        font-size: 16px;
        line-height: 1.6;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
        position: relative;
        z-index: 2;
    }
    .legal-content-box h3 {
        color: #FCD535 !important; /* 标题用币安黄，醒目 */
        margin-top: 0;
    }
    .legal-content-box strong {
        color: #fff !important;
    }

    /* 3. 按钮样式重构 */
    
    /* Primary (Binance Yellow) */
    button[kind="primary"] {
        background: linear-gradient(90deg, #FCD535 0%, #FBC100 100%) !important;
        color: #1e2329 !important;
        border: none !important;
        font-weight: 800 !important;
    }

    /* Secondary (Glass) */
    div.stButton > button:not([kind="primary"]) {
        background-color: rgba(15, 23, 42, 0.6) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(148, 163, 184, 0.3) !important;
        border-radius: 8px;
        transition: all 0.3s;
        position: relative;
        z-index: 1;
    }
    div.stButton > button:not([kind="primary"]):hover {
        border-color: #FCD535 !important;
        color: #ffffff !important;
        background-color: rgba(15, 23, 42, 1) !important;
    }

    /* 4. 真实 Logo 按钮样式 (Social Icons) */
    .social-icon-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        margin-right: 10px;
        transition: all 0.3s;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .social-icon-btn:hover {
        background: #FCD535;
        border-color: #FCD535;
        transform: translateY(-3px);
    }
    .social-icon-btn svg {
        fill: white;
        width: 20px;
        height: 20px;
    }
    .social-icon-btn:hover svg {
        fill: black; /* 悬停时图标变黑 */
    }

    /* 5. Cookie Banner */
    .cookie-banner {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #1e2329;
        border-top: 1px solid #FCD535;
        padding: 15px 20px;
        z-index: 9999;
        box-shadow: 0 -10px 40px rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
    }

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
        "cookie_msg": "We use cookies to ensure asset security. By continuing, you agree to our Terms.",
        "cookie_btn": "Accept & Continue",
        "f_comm": "COMMUNITY",
        "f_legal": "LEGAL",
        "f_prod": "PRODUCTS",
        "f_serv": "SUPPORT",
        "login_title": "Sign In",
        "login_email": "Access Code",
        "login_btn": "Verify & Enter",
        "login_error": "⚠️ Invalid Code.",
    },
    "中文": {
        "slogan": "捍卫你的数字资产",
        "sub_slogan": "Web3 版权保护全球标准 | 自动确权与维权",
        "btn_launch": "🚀 启动控制台",
        "cookie_msg": "我们使用 Cookie 保障您的资产安全。继续使用即表示您同意我们的条款。",
        "cookie_btn": "接受并继续",
        "f_comm": "官方社区",
        "f_legal": "法律条款",
        "f_prod": "产品中心",
        "f_serv": "客户支持",
        "login_title": "登录",
        "login_email": "访问密钥",
        "login_btn": "验证并进入",
        "login_error": "⚠️ 密钥错误。",
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး | ကမ္ဘာ့အဆင့်မီ နည်းပညာ",
        "btn_launch": "🚀 စနစ်စတင်မည်",
        "cookie_msg": "သင့်လုံခြုံရေးအတွက် Cookie အသုံးပြုပါသည်။",
        "cookie_btn": "လက်ခံမည်",
        "f_comm": "ကွန်မြူနတီ",
        "f_legal": "ဥပဒေ",
        "f_prod": "ထုတ်ကုန်များ",
        "f_serv": "ဝန်ဆောင်မှု",
        "login_title": "အကောင့်ဝင်ပါ",
        "login_email": "စကားဝှက်",
        "login_btn": "ဝင်မည်",
        "login_error": "⚠️ မှားယွင်းနေသည်။",
    }
}

# ==========================================
# 5. 逻辑与渲染 (Logic & Rendering)
# ==========================================
lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "中文", "Myanmar"], index=1)
T = TRANS[lang_choice]
L_TEXT = LEGAL_CONSTANTS[lang_choice]

if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'auth' not in st.session_state: st.session_state.auth = False
if 'cookies_accepted
