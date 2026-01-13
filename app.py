# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import random

# ==========================================
# 1. 核心配置 (Core Config)
# ==========================================
st.set_page_config(
    page_title="OriginGuard Web3",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed" # 默认收起侧边栏，更像官网
)

# ==========================================
# 2. 法律文本常量库 (IMMUTABLE LEGAL TEXTS)
# ==========================================
# CEO 指令：以下文本为法律合同，严禁 AI 随意修改或润色。
LEGAL_CONSTANTS = {
    "English": {
        "tos": """**1. Acceptance of Terms:** By accessing OriginGuard, you agree to be bound by these Terms. If you do not agree, do not use our services.\n\n**2. Authorized Use:** You affirm that you are the lawful copyright owner of any content you upload. Uploading stolen, illegal, or unauthorized content will result in immediate account termination and reporting to authorities.\n\n**3. Limitation of Liability:** OriginGuard is a technology provider. We provide blockchain evidence but do not guarantee specific legal outcomes in any jurisdiction.""",
        "refund": """**NO REFUND POLICY (STRICT):**\n\nOriginGuard utilizes public blockchain networks (Solana) to mint copyright certificates. When you click "Protect", network Gas fees are paid instantly and irreversibly to miners/validators.\n\n**THEREFORE, ALL SALES ARE FINAL.**\n\nOnce a transaction is initiated, it cannot be canceled, reversed, or refunded by OriginGuard, Stripe, or any bank. By using this service, you explicitly waive your right to a cooling-off period for digital goods.""",
        "privacy": """**1. Data Minimization:** We only hash your files to generate a digital fingerprint. We do not store your original high-resolution images on our public servers.\n\n**2. Data Sovereignty:** Your encrypted data remains yours. We do not sell, trade, or rent user data to third parties.\n\n**3. Cookies:** We use essential cookies to maintain your session security.""",
        "sla": """**Enterprise SLA:**\nFor Enterprise Plan subscribers, OriginGuard guarantees a 99.9% API Monthly Uptime Percentage. If we fall below this metric, you may be eligible for Service Credits.""",
        "disclaimer": """**Legal Disclaimer:**\nOriginGuard generates technological proof of existence and ownership. We are NOT a law firm and do not provide legal advice. The "Legal Hammer" (DMCA Notice) is an automated template tool; users are responsible for the legal accuracy of claims sent using this tool."""
    },
    "中文": {
        "tos": """**1. 条款接受：** 访问 OriginGuard 即表示您同意受本条款约束。如果您不同意，请勿使用我们的服务。\n\n**2. 授权使用：** 您声明您是您上传的任何内容的合法版权拥有者。上传被盗、非法或未经授权的内容将导致账户立即终止并向有关部门举报。\n\n**3. 责任限制：** OriginGuard 是技术提供商。我们提供区块链证据，但不保证在任何司法管辖区获得特定的法律结果。""",
        "refund": """**无退款政策 (严格执行)：**\n\nOriginGuard 利用公共区块链网络 (Solana) 铸造版权证书。当您点击“保护”时，网络 Gas 费即刻且不可逆地支付给矿工/验证者。\n\n**因此，所有销售均为最终交易。**\n\n交易一旦发起，OriginGuard、Stripe 或任何银行均无法取消、撤销或退款。使用本服务即表示您明确放弃数字商品的“冷静期”权利。""",
        "privacy": """**1. 数据最小化：** 我们仅对您的文件进行哈希处理以生成数字指纹。我们不会在公共服务器上存储您的原始高分辨率图像。\n\n**2. 数据主权：** 您的加密数据归您所有。我们不出售、交易或出租用户数据给第三方。\n\n**3. Cookie：** 我们仅使用必要的 Cookie 来维护您的会话安全。""",
        "sla": """**企业级 SLA：**\n对于企业计划订阅者，OriginGuard 承诺 99.9% 的 API 月度正常运行时间百分比。如果我们低于此指标，您可能有资格获得服务积分。""",
        "disclaimer": """**法律免责声明：**\nOriginGuard 生成存在和所有权的技术证明。我们不是律师事务所，不提供法律咨询。“法律重锤”(DMCA 通知) 是一个自动化模板工具；用户对使用此工具发送的索赔的法律准确性负责。"""
    },
    "Myanmar": {
        "tos": """**1. သဘောတူညီချက်:** OriginGuard ကို အသုံးပြုခြင်းဖြင့် သင်သည် ဤစည်းမျဉ်းများကို လိုက်နာရန် သဘောတူပါသည်။\n\n**2. တရားဝင်အသုံးပြုမှု:** သင်တင်သော ပုံများသည် သင်ပိုင်ဆိုင်ကြောင်း အာမခံရပါမည်။ သူတစ်ပါးပုံများကို ခိုးယူသုံးစွဲခြင်းကို တားမြစ်သည်။\n\n**3. တာဝန်ယူမှု:** ကျွန်ုပ်တို့သည် နည်းပညာကိုသာ ပံ့ပိုးပေးသည်။ တရားရုံး ဆုံးဖြတ်ချက်များအတွက် အာမခံချက်မပေးပါ။""",
        "refund": """**ငွေပြန်အမ်းမည်မဟုတ်ပါ (စည်းမျဉ်း):**\n\nSolana Blockchain တွင် မှတ်တမ်းတင်ပြီးပါက ပြန်လည်ပြင်ဆင်၍မရပါ။ ငွေပေးချေမှုများသည် အပြီးအပြတ်ဖြစ်သည်။\n\n**ထို့ကြောင့် ငွေပြန်အမ်းခြင်း မပြုလုပ်နိုင်ပါ။**\n\nဤဝန်ဆောင်မှုကို အသုံးပြုခြင်းဖြင့် သင်သည် ငွေပြန်အမ်းခွင့်ကို စွန့်လွှတ်လိုက်ပါသည်။""",
        "privacy": """**1. အချက်အလက် လုံခြုံရေး:** သင့်ပုံများကို ကျွန်ုပ်တို့ သိမ်းဆည်းမထားပါ။\n\n**2. ကိုယ်ပိုင်အချက်အလက်:** သင့်အချက်အလက်များကို အခြားသူများအား ရောင်းချခြင်း မပြုပါ။""",
        "sla": """**ဝန်ဆောင်မှု အာမခံချက် (SLA):**\nလုပ်ငန်းသုံး အကောင့်များအတွက် ၉၉.၉% အချိန်ပြည့် စနစ်အလုပ်လုပ်မည်ဟု အာမခံပါသည်။""",
        "disclaimer": """**ငြင်းဆိုချက်:**\nOriginGuard သည် နည်းပညာ ကုမ္ပဏီဖြစ်သည်။ ရှေ့နေရုံး မဟုတ်ပါ။ ဥပဒေရေးရာ အကြံဉာဏ်များ မပေးပါ။"""
    }
}

