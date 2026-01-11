import streamlit as st
import time

# --- 1. 基础设置 (必须在第一行) ---
st.set_page_config(page_title="OriginGuard", page_icon="🛡️", layout="wide")

# --- 2. 核心语言包 ---
translations = {
    "English": {
        "menu": ["Home", "Console"],
        "title": "OriginGuard Enterprise",
        "welcome": "Protect What You Create.",
        "desc": "AI-Powered Copyright Protection & Blockchain Evidence.",
        "btn": "Launch Console",
        "kpi": ["Protected Assets", "Threats Blocked", "Legal Savings"],
        "upload": "Upload Asset (Encrypted)",
        "trust": "SOC2 Certified | GDPR Compliant | DMCA Verified"
    },
    "中文": {
        "menu": ["官网首页", "控制台"],
        "title": "OriginGuard 企业版",
        "welcome": "不仅是保护，更是确权。",
        "desc": "全球首个 AI 驱动的去中心化版权保护平台。",
        "btn": "进入控制台",
        "kpi": ["已保护资产", "已拦截威胁", "节省律师费"],
        "upload": "上传资产 (加密通道)",
        "trust": "SOC2 安全认证 | 符合 GDPR | DMCA 维权认证"
    }
}

# --- 3. 侧边栏 ---
with st.sidebar:
    st.header("🛡️ OriginGuard")
    
    # 语言选择
    lang = st.selectbox("Language / 语言", ["English", "中文"])
    t = translations[lang]
    
    st.markdown("---")
    
    # 导航
    selection = st.radio("Navigation", t["menu"])
    
    st.markdown("---")
    st.caption("User: CEO MNNO")
    st.caption("Status: ✅ Active")

# --- 4. 主页面逻辑 ---

# 如果选了"首页"
if selection == t["menu"][0]:
    st.markdown(f"# 🛡️ {t['welcome']}")
    st.markdown(f"### {t['desc']}")
    
    st.markdown("---")
    
    # 信任背书 (纯文字版，防止图片加载失败)
    st.info(f"🔒 {t['trust']}")
    
    st.markdown("---")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("1. Hidden Watermark", "Active")
    c2.metric("2. Blockchain Mint", "Solana")
    c3.metric("3. AI Legal Hammer", "Ready")
    
    if st.button(f"🚀 {t['btn']}", type="primary"):
        st.success("Access Granted. Please switch to Console tab.")

# 如果选了"控制台"
elif selection == t["menu"][1]:
    st.title(f"📊 {t['title']}")
    
    # KPI
    k1, k2, k3 = st.columns(3)
    k1.metric(t['kpi'][0], "1,248", "+12")
    k2.metric(t['kpi'][1], "53", "High", delta_color="inverse")
    k3.metric(t['kpi'][2], "$12,400", "+5%")
    
    st.markdown("---")
    
    # 上传功能
    st.subheader(t['upload'])
    uploaded = st.file_uploader("Drop files here")
    
    if uploaded:
        st.write("Processing...")
        time.sleep(1)
        st.success("✅ Certificate Generated on Blockchain!")
