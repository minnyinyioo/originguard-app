import streamlit as st
import pandas as pd
import time

# --- 1. 全局配置 ---
st.set_page_config(
    page_title="OriginGuard Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. 注入“暗物质”CSS样式 (修复背景问题) ---
st.markdown("""
<style>
    /* 全局背景：深邃黑蓝渐变 */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #020617 100%);
        color: white;
    }
    
    /* 标题样式 */
    h1 {
        color: #ffffff !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* 按钮样式优化 */
    div.stButton > button {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    }
    
    /* 卡片背景 */
    div[data-testid="stMetricValue"] {
        color: #60a5fa !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 页面路由 ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def enter_dashboard():
    st.session_state.page = 'dashboard'

def go_home():
    st.session_state.page = 'landing'

# ==================================================
# 4. 官网落地页 (Landing Page)
# ==================================================
if st.session_state.page == 'landing':
    
    # 顶部
    c1, c2 = st.columns([1, 6])
    with c1:
        st.markdown("### 🛡️ OriginGuard")
    st.markdown("---")

    # 主视觉 (纯文字排版，无图更高级)
    st.markdown("""
    <div style="text-align: center; padding: 60px 0;">
        <h1 style="font-size: 56px; font-weight: 900; letter-spacing: -1px; margin-bottom: 20px;">
            <span style="background: -webkit-linear-gradient(45deg, #60a5fa, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Guard Your Creation.
            </span>
        </h1>
        <p style="font-size: 20px; color: #94a3b8; max-width: 700px; margin: 0 auto; line-height: 1.6;">
            Enterprise-grade copyright protection powered by 
            <span style="color:white; font-weight:bold;">Invisible AI Watermarking</span> 
            and <span style="color:white; font-weight:bold;">Solana Blockchain</span>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") 
    
    # 启动按钮
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 ACCESS CONSOLE (启动控制台)", use_container_width=True):
            enter_dashboard()
            st.rerun()

    st.markdown("---")

    # 核心能力
    st.markdown("<h3 style='text-align:center; color:#e2e8f0; margin-bottom:30px;'>Core Defense Matrix</h3>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 👁️ Stealth ID")
        st.info("AI 隐形水印植入")
        st.caption("Embeds invisible ownership data into pixels.")
    with c2:
        st.markdown("#### ⛓️ On-Chain Proof")
        st.info("Solana 链上存证")
        st.caption("Immutable timestamped certificates.")
    with c3:
        st.markdown("#### ⚡ Auto-Strike")
        st.info("自动法务打击")
        st.caption("Instant DMCA notices to platforms.")

    st.markdown("<br><br><div style='text-align:center; color:#475569; font-size:12px;'>© 2026 OriginGuard Solutions Inc. | Nonthaburi HQ</div>", unsafe_allow_html=True)


# ==================================================
# 5. 企业仪表盘 (Dashboard)
# ==================================================
elif st.session_state.page == 'dashboard':
    
    with st.sidebar:
        st.title("🛡️ Console")
        st.write("👤 **CEO: MNNO**")
        st.success("🟢 System Online")
        st.markdown("---")
        if st.button("⬅️ Log Out"):
            go_home()
            st.rerun()

    st.title("📊 Security Dashboard")
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Assets Secured", "1,248")
    kpi2.metric("Threats Detected", "53", "High", delta_color="inverse")
    kpi3.metric("Legal Notices", "41")
    kpi4.metric("Est. Value Saved", "$12,400")

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📂 Upload (上传)", "🌍 Monitor (监控)", "⚖️ Legal (法务)"])

    with tab1:
        st.subheader("Asset Encryption")
        st.file_uploader("Upload Master File (JPG/PNG)", type=['png', 'jpg'])
        st.button("🔒 Encrypt & Mint")
    
    with tab2:
        st.subheader("Global Threat Map")
        st.map(pd.DataFrame({'lat': [13.7563, 16.8409], 'lon': [100.5018, 96.1735]}))

    with tab3:
        st.subheader("Enforcement Actions")
        st.text_input("Infringing URL")
        st.button("🚀 Send DMCA Notice")
