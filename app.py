# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import random
import time
import requests # 新增：用于请求真实区块链数据

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
# 3. 动态 CSS (V4.6: 极速视觉引擎)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 1. 背景动画：风暴级星尘 (Hyper Stardust) */
    @keyframes move-background {
        from {transform: translate3d(0px, -200px, 0px);}
        to {transform: translate3d(0px, 800px, 0px);}
    }
    @keyframes nebula-pulse {
        0% { background-size: 100% 100%; }
        50% { background-size: 110% 110%; }
        100% { background-size: 100% 100%; }
    }
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1e1b4b 0%, #020617 90%);
        color: #ffffff !important; 
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
        animation: nebula-pulse 10s ease-in-out infinite; /* 背景也在缓慢呼吸 */
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: -1000px;
        left: 0;
        width: 100%;
        height: 300%;
        background-image: 
            radial-gradient(3px 3px at 100px 50px, #22d3ee, transparent),
            radial-gradient(4px 4px at 300px 450px, #818cf8, transparent),
            radial-gradient(2px 2px at 600px 100px, #ffffff, transparent),
            radial-gradient(3px 3px at 800px 300px, #FCD535, transparent); /* 增加金色粒子 */
        background-size: 800px 800px;
        animation: move-background 15s linear infinite; /* 速度提升 */
        opacity: 0.7; /* 亮度提升 */
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
        box-shadow: 0 5px 20px rgba(0,0,0,0.8);
        margin-bottom: 20px;
        position: relative;
        z-index: 2;
    }
    .legal-box h3 { color: #FCD535 !important; margin-top: 0; font-size: 20px; }

    /* 3. 按钮脉冲特效 (Violent Pulse) */
    @keyframes pulse-intense {
        0% { box-shadow: 0 0 0 0 rgba(252, 213, 53, 0.7); transform: scale(1); }
        50% { box-shadow: 0 0 20px 10px rgba(252, 213, 53, 0); transform: scale(1.03); }
        100% { box-shadow: 0 0 0 0 rgba(252, 213, 53, 0); transform: scale(1); }
    }
    /* Primary (Binance Yellow) */
    button[kind="primary"] {
        background: linear-gradient(90deg, #FCD535 0%, #FBC100 100%) !important;
        color: #1e2329 !important;
        border: none !important;
        font-weight: 800 !important;
        transition: all 0.2s;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        position: relative;
        z-index: 5;
    }
    button[kind="primary"]:hover {
        animation: pulse-intense 1s infinite; /* 剧烈脉冲 */
    }
    /* Secondary (Glass) */
    div.stButton > button:not([kind="primary"]) {
        background-color: rgba(15, 23, 42, 0.8) !important; /* 加深背景防雪盲 */
        color: #e2e8f0 !important;
        border: 1px solid rgba(148, 163, 184, 0.4) !important;
        border-radius: 6px;
        backdrop-filter: blur(5px);
    }
    div.stButton > button:not([kind="primary"]):hover {
        border-color: #FCD535 !important;
        color: #fff !important;
        background-color: rgba(15, 23, 42, 1) !important;
        box-shadow: 0 0 15px rgba(252, 213, 53, 0.3);
    }

    /* 4. Auth Card (首页悬浮登录框) */
    .auth-card {
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255,255,255,0.15);
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.8);
        margin-top: 20px;
        position: relative;
        z-index: 5;
    }

    /* 5. 真实 Logo 按钮 hack */
    .real-logo-btn {
        display: flex; align-items: center; justify-content: center; gap: 10px;
        width: 100%; padding: 10px; border-radius: 8px; font-weight: 600;
        cursor: pointer; transition: transform 0.2s; margin-bottom: 10px; text-decoration: none !important;
    }
    .real-logo-btn:hover { transform: scale(1.02); filter: brightness(1.1); }
    .btn-google { background: white; color: #3c4043; border: 1px solid #dadce0; }
    .btn-apple { background: black; color: white; border: 1px solid #333; }
    .btn-github { background: #24292e; color: white; border: 1px solid #333; }

    /* 6. Footer Title */
    .footer-title { color: #FCD535; font-weight: 700; font-size: 14px; margin-bottom: 10px; text-transform: uppercase; text-shadow: 0 0 10px rgba(252, 213, 53, 0.3); }
    
    /* 7. Breathing Text (Enhanced) */
    @keyframes breathe-deep {
        0% { opacity: 0.9; text-shadow: 0 0 10px rgba(34, 211, 238, 0.2); transform: translateY(0); }
        50% { opacity: 1; text-shadow: 0 0 30px rgba(34, 211, 238, 0.8); transform: translateY(-3px); }
        100% { opacity: 0.9; text-shadow: 0 0 10px rgba(34, 211, 238, 0.2); transform: translateY(0); }
    }
    .breathing-text { animation: breathe-deep 3s ease-in-out infinite; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. 语言字典
# ==========================================
TRANS = {
    "English": {
        "slogan": "Protect Your Original Videos & Photos",
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
        "slogan": "保护你的原创作品视频照片等",
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
# 5. 逻辑控制 & 真实区块链连接
# ==========================================
lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "中文", "Myanmar"], index=1)
T = TRANS[lang_choice]
L_TEXT = LEGAL_CONSTANTS[lang_choice]

if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'auth' not in st.session_state: st.session_state.auth = False
if 'cookies_accepted' not in st.session_state: st.session_state.cookies_accepted = False

def set_page(name): st.session_state.page = name
def handle_dev(): st.toast(T['dev_msg'], icon="🏗️")

# --- 🚀 功能：获取真实 Solana 区块高度 ---
@st.cache_data(ttl=10) # 缓存10秒，防止刷新太快被 API 封禁
def get_real_solana_block():
    try:
        # 使用 Solana 公共 RPC 节点
        url = "https://api.mainnet-beta.solana.com"
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getSlot"
        }
        response = requests.post(url, json=payload, headers=headers, timeout=2)
        if response.status_code == 200:
            block = response.json().get("result")
            return f"{block:,}" # 添加千位分隔符
    except:
        pass
    # 如果获取失败（超时或被限流），返回一个带标记的估算值，保证界面不崩
    return f"{random.randint(246000000, 247000000):,} (Est)"

# --- SVG 图标库 (Real Logos) ---
SVG_DISCORD = """<svg viewBox="0 0 127.14 96.36" width="20"><path fill="white" d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.11,77.11,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.89,11.1A105.89,105.89,0,0,0,126.6,80.22c2.36-24.44-5.42-48.18-18.9-72.15ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S54,46,53.89,53,48.84,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.25,60,73.25,53s5-12.74,11.44-12.74S96.23,46,96.12,53,91.08,65.69,84.69,65.69Z"/></svg>"""
SVG_TWITTER = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>"""
SVG_TELEGRAM = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>"""
SVG_FACEBOOK = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036c-2.148 0-2.971.956-2.971 3.059v.913h3.945l-.526 3.667h-3.419v7.98h-4.844z"/></svg>"""
SVG_GITHUB_FOOTER = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>"""
SVG_GOOGLE = """<svg width="18" height="18" viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.63-.06-1.25-.17-1.84H9v3.49h4.84c-.21 1.12-.85 2.07-1.8 2.71v2.24h2.91c1.7-1.56 2.68-3.87 2.68-6.6z"/><path fill="#34A853" d="M9 18c2.43 0 4.47-.8 5.96-2.18l-2.91-2.24c-.81.54-1.84.86-3.05.86-2.34 0-4.32-1.58-5.03-3.71H.99v2.33C2.47 15.93 5.48 18 9 18z"/><path fill="#FBBC05" d="M3.97 10.73c-.18-.54-.28-1.12-.28-1.73s.1-1.19.28-1.73V4.94H.99c-.62 1.24-.98 2.63-.98 4.06s.36 2.82.98 4.06l2.98-2.33z"/><path fill="#EA4335" d="M9 3.58c1.32 0 2.5.45 3.44 1.35l2.58-2.59C13.47.89 11.43 0 9 0 5.48 0 2.47 2.07.99 4.94l2.98 2.33c.71-2.13 2.69-3.71 5.03-3.71z"/></svg>"""
SVG_APPLE = """<svg width="18" height="18" viewBox="0 0 384 512" style="fill:white"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 52.3-11.4 69.5-34.3z"/></svg>"""
SVG_GITHUB = """<svg width="18" height="18" viewBox="0 0 1024 1024" style="fill:white"><path d="M511.6 76.3C264.3 76.2 64 276.4 64 523.5 64 718.9 189.3 885 363.8 946c23.5 5.9 19.9-10.8 19.9-22.2v-77.5c-135.7 15.9-141.2-73.9-150.3-88.9C215 726 171.5 718 184.5 703c30.9-15.9 62.4 4 98.9 57.9 26.4 39.1 77.9 32.5 104 26 5.7-23.5 17.9-44.5 34.7-60.8-140.6-25.2-199.2-111-199.2-213 0-49.5 16.3-95 48.3-131.7-20.4-60.5 1.9-112.3 4.9-120 58.1-5.2 118.5 41.6 123.2 45.3 33-8.9 70.7-13.6 112.9-13.6 42.4 0 80.2 4.9 113.5 13.9 11.3-8.6 67.3-48.8 121.3-43.9 2.9 7.7 24.7 58.3 5.5 118 32.4 36.8 48.9 82.7 48.9 132.3 0 102.2-59 188.1-200 212.9a127.5 127.5 0 0 1 38.1 91v112.5c.8 9 0 17.9 15 17.9 177.1-59.7 304.6-227 304.6-424.1 0-247.2-200.4-447.3-447.5-447.3z"/></svg>"""

# --- 组件：大页脚 ---
def render_fat_footer():
    st.write("")
    st.markdown("---")
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f"<div class='footer-title'>{T['f_comm']}</div>", unsafe_allow_html=True)
        # 5大社区矩阵
        st.markdown(f"""
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <button onclick="alert('Join Discord')" style="background:none; border:none; cursor:pointer;" title="Discord">{SVG_DISCORD}</button>
            <button onclick="alert('Follow X')" style="background:none; border:none; cursor:pointer;" title="Twitter/X">{SVG_TWITTER}</button>
            <button onclick="alert('Join TG')" style="background:none; border:none; cursor:pointer;" title="Telegram">{SVG_TELEGRAM}</button>
            <button onclick="alert('Join FB')" style="background:none; border:none; cursor:pointer;" title="Facebook">{SVG_FACEBOOK}</button>
            <button onclick="alert('Star GitHub')" style="background:none; border:none; cursor:pointer;" title="GitHub">{SVG_GITHUB_FOOTER}</button>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"<div class='footer-title'>{T['f_legal']}</div>", unsafe_allow_html=True)
        if st.button("Terms (ToS)", key="ft1", use_container_width=True): 
            st.session_state.view_legal = "tos"; set_page('legal_view'); st.rerun()
        if st.button("No Refunds", key="ft2", use_container_width=True):
            st.session_state.view_legal = "refund"; set_page('legal_view'); st.rerun()
        if st.button("Privacy", key="ft3", use_container_width=True):
            st.session_state.view_legal = "privacy"; set_page('legal_view'); st.rerun()

    with c3:
        st.markdown(f"<div class='footer-title'>{T['f_prod']}</div>", unsafe_allow_html=True)
        # Solana Scan: 现在是真实的外部链接
        st.link_button("🔗 Solana Scan", "https://solscan.io/", use_container_width=True)
        if st.button("API Docs", use_container_width=True): handle_dev()

    with c4:
        st.markdown(f"<div class='footer-title'>{T['f_serv']}</div>", unsafe_allow_html=True)
        if st.button("SLA Guarantee", use_container_width=True):
             st.session_state.view_legal = "sla"; set_page('legal_view'); st.rerun()
        st.info("✉️ support@originguard.com")

    st.markdown("<div style='text-align:center; color:#64748b; font-size:12px; margin-top:30px;'>© 2026 OriginGuard Solutions Inc.</div>", unsafe_allow_html=True)
    
    # Cookie Banner
    if not st.session_state.cookies_accepted:
        st.markdown(f"""
        <div class="cookie-banner">
            <span style="color:#fff; font-size:16px; margin-right:20px;">🍪 {T['cookie_msg']}</span>
        </div>
        """, unsafe_allow_html=True)
        c_k1, c_k2, c_k3 = st.columns([1,1,1])
        with c_k2:
             if st.button(T['cookie_btn'], type="primary", use_container_width=True, key="cookie_accept"):
                st.session_state.cookies_accepted = True
                st.rerun()

# --- 1. 官网首页 (Landing) + 身份网关 (Direct) ---
if st.session_state.page == 'landing':
    st.write("")
    
    col_text, col_auth = st.columns([1.2, 0.8])
    
    with col_text:
        st.write("")
        st.write("")
        st.markdown(f"""
        <div style="padding-right: 20px;">
            <h1 class="breathing-text" style="font-size: 56px; margin-bottom: 20px;">{T['slogan']}</h1>
            <p class="breathing-text" style="font-size: 22px; color: #f8fafc; font-weight:600; line-height:1.5;">{T['sub_slogan']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 真实区块高度获取
        real_block = get_real_solana_block()
        st.markdown(f"<div style='margin-top: 40px; color:#FCD535; font-weight:bold;'>🟢 Solana Mainnet Slot: #{real_block}</div>", unsafe_allow_html=True)

    with col_auth:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        tab_login, tab_reg = st.tabs([T['tab_login'], T['tab_reg']])
        
        # 登录逻辑
        with tab_login:
            pwd = st.text_input(T['lbl_email'], type="password", key="login_pwd", placeholder="origin2026")
            if st.button(T['btn_login'], type="primary", use_container_width=True):
                if pwd == "origin2026":
                    with st.spinner("Verifying..."): time.sleep(1)
                    st.session_state.auth = True; set_page('dashboard'); st.rerun()
                else:
                    st.error(T['err_login'])
            
            st.markdown(f"<div style='text-align:center; color:#94a3b8; font-size:12px; margin:15px 0;'>{T['or_connect']}</div>", unsafe_allow_html=True)
            st.markdown(f"""
            <a href="#" class="real-logo-btn btn-google">{SVG_GOOGLE} Continue with Google</a>
            <a href="#" class="real-logo-btn btn-apple">{SVG_APPLE} Continue with Apple</a>
            <a href="#" class="real-logo-btn btn-github">{SVG_GITHUB} Continue with GitHub</a>
            """, unsafe_allow_html=True)

        # 注册逻辑
        with tab_reg:
            st.text_input("Email", placeholder="user@example.com")
            st.text_input(T['lbl_pwd'], type="password", key="reg_pwd")
            st.text_input(T['lbl_cpwd'], type="password", key="reg_cpwd")
            if st.button(T['btn_reg'], type="primary", use_container_width=True):
                with st.spinner("Creating Identity..."): time.sleep(2)
                st.success(T['suc_reg'])
                time.sleep(1); st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    render_fat_footer()

# --- 2. 控制台 (Dashboard) ---
elif st.session_state.page == 'dashboard':
    if not st.session_state.auth: set_page('landing'); st.rerun()
    
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
        if st.button("Encrypt", type="primary"): handle_dev()
    with t2:
        st.text_input("Infringing URL")
        if st.button("Send Notice", type="primary"): handle_dev()

    render_fat_footer()

# --- 3. 法律详情页 ---
elif st.session_state.page == 'legal_view':
    st.button("⬅️ Back", on_click=lambda: set_page('landing'))
    st.markdown("---")
    
    key = st.session_state.get('view_legal', 'tos')
    content = L_TEXT.get(key, "Error")
    
    st.markdown(f"""
    <div class="legal-box">
        {content}
    </div>
    """, unsafe_allow_html=True)
    
    render_fat_footer()
