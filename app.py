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
        font-family: 'Inter', 'Noto Sans Myanmar', sans-serif;
        color: #e2e8f0;
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

    /* 法律条款警示框样式重写 */
    div[data-testid="stNotification"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        color: #f8fafc;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 语言字典库 (The Translation Matrix)
# ==========================================
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
        "btn_legal": "⚖️ Legal Center", 
        "btn_back_dash": "⬅️ Back to Dashboard",
        "legal_page_title": "Legal Shield & Compliance",
        "policy_refund_t": "🚫 No-Refund Policy (Blockchain Immutable)",
        "policy_refund_d": "Once a certificate is minted on the Solana Blockchain, the transaction creates a permanent, irreversible record. Gas fees are paid instantly to the network. Therefore, OriginGuard cannot offer refunds or cancellations once protection is activated. All sales are final.",
        "policy_sla_t": "⚡ Service Level Agreement (SLA)",
        "policy_sla_d": "For Enterprise subscribers, we guarantee 99.9% API uptime. In the event of downtime exceeding 1 hour, users will be compensated with service credits.",
        "policy_privacy_t": "🔒 Privacy & Data Sovereignty",
        "policy_privacy_d": "We do not sell, trade, or rent your personal identification information. Master files are encrypted locally before hashing. You own your data.",
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
        "btn_legal": "⚖️ 法务中心",
        "btn_back_dash": "⬅️ 返回控制台",
        "legal_page_title": "法律护盾与合规中心",
        "policy_refund_t": "🚫 无退款政策 (区块链不可篡改)",
        "policy_refund_d": "一旦证书在 Solana 区块链上铸造完成，该交易即生成永久且不可逆的记录。Gas 费已实时支付给网络节点。因此，OriginGuard 无法对已激活的保护服务提供退款或取消。所有销售均为最终决定。",
        "policy_sla_t": "⚡ 服务等级协议 (SLA)",
        "policy_sla_d": "对于企业级订阅用户，我们承诺 99.9% 的 API 正常运行时间。如果宕机时间超过 1 小时，我们将赔偿服务积分。",
        "policy_privacy_t": "🔒 隐私与数据主权",
        "policy_privacy_d": "我们绝不出售、交易或出租您的个人身份信息。您的源文件在哈希计算前均会在本地加密。数据归您所有。",
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
        "btn_legal": "⚖️ ဥပဒေဌာန",
        "btn_back_dash": "⬅️ ဒက်ရှ်ဘုတ် သို့ပြန်သွားရန်",
        "legal_page_title": "ဥပဒေနှင့် စည်းမျဉ်းများ",
        "policy_refund_t": "🚫 ငွေပြန်အမ်းမည်မဟုတ်ပါ (No Refund)",
        "policy_refund_d": "Solana Blockchain တွင် မှတ်တမ်းတင်ပြီးပါက ပြန်လည်ပြင်ဆင်၍မရပါ။ ထို့ကြောင့် ငွေပြန်အမ်းခြင်း မပြုလုပ်နိုင်ပါ။",
        "policy_sla_t": "⚡ ဝန်ဆောင်မှု အာမခံချက် (SLA)",
        "policy_sla_d": "စနစ်ပိုင်းဆိုင်ရာ ၉၉.၉% အချိန်ပြည့် အလုပ်လုပ်မည်ဟု အာမခံပါသည်။",
        "policy_privacy_t": "🔒 ကိုယ်ပိုင်အချက်အလက် လုံခြုံရေး",
        "policy_privacy_d": "သင်၏ အချက်အလက်များကို ရောင်းချခြင်း မပြုပါ။",
        "footer": "© 2026 OriginGuard Solutions. မူပိုင်ခွင့် ရယူထားသည်။"
    }
}

# ==========================================
# 3. 语言选择与路由 (Logic)
# ==========================================
lang_choice = st.sidebar.selectbox(
    "🌐 Language / ဘာသာစကား / 语言",
    ["English", "中文", "Myanmar"],
    index=1
)
T = TRANS[lang_choice]

if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def set_page(page_name):
    st.session_state.page = page_name

# --- 1. 落地页 (Landing Page) ---
if st.session_state.page == 'landing':
    st.write("")
    st.write("")
    st.markdown(f"""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 56px; margin-bottom: 20px;">{T['slogan']}</h1>
        <p style="font-size: 20px; color: #94a3b8; max-width: 800px; margin: 0 auto;">{T['sub_slogan']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(T['btn_launch'], use_container_width=True):
            set_page('dashboard')
            st.rerun()

    st.markdown("---")
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

# --- 2. 仪表盘 (Dashboard) ---
elif st.session_state.page == 'dashboard':
    with st.sidebar:
        st.title(T['sidebar_title'])
        st.write(f"👤 **MNNO** ({T['role']})")
        st.success(T['status'])
        st.markdown("---")
        # 法务中心入口
        if st.button(T['btn_legal']):
            set_page('legal')
            st.rerun()
        st.markdown("---")
        if st.button(T['btn_logout']):
            set_page('landing')
            st.rerun()

    st.title(T['dash_title'])
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Protected", "1,248")
    k2.metric("Blocked", "53", "High", delta_color="inverse")
    k3.metric("Actions", "41")
    k4.metric("Saved", "$12,400")

    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["🛡️ Protect", "🌍 Map", "⚖️ Legal"])
    with tab1:
        st.file_uploader("JPG / PNG", type=['png', 'jpg'])
        st.button("🔒 Encrypt & Mint")
    with tab2:
        st.map(pd.DataFrame({'lat': [13.7563], 'lon': [100.5018]}))
    with tab3:
        st.text_input("URL")
        st.button("🚀 DMCA")

# --- 3. 法务中心 (Legal Center) ---
elif st.session_state.page == 'legal':
    with st.sidebar:
        st.title(T['sidebar_title'])
        st.write(f"👤 **MNNO** ({T['role']})")
        st.markdown("---")
        if st.button(T['btn_back_dash']):
            set_page('dashboard')
            st.rerun()
        if st.button(T['btn_logout']):
            set_page('landing')
            st.rerun()

    st.title(T['legal_page_title'])
    st.markdown("---")

    # 渲染法律条款 (使用 f-string)
    st.error(f"### {T['policy_refund_t']}\n\n{T['policy_refund_d']}")
    st.info(f"### {T['policy_sla_t']}\n\n{T['policy_sla_d']}")
    st.success(f"### {T['policy_privacy_t']}\n\n{T['policy_privacy_d']}")
    
    st.markdown("---")
    st.caption("OriginGuard Legal Engine v3.1")
