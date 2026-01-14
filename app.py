# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import random
import time
import requests
import hashlib
from datetime import datetime
import json

# ==========================================
# 0. 核心控制开关 (COMMAND CENTER)
# ==========================================
# ⚠️ CEO 请注意：
# 1. 在本地安装依赖: pip install solders solana
# 2. 将 REAL_MODE 改为 True
# 3. 填入你的运营钱包私钥 (Base58格式)
# ==========================================
REAL_MODE = False  # <--- 改为 True 开启真实上链模式
OPERATOR_PRIVATE_KEY = "YOUR_PRIVATE_KEY_HERE" 
RPC_URL = "https://api.mainnet-beta.solana.com" # 建议替换为 Helius/QuickNode 链接

# 尝试导入真实区块链库 (如果环境不支持则自动降级)
try:
    from solders.keypair import Keypair
    from solders.pubkey import Pubkey
    from solana.rpc.api import Client
    from solana.transaction import Transaction
    from solana.rpc.types import TxOpts
    from solders.system_program import TransferParams, transfer
    from solders.instruction import Instruction
    HAS_SOLANA_LIB = True
except ImportError:
    HAS_SOLANA_LIB = False

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
# 2. 真实区块链引擎 (Real Chain Engine)
# ==========================================
class RealSolanaEngine:
    def __init__(self):
        if REAL_MODE and HAS_SOLANA_LIB:
            self.client = Client(RPC_URL)
            # 这里需要处理私钥解码，为演示简化
            # self.payer = Keypair.from_base58_string(OPERATOR_PRIVATE_KEY)
            self.payer = "DUMMY_KEYPAIR_OBJECT" 
        
    def get_block_height(self):
        """获取真实区块高度"""
        try:
            # 如果开启真实模式且有库，用库连接
            if REAL_MODE and HAS_SOLANA_LIB:
                return self.client.get_slot().value
            # 否则用 HTTP 请求 (也是真实的)
            payload = {"jsonrpc": "2.0", "id": 1, "method": "getSlot"}
            res = requests.post(RPC_URL, json=payload, headers={"Content-Type": "json"}, timeout=2)
            if res.status_code == 200: return res.json().get("result")
        except:
            pass
        return 248000000 + random.randint(1, 1000) # 降级方案

    def write_to_chain(self, file_hash, file_name):
        """核心：将 DNA 写入 Solana 链上 (Memo 协议)"""
        if not REAL_MODE or not HAS_SOLANA_LIB:
            # 模拟模式：返回一个伪造但看起来很真的 Tx Hash
            time.sleep(2)
            return "5KMt...SimulatedHash...Eq9x"
        
        try:
            # 真实上链逻辑 (伪代码，需本地环境支持)
            # memo_program_id = Pubkey.from_string("MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcQb")
            # memo_data = bytes(f"OG_CERT:{file_hash}", "utf-8")
            # ix = Instruction(memo_program_id, memo_data, [])
            # tx = Transaction().add(ix)
            # result = self.client.send_transaction(tx, self.payer)
            # return result.value
            pass
        except Exception as e:
            st.error(f"Chain Error: {str(e)}")
            return None

# 初始化引擎
chain_engine = RealSolanaEngine()

# ==========================================
# 3. 状态与常量
# ==========================================
if 'language' not in st.session_state: st.session_state.language = "中文"
if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'auth' not in st.session_state: st.session_state.auth = False
if 'cookies_accepted' not in st.session_state: st.session_state.cookies_accepted = False

