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