# ==========================================
# 3. 动态 CSS (V3.5 风格保持不变)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp {
        background: linear-gradient(-45deg, #020617, #1e1b4b, #312e81, #0f172a);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
        color: #e2e8f0;
    }

    h1 {
        background: linear-gradient(90deg, #22d3ee, #818cf8, #c084fc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        letter-spacing: -1px;
        animation: gradientText 3s linear infinite;
    }
    @keyframes gradientText {
        0% {background-position: 0% center;}
        100% {background-position: 200% center;}
    }

    /* 底部法律导航栏样式 */
    .legal-nav {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.1);
        flex-wrap: wrap;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #0ea5e9 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
    }
    /* 强制换行适配 */
    div[data-testid="stNotification"] { word-wrap: break-word; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. 语言字典 (UI 文本)
# ==========================================
TRANS = {
    "English": {
        "slogan": "Protect What You Create.",
        "sub_slogan": "The Global Standard for Web3 Copyright Defense.",
        "btn_launch": "🚀 LAUNCH CONSOLE",
        "live_status": "🟢 LIVE: Solana Mainnet Block #",
        "footer_warning": "⚠️ IMPORTANT: Blockchain transactions are final. Gas fees are non-refundable.",
        "footer_copy": "© 2026 OriginGuard Solutions. Nonthaburi HQ.",
        "titles": ["Terms", "Refund", "Privacy", "SLA", "Disclaimer"],
        "back": "⬅️ Back to Home"
    },
    "中文": {
        "slogan": "捍卫你的数字资产",
        "sub_slogan": "Web3 版权保护全球标准 | 自动确权与维权",
        "btn_launch": "🚀 启动控制台 (演示版)",
        "live_status": "🟢 实时连接: Solana 主网区块高度 #",
        "footer_warning": "⚠️ 重要提示：区块链交易均为最终交易。Gas 费概不退款。",
        "footer_copy": "© 2026 OriginGuard Solutions. 泰国暖武里总部.",
        "titles": ["服务条款", "无退款政策", "隐私政策", "SLA承诺", "免责声明"],
        "back": "⬅️ 返回首页"
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး | ကမ္ဘာ့အဆင့်မီ နည်းပညာ",
        "btn_launch": "🚀 စနစ်စတင်မည်",
        "live_status": "🟢 တိုက်ရိုက်: Solana Mainnet Block #",
        "footer_warning": "⚠️ အရေးကြီးသည် - Blockchain ငွေပေးချေမှုများသည် ပြင်ဆင်၍မရပါ။ ငွေပြန်အမ်းမည် မဟုတ်ပါ။",
        "footer_copy": "© 2026 OriginGuard Solutions.",
        "titles": ["စည်းမျဉ်းများ", "ငွေပြန်မအမ်းပါ", "လုံခြုံရေး", "SLA", "ငြင်းဆိုချက်"],
        "back": "⬅️ ပြန်သွားရန်"
    }
}

# ==========================================
# 5. 逻辑控制
# ==========================================
# 侧边栏只放语言选择，保持首页干净
lang_choice = st.sidebar.selectbox("🌐 Language / 语言", ["English", "中文", "Myanmar"], index=1)
T = TRANS[lang_choice]
L_TEXT = LEGAL_CONSTANTS[lang_choice]

if 'page' not in st.session_state: st.session_state.page = 'landing'
def set_page(name): st.session_state.page = name

# --- 公共底部组件 (Public Footer) ---
def render_footer():
    st.write("")
    st.write("")
    st.error(T['footer_warning']) # 红色警示带
    
    # 法律链接矩阵 (5个按钮一排)
    cols = st.columns(5)
    labels = T['titles'] # ["Terms", "Refund", "Privacy", "SLA", "Disclaimer"]
    keys = ["tos", "refund", "privacy", "sla", "disclaimer"]
    
    for i, col in enumerate(cols):
        if col.button(labels[i], key=f"btn_{keys[i]}", use_container_width=True):
            st.session_state.view_legal = keys[i] # 记录想看哪个条款
            set_page('legal_view')
            st.rerun()
            
    st.markdown(f"<div style='text-align: center; color: #64748b; font-size: 12px; margin-top: 20px;'>{T['footer_copy']}</div>", unsafe_allow_html=True)

# --- 1. 官网首页 (Landing Page) ---
if st.session_state.page == 'landing':
    st.write("")
    st.markdown(f"""
    <div style="text-align: center; padding: 80px 0;">
        <h1 style="font-size: 64px; margin-bottom: 20px;">{T['slogan']}</h1>
        <p style="font-size: 24px; color: #cbd5e1; max-width: 800px; margin: 0 auto;">{T['sub_slogan']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 模拟区块高度
    block_num = random.randint(245000000, 245999999)
    st.markdown(f"<div style='text-align: center; margin-bottom: 40px; color:#4ade80;'>{T['live_status']}{block_num}</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        # 这里特别注明是 Console (演示版)
        if st.button(T['btn_launch'], use_container_width=True):
            set_page('dashboard')
            st.rerun()
    
    # 渲染底部 (现在每个访问者第一时间就能看到法律条款)
    render_footer()

# --- 2. 控制台 (Dashboard - Demo Mode) ---
elif st.session_state.page == 'dashboard':
    with st.sidebar:
        st.write("👤 **Guest / Demo User**") # 修正：不再显示 CEO，避免误会
        st.info("Demo Mode Active")
        if st.button(T['back']): set_page('landing'); st.rerun()

    st.title("📊 Security Dashboard (Demo)")
    
    # 模拟数据
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Assets", "1,248")
    k2.metric("Threats", "53", "High", delta_color="inverse")
    k3.metric("Legal", "41")
    k4.metric("Saved", "$12,400")
    
    st.markdown("---")
    st.caption("Upload & Protect features are in simulation mode.")
    
    # 依然展示底部，保持合规
    render_footer()

# --- 3. 法律条款详情页 (Legal View) ---
elif st.session_state.page == 'legal_view':
    st.button(T['back'], on_click=lambda: set_page('landing'))
    st.markdown("---")
    
    # 获取当前要看的条款内容
    view_key = st.session_state.get('view_legal', 'tos')
    content = L_TEXT.get(view_key, "Content not found.")
    
    # 渲染条款
    st.markdown(f"""
    <div style="background: rgba(15, 23, 42, 0.6); padding: 40px; border-radius: 12px; border: 1px solid #334155;">
        {content}
    </div>
    """, unsafe_allow_html=True)
    
    render_footer()
