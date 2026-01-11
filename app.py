import streamlit as st
import pandas as pd

# ==========================================
# 1. 核心配置与 Web3 皮肤 (Core Config & Style)
# ==========================================
st.set_page_config(
    page_title="OriginGuard Web3",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 注入 CSS：Web3 深色主题 + 缅甸字体支持 + 高对比度文字
# 特别增加了针对 Warning/Error 提示框的样式优化，使其符合 Cyberpunk 风格
st.markdown("""
<style>
    /* 引入 Google Noto Sans Myanmar 字体，解决乱码 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 全局背景：深空灰蓝 Web3 渐变 */
    .stApp {
        background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
        font-family: 'Inter', 'Noto Sans Myanmar', sans-serif;
        color: #e2e8f0;
    }

    /* 标题高亮：青色渐变 */
    h1, h2, h3 {
        background: -webkit-linear-gradient(45deg, #22d3ee, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }
    
    /* 侧边栏样式 */
    section[data-testid="stSidebar"] {
        background-color: #0b1121;
        border-right: 1px solid #1e293b;
    }
    
    /* 按钮：Web3 霓虹蓝 */
    div.stButton > button {
        background: linear-gradient(90deg, #0ea5e9 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        box-shadow: 0 0 10px rgba(14, 165, 233, 0.3);
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.6);
        color: #fff;
    }

    /* 法律条款警示框样式重写 */
    div[data-testid="stNotification"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        color: #f8fafc;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 语言字典库 (The Translation Matrix)
# ==========================================
# 包含了新增的法律条款翻译
TRANS = {
    "English": {
        "slogan": "Protect What You Create.",
        "sub_slogan": "Web3 Copyright Protection | AI Watermarking | Blockchain Evidence",
        "btn_launch": "🚀 LAUNCH CONSOLE",
        "core_tech": "Core Technology",
        "tech_1_t": "Invisible Watermark",
        "tech_1_d": "AI-embedded DNA in pixels.",
        "tech_2_t": "Blockchain Proof",
        "tech_2_d": "Immutable Solana Certificates.",
        "tech_3_t": "AI Legal Hammer",
        "tech_3_d": "Auto-send DMCA notices.",
        "dash_title": "Security Dashboard",
        "sidebar_title": "Console",
        "role": "CEO / Admin",
        "status": "🟢 System Online",
        "btn_logout": "⬅️ Log Out",
        "btn_legal": "⚖️ Legal Center", 
        "btn_back_dash": "⬅️ Back to Dashboard",
        "legal_page_title": "Legal Shield & Compliance",
        "policy_refund_t": "🚫 No-Refund Policy (Blockchain Immutable)",
        "policy_refund_d": "Once a certificate is minted on the Solana Blockchain, the transaction creates a permanent, irreversible record. Gas fees are paid instantly to the network. Therefore, OriginGuard cannot offer refunds or cancellations once protection is activated. All sales are final.",
        "policy_sla_t": "⚡ Service Level Agreement (SLA)",
        "policy_sla_d": "For Enterprise subscribers, we guarantee 99.9% API uptime. In the event of downtime exceeding 1 hour, users will be compensated with service credits.",
        "policy_privacy_t": "🔒 Privacy & Data Sovereignty",
        "policy_privacy_d": "We do not sell, trade, or rent your personal identification information. Master files are encrypted locally before hashing. You own your data.",
        "footer": "© 2026 OriginGuard Solutions. All rights reserved."
    },
    "中文": {
        "slogan": "捍卫你的数字资产",
        "sub_slogan": "Web3 版权保护 | AI 隐形水印 | 区块链存证",
        "btn_launch": "🚀 启动控制台",
        "core_tech": "核心技术矩阵",
        "tech_1_t": "隐形水印",
        "tech_1_d": "像素级 AI 植入，肉眼不可见。",
        "tech_2_t": "区块链存证",
        "tech_2_d": "Solana 链上永久确权证书。",
        "tech_3_t": "AI 法律重锤",
        "tech_3_d": "自动发送跨国律师函。",
        "dash_title": "安全控制台",
        "sidebar_title": "管理中心",
        "role": "CEO / 管理员",
        "status": "🟢 系统运行中",
        "btn_logout": "⬅️ 退出登录",
        "btn_legal": "⚖️ 法务中心",
        "btn_back_dash": "⬅️ 返回控制台",
        "legal_page_title": "法律护盾与合规中心",
        "policy_refund_t": "🚫 无退款政策 (区块链不可篡改)",
        "policy_refund_d": "一旦证书在 Solana 区块链上铸造完成，该交易即生成永久且不可逆的记录。Gas 费已实时支付给网络节点。因此，OriginGuard 无法对已激活的保护
