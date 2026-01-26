import streamlit as st

st.set_page_config(
    page_title="OriginGuard V6.1 - Home",
    page_icon="🛡️",
    layout="wide"
)

# ===== 优化字体CSS =====
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
    }
    .stButton > button {
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 12px 24px;
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.6);
    }
    .feature-card {
        background: rgba(26, 31, 58, 0.8);
        border: 2px solid #00ff41;
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.3);
        transition: all 0.3s;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 30px rgba(0, 255, 65, 0.5);
    }
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px #00ff41; }
        50% { text-shadow: 0 0 20px #00ff41, 0 0 30px #00ff41; }
    }
    .animate-glow {
        animation: glow 2s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

# ===== 主页内容 =====
st.markdown('<h1 class="animate-glow">🛡️ OriginGuard V6.1</h1>', unsafe_allow_html=True)
st.markdown('<h2>主动防御协议 | Active Defense Protocol</h2>', unsafe_allow_html=True)
st.markdown('<h3 style="color:#ff00ff">保护你的原创作品视频照片等</h3>', unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🔐 100%安全架构</h3>
        <p style="color:#aaa;">零数据存储，仅生成数学指纹<br>您的文件永不上传到服务器<br>完全保护隐私</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>⛓️ 区块链验证</h3>
        <p style="color:#aaa;">Solana区块链实时验证<br>不可篡改的原创证明<br>全球认可的时间戳</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 24/7雷达扫描</h3>
        <p style="color:#aaa;">实时监控威胁<br>主动防御系统<br>全天候保护</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown('<h2>🚀 快速开始</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
    <h3>1️⃣ 上传您的原创作品</h3>
    <p>支持图片、视频、文档等多种格式</p>
    <h3 style="margin-top: 20px;">2️⃣ 生成DNA指纹</h3>
    <p>使用SHA-256算法生成唯一哈希值</p>
    <h3 style="margin-top: 20px;">3️⃣ 保存您的证明</h3>
    <p>妥善保存DNA哈希值作为原创证明</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<h2>⚙️ 技术规格</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>🔒 安全技术</h4>
        <ul style="color:#aaa; line-height: 2;">
            <li>SHA-256哈希算法</li>
            <li>环境变量加密</li>
            <li>零数据存储架构</li>
            <li>代码安全扫描（CodeQL）</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>🌐 区块链集成</h4>
        <ul style="color:#aaa; line-height: 2;">
            <li>Solana主网连接</li>
            <li>实时RPC验证</li>
            <li>去中心化存储</li>
            <li>智能合约支持</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 50px;'>
    <p style="font-size: 18px;">🛡️ OriginGuard V6.1 | 100% Secure | 24/7 Protection</p>
    <p style="font-size: 14px; color: #888;">Powered by Solana Blockchain | Zero Data Storage Architecture</p>
</div>
""", unsafe_allow_html=True)
