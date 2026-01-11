import streamlit as st
import pandas as pd
import time

# --- 1. 全局配置 (必须在第一行) ---
st.set_page_config(
    page_title="OriginGuard - Digital Asset Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. 页面路由逻辑 ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def enter_dashboard():
    st.session_state.page = 'dashboard'

def go_home():
    st.session_state.page = 'landing'

# ==================================================
# 3. 官网落地页 (Landing Page)
# ==================================================
if st.session_state.page == 'landing':
    
    # 顶部导航栏
    c1, c2 = st.columns([1, 6])
    with c1:
        st.write("### 🛡️ OriginGuard")
    st.markdown("---")

    # 主视觉区域 (Hero Section)
    st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 50px; font-weight: 800; background: -webkit-linear-gradient(45deg, #007CF0, #00DFD8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Protect What You Create.
        </h1>
        <p style="font-size: 20px; color: #666; max-width: 700px; margin: 0 auto;">
            The world's first AI-Powered copyright protection platform.
            <br>Stop theft before it happens.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # 空行占位
    
    # 巨大的启动按钮
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 LAUNCH ENTERPRISE CONSOLE (启动控制台)", use_container_width=True, type="primary"):
            enter_dashboard()
            st.rerun()

    st.markdown("---")

    # 核心技术展示
    st.subheader("💡 Core Technology")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("👁️ Invisible Watermark")
        st.caption("AI-embedded DNA survives compression.")
    with c2:
        st.info("⛓️ Blockchain Evidence")
        st.caption("Immutable ownership certificates on Solana.")
    with c3:
        st.info("⚖️ AI Legal Hammer")
        st.caption("Automated DMCA takedowns sent instantly.")

    st.markdown("<br><br><div style='text-align:center; color:gray; font-size:12px;'>© 2026 OriginGuard Solutions.</div>", unsafe_allow_html=True)


# ==================================================
# 4. 企业仪表盘 (Dashboard)
# ==================================================
elif st.session_state.page == 'dashboard':
    
    # 侧边栏
    with st.sidebar:
        st.title("🛡️ Console")
        st.write("👤 **MNNO (CEO)**")
        st.success("🟢 System Online")
        st.markdown("---")
        if st.button("⬅️ Log Out"):
            go_home()
            st.rerun()

    # 仪表盘顶部数据
    st.title("📊 Enterprise Dashboard")
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Protected Assets", "1,248", "+12")
    kpi2.metric("Threats Blocked", "53", "High Alert", delta_color="inverse")
    kpi3.metric("Legal Actions", "41", "+3")
    kpi4.metric("Cost Saved", "$12,400")

    st.markdown("---")

    # 功能选项卡
    tab1, tab2, tab3 = st.tabs(["🛡️ Protect (保护)", "🌍 Map (监控)", "⚖️ Legal (法务)"])

    with tab1:
        st.write("### Upload Master File")
        uploaded = st.file_uploader("Drag and drop to encrypt", type=['png', 'jpg'])
        if uploaded:
            st.success("File Encrypted & Hashed on Blockchain!")
    
    with tab2:
        st.write("### Live Threat Map")
        data = pd.DataFrame({'lat': [13.7563, 16.8409], 'lon': [100.5018, 96.1735]})
        st.map(data)

    with tab3:
        st.write("### Enforcement Center")
        st.text_input("Infringing URL (Facebook/TikTok)")
        st.button("🚀 Send Legal Notice")

    st.caption("OriginGuard Enterprise System v2.1")
