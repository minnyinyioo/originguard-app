# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
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

# --- 🎨 CSS 动态注入：极速流光 + 底部矩阵 ---
st.markdown("""
<style>
    /* 1. 字体库：Padauk (缅文首选) */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 2. 动态背景：流动的深海光影 (提速至 15s，肉眼可见的流动) */
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp {
        background: linear-gradient(-45deg, #020617, #1e1b4b, #312e81, #0f172a);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite; /* 提速4倍 */
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
        color: #e2e8f0;
    }

    /* 3. 区块高度跳动特效 (心跳脉冲) */
    @keyframes pulse-green {
        0% {box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7);}
        70% {box-shadow: 0 0 0 10px rgba(74, 222, 128, 0);}
        100% {box-shadow: 0 0 0 0 rgba(74, 222, 128, 0);}
    }
    .live-status {
        animation: pulse-green 2s infinite;
        border-radius: 20px;
    }

    /* 4. 标题特效：全息流光 */
    h1 {
        background: linear-gradient(90deg, #22d3ee, #818cf8, #c084fc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        letter-spacing: -1px;
        animation: gradientText 3s linear infinite; /* 标题流动也提速 */
    }
    @keyframes gradientText {
        0% {background-position: 0% center;}
        100% {background-position: 200% center;}
    }

    /* 5. 卡片悬浮特效 */
    div[data-testid="stMetric"], div.stInfo, div.stWarning, div.stError, div.stSuccess {
        background-color: rgba(15, 23, 42, 0.6); 
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s ease;
    }
    div[data-testid="stMetric"]:hover, div.stInfo:hover {
        transform: translateY(-5px) scale(1.02);
        border-color: #22d3ee;
        box-shadow: 0 10px 30px -10px rgba(34, 211, 238, 0.4);
    }

    /* 6. 底部法律按钮样式 (Footer Buttons) */
    .footer-btn button {
        background: transparent !important;
        border: 1px solid #334155 !important;
        color: #94a3b8 !important;
        font-size: 12px !important;
    }
    .footer-btn button:hover {
        border-color: #818cf8 !important;
        color: #fff !important;
    }
    
    /* 7. 强制换行适配 */
    div[data-testid="stNotification"] {
        word-wrap: break-word;
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
        "btn_logout": "Log Out",
        
        # Footer Links (Short)
        "link_tos": "Terms",
        "link_privacy": "Privacy",
        "link_refund": "No Refunds",
        "link_sla": "SLA",
        "link_disclaimer": "Disclaimer",
        "footer_warning": "⚠️ IMPORTANT: All blockchain transactions are final. Once protected, gas fees are burned and strictly non-refundable.",
        "footer_copyright": "© 2026 OriginGuard Solutions. Nonthaburi HQ.",

        # Legal Page Content
        "legal_title": "Legal Shield & Compliance",
        "tos_t": "Terms of Service",
        "tos_d": "We prohibit protection of stolen assets. Violators banned.",
        "refund_t": "No-Refund Policy (Immutable)",
        "refund_d": "Blockchain actions are irreversible. All sales final.",
        "sla_t": "SLA Guarantee",
        "sla_d": "99.9% Uptime for Enterprise users.",
        "privacy_t": "Data Privacy",
        "privacy_d": "Your original files are encrypted locally.",
        "disclaimer_t": "Legal Disclaimer",
        "disclaimer_d": "OriginGuard provides technological evidence, not legal advice."
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
        "btn_logout": "退出登录",

        # 底部链接 (Footer)
        "link_tos": "服务条款",
        "link_privacy": "隐私政策",
        "link_refund": "无退款声明",
        "link_sla": "SLA承诺",
        "link_disclaimer": "免责声明",
        "footer_warning": "⚠️ 重要提示：所有区块链交易均为最终交易。保护一旦激活，Gas费即刻消耗，严格执行“无退款”政策。",
        "footer_copyright": "© 2026 OriginGuard Solutions. 泰国暖武里总部.",

        # Legal Page Content
        "legal_title": "法律护盾与合规",
        "tos_t": "服务条款 (ToS)",
        "tos_d": "严禁保护盗版内容。违规者将立即封号。",
        "refund_t": "无退款政策 (链上不可逆)",
        "refund_d": "区块链操作不可逆，Gas 费实时消耗。概不退款。",
        "sla_t": "SLA 服务承诺",
        "sla_d": "企业级用户享受 99.9% 在线率保证。",
        "privacy_t": "数据隐私",
        "privacy_d": "源文件本地加密，绝不触网泄露。",
        "disclaimer_t": "免责声明",
        "disclaimer_d": "OriginGuard 提供技术证据，而非法律咨询服务。"
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
        "btn_logout": "ထွက်မည်",

        # Footer
        "link_tos": "စည်းမျဉ်းများ",
        "link_privacy": "လုံခြုံရေး",
        "link_refund": "ငွေပြန်မအမ်းပါ",
        "link_sla": "SLA",
        "link_disclaimer": "ငြင်းဆိုချက်",
        "footer_warning": "⚠️ အရေးကြီးသည် - Blockchain ငွေပေးချေမှုများသည် ပြင်ဆင်၍မရပါ။ ငွေပြန်အမ်းမည် မဟုတ်ပါ။",
        "footer_copyright": "© 2026 OriginGuard Solutions.",

        # Legal Page
        "legal_title": "ဥပဒေနှင့် စည်းမျဉ်းများ",
        "tos_t": "ဝန်ဆောင်မှု စည်းမျဉ်းများ",
        "tos_d": "သူတစ်ပါးပိုင်ဆိုင်မှုကို ခိုးယူအသုံးပြုခြင်းကို တားမြစ်သည်။",
        "refund_t": "ငွေပြန်အမ်းမည်မဟုတ်ပါ (No Refund)",
        "refund_d": "Blockchain တွင် မှတ်တမ်းတင်ပြီးပါက ပြန်လည်ပြင်ဆင်၍မရပါ။",
        "sla_t": "ဝန်ဆောင်မှု အာမခံချက်",
        "sla_d": "၉၉.၉% အချိန်ပြည့် အလုပ်လုပ်မည်။",
        "privacy_t": "ကိုယ်ပိုင်အချက်အလက် လုံခြုံရေး",
        "privacy_d": "သင်၏ အချက်အလက်များကို လုံခြုံစွာ သိမ်းဆည်းထားမည်။",
        "disclaimer_t": "ငြင်းဆိုချက်",
        "disclaimer_d": "ကျွန်ုပ်တို့သည် နည်းပညာကိုသာ ပံ့ပိုးပေးသည်။"
    }
}

# ==========================================
# 3. 逻辑控制与页面渲染
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

# --- 公共底部组件 (The Trust Footer) ---
def render_footer():
    st.markdown("---")
    # 1. 醒目的无退款警告 (区块链不可逆)
    st.error(T['footer_warning'])
    
    # 2. 法律链接矩阵
    f1, f2, f3, f4, f5 = st.columns(5)
    # 使用 container 宽度让按钮看起来像导航条
    if f1.button(T['link_tos'], key="f_tos", use_container_width=True): set_page('legal'); st.rerun()
    if f2.button(T['link_privacy'], key="f_priv", use_container_width=True): set_page('legal'); st.rerun()
    if f3.button(T['link_refund'], key="f_ref", use_container_width=True): set_page('legal'); st.rerun()
    if f4.button(T['link_sla'], key="f_sla", use_container_width=True): set_page('legal'); st.rerun()
    if f5.button(T['link_disclaimer'], key="f_disc", use_container_width=True): set_page('legal'); st.rerun()
    
    st.markdown(f"<div style='text-align: center; color: #64748b; font-size: 12px; margin-top: 20px;'>{T['footer_copyright']}</div>", unsafe_allow_html=True)

# --- 1. 动态落地页 (Landing) ---
if st.session_state.page == 'landing':
    st.write("")
    # 动态标题
    st.markdown(f"""
    <div style="text-align: center; padding: 60px 0;">
        <h1 style="font-size: 60px; margin-bottom: 20px;">{T['slogan']}</h1>
        <p style="font-size: 22px; color: #cbd5e1; max-width: 800px; margin: 0 auto; text-shadow: 0 0 10px rgba(0,0,0,0.5);">
            {T['sub_slogan']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 区块跳动 (Trust Ticker) - 增加 class="live-status" 触发脉冲动画
    live_block = random.randint(245000000, 245999999)
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 40px;">
        <span class="live-status" style="background: rgba(34, 197, 94, 0.1); color: #4ade80; padding: 8px 20px; border: 1px solid #22c55e;">
            {T['live_status']}{live_block}
        </span>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(T['btn_launch'], use_container_width=True):
            set_page('dashboard')
            st.rerun()

    st.markdown("---")
    st.subheader(T['core_tech'])
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**{T['tech_1_t']}**\n\n{T['tech_1_d']}")
    with col2:
        st.info(f"**{T['tech_2_t']}**\n\n{T['tech_2_d']}")
    with col3:
        st.info(f"**{T['tech_3_t']}**\n\n{T['tech_3_d']}")

    # 渲染底部
    render_footer()

# --- 2. 仪表盘 (Dashboard) ---
elif st.session_state.page == 'dashboard':
    with st.sidebar:
        st.title(T['sidebar_title'])
        st.write(f"👤 **MNNO**")
        st.success("🟢 ONLINE")
        st.markdown("---")
        if st.button(T['btn_logout']):
            set_page('landing')
            st.rerun()

    st.title("📊 " + T['sidebar_title'])
    
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

    # 渲染底部 (确保控制台也有法律保护)
    render_footer()

# --- 3. 法务中心 (Legal) ---
elif st.session_state.page == 'legal':
    with st.sidebar:
        st.title(T['sidebar_title'])
        if st.button("⬅️ " + T['btn_launch'].split(" ")[1]): # Back button
            set_page('landing')
            st.rerun()

    st.title(T['legal_title'])
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.warning(f"### {T['tos_t']}\n{T['tos_d']}")
        st.success(f"### {T['privacy_t']}\n{T['privacy_d']}")
        st.info(f"### {T['disclaimer_t']}\n{T['disclaimer_d']}")
    with c2:
        # 无退款 - 红色高亮
        st.error(f"### {T['refund_t']}\n{T['refund_d']}")
        st.info(f"### {T['sla_t']}\n{T['sla_d']}")
    
    # 法务页面也需要底部，形成闭环
    render_footer()
