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
        "tos": """### 1. ORIGINALITY MANDATE
**You certify that all uploaded content is your ORIGINAL creation.**
OriginGuard is a tool for creators, not thieves.

### 2. LIABILITY DISCLAIMER
**You bear full legal consequences for non-original content.**
If you upload stolen assets, you indemnify OriginGuard against all claims. We will cooperate with law enforcement to provide your IP and hash logs.

### 3. Service Limits
We provide immutable evidence. We do not guarantee court rulings.""",
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
        "tos": """### 1. 原创性强制承诺
**您必须保证上传的所有内容均为您的原创作品。**
OriginGuard 是为创作者服务的平台，绝不庇护盗窃者。

### 2. 侵权后果自负
**如上传非原创内容，您将承担全部法律后果。**
若发生版权纠纷，您同意赔偿 OriginGuard 的一切损失。我们将配合执法机构提供您的 IP 和哈希日志。

### 3. 服务限制
我们提供不可篡改的证据，但不保证特定法庭的判决结果。""",
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
        "tos": """### မူရင်းပိုင်ရှင်ဖြစ်ရမည်
သင်တင်သော အရာများသည် သင်၏ ကိုယ်ပိုင်ဖန်တီးမှု ဖြစ်ရမည်။

### ဥပဒေအရ တာဝန်ယူမှု
သူတစ်ပါး၏ လက်ရာများကို ခိုးယူအသုံးပြုပါက ဥပဒေအရ အရေးယူခြင်းကို ခံရမည်။""",
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
# 3. 动态 CSS (V4.4: 脉冲 + 真实 Logo + 首页布局)
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

    /* 2. 法律条款专用容器 */
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
    .legal-box h3 { color: #FCD535 !important; margin-top: 0; font-size: 20px; }

    /* 3. 按钮脉冲特效 & 样式 */
    @keyframes pulse-yellow {
        0% { box-shadow: 0 0 0 0 rgba(252, 213, 53, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(252, 213, 53, 0); }
        100% { box-shadow: 0 0 0 0 rgba(252, 213, 53, 0); }
    }
    /* Primary (Binance Yellow) */
    button[kind="primary"] {
        background: linear-gradient(90deg, #FCD535 0%, #FBC100 100%) !important;
        color: #1e2329 !important;
        border: none !important;
        font-weight: 800 !important;
        transition: all 0.3s;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    button[kind="primary"]:hover {
        transform: scale(1.02);
        animation: pulse-yellow 1.5s infinite;
    }
    /* Secondary (Glass) */
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

    /* 4. Auth Card (首页悬浮登录框) */
    .auth-card {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6);
        margin-top: 20px;
    }

    /* 5. 真实 Logo 按钮 hack */
    .real-logo-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        width: 100%;
        padding: 10px;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.2s;
        margin-bottom: 10px;
        text-decoration: none !important;
    }
    .real-logo-btn:hover { transform: scale(1.02); }
    .btn-google { background: white; color: #3c4043; border: 1px solid #dadce0; }
    .btn-apple { background: black; color: white; border: 1px solid #333; }
    .btn-github { background: #24292e; color: white; border: 1px solid #333; }

    /* 6. Cookie 弹窗 */
    .cookie-banner {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: #1e2329; border-top: 2px solid #FCD535;
        padding: 20px; z-index: 9999;
        display: flex; justify-content: center; align-items: center;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
    }

    /* 7. Footer Title */
    .footer-title { color: #FCD535; font-weight: 700; font-size: 14px; margin-bottom: 10px; text-transform: uppercase; }
    
    /* 8. Breathing Text */
    @keyframes breathe {
        0% { opacity: 0.9; text-shadow: 0 0 5px rgba(255,255,255,0.1); }
        50% { opacity: 1; text-shadow: 0 0 25px rgba(34, 211, 238, 0.6); }
        100% { opacity: 0.9; text-shadow: 0 0 5px rgba(255,255,255,0.1); }
    }
    .breathing-text { animation: breathe 3s ease-in-out infinite; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. 语言字典
# ==========================================
TRANS = {
    "English": {
        "slogan": "Protect What You Create.",
        "sub_slogan": "The Global Standard for Web3 Copyright Defense.",
        "cookie_msg": "We use strictly necessary cookies to maintain your cryptographic session and ensure asset security. By using OriginGuard, you agree to our Terms.",
        "cookie_btn": "Accept & Secure Session",
        "f_comm": "Community", "f_legal": "Legal", "f_prod": "Products", "f_serv": "Support",
        "titles": ["Terms (Originality)", "No Refund Policy", "Privacy", "SLA", "Disclaimer"],
        "dev_msg": "🚧 Feature currently under active development.",
        # Auth
        "tab_login": "Sign In", "tab_reg": "Register",
        "lbl_email": "Email / Access Code", "lbl_pwd": "Password", "lbl_cpwd": "Confirm Password",
        "btn_login": "Sign In", "btn_reg": "Start Your Originality Protection Journey",
        "err_login": "Invalid Credentials. Try 'origin2026'.",
        "suc_reg": "Account created! Please log in.",
        "or_connect": "OR CONNECT WITH"
    },
    "中文": {
        "slogan": "捍卫你的数字资产",
        "sub_slogan": "Web3 版权保护全球标准 | 自动确权与维权",
        "cookie_msg": "OriginGuard 使用必要的 Cookie 来维护您的加密会话并确保资产安全。继续使用即表示您同意我们的服务条款。",
        "cookie_btn": "接受并保护会话",
        "f_comm": "官方社区", "f_legal": "法律条款", "f_prod": "产品中心", "f_serv": "客户支持",
        "titles": ["原创性条款", "无退款政策", "隐私政策", "SLA承诺", "免责声明"],
        "dev_msg": "🚧 该功能正在紧急开发中，敬请期待。",
        # Auth
        "tab_login": "登录", "tab_reg": "注册",
        "lbl_email": "邮箱 / 访问密钥", "lbl_pwd": "密码", "lbl_cpwd": "确认密码",
        "btn_login": "立即登录", "btn_reg": "开启您的原创保护之旅",
        "err_login": "凭证错误。演示密码为 'origin2026'。",
        "suc_reg": "账户创建成功！请登录。",
        "or_connect": "或通过以下方式连接"
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး",
        "cookie_msg": "လုံခြုံရေးအတွက် Cookie အသုံးပြုပါသည်။",
        "cookie_btn": "လက်ခံမည်",
        "f_comm": "ကွန်မြူနတီ", "f_legal": "ဥပဒေ", "f_prod": "ထုတ်ကုန်များ", "f_serv": "ဝန်ဆောင်မှု",
        "titles": ["စည်းမျဉ်းများ", "ငွေပြန်မအမ်းပါ", "လုံခြုံရေး", "SLA", "ငြင်းဆိုချက်"],
        "dev_msg": "🚧 တည်ဆောက်ဆဲ",
        # Auth
        "tab_login": "အကောင့်ဝင်ရန်", "tab_reg": "စာရင်းသွင်းရန်",
        "lbl_email": "အီးမေးလ်", "lbl_pwd": "စကားဝှက်", "lbl_cpwd": "အတည်ပြုပါ",
        "btn_login": "ဝင်မည်", "btn_reg": "ကာကွယ်မှု စတင်မည်",
        "err_login": "မှားယွင်းနေသည်။",
        "suc_reg": "အောင်မြင်ပါသည်။",
        "or_connect": "ချိတ်ဆက်ပါ"
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
def handle_dev(): st.toast(T['dev_msg'], icon="🏗️")

# --- SVG 图标库 (Real Logos) ---
# Footer Icons
SVG_DISCORD = """<svg viewBox="0 0 127.14 96.36" width="20"><path fill="white" d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.11,77.11,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.89,11.1A105.89,105.89,0,0,0,126.6,80.22c2.36-24.44-5.42-48.18-18.9-72.15ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S54,46,53.89,53,48.84,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.25,60,73.25,53s5-12.74,11.44-12.74S96.23,46,96.12,53,91.08,65.69,84.69,65.69Z"/></svg>"""
SVG_TWITTER = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8
