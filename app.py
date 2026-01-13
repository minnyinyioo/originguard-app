# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import time
import random

# ==========================================
# 1. 核心配置与动态引擎 (Core Config & Dynamic Engine)
# ==========================================
st.set_page_config(
    page_title="OriginGuard Web3",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 🎨 CSS 动态注入：呼吸光效 + 悬浮反馈 ---
st.markdown("""
<style>
    /* 1. 字体库：Padauk (缅文首选) */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 2. 动态背景：流动的深海光影 (60秒循环一次) */
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp {
        background: linear-gradient(-45deg, #020617, #0f172a, #1e1b4b, #0f172a);
        background-size: 400% 400%;
        animation: gradientBG 60s ease infinite;
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
        color: #e2e8f0;
    }

    /* 3. 标题特效：全息渐变 + 呼吸感 */
    h1 {
        background: linear-gradient(90deg, #22d3ee, #818cf8, #c084fc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        letter-spacing: -1px;
        animation: gradientText 5s linear infinite;
    }
    @keyframes gradientText {
        0% {background-position: 0% center;}
        100% {background-position: 200% center;}
    }

    /* 4. 卡片悬浮特效：鼠标放上去会浮起 + 发光 */
    div[data-testid="stMetric"], div.stInfo, div.stWarning, div.stError, div.stSuccess {
        background-color: rgba(30, 41, 59, 0.5); /* 半透明玻璃态 */
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s ease;
    }
    div[data-testid="stMetric"]:hover, div.stInfo:hover {
        transform: translateY(-5px); /* 上浮 */
        border-color: #22d3ee; /* 变亮 */
        box-shadow: 0 10px 30px -10px rgba(34, 211, 238, 0.3);
    }

    /* 5. 按钮：脉冲光环 (吸引点击) */
    div.stButton > button {
        background: linear-gradient(90deg, #0ea5e9 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        transition: all 0.3s;
        position: relative;
        overflow: hidden;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(14, 165, 233, 0.7);
    }
    
    /* 6. 侧边栏优化 */
    section[data-testid="stSidebar"] {
        background-color: #020617;
        border-right: 1px solid #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 语言字典库 (Translation Matrix)
# ==========================================
TRANS = {
    "English": {
        "slogan": "Protect What You Create.",
        "sub_slogan": "The Global Standard for Web3 Copyright Defense.",
        "live_status": "🟢 LIVE: Solana Mainnet Block #",
        "btn_launch": "🚀 LAUNCH CONSOLE",
        "core_tech": "Core Defense Matrix",
        "tech_1_t": "Invisible DNA",
        "tech_1_d": "AI-embedded watermarks immune to cropping.",
        "tech_2_t": "On-Chain Truth",
        "tech_2_d": "Immutable Solana certificates.",
        "tech_3_t": "Auto-Strike",
        "tech_3_d": "Instant DMCA legal takedowns.",
        "sidebar_title": "Command Center",
        "role": "CEO / Admin",
        "btn_legal": "⚖️ Legal & Compliance", 
        "btn_back": "⬅️ Back",
        "btn_logout": "Log Out",
        # Legal
        "legal_title": "Legal Shield",
        "tos": "Terms of Service",
        "tos_d": "We prohibit protection of stolen assets. Violators banned.",
        "refund": "No-Refund Policy",
        "refund_d": "Blockchain actions are irreversible. All sales final.",
        "sla": "SLA Guarantee",
        "sla_d": "99.9% Uptime for Enterprise users.",
        "privacy": "Data Privacy",
        "privacy_d": "Your original files are encrypted locally.",
        "footer": "© 2026 OriginGuard Solutions. Nonthaburi HQ."
    },
    "中文": {
        "slogan": "捍卫你的数字资产",
        "sub_slogan": "Web3 版权保护全球标准 | 自动确权与维权",
        "live_status": "🟢 实时连接: Solana 主网区块高度 #",
        "btn_launch": "🚀 启动控制台",
        "core_tech": "核心防御矩阵",
        "tech_1_t": "隐形 DNA",
        "tech_1_d": "免疫裁剪和压缩的 AI 隐形水印。",
        "tech_2_t": "链上真理",
        "tech_2_d": "不可篡改的 Solana 永久证书。",
        "tech_3_t": "自动打击",
        "tech_3_d": "毫秒级生成跨国 DMCA 律师函。",
        "sidebar_title": "指挥中心",
        "role": "CEO / 管理员",
        "btn_legal": "⚖️ 法务合规中心",
        "btn_back": "⬅️ 返回",
        "btn_logout": "退出登录",
        # Legal
        "legal_title": "法律护盾",
        "tos": "服务条款 (ToS)",
        "tos_d": "严禁保护盗版内容。违规者将立即封号。",
        "refund": "无退款政策",
        "refund_d": "区块链操作不可逆，Gas 费实时消耗。概不退款。",
        "sla": "SLA 服务承诺",
        "sla_d": "企业级用户享受 99.9% 在线率保证。",
        "privacy": "数据隐私",
        "privacy_d": "源文件本地加密，绝不触网泄露。",
        "footer": "© 2026 OriginGuard Solutions. 泰国暖武里总部."
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး | ကမ္ဘာ့အဆင့်မီ နည်းပညာ",
        "live_status": "🟢 တိုက်ရိုက်: Solana Mainnet Block #",
        "btn_launch": "🚀 စနစ်စတင်မည်",
        "core_tech": "အဓိက နည်းပညာများ",
        "tech_1_t": "မမြင်ရသော ရေစာ",
        "tech_1_d": "AI နည်းပညာဖြင့် ပုံရိပ်ထဲတွင် မြှုပ်နှံထားသည်။",
        "tech_2_t": "Blockchain သက်သေ",
        "tech_2_d": "Solana ပေါ်တွင် ဖျက်၍မရသော မှတ်တမ်း။",
        "tech_3_t": "အလိုအလျောက် တိုင်ကြားခြင်း",
        "tech_3_d": "DMCA တိုင်ကြားစာ ချက်ချင်းပို့မည်။",
        "sidebar_title": "ထိန်းချုပ်ခန်း",
        "role": "CEO / အက်ဒမင်",
        "btn_legal": "⚖️ ဥပဒေဌာန",
        "btn_back": "⬅️ ပြန်သွားရန်",
        "btn_logout": "ထွက်မည်",
        # Legal
        "legal_title": "ဥပဒေနှင့် စည်းမျဉ်းများ",
        "tos": "ဝန်ဆောင်မှု စည်းမျဉ်းများ",
        "tos_d": "သူတစ်ပါးပိုင်ဆိုင်မှုကို ခိုးယူအသုံးပြုခြင်းကို တားမြစ်သည်။",
        "refund": "ငွေပြန်အမ်းမည်မဟုတ်ပါ (No Refund)",
        "refund_d": "Blockchain တွင် မှတ်တမ်းတင်ပြီးပါက ပြန်လည်ပြင်ဆင်၍မရပါ။",
        "sla": "ဝန်ဆောင်မှု အာမခံချက်",
        "sla_d": "၉၉.၉% အချိန်ပြည့် အလုပ်လုပ်မည်။",
        "privacy": "ကိုယ်ပိုင်အချက်အလက် လုံခြုံရေး",
        "privacy_d": "သင်၏ အချက်အလက်များကို လုံခြုံစွာ သိမ်းဆည်းထားမည်။",
        "footer": "© 2026 OriginGuard Solutions."
    }
}

# ==========================================
# 3. 逻辑控制 (Logic Control)
# ==========================================
lang_choice = st.sidebar.selectbox(
    "🌐 Language / ဘာသာစကား",
    ["English", "中文", "Myanmar"],
    index=1
)
T = TRANS[lang_choice]

if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def set_page(page_name):
    st.session_state.page = page_name

# --- 1. 动态落地页 (Dynamic Landing Page) ---
if st.session_state.page == 'landing':
    
    st.write("")
    # 动态标题区
    st.markdown(f"""
    <div style="text-align: center; padding: 60px 0;">
        <h1 style="font-size: 60px; margin-bottom: 20px;">{T['slogan']}</h1>
        <p style="font-size: 22px; color: #cbd5e1; max-width: 800px; margin: 0 auto; text-shadow: 0 0 10px rgba(0,0,0,0.5);">
            {T['sub_slogan']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 模拟“实时数据流” (增加信任感)
    live_block = random.randint(245000000, 245999999)
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 40px;">
        <span style="background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 5px 15px; border-radius: 20px; font-family: monospace; font-size: 14px; border: 1px solid #22c55e;">
            {T['live_status']}{live_block}
        </span>
    </div>
    """, unsafe_allow_html=True)

    # 巨大的启动按钮
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(T['btn_launch'], use_container_width=True):
            set_page('dashboard')
            st.rerun()

    st.markdown("---")
    
    # 悬浮卡片展示核心技术
    st.subheader(T['core_tech'])
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**{T['tech_1_t']}**\n\n{T['tech_1_d']}")
    with col2:
        st.info(f"**{T['tech_2_t']}**\n\n{T['tech_2_d']}")
    with col3:
        st.info(f"**{T['tech_3_t']}**\n\n{T['tech_3_d']}")

    st.markdown("---")
    st.caption(T['footer'])

# --- 2. 仪表盘 (Dashboard) ---
elif st.session_state.page == 'dashboard':
    with st.sidebar:
        st.title(T['sidebar_title'])
        st.write(f"👤 **MNNO**")
        st.success("🟢 ONLINE")
        st.markdown("---")
        if st.button(T['btn_legal']):
            set_page('legal')
            st.rerun()
        st.markdown("---")
        if st.button(T['btn_logout']):
            set_page('landing')
            st.rerun()

    st.title("📊 " + T['sidebar_title'])
    
    # 动态数据展示
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Assets", "1,248", "+12")
    k2.metric("Threats", "53", "High Alert", delta_color="inverse")
    k3.metric("Legal", "41", "+3")
    k4.metric("Saved", "$12,400")

    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["🛡️ Protect", "🌍 Map", "⚖️ DMCA"])
    
    with tab1:
        st.file_uploader("JPG/PNG", type=['png', 'jpg'])
        st.button("🔒 Encrypt")
    with tab2:
        st.map(pd.DataFrame({'lat': [13.7563], 'lon': [100.5018]}))
    with tab3:
        st.text_input("Infringing URL")
        st.button("🚀 Strike")

# --- 3. 法务中心 (Legal) ---
elif st.session_state.page == 'legal':
    with st.sidebar:
        st.title(T['sidebar_title'])
        if st.button(T['btn_back']):
            set_page('dashboard')
            st.rerun()

    st.title(T['legal_title'])
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.warning(f"### {T['tos']}\n{T['tos_d']}")
        st.success(f"### {T['privacy']}\n{T['privacy_d']}")
    with c2:
        st.error(f"### {T['refund']}\n{T['refund_d']}")
        st.info(f"### {T['sla']}\n{T['sla_d']}")
    
    st.markdown("---")
    st.caption("OriginGuard Compliance Engine v3.4")
    
