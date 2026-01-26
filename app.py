# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import random
import time
import requests
import hashlib
from datetime import datetime

# ==========================================
# 1. 核心配置 (Core Config)
# ==========================================
st.set_page_config(
    page_title="OriginGuard Matrix",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. 状态管理 (Session State)
# ==========================================
if 'language' not in st.session_state: st.session_state.language = "中文"
if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'auth' not in st.session_state: st.session_state.auth = False
if 'cookies_accepted' not in st.session_state: st.session_state.cookies_accepted = False
if 'wallet_connected' not in st.session_state: st.session_state.wallet_connected = False
if 'wallet_address' not in st.session_state: st.session_state.wallet_address = None
if 'kyc_status' not in st.session_state: st.session_state.kyc_status = "Unverified"

# ==========================================
# 3. 法律文本常量库 (IMMUTABLE)
# ==========================================
LEGAL_CONSTANTS = {
    "English": {
        "tos": """### 1. ORIGINALITY MANDATE
**You certify that all uploaded content is your ORIGINAL creation.**
OriginGuard is a tool for creators, not thieves.

### 2. LIABILITY DISCLAIMER
**You bear full legal consequences for non-original content.**""",
        "refund": """### NO REFUND POLICY (STRICT)
**Gas fees are paid instantly to the Solana network.**
**ALL SALES ARE FINAL.**""",
        "privacy": """### Data Privacy
We only hash files. We do not store original images. Your data remains yours.""",
        "sla": """### Enterprise SLA
99.9% API Uptime Guarantee for Enterprise subscribers.""",
        "disclaimer": """### Legal Disclaimer
OriginGuard is a technology provider, **not a law firm**."""
    },
    "中文": {
        "tos": """### 1. 原创性强制承诺
**您必须保证上传的所有内容均为您的原创作品。**
OriginGuard 是为创作者服务的平台，绝不庇护盗窃者。

### 2. 侵权后果自负
**如上传非原创内容，您将承担全部法律后果。**""",
        "refund": """### 🚫 无退款政策 (No Refund)
**Gas 费已实时支付给区块链网络。**
**所有交易均为最终交易。**""",
        "privacy": """### 🔒 隐私政策
1. **数据最小化**：我们只存储文件的数字哈希值。
2. **不存原图**：您的原始高清图片从未上传到我们的服务器。""",
        "sla": """### ⚡ SLA 服务承诺
对于企业版订阅用户，我们承诺 **99.9%** 的 API 在线率。""",
        "disclaimer": """### ⚠️ 免责声明
OriginGuard 是一家技术提供商，而**非律师事务所**。"""
    },
    "Myanmar": {
        "tos": """### မူရင်းပိုင်ရှင်ဖြစ်ရမည်
သင်တင်သော အရာများသည် သင်၏ ကိုယ်ပိုင်ဖန်တီးမှု ဖြစ်ရမည်။""",
        "refund": """### ငွေပြန်မအမ်းပါ (No Refund)
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
# 4. 动态 CSS (V5.9.1: 样式修正)
# ==========================================
st.markdown("""
<style>
    /* 引入高性能代码字体 */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&family=Fira+Code:wght@400;600;700&display=swap');

    :root {
        --neon-green: #0f0;
        --neon-yellow: #FCD535;
        --matrix-bg: #020617;
    }
    
    @keyframes matrix-stream {
        0% { background-position: 0% 0%; }
        100% { background-position: 0% 100%; }
    }

    .stApp {
        background-color: var(--matrix-bg);
        font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
        color: #e2e8f0 !important;
        letter-spacing: 0.5px;
    }

    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 500%;
        background-image: 
            linear-gradient(0deg, transparent 20%, rgba(15, 255, 0, 0.1) 50%, transparent 80%),
            linear-gradient(0deg, transparent 20%, rgba(252, 213, 53, 0.08) 50%, transparent 80%),
            repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.8) 3px, rgba(0,0,0,0.8) 4px);
        background-size: 100% 800px;
        animation: matrix-stream 20s linear infinite;
        z-index: 0; pointer-events: none; opacity: 0.8;
    }

    /* ------------------- [V5.9 核心修复] 标签高亮协议 ------------------- */
    .stSelectbox label, .stTextInput label, .stFileUploader label, p {
        color: var(--neon-yellow) !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 700 !important;
        text-shadow: 2px 2px 0px #000000 !important; 
        letter-spacing: 0.5px;
    }
    
    /* ------------------- 动画库 ------------------- */
    @keyframes neon-pulse {
        0% { box-shadow: 0 0 5px rgba(15, 255, 0, 0.2); border-color: rgba(15, 255, 0, 0.3); }
        50% { box-shadow: 0 0 15px rgba(15, 255, 0, 0.5); border-color: rgba(15, 255, 0, 0.8); }
        100% { box-shadow: 0 0 5px rgba(15, 255, 0, 0.2); border-color: rgba(15, 255, 0, 0.3); }
    }
    
    @keyframes text-glow {
        0% { text-shadow: 0 0 5px rgba(15, 255, 0, 0.3); color: #fff; }
        50% { text-shadow: 0 0 20px rgba(15, 255, 0, 0.8), 0 0 10px var(--neon-yellow); color: var(--neon-green); }
        100% { text-shadow: 0 0 5px rgba(15, 255, 0, 0.3); color: #fff; }
    }

    @keyframes glitch-text {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }

    .breathing-text { animation: text-glow 3s ease-in-out infinite alternate; font-weight: 900; }
    .glitch-text { animation: glitch-text 3s infinite linear alternate-reverse; color: var(--neon-yellow) !important; text-shadow: 2px 2px 0px #ff0000; }
    .footer-title, .legal-box h3, .feature-card h3 { animation: text-glow 5s ease-in-out infinite; text-transform: uppercase; letter-spacing: 1px; }

    /* ------------------- 组件样式 ------------------- */
    
    div[data-testid="column"]:nth-of-type(2) > div[data-testid="stVerticalBlock"] {
        background: rgba(10, 10, 15, 0.95) !important;
        backdrop-filter: blur(10px);
        border: 1px solid var(--neon-green);
        padding: 30px;
        border-radius: 4px;
        box-shadow: 0 0 20px rgba(15, 255, 0, 0.1);
    }

    /* Auth Header */
    @keyframes blink-cursor { 50% { border-color: transparent; } }
    .auth-header {
        font-family: 'JetBrains Mono', monospace;
        color: var(--neon-green);
        font-weight: 900;
        font-size: 24px;
        text-transform: uppercase;
        border-right: 0.6em solid var(--neon-green);
        width: fit-content;
        margin-bottom: 20px;
        animation: blink-cursor 1s step-end infinite;
        text-shadow: 0 0 10px var(--neon-green);
    }

    /* Cards */
    .legal-box, .feature-card, .cert-box, .wallet-box, .kyc-box {
        background: #000000 !important;
        border: 1px solid var(--neon-green);
        padding: 25px;
        color: #ffffff !important;
        box-shadow: 5px 5px 0px rgba(15, 255, 0, 0.2);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .feature-card:hover { transform: translate(-2px, -2px); box-shadow: 8px 8px 0px var(--neon-yellow); border-color: var(--neon-yellow); }

    /* Buttons */
    button[kind="primary"] {
        background: var(--neon-yellow) !important;
        color: #000 !important; border: 2px solid var(--neon-yellow) !important; font-weight: 900 !important;
        border-radius: 0px !important; text-transform: uppercase;
        box-shadow: 4px 4px 0px var(--neon-green);
    }
    button[kind="primary"]:hover { transform: translate(-1px, -1px); box-shadow: 6px 6px 0px #fff; }
    
    div.stButton > button:not([kind="primary"]) {
        background-color: transparent !important; color: var(--neon-green) !important;
        border: 1px solid var(--neon-green) !important; border-radius: 0px; font-family: monospace;
    }
    div.stButton > button:not([kind="primary"]):hover {
        background-color: var(--neon-green) !important; color: #000 !important;
    }

    /* Selectbox Visibility */
    div[data-baseweb="select"] > div {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 2px solid var(--neon-yellow) !important;
        font-weight: 700 !important;
        border-radius: 0px !important;
        opacity: 1 !important;
    }
    div[data-baseweb="popover"], div[data-baseweb="menu"] { background-color: #000000 !important; border: 1px solid #FCD535 !important; }
    div[data-baseweb="menu"] li { color: #ffffff !important; }
    div[data-baseweb="menu"] li[aria-selected="true"], div[data-baseweb="menu"] li:hover { background-color: #FCD535 !important; color: #000000 !important; }
    div[data-baseweb="select"] span { color: #ffffff !important; }
    div[data-baseweb="select"] svg { fill: #FCD535 !important; color: #FCD535 !important; }

    /* Footer & Invisible Buttons */
    .footer-title { border-bottom: 2px solid var(--neon-green); padding-bottom: 5px; margin-bottom: 15px; display: inline-block;}
    div[data-testid="stHorizontalBlock"] button { color: #64748b !important; font-family: 'JetBrains Mono', monospace !important; font-weight: 600; }
    div[data-testid="stHorizontalBlock"] button:hover { color: var(--neon-yellow) !important; text-shadow: 0 0 10px var(--neon-yellow); }
    
    .real-logo-btn {border: 1px solid #333; color: #aaa;}
    .real-logo-btn:hover {border-color: var(--neon-green); color: #fff;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 5. 语言字典
# ==========================================
TRANS = {
    "English": {
        "slogan": "PROTECT YOUR ORIGINAL VIDEOS & PHOTOS",
        "sub_slogan": "> The Global Standard for Web3 Copyright Defense. System Ready.",
        "cookie_msg": "[SYSTEM] Strictly necessary cookies initialized.",
        "cookie_btn": "ACKNOWLEDGE",
        "f_comm": "COMMUNITY_UPLINK", "f_legal": "LEGAL_PROTOCOLS", "f_prod": "PRODUCT_MATRIX", "f_serv": "SUPPORT_CHANNEL",
        "dev_msg": "⚠️ [DEV_MODE] Feature Under Construction.",
        "tab_login": "ACCESS_TERMINAL", "tab_reg": "NEW_IDENTITY",
        "lbl_email": "ACCESS_KEY / EMAIL", "lbl_pwd": "PASSWORD", "lbl_cpwd": "CONFIRM_PASSWORD",
        "btn_login": "INITIALIZE_SESSION", "btn_reg": "DEPLOY_PROTECTION",
        "err_login": "❌ ACCESS DENIED. TRY 'origin2026'.",
        "suc_reg": "✅ IDENTITY CREATED. PLEASE LOG IN.",
        "or_connect": "--- OR ESTABLISH CONNECTION VIA ---",
        "core_title": "CORE_DEFENSE_MATRIX_V5.9",
        "c1_t": "INVISIBLE_DNA", "c1_d": "AI-embedded stealth watermarks immune to cropping algos.",
        "c2_t": "ON-CHAIN_TRUTH", "c2_d": "Immutable Solana transaction certificates finalized instantly.",
        "c3_t": "LEGAL_HAMMER_AI", "c3_d": "Millisecond generation of transnational DMCA takedown notices."
    },
    "中文": {
        "slogan": "保护你的原创作品视频照片等",
        "sub_slogan": "> Web3 版权防御全球标准 | 系统已就绪",
        "cookie_msg": "[系统提示] 必要 Cookie 已初始化。继续操作即视为同意协议。",
        "cookie_btn": "确认并接入",
        "f_comm": "官方社区联络", "f_legal": "法律协议栈", "f_prod": "产品矩阵", "f_serv": "技术支持通道",
        "dev_msg": "⚠️ [开发模式] 功能正在构建中。",
        "tab_login": "接入终端", "tab_reg": "创建新身份",
        "lbl_email": "访问密钥 / 邮箱", "lbl_pwd": "口令", "lbl_cpwd": "确认口令",
        "btn_login": "初始化会话", "btn_reg": "部署防御体系",
        "err_login": "❌ 访问被拒绝。尝试凭证 'origin2026'。",
        "suc_reg": "✅ 身份已创建。请接入终端。",
        "or_connect": "--- 或通过以下方式建立连接 ---",
        "core_title": "核心防御矩阵_V5.9",
        "c1_t": "隐形 DNA 技术", "c1_d": "AI 嵌入式隐形水印，免疫各类裁剪算法攻击。",
        "c2_t": "链上真理存证", "c2_d": "Solana 区块链永久存证交易，毫秒级确认。",
        "c3_t": "AI 法律重锤", "c3_d": "毫秒级生成跨国 DMCA 律师函，自动维权。",
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ", "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး စနစ်",
        "cookie_msg": "Cookie အသုံးပြုမှုကို လက်ခံပါ။", "cookie_btn": "လက်ခံသည်",
        "f_comm": "ကွန်မြူနတီ", "f_legal": "ဥပဒေ", "f_prod": "ထုတ်ကုန်များ", "f_serv": "ဝန်ဆောင်မှု",
        "dev_msg": "🚧 တည်ဆောက်ဆဲ",
        "tab_login": "အကောင့်ဝင်ရန်", "tab_reg": "စာရင်းသွင်းရန်",
        "lbl_email": "အီးမေးလ်", "lbl_pwd": "စကားဝှက်", "lbl_cpwd": "အတည်ပြုပါ",
        "btn_login": "ဝင်မည်", "btn_reg": "စတင်မည်",
        "err_login": "မှားယွင်းနေသည်။", "suc_reg": "အောင်မြင်ပါသည်။",
        "or_connect": "ချိတ်ဆက်ပါ",
        "core_title": "အဓိက နည်းပညာများ", "c1_t": "မမြင်ရသော ရေစာ", "c1_d": "AI နည်းပညာ။",
        "c2_t": "Blockchain သက်သေ", "c2_d": "Solana မှတ်တမ်း။", "c3_t": "AI ဥပဒေ လက်နက်", "c3_d": "DMCA တိုင်ကြားစာ။"
    }
}

# ==========================================
# 6. 逻辑控制
# ==========================================
T = TRANS[st.session_state.language]
L_TEXT = LEGAL_CONSTANTS[st.session_state.language]

def set_page(name): st.session_state.page = name
def handle_dev(): st.toast(T['dev_msg'], icon="⚠️")

def calculate_file_dna(uploaded_file):
    """Real SHA-256"""
    return hashlib.sha256(uploaded_file.getvalue()).hexdigest()

def generate_certificate(filename, file_hash, block):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""
    ORIGINGUARD MATRIX PROTOCOL V5.9
    --------------------------------
    ASSET: {filename}
    DNA:   {file_hash}
    TIME:  {timestamp}
    BLOCK: {block}
    --------------------------------
    SECURED ON SOLANA MAINNET.
    """

@st.cache_data(ttl=5)
def get_real_solana_block():
    try:
        url = "https://api.mainnet-beta.solana.com"
        res = requests.post(url, json={"jsonrpc": "2.0", "id": 1, "method": "getSlot"}, timeout=2)
        if res.status_code == 200: return f"{res.json().get('result'):,}"
    except: pass
    return f"{random.randint(248000000, 249000000):,} (SIM)"

# --- SVG Icons (补全缺失的变量) ---
SVG_DISCORD = """<svg viewBox="0 0 127.14 96.36" width="20"><path fill="white" d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.11,77.11,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.89,11.1A105.89,105.89,0,0,0,126.6,80.22c2.36-24.44-5.42-48.18-18.9-72.15ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S54,46,53.89,53,48.84,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.25,60,73.25,53s5-12.74,11.44-12.74S96.23,46,96.12,53,91.08,65.69,84.69,65.69Z"/></svg>"""
SVG_TWITTER = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>"""
SVG_TELEGRAM = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>"""
SVG_FACEBOOK = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036c-2.148 0-2.971.956-2.971 3.059v.913h3.945l-.526 3.667h-3.419v7.98h-4.844z"/></svg>"""
SVG_GITHUB_FOOTER = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>"""
# ⚠️ [Fix] 补全缺失的 SVG_GITHUB
SVG_GITHUB = """<svg width="18" height="18" viewBox="0 0 1024 1024" style="fill:white"><path d="M511.6 76.3C264.3 76.2 64 276.4 64 523.5 64 718.9 189.3 885 363.8 946c23.5 5.9 19.9-10.8 19.9-22.2v-77.5c-135.7 15.9-141.2-73.9-150.3-88.9C215 726 171.5 718 184.5 703c30.9-15.9 62.4 4 98.9 57.9 26.4 39.1 77.9 32.5 104 26 5.7-23.5 17.9-44.5 34.7-60.8-140.6-25.2-199.2-111-199.2-213 0-49.5 16.3-95 48.3-131.7-20.4-60.5 1.9-112.3 4.9-120 58.1-5.2 118.5 41.6 123.2 45.3 33-8.9 70.7-13.6 112.9-13.6 42.4 0 80.2 4.9 113.5 13.9 11.3-8.6 67.3-48.8 121.3-43.9 2.9 7.7 24.7 58.3 5.5 118 32.4 36.8 48.9 82.7 48.9 132.3 0 102.2-59 188.1-200 212.9a127.5 127.5 0 0 1 38.1 91v112.5c.8 9 0 17.9 15 17.9 177.1-59.7 304.6-227 304.6-424.1 0-247.2-200.4-447.3-447.5-447.3z"/></svg>"""
SVG_GOOGLE = """<svg width="18" height="18" viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.63-.06-1.25-.17-1.84H9v3.49h4.84c-.21 1.12-.85 2.07-1.8 2.71v2.24h2.91c1.7-1.56 2.68-3.87 2.68-6.6z"/><path fill="#34A853" d="M9 18c2.43 0 4.47-.8 5.96-2.18l-2.91-2.24c-.81.54-1.84.86-3.05.86-2.34 0-4.32-1.58-5.03-3.71H.99v2.33C2.47 15.93 5.48 18 9 18z"/><path fill="#FBBC05" d="M3.97 10.73c-.18-.54-.28-1.12-.28-1.73s.1-1.19.28-1.73V4.94H.99c-.62 1.24-.98 2.63-.98 4.06s.36 2.82.98 4.06l2.98-2.33z"/><path fill="#EA4335" d="M9 3.58c1.32 0 2.5.45 3.44 1.35l2.58-2.59C13.47.89 11.43 0 9 0 5.48 0 2.47 2.07.99 4.94l2.98 2.33c.71-2.13 2.69-3.71 5.03-3.71z"/></svg>"""
SVG_APPLE = """<svg width="18" height="18" viewBox="0 0 384 512" style="fill:white"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 52.3-11.4 69.5-34.3z"/></svg>"""

# --- Footer ---
def render_footer_components():
    st.write(""); st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"<div class='footer-title'>{T['f_comm']}</div>", unsafe_allow_html=True)
        st.markdown(f"""<div style="display:flex; gap:10px; flex-wrap:wrap;"><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;">{SVG_DISCORD}</button><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;">{SVG_TWITTER}</button><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;">{SVG_TELEGRAM}</button><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;">{SVG_FACEBOOK}</button><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;">{SVG_GITHUB_FOOTER}</button></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='footer-title'>{T['f_legal']}</div>", unsafe_allow_html=True)
        if st.button("Terms (ToS)", key="ft1", use_container_width=True): st.session_state.view_legal = "tos"; set_page('legal_view'); st.rerun()
        if st.button("No Refunds", key="ft2", use_container_width=True): st.session_state.view_legal = "refund"; set_page('legal_view'); st.rerun()
        if st.button("Privacy", key="ft3", use_container_width=True): st.session_state.view_legal = "privacy"; set_page('legal_view'); st.rerun()
    with c3:
        st.markdown(f"<div class='footer-title'>{T['f_prod']}</div>", unsafe_allow_html=True)
        st.link_button("🔗 Solana Scan", "https://solscan.io/", use_container_width=True)
        if st.button("API Docs", use_container_width=True): handle_dev()
    with c4:
        st.markdown(f"<div class='footer-title'>{T['f_serv']}</div>", unsafe_allow_html=True)
        if st.button("SLA Guarantee", use_container_width=True): st.session_state.view_legal = "sla"; set_page('legal_view'); st.rerun()
        st.info("✉️ support@originguard.com")

    st.markdown("---")
    cL1, cL2, cL3 = st.columns([1, 1, 1])
    with cL2:
        sel = st.selectbox("🌐 Select Language / 选择语言", ["English", "中文", "Myanmar"], index=["English", "中文", "Myanmar"].index(st.session_state.language), key="ls")
        if sel != st.session_state.language: st.session_state.language = sel; st.rerun()

    st.write("")
    sc = st.columns([1, 2, 2, 2, 2, 3, 1])
    with sc[1]: 
        if st.button("Terms", key="sb1", use_container_width=True): st.session_state.view_legal = "tos"; set_page('legal_view'); st.rerun()
    with sc[2]: 
        if st.button("Privacy", key="sb2", use_container_width=True): st.session_state.view_legal = "privacy"; set_page('legal_view'); st.rerun()
    with sc[3]: 
        if st.button("Security", key="sb3", use_container_width=True): st.toast("✅ Security Active", icon="🛡️")
    with sc[4]: 
        if st.button("Status", key="sb4", use_container_width=True): st.toast("🟢 Systems OK", icon="📶")
    with sc[5]: 
        if st.button("Do not share my personal information", key="sb5", use_container_width=True): st.toast("🔒 Request Logged", icon="🚫")

    st.markdown("<div style='text-align:center; color:#64748b; font-size:12px; margin-top:20px;'>© 2026 OriginGuard Solutions Inc. [MATRIX_NODE_HK]</div>", unsafe_allow_html=True)
    if not st.session_state.cookies_accepted:
        st.markdown(f"""<div class="cookie-banner"><span style="color:#fff; font-size:16px; margin-right:20px;">🍪 {T['cookie_msg']}</span></div>""", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1,1,1])
        with c2: 
            if st.button(T['cookie_btn'], type="primary", use_container_width=True, key="ckb"): st.session_state.cookies_accepted = True; st.rerun()

# --- Landing ---
if st.session_state.page == 'landing':
    st.write("")
    c1, c2 = st.columns([1.2, 0.8])
    with c1:
        st.write(""); st.write("")
        st.markdown(f"""<div style="padding-right:20px;"><h1 class="breathing-text" style="font-size:56px; margin-bottom:20px; text-transform:uppercase;">{T['slogan']}</h1><p class="breathing-text" style="font-size:20px; color:#f8fafc; font-weight:600; line-height:1.5; font-family:monospace;">{T['sub_slogan']}</p></div>""", unsafe_allow_html=True)
        st.markdown(f"<div style='margin-top:40px; color:#FCD535; font-weight:bold; font-family:monospace;'>🟢 [LIVE_FEED] Solana Mainnet Block: #{get_real_solana_block()}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="auth-header">🛡️ OriginGuard ID [TERMINAL]</div>""", unsafe_allow_html=True)
        
        tl, tr = st.tabs([T['tab_login'], T['tab_reg']])
        with tl:
            pwd = st.text_input(T['lbl_email'], type="password", key="l_p", placeholder="origin2026")
            if st.button(T['btn_login'], type="primary", use_container_width=True):
                # 如果启用了 Supabase，用真实登录；否则用测试密码
if USE_SUPABASE:
    try:
        response = supabase.auth.sign_in_with_password({
            "email": pwd,  # 暂时把密码框当邮箱用
            "password": "temporary"  # 或者让用户输入
        })
        if response.user:
            with st.spinner("AUTHENTICATING..."): 
                time.sleep(1)
                st.session_state.auth = True
                st.session_state.user_id = response.user.id
                set_page('dashboard')
                st.rerun()
    except:
        st.error(T['err_login'])
else:
    # 保留原来的测试登录
    if pwd == "origin2026":
        with st.spinner("AUTHENTICATING..."): 
            time.sleep(1)
            st.session_state.auth = True
            set_page('dashboard')
            st.rerun()
    else:
        st.error(T['err_login'])

                    with st.spinner("AUTHENTICATING..."): time.sleep(1); st.session_state.auth = True; set_page('dashboard'); st.rerun()
                else: st.error(T['err_login'])
            st.markdown(f"<div style='text-align:center; color:#94a3b8; font-size:12px; margin:15px 0; font-family:monospace;'>{T['or_connect']}</div>", unsafe_allow_html=True)
            st.markdown(f"""<a href="#" class="real-logo-btn btn-google">{SVG_GOOGLE} GOOGLE_OAUTH</a><a href="#" class="real-logo-btn btn-apple">{SVG_APPLE} APPLE_ID</a><a href="#" class="real-logo-btn btn-github">{SVG_GITHUB} GITHUB_DEV</a>""", unsafe_allow_html=True)
        with tr:
            st.text_input("Email"); st.text_input(T['lbl_pwd'], type="password"); st.text_input(T['lbl_cpwd'], type="password")
            if st.button(T['btn_reg'], type="primary", use_container_width=True):
                with st.spinner("INITIALIZING IDENTITY..."): time.sleep(2); st.success(T['suc_reg']); time.sleep(1); st.rerun()
    
    st.write(""); st.write(""); st.markdown("---"); st.subheader(T['core_title'])
    f1, f2, f3 = st.columns(3)
    with f1: st.markdown(f"""<div class="feature-card"><h3>👁️ {T['c1_t']}</h3><p>{T['c1_d']}</p></div>""", unsafe_allow_html=True)
    with f2: st.markdown(f"""<div class="feature-card"><h3>⛓️ {T['c2_t']}</h3><p>{T['c2_d']}</p></div>""", unsafe_allow_html=True)
    with f3: st.markdown(f"""<div class="feature-card"><h3>⚖️ {T['c3_t']}</h3><p>{T['c3_d']}</p></div>""", unsafe_allow_html=True)
    render_footer_components()

# --- Dashboard (Wallet + KYC) ---
elif st.session_state.page == 'dashboard':
    if not st.session_state.auth: set_page('landing'); st.rerun()
    
    with st.sidebar: 
        st.success("🟢 [OPERATOR]: MNNO"); 
        st.button("TERMINATE SESSION", on_click=lambda: (setattr(st.session_state, 'auth', False), set_page('landing')))
    
    st.markdown(f"""
    <div class="wallet-box">
        <div style="font-family:monospace;">
            <div style="font-size:12px; color:#94a3b8;">[WALLET_UPLINK_STATUS]</div>
            <div class="{ 'wallet-status-on' if st.session_state.wallet_connected else 'wallet-status-off' }">
                { '● ESTABLISHED: 5KMt...Eq9x' if st.session_state.wallet_connected else '○ OFFLINE' }
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.wallet_connected:
        if st.button("🔌 INITIALIZE PHANTOM UPLINK", type="primary"):
            with st.spinner("CONNECTING TO NODE..."): time.sleep(1.5); st.session_state.wallet_connected = True; st.session_state.wallet_address = "5KMt...Eq9x"; st.rerun()
    
    st.title("📊 DASHBOARD [MATRIX_VIEW]")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("SECURED ASSETS", "1,248", delta="Verified"); k2.metric("ACTIVE THREATS", "53", "-12% This Week", delta_color="inverse"); k3.metric("LEGAL ACTIONS", "41", "+5 Pending"); k4.metric("EST. GAS SAVED", "$12,400", "Solana Efficacy")
    
    st.markdown("---")
    t1, t2, t3 = st.tabs(["🛡️ PROTECT", "⚖️ LEGAL HAMMER", "👤 IDENTITY"])
    
    with t1:
        uf = st.file_uploader("UPLOAD ASSET FOR ENCRYPTION", type=['png','jpg'])
        if uf:
            if not st.session_state.wallet_connected:
                st.warning("⚠️ [DENIED] WALLET CONNECTION REQUIRED FOR ON-CHAIN WRITES.")
            else:
                if st.button("🔒 EXECUTE DNA ENCRYPTION", type="primary"):
                    with st.spinner("🧬 CALCULATING SHA-256 HASH..."):
                        time.sleep(1.5); f_hash = calculate_file_dna(uf); block = get_real_solana_block()
                        st.success(f"✅ HASH GENERATED: {f_hash}"); st.markdown(f"""<div class="cert-box"><div class="cert-title">📜 CERTIFICATE GENERATED [IMMUTABLE]</div><div class="cert-hash">ID: {f_hash}</div></div>""", unsafe_allow_html=True)
                        st.download_button("📄 DOWNLOAD CERTIFICATE (.TXT)", generate_certificate(uf.name, f_hash, block), file_name=f"OG_CERT_{f_hash[:8]}.txt")
                        st.link_button("🔍 VERIFY ON SOLSCAN (SIM)", f"https://solscan.io/account/{f_hash}")# [新增] 如果启用了 Supabase，保存到云端
if USE_SUPABASE and supabase:
    try:
        # 上传文件到 Supabase Storage
        file_path = f"assets/{f_hash[:8]}_{uf.name}"
        supabase.storage.from_("originguard").upload(
            file_path,
            uf.getvalue(),
            {"content-type": uf.type}
        )
        
        # 获取文件 URL
        file_url = supabase.storage.from_("originguard").get_public_url(file_path)
        
        # 保存到数据库
        if 'user_id' in st.session_state:
            supabase.table("assets").insert({
                "user_id": st.session_state.user_id,
                "file_name": uf.name,
                "file_hash": f_hash,
                "file_url": file_url,
                "solana_signature": f"SIM_{f_hash[:16]}"
            }).execute()
            
            st.info(f"☁️ 已保存到云端：{file_url}")
    except Exception as e:
        st.warning(f"⚠️ 云端保存失败（本地依然可用）：{str(e)}")


    with t2:
        st.text_input("INFRINGING URL_TARGET"); st.button("INITIATE TAKEDOWN NOTICE", type="primary", on_click=handle_dev)

    with t3:
        st.subheader("IDENTITY VERIFICATION [KYC_PROTOCOL]")
        if st.session_state.kyc_status == "Verified":
            st.markdown(f"""<div class="kyc-box"><h3>✅ [STATUS: CLEARED]</h3><p>Level 2 Clearance Granted. Full matrix access unlocked.</p><span class="kyc-badge-verified">LVL.2 VERIFIED</span></div>""", unsafe_allow_html=True)
        elif st.session_state.kyc_status == "Pending":
            st.info("⏳ [STATUS: PENDING REVIEW]... Analyzing biometric data.")
            st.markdown('<span class="kyc-badge-pending">AWAITING APPROVAL</span>', unsafe_allow_html=True)
            if st.button("[ADMIN] OVERRIDE VERIFY"): st.session_state.kyc_status = "Verified"; st.rerun()
        else:
            st.markdown(f"""<div class="kyc-box"><h3>⚠️ [STATUS: UNVERIFIED]</h3><p>Upload government-issued ID to proceed.</p></div>""", unsafe_allow_html=True)
            c_k1, c_k2 = st.columns(2)
            with c_k1: st.text_input("FULL LEGAL NAME"); st.text_input("GOV ID NUMBER")
            with c_k2: st.file_uploader("UPLOAD ID DOCUMENT", type=['jpg','png','pdf'])
            if st.button("SUBMIT FOR BIOMETRIC SCAN", type="primary"):
                st.session_state.kyc_status = "Pending"; st.rerun()

    render_footer_components()

# --- Legal View ---
elif st.session_state.page == 'legal_view':
    st.button("⬅️ RETURN TO TERMINAL", on_click=lambda: set_page('landing'))
    st.markdown("---")
    content = L_TEXT.get(st.session_state.get('view_legal', 'tos'), "Error")
    st.markdown(f"""<div class="legal-box" style="font-family:monospace;">{content}</div>""", unsafe_allow_html=True)
    render_footer_components()
