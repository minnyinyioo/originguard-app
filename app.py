import streamlit as st
import time

# ==========================================
# 1. 页面基础配置 (必须第一行)
# ==========================================
st.set_page_config(
    page_title="OriginGuard - Web3 Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. 核心：注入 Web3 动态灵魂 (CSS & 动画)
# ==========================================
# 这里是魔法发生的地方：深色模式、动态背景、霓虹光影、毛玻璃特效
st.markdown("""
<style>
    /* 引入现代科技字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

    /* 全局强制深色主题与背景 */
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
        background-image: url("https://i.imgur.com/MxK3F6t.gif"); /* 动态区块链网络背景图 */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }
    
    /* 给背景加一个暗色遮罩，让文字更清晰 */
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.7); /* 70% 黑色透明遮罩 */
        z-index: 0;
    }
    
    /* 让所有内容浮在遮罩之上 */
    [data-testid="stHeader"], [data-testid="block-container"] {
        z-index: 1;
        position: relative;
        background: transparent;
    }

    /* --- 自定义组件样式 --- */

    /* 1. 渐变大标题文本 */
    .gradient-text {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        background: linear-gradient(135deg, #00C6FF 0%, #0072FF 50%, #9D50BB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    /* 2. 毛玻璃卡片 (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* 3. 霓虹按钮 */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #00C6FF, #0072FF);
        color: white; border: none; padding: 0.75rem 1.5rem;
        font-weight: 700; letter-spacing: 1px;
        border-radius: 8px;
        box-shadow: 0 0 15px rgba(0, 198, 255, 0.5);
        transition: all 0.3s;
    }
    div.stButton > button[kind="primary"]:hover {
        box-shadow: 0 0 30px rgba(0, 198, 255, 0.8);
        transform: scale(1.05);
    }

    /* 4. KPI 指标样式优化 */
    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        color: #00C6FF !important;
        text-shadow: 0 0 10px rgba(0, 198, 255, 0.5);
    }
    [data-testid="stMetricLabel"] { color: #a1a1aa; }

    /* 5. 语言选择器和 Tab 美化 */
    [data-testid="stRadio"] > div {
        background: rgba(255,255,255,0.1);
        padding: 5px; border-radius: 8px;
    }
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    .stTabs [data-baseweb="tab"] { color: #a1a1aa; }
    .stTabs [aria-selected="true"] {
        background: rgba(255,255,255,0.1) !important;
        color: #00C6FF !important;
        border-radius: 8px 8px 0 0;
    }

    /* 隐藏掉不必要的 Streamlit 元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 语言包字典
# ==========================================
translations = {
    "English": {
        "nav_home": "HUB", "nav_dash": "CONSOLE",
        "hero_title": "Protect What You Create.",
        "hero_sub": "The world's first AI-Powered, Blockchain-Backed Copyright Defense System.",
        "btn_start": "INITIALIZE SYSTEM 🚀",
        "trust_title": "TRUSTED BY ENTERPRISES GLOBALLY",
        "kpi_1": "SECURED ASSETS", "kpi_2": "THREATS NEUTRALIZED", "kpi_3": "LEGAL SAVINGS",
        "upload_title": "ENCRYPTED UPLOAD CHANNEL",
        "footer": "© 2026 ORIGINGUARD INC. | SOC2 TYPE II | GDPR READY | SOLANA MAINNET"
    },
    "中文": {
        "nav_home": "枢纽中心", "nav_dash": "控制台",
        "hero_title": "捍卫你的数字疆土。",
        "hero_sub": "全球首个 AI 驱动、区块链存证的去中心化版权防御系统。",
        "btn_start": "初始化系统 🚀",
        "trust_title": "全球企业的信赖之选",
        "kpi_1": "已确权资产", "kpi_2": "已瓦解威胁", "kpi_3": "节省法务成本",
        "upload_title": "加密上传通道",
        "footer": "© 2026 ORIGINGUARD INC. | SOC2 TYPE II 认证 | 符合 GDPR | Solana 主网"
    }
}

# ==========================================
# 4. 页面布局
# ==========================================

# --- 顶部导航栏 ---
col_logo, col_lang = st.columns([6, 1])
with col_logo:
    # 使用 HTML 渲染带 Logo 的渐变标题
    st.markdown("""
        <h1>
            <span style='font-size:40px;'>🛡️</span> 
            <span class='gradient-text' style='font-size:40px;'>ORIGIN GUARD</span>
        </h1>
    """, unsafe_allow_html=True)
with col_lang:
    # 语言切换器 (保持清晰可见)
    lang = st.radio("🌐 LANGUAGE", ["English", "中文"], horizontal=True, label_visibility="collapsed")

t = translations[lang]

st.markdown("---")

# --- 核心 Tab 导航 ---
tab_home, tab_console = st.tabs([f"🌐 {t['nav_home']}", f"🖥️ {t['nav_dash']}"])

# ==========================================
# 5. 首页 (Web3 动态展示区)
# ==========================================
with tab_home:
    # 巨大的 Hero 区域
    st.markdown(f"""
    <div style="text-align: center; padding: 80px 20px;">
        <h1 class="gradient-text" style="font-size: 72px; letter-spacing: -2px; line-height: 1.1;">
            {t['hero_title']}
        </h1>
        <p style="font-size: 24px; color: #a1a1aa; max-width: 800px; margin: 30px auto; font-family: 'JetBrains Mono', monospace;">
            >> {t['hero_sub']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 居中的霓虹启动按钮
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(t['btn_start'], type="primary", use_container_width=True):
            with st.spinner("Establishing Secure Connection to Solana Node..."):
                time.sleep(2)
            st.toast("System Online. Access Console.", icon="🟢")

    st.markdown("<br><br><br>", unsafe_allow_html=True) # Spacer

    # 信任背书 (使用毛玻璃卡片)
    st.markdown(f"<h4 style='text-align:center; color:#a1a1aa; letter-spacing:2px;'>{t['trust_title']}</h4>", unsafe_allow_html=True)
    
    trust1, trust2, trust3, trust4 = st.columns(4)
    with trust1:
        st.markdown("""<div class="glass-card" style="text-align:center;">🔒 SOC2 <br>Certified</div>""", unsafe_allow_html=True)
    with trust2:
        st.markdown("""<div class="glass-card" style="text-align:center;">🇪🇺 GDPR <br>Compliant</div>""", unsafe_allow_html=True)
    with trust3:
        st.markdown("""<div class="glass-card" style="text-align:center;">⛓️ Solana <br>Mainnet</div>""", unsafe_allow_html=True)
    with trust4:
        st.markdown("""<div class="glass-card" style="text-align:center;">⚖️ DMCA <br>Verified</div>""", unsafe_allow_html=True)

# ==========================================
# 6. 控制台 (专业数据区)
# ==========================================
with tab_console:
    st.markdown(f"### 📊 EXECUTIVE DASHBOARD [{lang}]")
    st.caption("Network Status: 🟢 Connected | Latency: 24ms")
    
    # 关键指标 (会自动应用上面的霓虹样式)
    k1, k2, k3 = st.columns(3)
    k1.metric(t['kpi_1'], "1,248,920", "Live")
    k2.metric(t['kpi_2'], "53,401", "High Alert", delta_color="inverse")
    k3.metric(t['kpi_3'], "$1.2M+", "+15%")
    
    st.markdown("---")
    
    # 上传功能 (包裹在毛玻璃卡片中)
    st.markdown(f"""<div class="glass-card"><h4>📤 {t['upload_title']}</h4></div>""", unsafe_allow_html=True)
    uploaded = st.file_uploader("", label_visibility="collapsed")
    
    if uploaded:
        with st.status("Processing Asset...", expanded=True):
            st.write("Generationg Zero-Knowledge Proof...")
            time.sleep(1)
            st.write("Hashing to Blockchain...")
            time.sleep(1)
        st.success("✅ Asset Secured on-chain!")

# ==========================================
# 7. 底部
# ==========================================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #52525b; font-size: 12px; margin-top: 50px; font-family: 'JetBrains Mono', monospace;">
    {t['footer']}
</div>
""", unsafe_allow_html=True)
