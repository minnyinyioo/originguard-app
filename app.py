import streamlit as st
import pandas as pd
import time

# --- 全局页面设置 ---
st.set_page_config(
    page_title="OriginGuard - Digital Asset Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 会话状态管理 (用来控制是看官网还是看后台) ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def enter_dashboard():
    st.session_state.page = 'dashboard'

def go_home():
    st.session_state.page = 'landing'

# ==================================================
# 1. 官网落地页 (Landing Page) - 回答"我们是谁"
# ==================================================
if st.session_state.page == 'landing':
    
    # --- 顶部导航 ---
    col1, col2 = st.columns([1, 5])
    with col1:
        st.write("## 🛡️ OriginGuard")
    with col2:
        st.write("") # Spacer

    st.markdown("---")

    # --- Hero Section (主视觉区) ---
    # 这里回答：我们是干什么的？
    st.markdown("""
    <div style="text-align: center; padding: 50px 0;">
        <h1 style="font-size: 60px; font-weight: 800; background: -webkit-linear-gradient(45deg, #007CF0, #00DFD8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Protect What You Create.
        </h1>
        <p style="font-size: 24px; color: #666; max-width: 800px; margin: 0 auto;">
            The world's first <b>AI-Powered</b> copyright protection platform backed by <b>Blockchain Immutability</b>.
            <br>Stop theft before it happens.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # --- 巨大的启动按钮 ---
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("🚀 LAUNCH ENTERPRISE CONSOLE\n(进入企业控制台)", use_container_width=True, type="primary"):
            enter_dashboard()
            st.rerun()

    st.markdown("---")

    # --- Feature Section (核心技术) ---
    # 这里回答：通过什么技术运行？
    st.subheader("💡 Core Technology (核心技术)")
    
    f1, f2, f3 = st.columns(3)
    
    with f1:
        st.markdown("### 👁️ Invisible Watermark")
        st.info("隐形水印技术")
        st.write("Our AI embeds a hidden 'DNA' into your images. It survives compression, cropping, and screenshots. Even if they steal it, we can prove it's yours.")
    
    with f2:
        st.markdown("### ⛓️ Blockchain Evidence")
        st.info("区块链存证")
        st.write("Every asset is hashed and minted on the **Solana Blockchain**. This creates an immutable, court-admissible certificate of ownership.")
    
    with f3:
        st.markdown("### ⚖️ AI Legal Hammer")
        st.info("AI 自动维权")
        st.write("Detected a theft? Our AI generates and sends DMCA Takedown Notices to Facebook/TikTok legal departments instantly.")

    st.markdown("---")

    # --- Why Us Section (信任背书) ---
    # 这里回答：为什么选我们？
    st.subheader("🏆 Why OriginGuard?")
    
    w1, w2, w3, w4 = st.columns(4)
    with w1:
        st.metric(label="Protection Speed", value="0.5s", delta="Real-time")
    with w2:
        st.metric(label="Cost Savings", value="90%", delta="vs Lawyers")
    with w3:
        st.metric(label="Success Rate", value="99.9%", delta="Blockchain Verified")
    with w4:
        st.metric(label="Global Coverage", value="180+", delta="Countries")

    # --- 底部 ---
    st.markdown("<br><br><div style='text-align:center; color:gray; font-size:12px;'>© 2026 OriginGuard Solutions. Built for the Creator Economy.</div>", unsafe_allow_html=True)


# ==================================================
# 2. 企业仪表盘 (Dashboard) - 真正的功能区
# ==================================================
elif st.session_state.page == 'dashboard':
    
    # 侧边栏
    with st.sidebar:
        st.title("🛡️ Console")
        st.write("**User:** MNNO (CEO)")
        st.markdown("---")
        if st.button("⬅️ Log Out"):
            go_home()
            st.rerun()
    
    # 仪表盘主内容 (这就是刚才那个专业的界面)
    st.markdown("## 📊 Enterprise Dashboard")
    st.markdown("**Status:** 🟢 System Operational | **Network:** Solana Mainnet")
    
    # 关键数据卡片
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Protected Assets", "1,248")
    col2.metric("Violations Found", "53", "High Alert", delta_color="inverse")
    col3.metric("Legal Actions Sent", "41")
    col4.metric("Money Saved", "$12,400")

    st.markdown("---")

    # 功能区
    tab1, tab2, tab3 = st.tabs(["🛡️ Protect (保护)", "🔍 Monitor (监控)", "⚖️ Enforce (维权)"])
    
    with tab1:
        st.write("### Upload Assets for Encryption")
        st.file_uploader("Upload Image", type=['png', 'jpg'])
        st.button("Encrypt & Mint Certificate")
        
    with tab2:
        st.write("### Global Threat Map")
        st.map(pd.DataFrame({'lat': [13.7563, 16.8409], 'lon': [100.5018, 96.1735]}))
        
    with tab3:
        st.write("### AI Legal Department")
        st.text_input("Paste Infringing URL")
        st.button("🚀 Fire Legal Hammer")
