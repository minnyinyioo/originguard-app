import streamlit as st
import pandas as pd
import time

# --- 1. 企业级页面配置 (Enterprise Config) ---
st.set_page_config(
    page_title="OriginGuard Enterprise Console",
    page_icon="⚖️",
    layout="wide", # 开启宽屏模式，霸气
    initial_sidebar_state="expanded"
)

# --- 2. 侧边栏导航 (Professional Sidebar) ---
with st.sidebar:
    st.title("🛡️ OriginGuard")
    st.caption("Global Copyright Protection")
    st.markdown("---")
    
    # 模拟用户头像
    col1, col2 = st.columns([1, 4])
    with col1:
        st.write("👤")
    with col2:
        st.write("**MNNO (CEO)**")
        st.caption("Admin Access: Level 1")
    
    st.markdown("---")
    
    menu = st.radio(
        "WORKSTATION",
        ["Dashboard (仪表盘)", "Asset Protection (资产确权)", "Enforcement (维权行动)", "Legal Docs (法务中心)", "Settings (设置)"]
    )
    
    st.markdown("---")
    st.info("System Status: 🟢 Operational")
    st.caption("v2.0.1 Enterprise Build")

# --- 3. 主界面逻辑 ---

if menu == "Dashboard (仪表盘)":
    # 顶部欢迎语
    st.markdown("## 📊 Executive Overview")
    st.markdown("Welcome back, CEO. Here is the daily security briefing.")
    
    # 关键指标 (KPIs) - 这是一个专业公司该看的数据
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Protected Assets (已保护资产)", value="1,248", delta="+12 Today")
    with col2:
        st.metric(label="Infringements Detected (监测盗图)", value="53", delta="High Alert", delta_color="inverse")
    with col3:
        st.metric(label="Takedown Success (维权成功率)", value="94.8%", delta="+2.1%")
    with col4:
        st.metric(label="Pending Lawsuits (进行中案件)", value="3")

    st.markdown("---")

    # 图表区域
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("🌍 Global Threat Map (全球威胁监控)")
        # 模拟一个地图数据
        map_data = pd.DataFrame({
            'lat': [16.8409, 13.7563, 1.3521, 37.7749],
            'lon': [96.1735, 100.5018, 103.8198, -122.4194]
        })
        st.map(map_data, zoom=3)
        st.caption("Real-time monitoring nodes: Yangon, Bangkok, Singapore, San Francisco.")

    with c2:
        st.subheader("Recent Activity")
        st.success("✅ Certificate #OG-8829 minted on Solana.")
        st.warning("⚠️ Facebook violation detected (User: ID_992).")
        st.info("ℹ️ Legal Letter sent to TikTok Legal Dept.")
        st.success("✅ Payment received ($199.00 Enterprise Plan).")

elif menu == "Asset Protection (资产确权)":
    st.markdown("## 🛡️ Intellectual Property Vault")
    st.write("Upload high-fidelity assets for Invisible Watermarking & Blockchain Hashing.")
    
    # 专业上传区
    uploaded_file = st.file_uploader("Drop Master Files Here (RAW/JPG/PNG)", type=['png', 'jpg'])
    
    if uploaded_file:
        with st.spinner("Encrypting & Hashing..."):
            time.sleep(2)
        st.success("✅ Asset Secured. Blockchain Certificate Generated.")
        
        # 模拟证书预览
        st.info("🔗 Blockchain Hash: 0x71C...92A | Time: 2026-01-11 15:30:00 UTC")

elif menu == "Enforcement (维权行动)":
    st.markdown("## ⚖️ Legal Enforcement Unit")
    st.write("Automated DMCA Takedown & Cease and Desist Issuance.")
    
    url = st.text_input("Infringing URL (Facebook/TikTok Post Link)", placeholder="https://facebook.com/...")
    
    if st.button("🚀 Initiate Legal Strike"):
        if url:
            with st.status("Executing Legal Protocols..."):
                st.write("🔍 Scanning Target Content...")
                time.sleep(1)
                st.write("📝 Generating Legal Documents (v6.0)...")
                time.sleep(1)
                st.write("📧 Dispatching to Platform Legal Dept...")
                time.sleep(1)
                st.write("✅ Case ID #9921 Created.")
            st.success("Takedown Notice Sent Successfully.")
        else:
            st.error("Please provide a valid URL.")

elif menu == "Legal Docs (法务中心)":
    st.markdown("## 📂 Corporate Legal Documents")
    
    d1, d2 = st.columns(2)
    with d1:
        st.download_button("📥 Download Company Terms of Service", "TOS Content", "TOS.pdf")
    with d2:
        st.download_button("📥 Download Privacy Policy", "Privacy Content", "Privacy.pdf")
        
    st.info("All documents are compliant with international copyright laws (Berne Convention).")

# --- 底部版权 ---
st.markdown("---")
st.caption("© 2026 OriginGuard Solutions, Inc. | Enterprise Security Standard | Nonthaburi, Thailand HQ")
