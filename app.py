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
st.markdown("""
<style>
    /* 引入 Google Noto Sans Myanmar 字体，解决乱码 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 全局背景：深空灰蓝 Web3 渐变 */
    .stApp {
        background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
        font-family: 'Inter', 'Noto Sans Myanmar', sans-serif; /* 优先使用缅文适配字体 */
        color: #e2e8f0; /* 亮灰白文字，确保看得清 */
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

    /* 数据卡片背景 */
    div[data-testid="stMetricValue"] {
        color: #38bdf8 !important; /* 青蓝色数字 */
    }
    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important; /* 浅灰标签 */
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 语言字典库 (The Translation Matrix)
# ==========================================
# 这里定义了所有界面文字，确保 100% 语言隔离
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
        "kpi_1": "Protected Assets",
        "kpi_2": "Threats Blocked",
        "kpi_3": "Legal Actions",
        "kpi_4": "Cost Saved",
        "tab_1": "🛡️ Protect",
        "tab_2": "🌍 Map",
        "tab_3": "⚖️ Legal",
        "upload_title": "Asset Encryption",
        "upload_btn": "🔒 Encrypt & Mint",
        "map_title": "Global Threat Map",
        "legal_title": "Enforcement Actions",
        "legal_input": "Infringing URL",
        "legal_btn": "🚀 Send Notice",
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
        "kpi_1": "已保护资产",
        "kpi_2": "拦截威胁",
        "kpi_3": "维权行动",
        "kpi_4": "节省成本",
        "tab_1": "🛡️ 确权保护",
        "tab_2": "🌍 全球监控",
        "tab_3": "⚖️ 法律打击",
        "upload_title": "资产加密上传",
        "upload_btn": "🔒 加密并铸造证书",
        "map_title": "全球威胁态势图",
        "legal_title": "维权执行中心",
        "legal_input": "输入侵权链接 (URL)",
        "legal_btn": "🚀 发送律师函",
        "footer": "© 2026 OriginGuard Solutions. 版权所有。"
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး | AI နည်းပညာ | Blockchain သက်သေ",
        "btn_launch": "🚀 စနစ်စတင်မည်",
        "core_tech": "အဓိက နည်းပညာများ",
        "tech_1_t": "မမြင်ရသော ရေစာ",
        "tech_1_d": "AI နည်းပညာဖြင့် ပုံရိပ်ထဲတွင် မြှုပ်နှံထားသည်။",
        "tech_2_t": "Blockchain သက်သေ",
        "tech_2_d": "Solana ပေါ်တွင် ဖျက်၍မရသော မှတ်တမ်း။",
        "tech_3_t": "AI ဥပဒေ လက်နက်",
        "tech_3_d": "DMCA တိုင်ကြားစာ အလိုအလျောက် ပေးပို့ခြင်း။",
        "dash_title": "လုံခြုံရေး ဒက်ရှ်ဘုတ်",
        "sidebar_title": "ထိန်းချုပ်ခန်း",
        "role": "CEO / အက်ဒမင်",
        "status": "🟢 စနစ် အလုပ်လုပ်နေသည်",
        "btn_logout": "⬅️ ထွက်မည်",
        "kpi_1": "ကာကွယ်ထားသော ပိုင်ဆိုင်မှု",
        "kpi_2": "တားဆီးထားသော ခြိမ်းခြောက်မှု",
        "kpi_3": "ဥပဒေအရ အရေးယူမှု",
        "kpi_4": "သက်သာသော ကုန်ကျစရိတ်",
        "tab_1": "🛡️ ကာကွယ်ရန်",
        "tab_2": "🌍 မြေပုံ",
        "tab_3": "⚖️ ဥပဒေ",
        "upload_title": "ဖိုင်တင်ရန်",
        "upload_btn": "🔒 မှတ်ပုံတင်မည်",
        "map_title": "ကမ္ဘာလုံးဆိုင်ရာ ခြိမ်းခြောက်မှု မြေပုံ",
        "legal_title": "ဥပဒေ အရေးယူ ဆောင်ရွက်ချက်များ",
        "legal_input": "လင့်ခ် ထည့်ပါ (URL)",
        "legal_btn": "🚀 တိုင်ကြားစာ ပို့မည်",
        "footer": "© 2026 OriginGuard Solutions. မူပိုင်ခွင့် ရယူထားသည်။"
    }
}

# ==========================================
# 3. 语言选择逻辑 (Language Switcher)
# ==========================================
# 在侧边栏放置语言选择器，默认中文
lang_choice = st.sidebar.selectbox(
    "🌐 Language / ဘာသာစကား / 语言",
    ["English", "中文", "Myanmar"],
    index=1 # 默认选中中文
)

# 获取当前语言的字典
T = TRANS[lang_choice]

# ==========================================
# 4. 页面路由与渲染 (Page Rendering)
# ==========================================
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def enter_dashboard():
    st.session_state.page = 'dashboard'

def go_home():
    st.session_state.page = 'landing'

# --- 落地页 (Landing Page) ---
if st.session_state.page == 'landing':
    
    st.write("")
    st.write("")
    
    # 标题区
    st.markdown(f"""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 56px; margin-bottom: 20px;">
            {T['slogan']}
        </h1>
        <p style="font-size: 20px; color: #94a3b8; max-width: 800px; margin: 0 auto;">
            {T['sub_slogan']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")

    # 启动按钮
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(T['btn_launch'], use_container_width=True):
            enter_dashboard()
            st.rerun()

    st.markdown("---")

    # 核心技术区
    st.subheader(T['core_tech'])
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info(T['tech_1_t'])
        st.caption(T['tech_1_d'])
    with c2:
        st.info(T['tech_2_t'])
        st.caption(T['tech_2_d'])
    with c3:
        st.info(T['tech_3_t'])
        st.caption(T['tech_3_d'])
        
    st.markdown("---")
    st.caption(T['footer'])

# --- 仪表盘 (Dashboard) ---
elif st.session_state.page == 'dashboard':
    
    # 侧边栏信息
    with st.sidebar:
        st.title(T['sidebar_title'])
        st.write(f"👤 **MNNO** ({T['role']})")
        st.success(T['status'])
        st.markdown("---")
        if st.button(T['btn_logout']):
            go_home()
            st.rerun()

    # 主标题
    st.title(T['dash_title'])
    
    # KPI 卡片
    k1, k2, k3, k4 = st.columns(4)
    k1.metric(T['kpi_1'], "1,248")
    k2.metric(T['kpi_2'], "53", "High", delta_color="inverse")
    k3.metric(T['kpi_3'], "41")
    k4.metric(T['kpi_4'], "$12,400")

    st.markdown("---")

    # 功能 Tabs
    tab1, tab2, tab3 = st.tabs([T['tab_1'], T['tab_2'], T['tab_3']])

    with tab1:
        st.subheader(T['upload_title'])
        st.file_uploader("JPG / PNG", type=['png', 'jpg'])
        st.button(T['upload_btn'])
    
    with tab2:
        st.subheader(T['map_title'])
        st.map(pd.DataFrame({'lat': [13.7563, 16.8409], 'lon': [100.5018, 96.1735]}))

    with tab3:
        st.subheader(T['legal_title'])
        st.text_input(T['legal_input'])
        st.button(T['legal_btn'])