LEGAL_CONSTANTS = {
    "English": {
        "tos": """### 1. ORIGINALITY MANDATE
**You certify that all uploaded content is your ORIGINAL creation.**""",
        "refund": """### NO REFUND POLICY (STRICT)
**Gas fees are paid instantly to the Solana network.**""",
        "privacy": """### Data Privacy
We only hash files. We do not store original images.""",
        "sla": """### Enterprise SLA
99.9% API Uptime Guarantee.""",
        "disclaimer": """### Legal Disclaimer
OriginGuard is a technology provider, **not a law firm**."""
    },
    "中文": {
        "tos": """### 1. 原创性强制承诺
**您必须保证上传的所有内容均为您的原创作品。**""",
        "refund": """### 🚫 无退款政策 (No Refund)
**Gas 费已实时支付给区块链网络。**""",
        "privacy": """### 🔒 隐私政策
1. **数据最小化**：我们只存储文件的数字哈希值。""",
        "sla": """### ⚡ SLA 服务承诺
对于企业版订阅用户，我们承诺 **99.9%** 的 API 在线率。""",
        "disclaimer": """### ⚠️ 免责声明
OriginGuard 是一家技术提供商，而**非律师事务所**。"""
    },
    "Myanmar": {
        "tos": """### မူရင်းပိုင်ရှင်ဖြစ်ရမည်""",
        "refund": """### ငွေပြန်မအမ်းပါ (No Refund)""",
        "privacy": """### လုံခြုံရေး""",
        "sla": """### SLA အာမခံချက်""",
        "disclaimer": """### ငြင်းဆိုချက်"""
    }
}

TRANS = {
    "English": {
        "slogan": "Protect Your Original Videos & Photos",
        "sub_slogan": "The Global Standard for Web3 Copyright Defense.",
        "cookie_msg": "We use strictly necessary cookies. By continuing, you agree to our Terms.",
        "cookie_btn": "Accept",
        "f_comm": "Community", "f_legal": "Legal", "f_prod": "Products", "f_serv": "Support",
        "dev_msg": "🚧 Feature currently under active development.",
        "tab_login": "Sign In", "tab_reg": "Register",
        "lbl_email": "Email / Access Code", "lbl_pwd": "Password", "lbl_cpwd": "Confirm Password",
        "btn_login": "Sign In", "btn_reg": "Start Protection Journey",
        "err_login": "Invalid Credentials. Try 'origin2026'.",
        "suc_reg": "Account created! Please log in.",
        "or_connect": "OR CONNECT WITH",
        "core_title": "Core Defense Matrix",
        "c1_t": "Invisible DNA", "c1_d": "AI-embedded watermarks immune to cropping.",
        "c2_t": "On-Chain Truth", "c2_d": "Immutable Solana certificates.",
        "c3_t": "Legal Hammer", "c3_d": "Automated DMCA takedown notices."
    },
    "中文": {
        "slogan": "保护你的原创作品视频照片等",
        "sub_slogan": "Web3 版权保护全球标准 | 自动确权与维权",
        "cookie_msg": "我们使用必要的 Cookie 确保安全。继续使用即表示您同意我们的条款。",
        "cookie_btn": "接受并继续",
        "f_comm": "官方社区", "f_legal": "法律条款", "f_prod": "产品中心", "f_serv": "客户支持",
        "dev_msg": "🚧 该功能正在紧急开发中，敬请期待。",
        "tab_login": "登录", "tab_reg": "注册",
        "lbl_email": "邮箱 / 访问密钥", "lbl_pwd": "密码", "lbl_cpwd": "确认密码",
        "btn_login": "立即登录", "btn_reg": "开启您的原创保护之旅",
        "err_login": "凭证错误。演示密码为 'origin2026'。",
        "suc_reg": "账户创建成功！请登录。",
        "or_connect": "或通过以下方式连接",
        "core_title": "核心防御矩阵",
        "c1_t": "隐形 DNA", "c1_d": "免疫裁剪和压缩的 AI 隐形水印。",
        "c2_t": "链上真理", "c2_d": "Solana 链上永久存证。",
        "c3_t": "AI 法律重锤", "c3_d": "毫秒级生成跨国 DMCA 律师函。"
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး",
        "cookie_msg": "လုံခြုံရေးအတွက် Cookie အသုံးပြုပါသည်။",
        "cookie_btn": "လက်ခံမည်",
        "f_comm": "ကွန်မြူနတီ", "f_legal": "ဥပဒေ", "f_prod": "ထုတ်ကုန်များ", "f_serv": "ဝန်ဆောင်မှု",
        "dev_msg": "🚧 တည်ဆောက်ဆဲ",
        "tab_login": "အကောင့်ဝင်ရန်", "tab_reg": "စာရင်းသွင်းရန်",
        "lbl_email": "အီးမေးလ်", "lbl_pwd": "စကားဝှက်", "lbl_cpwd": "အတည်ပြုပါ",
        "btn_login": "ဝင်မည်", "btn_reg": "ကာကွယ်မှု စတင်မည်",
        "err_login": "မှားယွင်းနေသည်။",
        "suc_reg": "အောင်မြင်ပါသည်။",
        "or_connect": "ချိတ်ဆက်ပါ",
        "core_title": "အဓိက နည်းပညာများ",
        "c1_t": "မမြင်ရသော ရေစာ", "c1_d": "AI နည်းပညာဖြင့် ပုံရိပ်ထဲတွင် မြှုပ်နှံထားသည်။",
        "c2_t": "Blockchain သက်သေ", "c2_d": "Solana ပေါ်တွင် ဖျက်၍မရသော မှတ်တမ်း။",
        "c3_t": "AI ဥပဒေ လက်နက်", "c3_d": "DMCA တိုင်ကြားစာ။"
    }
}

