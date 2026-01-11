import streamlit as st
import time

# --- 1. 基础设置 ---
st.set_page_config(
    page_title="OriginGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed" # 默认收起侧边栏，因为我们把功能放到了主屏
)

# --- 2. 语言包字典 (严格区分) ---
translations = {
    "English": {
        "nav_home": "Home", "nav_dash": "Console",
        "hero_title": "Protect What You Create.",
        "hero_sub": "The world's first AI-Powered Copyright Protection Platform.",
        "btn_start": "Launch Console",
        "kpi_1": "Protected Assets", "kpi_2": "Threats Blocked", "kpi_3": "Legal Savings",
        "upload_title": "Secure Upload (Encrypted)",
        "footer": "© 2026 OriginGuard Inc. | SOC2 Certified | GDPR Compliant"
    },
    "中文": {
        "nav_home": "首页", "nav_dash": "控制台",
        "hero_title": "不仅是保护，更是确权。",
        "hero_sub": "全球首个 AI 驱动的去中心化版权保护平台。",
        "btn_start": "进入控制台",
        "kpi_1": "已保护资产", "kpi_2": "已拦截威胁", "kpi_3": "节省律师费",
        "upload_title": "安全上传 (端到端加密)",
        "footer": "© 2026 OriginGuard Inc. | SOC2 安全认证 | 符合 GDPR 标准"
    }
}

# ==========================================
# 3. 顶部导航栏 (最显眼的地方)
# ==========================================
# 我们用两列布局：左边是 Logo，右边是语言切换
col_logo, col_lang = st.columns([5, 1])

with col_logo:
    # 大标题
    st.title("🛡️ OriginGuard Enterprise")

with col_lang:
    # --- 语言切换器在这里！(Top Right) ---
    # 使用 horizontal=True 让它横着排，更像现代 APP
    lang = st.radio("🌐 Language / 语言", ["English", "中文"], horizontal=True)

# 获取当前语言的文本
t = translations[lang]

st.markdown("---")

# ==========================================
# 4. 核心功能区 (直接展示，不再藏着掖着)
# ==========================================

# 简单的标签页导航
tab_home, tab_console = st.tabs([f"🏠 {t['nav_home']}", f"📊 {t['nav_dash']}"])

# --- 首页 (Home) ---
with tab_home:
    st.markdown(f"## {t['hero_title']}")
    st.caption(f"{t['hero_sub']}")
    
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b", caption="Global Threat Monitoring Center", use_container_width=True)
    
    if st.button(f"🚀 {t['btn_start']}", type="primary"):
        st.toast("Access Granted!", icon="✅")
        st.info("Please switch to the 'Console' tab above.")

# --- 控制台 (Console) ---
with tab_console:
    st.markdown(f"### CEO Dashboard ({lang})")
    
    # 关键数据
    k1, k2, k3 = st.columns(3)
    k1.metric(t['kpi_1'], "1,248", "+12")
    k2.metric(t['kpi_2'], "53", "High", delta_color="inverse")
    k3.metric(t['kpi_3'], "$12,400", "+5%")
    
    st.markdown("---")
    
    # 上传功能
    st.subheader(t['upload_title'])
    uploaded = st.file_uploader("Drop Files Here / 拖拽文件至此")
    
    if uploaded:
        with st.spinner("Encrypting..."):
            time.sleep(1)
        st.success("✅ Blockchain Certificate Minted!")

# ==========================================
# 5. 底部版权
# ==========================================
st.markdown("---")
st.caption(t['footer'])
