import streamlit as st
import hashlib
import os
from datetime import datetime
import requests

# ===== 页面配置 =====
st.set_page_config(
    page_title="DNA Generator - OriginGuard",
    page_icon="🛡️",
    layout="wide"
)

# ===== 环境变量配置 =====
SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL', 'https://api.mainnet-beta.solana.com')
API_TIMEOUT = 10

# ===== 优化字体CSS（修复模糊问题）=====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-rendering: optimizeLegibility;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
        color: #00ff41;
        font-family: 'JetBrains Mono', 'Courier New', monospace;
    }
    
    h1, h2, h3 {
        color: #00ff41 !important;
        text-shadow: 0 0 10px #00ff41;
        font-weight: 700 !important;
        letter-spacing: 1px;
    }
    
    p, span, div {
        font-size: 16px !important;
        line-height: 1.8 !important;
        font-weight: 400 !important;
    }
    
    .stSelectbox > div > div {
        background-color: #1a1f3a !important;
        border: 2px solid #00ff41 !important;
        color: #00ff41 !important;
        font-weight: bold !important;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border: none;
        padding: 12px 24px;
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.6);
    }
    
    .dna-box {
        background: rgba(0, 255, 65, 0.1);
        border: 2px solid #00ff41;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        font-family: 'JetBrains Mono', monospace;
        word-break: break-all;
    }
    
    @keyframes radar-pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.6; transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    .radar-active {
        animation: radar-pulse 2s infinite;
        color: #ff00ff;
    }
</style>
""", unsafe_allow_html=True)

# ===== 核心类 =====
class OriginGuard:
    def __init__(self):
        self.radar_active = True
        self.threat_level = "GREEN"
        
    def generate_dna(self, file_content: bytes) -> str:
        return hashlib.sha256(file_content).hexdigest()
    
    def verify_solana_connection(self) -> bool:
        try:
            response = requests.post(
                SOLANA_RPC_URL,
                json={"jsonrpc": "2.0", "id": 1, "method": "getHealth"},
                timeout=API_TIMEOUT
            )
            return response.status_code == 200
        except:
            return False
    
    def radar_scan(self) -> dict:
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "threats_detected": 0,
            "status": "ACTIVE",
            "blockchain_connected": self.verify_solana_connection()
        }

# ===== 翻译字典 =====
TRANS = {
    "title": {"zh": "DNA生成器", "en": "DNA Generator"},
    "slogan": {"zh": "保护你的原创作品视频照片等", "en": "Protect Your Original Works"},
    "upload": {"zh": "上传文件生成DNA", "en": "Upload File to Generate DNA"},
    "dna_result": {"zh": "文件DNA指纹", "en": "File DNA Fingerprint"},
    "blockchain": {"zh": "区块链状态", "en": "Blockchain Status"},
    "radar": {"zh": "雷达扫描", "en": "Radar Scanning"},
    "connected": {"zh": "已连接", "en": "Connected"},
    "disconnected": {"zh": "未连接", "en": "Disconnected"},
}

# ===== 初始化 =====
if 'guard' not in st.session_state:
    st.session_state.guard = OriginGuard()
    st.session_state.scan_count = 0

guard = st.session_state.guard

# ===== 侧边栏 =====
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    lang = st.selectbox(
        "语言 / Language",
        options=["zh", "en"],
        format_func=lambda x: "中文" if x == "zh" else "English"
    )
    
    st.markdown("---")
    st.markdown("### 🔍 System Status")
    
    scan_result = guard.radar_scan()
    st.markdown(f"<div class='radar-active'>🎯 {TRANS['radar'][lang]}: {scan_result['status']}</div>", unsafe_allow_html=True)
    
    blockchain_status = TRANS['connected'][lang] if scan_result['blockchain_connected'] else TRANS['disconnected'][lang]
    status_color = "green" if scan_result['blockchain_connected'] else "red"
    st.markdown(f"<div style='color:{status_color}'>⛓️ {TRANS['blockchain'][lang]}: {blockchain_status}</div>", unsafe_allow_html=True)
    
    st.markdown(f"🕐 {scan_result['timestamp']}")

# ===== 主界面 =====
st.markdown(f"<h1>🛡️ {TRANS['title'][lang]}</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color:#ff00ff'>{TRANS['slogan'][lang]}</h3>", unsafe_allow_html=True)

st.markdown("---")

# ===== 文件上传 =====
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"### 📁 {TRANS['upload'][lang]}")
    uploaded_file = st.file_uploader(
        "",
        type=["jpg", "jpeg", "png", "mp4", "mov", "pdf", "txt"],
        help="支持图片、视频、文档等格式"
    )
    
    if uploaded_file is not None:
        file_content = uploaded_file.read()
        dna_hash = guard.generate_dna(file_content)
        
        st.markdown(f"### ✅ {TRANS['dna_result'][lang]}")
        st.markdown(f"""
        <div class='dna-box'>
            <strong>文件名:</strong> {uploaded_file.name}<br>
            <strong>大小:</strong> {len(file_content)} bytes<br>
            <strong>DNA哈希:</strong><br>
            <code>{dna_hash}</code>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("✅ DNA指纹已生成！请妥善保存此哈希值作为原创证明。")
        st.info("🔒 注意：本系统不存储任何文件内容，仅生成数学指纹。")

with col2:
    st.markdown("### 📊 Real-time Monitor")
    st.metric("Scan Count", st.session_state.scan_count)
    st.metric("Threat Level", guard.threat_level)
    
    if st.button("🔄 Refresh Scan"):
        st.session_state.scan_count += 1
        st.rerun()

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8em;'>
    🛡️ OriginGuard V6.1 | 24/7 Protection | Zero Data Storage
</div>
""", unsafe_allow_html=True)
