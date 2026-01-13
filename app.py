# -*- coding: utf-8 -*-
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

# --- 🎨 CSS 注入：强制加载缅语字体 + 移动端防爆版 ---
st.markdown("""
<style>
    /* 1. 引入字体库：Padauk (缅文首选), Noto Sans Myanmar (缅文备选), Inter (英文) */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 2. 全局强制字体策略 (!important 解决乱码核心) */
    html, body, [class*="css"] {
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
    }

    /* 3. 背景：深空灰蓝 Web3 渐变 */
    .stApp {
        background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
        color: #e2e8f0;
    }

    /* 4. 标题高亮：青色渐变 & 增加行高防止缅语被切头 */
    h1, h2, h3 {
        background: -webkit-linear-gradient(45deg, #22d3ee, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        line-height: 1.6 !important; /* 修复缅语字符上下标显示不全 */
        padding-bottom: 10px;
    }
    
    /* 5. 侧边栏样式 */
    section[data-testid="stSidebar"] {
        background-color: #0b1121;
        border-right: 1px solid #1e293b;
    }
    
    /* 6. 按钮：Web3 霓虹蓝 */
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

    /* 7. 法律条款框 (Cyberpunk 风格) & 强制换行 */
    div[data-testid="stNotification"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        color: #f8fafc;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        word-wrap: break-word; /* 防止长句子撑爆手机屏幕 */
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 语言字典库 (Translation Matrix - Verified)
# ==========================================
# CTO 注：缅语部分已检查，使用标准 Unicode 编码，配合上述 CSS 可完美显示。
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
        "legal_page_title": "Legal & Compliance Center",
        
        # --- 法律条款 (English) ---
        "policy_tos_t": "📜 Terms of Service (ToS)",
        "policy_tos_d": "By using OriginGuard, you agree that you are the lawful owner of any uploaded assets. We strictly prohibit the protection of stolen content. Violators will have their accounts terminated immediately.",
        "policy_disclaimer_t": "⚠️ Legal Disclaimer",
        "policy_disclaimer_d": "OriginGuard provides technological evidence (hash/metadata) for copyright claims. We are a technology provider, not a law firm. Our automated DMCA notices are tools for your use; we do not guarantee specific legal outcomes in court.",
        "policy_refund_t": "🚫 No-Refund Policy",
        "policy_refund_d": "Blockchain transactions are irreversible. Once a certificate is minted on Solana, gas fees are burned. Therefore, all sales are final and non-refundable.",
        "policy_sla_t": "⚡ Service Level Agreement (SLA)",
        "policy_sla_d": "We guarantee 99.9% system uptime. Scheduled maintenance will be notified 24 hours in advance.",
        "policy_privacy_t": "🔒 Privacy Policy",
        "policy_privacy_d": "We collect minimal data required for blockchain hashing. Your original files are encrypted locally and never sold to third parties.",
        "policy_copyright_t": "© Intellectual Property Notice",
        "policy_copyright_d": "The OriginGuard algorithm, UI design, and 'Invisible DNA' technology are proprietary intellectual property of OriginGuard Solutions Inc.",
        
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
        "legal_page_title": "法律合规与声明",
        
        # --- 法律条款 (中文) ---
        "policy_tos_t": "📜 服务条款 (ToS)",
        "policy_tos_d": "使用 OriginGuard 即表示您同意您是上传资产的合法拥有者。我们严禁利用本平台保护盗版内容。违规账号将被立即封禁。",
        "policy_disclaimer_t": "⚠️ 免责声明",
        "policy_disclaimer_d": "OriginGuard 提供用于版权主张的技术证据（哈希/元数据）。我们是技术提供商，而非律师事务所。自动生成的律师函仅供您使用，我们不承诺特定法庭判决结果。",
        "policy_refund_t": "🚫 无退款政策",
        "policy_refund_d": "区块链交易不可逆转。一旦证书在 Solana 上铸造，Gas 费即被消耗。因此，所有销售均为最终决定，概不退款。",
        "policy_sla_t": "⚡ 服务等级协议 (SLA)",
        "policy_sla_d": "我们承诺 99.9% 的系统正常运行时间。计划维护将提前 24 小时通知。",
        "policy_privacy_t": "🔒 隐私政策",
        "policy_privacy_d": "我们仅收集区块链哈希所需的最小化数据。您的源文件在本地加密，绝不出售给第三方。",
        "policy_copyright_t": "© 知识产权声明",
        "policy_copyright_d": "OriginGuard 的算法、UI 设计及“隐形 DNA”技术均为 OriginGuard Solutions Inc. 的专有知识产权。",
        
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
        
        # --- 法律条款 (缅文 - 使用 Padauk 字体渲染) ---
        "policy_tos_t": "📜 ဝန်ဆောင်မှု စည်းမျဉ်းများ (Terms of Service)",
        "policy_tos_d": "OriginGuard ကို အသုံးပြုခြင်းဖြင့် သင်သည် ပိုင်ဆိုင်မှုများ၏ တရားဝင်ပိုင်ရှင်ဖြစ်ကြောင်း သဘောတူပါသည်။ သူတစ်ပါးပိုင်ဆိုင်မှုကို ခိုးယူအသုံးပြုခြင်းကို တားမြစ်သည်။",
        "policy_disclaimer_t": "⚠️ ဥပဒေကြောင်းအရ ငြင်းဆိုချက် (Disclaimer)",
        "policy_disclaimer_d": "OriginGuard သည် နည်းပညာ အထောက်အထားများကိုသာ ပံ့ပိုးပေးပါသည်။ ကျွန်ုပ်တို့သည် ရှေ့နေရုံးမဟုတ်ပါ။ တရားရုံးဆုံးဖြတ်ချက်များအတွက် အာမခံချက်မပေးပါ။",
        "policy_refund_t": "🚫 ငွေပြန်အမ်းမည်မဟုတ်ပါ (No Refund)",
        "policy_refund_d": "Solana Blockchain တွင် မှတ်တမ်းတင်ပြီးပါက ပြန်လည်ပြင်ဆင်၍မရပါ။ ထို့ကြောင့် ငွေပြန်အမ်းခြင်း မပြုလုပ်နိုင်ပါ။",
        "policy_sla_t": "⚡ ဝန်ဆောင်မှု အာမခံချက် (SLA)",
        "policy_sla_d": "စနစ်ပိုင်းဆိုင်ရာ ၉၉.၉% အချိန်ပြည့် အလုပ်လုပ်မည်ဟု အာမခံပါသည်။",
        "policy_privacy_t": "🔒 ကိုယ်ပိုင်အချက်အလက် လုံခြုံရေး (Privacy)",
        "policy_privacy_d": "သင်၏ အချက်အလက်များကို ရောင်းချခြင်း မပြုပါ။ လုံခြုံစွာ သိမ်းဆည်းထားမည်။",
        "policy_copyright_t": "© မူပိုင်ခွင့် အသိပေးချက်",
        "policy_copyright_d": "OriginGuard ၏ နည်းပညာနှင့် ဒီဇိုင်းများသည် ကုမ္ပဏီ၏ မူပိုင်ခွင့်များ ဖြစ်သည်။",
        
        "footer": "© 2026 OriginGuard Solutions. မူပိုင်ခွင့် ရယူထားသည်။"
    }
}

# ==========================================
# 3. 语言选择与路由逻辑
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

# --- 3. 法务中心 (Legal Center) [大厂级合规页面] ---
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
    st.write("Last Updated: January 13, 2026")
    st.markdown("---")

    # 分栏布局：模仿 Coinbase/Binance 的条款展示
    col1, col2 = st.columns(2)
    
    with col1:
        # 服务条款 (ToS)
        st.warning(f"### {T['policy_tos_t']}\n\n{T['policy_tos_d']}")
        # 隐私政策
        st.success(f"### {T['policy_privacy_t']}\n\n{T['policy_privacy_d']}")
        # 知识产权
        st.info(f"### {T['policy_copyright_t']}\n\n{T['policy_copyright_d']}")
        
    with col2:
        # 免责声明 (Disclaimer) - 关键防身条款
        st.error(f"### {T['policy_disclaimer_t']}\n\n{T['policy_disclaimer_d']}")
        # 无退款政策
        st.error(f"### {T['policy_refund_t']}\n\n{T['policy_refund_d']}")
        # SLA
        st.info(f"### {T['policy_sla_t']}\n\n{T['policy_sla_d']}")
    
    st.markdown("---")
    st.caption("Compliance Framework v3.3 | Contact: legal@originguard.com")