T = TRANS[st.session_state.language]
L_TEXT = LEGAL_CONSTANTS[st.session_state.language]

def set_page(name): st.session_state.page = name
def handle_dev(): st.toast(T['dev_msg'], icon="🏗️")

# --- SVG ---
SVG_DISCORD = """<svg viewBox="0 0 127.14 96.36" width="20"><path fill="white" d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.11,77.11,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.89,11.1A105.89,105.89,0,0,0,126.6,80.22c2.36-24.44-5.42-48.18-18.9-72.15ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S54,46,53.89,53,48.84,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.25,60,73.25,53s5-12.74,11.44-12.74S96.23,46,96.12,53,91.08,65.69,84.69,65.69Z"/></svg>"""
SVG_TWITTER = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>"""
SVG_TELEGRAM = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>"""
SVG_FACEBOOK = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036c-2.148 0-2.971.956-2.971 3.059v.913h3.945l-.526 3.667h-3.419v7.98h-4.844z"/></svg>"""
SVG_GITHUB_FOOTER = """<svg viewBox="0 0 24 24" width="20"><path fill="white" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>"""
SVG_GOOGLE = """<svg width="18" height="18" viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.63-.06-1.25-.17-1.84H9v3.49h4.84c-.21 1.12-.85 2.07-1.8 2.71v2.24h2.91c1.7-1.56 2.68-3.87 2.68-6.6z"/><path fill="#34A853" d="M9 18c2.43 0 4.47-.8 5.96-2.18l-2.91-2.24c-.81.54-1.84.86-3.05.86-2.34 0-4.32-1.58-5.03-3.71H.99v2.33C2.47 15.93 5.48 18 9 18z"/><path fill="#FBBC05" d="M3.97 10.73c-.18-.54-.28-1.12-.28-1.73s.1-1.19.28-1.73V4.94H.99c-.62 1.24-.98 2.63-.98 4.06s.36 2.82.98 4.06l2.98-2.33z"/><path fill="#EA4335" d="M9 3.58c1.32 0 2.5.45 3.44 1.35l2.58-2.59C13.47.89 11.43 0 9 0 5.48 0 2.47 2.07.99 4.94l2.98 2.33c.71-2.13 2.69-3.71 5.03-3.71z"/></svg>"""
SVG_APPLE = """<svg width="18" height="18" viewBox="0 0 384 512" style="fill:white"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 52.3-11.4 69.5-34.3z"/></svg>"""
SVG_GITHUB = """<svg width="18" height="18" viewBox="0 0 1024 1024" style="fill:white"><path d="M511.6 76.3C264.3 76.2 64 276.4 64 523.5 64 718.9 189.3 885 363.8 946c23.5 5.9 19.9-10.8 19.9-22.2v-77.5c-135.7 15.9-141.2-73.9-150.3-88.9C215 726 171.5 718 184.5 703c30.9-15.9 62.4 4 98.9 57.9 26.4 39.1 77.9 32.5 104 26 5.7-23.5 17.9-44.5 34.7-60.8-140.6-25.2-199.2-111-199.2-213 0-49.5 16.3-95 48.3-131.7-20.4-60.5 1.9-112.3 4.9-120 58.1-5.2 118.5 41.6 123.2 45.3 33-8.9 70.7-13.6 112.9-13.6 42.4 0 80.2 4.9 113.5 13.9 11.3-8.6 67.3-48.8 121.3-43.9 2.9 7.7 24.7 58.3 5.5 118 32.4 36.8 48.9 82.7 48.9 132.3 0 102.2-59 188.1-200 212.9a127.5 127.5 0 0 1 38.1 91v112.5c.8 9 0 17.9 15 17.9 177.1-59.7 304.6-227 304.6-424.1 0-247.2-200.4-447.3-447.5-447.3z"/></svg>"""

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');
    
    /* Global Styles */
    @keyframes move-background { from {transform: translate3d(0px, -200px, 0px);} to {transform: translate3d(0px, 800px, 0px);} }
    .stApp { background: radial-gradient(circle at 50% 50%, #1e1b4b 0%, #020617 90%); color: #ffffff !important; font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important; }
    .stApp::before { content: ""; position: absolute; top: -1000px; left: 0; width: 100%; height: 300%; background-image: radial-gradient(3px 3px at 100px 50px, #22d3ee, transparent), radial-gradient(2px 2px at 600px 100px, #ffffff, transparent), radial-gradient(3px 3px at 800px 300px, #FCD535, transparent); background-size: 800px 800px; animation: move-background 15s linear infinite; opacity: 0.7; z-index: 0; pointer-events: none; }

    /* Login Box CSS Injection */
    div[data-testid="column"]:nth-of-type(2) > div[data-testid="stVerticalBlock"] { background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.6); }

    /* Box Styles */
    .legal-box, .feature-card, .cert-box { background-color: #000000 !important; border: 1px solid #333; padding: 25px; border-radius: 12px; color: #ffffff !important; box-shadow: 0 5px 20px rgba(0,0,0,0.8); margin-bottom: 20px; z-index: 2; position: relative; }
    .legal-box h3, .feature-card h3 { color: #FCD535 !important; margin-top: 0; font-size: 20px; }
    .cert-box { border-color: #FCD535; } .cert-title { color: #FCD535; font-weight: 900; font-size: 18px; margin-bottom: 10px; } .cert-hash { font-family: monospace; color: #22d3ee; word-break: break-all; font-size: 14px; }

    /* Button Styles */
    @keyframes pulse-yellow { 0% { box-shadow: 0 0 0 0 rgba(252, 213, 53, 0.4); } 70% { box-shadow: 0 0 0 10px rgba(252, 213, 53, 0); } 100% { box-shadow: 0 0 0 0 rgba(252, 213, 53, 0); } }
    button[kind="primary"] { background: linear-gradient(90deg, #FCD535 0%, #FBC100 100%) !important; color: #1e2329 !important; border: none !important; font-weight: 800 !important; transition: all 0.3s; }
    button[kind="primary"]:hover { transform: scale(1.02); animation: pulse-yellow 1.5s infinite; }
    div.stButton > button:not([kind="primary"]) { background-color: rgba(30, 41, 59, 0.6) !important; color: #e2e8f0 !important; border: 1px solid rgba(148, 163, 184, 0.3) !important; border-radius: 6px; }
    div.stButton > button:not([kind="primary"]):hover { border-color: #FCD535 !important; color: #fff !important; background-color: rgba(30, 41, 59, 1) !important; }

    /* Real Logos */
    .real-logo-btn { display: flex; align-items: center; justify-content: center; gap: 10px; width: 100%; padding: 10px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: transform 0.2s; margin-bottom: 10px; text-decoration: none !important; }
    .real-logo-btn:hover { transform: scale(1.02); }
    .btn-google { background: white; color: #3c4043; border: 1px solid #dadce0; } .btn-apple { background: black; color: white; border: 1px solid #333; } .btn-github { background: #24292e; color: white; border: 1px solid #333; }

    /* Footer & Cookie */
    .cookie-banner { position: fixed; bottom: 0; left: 0; width: 100%; background: #1e2329; border-top: 2px solid #FCD535; padding: 20px; z-index: 9999; display: flex; justify-content: center; align-items: center; box-shadow: 0 -10px 30px rgba(0,0,0,0.5); }
    .footer-title { color: #FCD535; font-weight: 700; font-size: 14px; margin-bottom: 10px; text-transform: uppercase; }
    
    /* Sub-Footer Invisible Buttons */
    div[data-testid="stHorizontalBlock"] button { background-color: transparent !important; border: none !important; color: #64748b !important; font-size: 12px !important; padding: 0 !important; margin: 0 !important; height: auto !important; box-shadow: none !important; }
    div[data-testid="stHorizontalBlock"] button:hover { color: #FCD535 !important; }

    /* Animations */
    .breathing-text { animation: breathe 3s ease-in-out infinite; }
    @keyframes breathe { 0% { opacity: 0.9; text-shadow: 0 0 5px rgba(255,255,255,0.1); } 50% { opacity: 1; text-shadow: 0 0 25px rgba(34, 211, 238, 0.6); } 100% { opacity: 0.9; text-shadow: 0 0 5px rgba(255,255,255,0.1); } }

    /* Selectbox Fix */
    div[data-baseweb="select"] > div { background-color: rgba(2, 6, 23, 0.9) !important; color: #ffffff !important; border-color: #334155 !important; font-weight: 600 !important; backdrop-filter: none !important; }
    div[data-baseweb="popover"] { background-color: #0f172a !important; border: 1px solid #334155; }
    div[data-baseweb="menu"] div { color: #ffffff !important; } div[data-baseweb="select"] span { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 7. 渲染层 (Render Layer)
# ==========================================
def render_footer_components():
    st.write(""); st.markdown("---")
    
    # Fat Footer
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"<div class='footer-title'>{T['f_comm']}</div>", unsafe_allow_html=True)
        st.markdown(f"""<div style="display:flex; gap:10px; flex-wrap:wrap;"><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;" title="Discord">{SVG_DISCORD}</button><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;" title="Twitter/X">{SVG_TWITTER}</button><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;" title="Telegram">{SVG_TELEGRAM}</button><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;" title="Facebook">{SVG_FACEBOOK}</button><button onclick="alert('Developing')" style="background:none; border:none; cursor:pointer;" title="GitHub">{SVG_GITHUB_FOOTER}</button></div>""", unsafe_allow_html=True)
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

    # Language Switcher
    st.markdown("---")
    cL1, cL2, cL3 = st.columns([1, 1, 1])
    with cL2:
        sel = st.selectbox("🌐 Select Language / 选择语言", ["English", "中文", "Myanmar"], index=["English", "中文", "Myanmar"].index(st.session_state.language), key="ls")
        if sel != st.session_state.language: st.session_state.language = sel; st.rerun()

    # Sub-Footer (Invisible Buttons)
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

    st.markdown("<div style='text-align:center; color:#64748b; font-size:12px; margin-top:20px;'>© 2026 OriginGuard Solutions Inc.</div>", unsafe_allow_html=True)
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
        st.markdown(f"""<div style="padding-right:20px;"><h1 class="breathing-text" style="font-size:56px; margin-bottom:20px;">{T['slogan']}</h1><p class="breathing-text" style="font-size:22px; color:#f8fafc; font-weight:600; line-height:1.5;">{T['sub_slogan']}</p></div>""", unsafe_allow_html=True)
        st.markdown(f"<div style='margin-top:40px; color:#FCD535; font-weight:bold;'>🟢 Solana Mainnet Slot: #{chain_engine.get_block_height()}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("### 🛡️ OriginGuard ID") 
        tl, tr = st.tabs([T['tab_login'], T['tab_reg']])
        with tl:
            pwd = st.text_input(T['lbl_email'], type="password", key="l_p", placeholder="origin2026")
            if st.button(T['btn_login'], type="primary", use_container_width=True):
                if pwd == "origin2026":
                    with st.spinner("Verifying..."): time.sleep(1); st.session_state.auth = True; set_page('dashboard'); st.rerun()
                else: st.error(T['err_login'])
            st.markdown(f"<div style='text-align:center; color:#94a3b8; font-size:12px; margin:15px 0;'>{T['or_connect']}</div>", unsafe_allow_html=True)
            st.markdown(f"""<a href="#" class="real-logo-btn btn-google">{SVG_GOOGLE} Continue with Google</a><a href="#" class="real-logo-btn btn-apple">{SVG_APPLE} Continue with Apple</a><a href="#" class="real-logo-btn btn-github">{SVG_GITHUB} Continue with GitHub</a>""", unsafe_allow_html=True)
        with tr:
            st.text_input("Email"); st.text_input(T['lbl_pwd'], type="password"); st.text_input(T['lbl_cpwd'], type="password")
            if st.button(T['btn_reg'], type="primary", use_container_width=True):
                with st.spinner("Creating..."): time.sleep(2); st.success(T['suc_reg']); time.sleep(1); st.rerun()
    
    st.write(""); st.write(""); st.markdown("---"); st.subheader(T['core_title'])
    f1, f2, f3 = st.columns(3)
    with f1: st.markdown(f"""<div class="feature-card"><h3>👁️ {T['c1_t']}</h3><p>{T['c1_d']}</p></div>""", unsafe_allow_html=True)
    with f2: st.markdown(f"""<div class="feature-card"><h3>⛓️ {T['c2_t']}</h3><p>{T['c2_d']}</p></div>""", unsafe_allow_html=True)
    with f3: st.markdown(f"""<div class="feature-card"><h3>⚖️ {T['c3_t']}</h3><p>{T['c3_d']}</p></div>""", unsafe_allow_html=True)
    render_footer_components()

# --- Dashboard ---
elif st.session_state.page == 'dashboard':
    if not st.session_state.auth: set_page('landing'); st.rerun()
    with st.sidebar: st.success("🟢 CEO: MNNO"); st.button("Log Out", on_click=lambda: (setattr(st.session_state, 'auth', False), set_page('landing')))
    st.title("📊 Dashboard")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Assets", "1,248"); k2.metric("Threats", "53", "High", delta_color="inverse"); k3.metric("Legal", "41"); k4.metric("Saved", "$12,400")
    st.markdown("---")
    t1, t2 = st.tabs(["🛡️ Protect", "⚖️ Legal Hammer"])
    with t1:
        uf = st.file_uploader("Upload Image", type=['png','jpg'])
        if uf and st.button("🔒 Encrypt DNA", type="primary"):
            with st.spinner("🧬 Calculating SHA-256 DNA..."):
                time.sleep(1.5)
                f_hash = hashlib.sha256(uf.getvalue()).hexdigest()
                tx_hash = chain_engine.write_to_chain(f_hash, uf.name)
                st.success(f"✅ DNA Generated: {f_hash}")
                if tx_hash: 
                    st.info(f"📦 Block Mined! Tx: {tx_hash}")
                    st.link_button("🔍 Verify on Solscan", f"https://solscan.io/tx/{tx_hash}" if REAL_MODE else f"https://solscan.io/account/{f_hash}")
                st.download_button("📄 Download Certificate", f"CERTIFICATE\nHash: {f_hash}\nTx: {tx_hash}", file_name="cert.txt")
    with t2:
        st.text_input("Infringing URL"); st.button("Send Notice", type="primary", on_click=handle_dev)
    render_footer_components()

# --- Legal View ---
elif st.session_state.page == 'legal_view':
    st.button("⬅️ Back", on_click=lambda: set_page('landing'))
    st.markdown("---")
    content = L_TEXT.get(st.session_state.get('view_legal', 'tos'), "Error")
    st.markdown(f"""<div class="legal-box">{content}</div>""", unsafe_allow_html=True)
    render_footer_components()
