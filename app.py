# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import random
import time

# ==========================================
# 1. 核心配置 (Core Config)
# ==========================================
st.set_page_config(
    page_title="OriginGuard Web3",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. 法律文本常量库 (IMMUTABLE LEGAL TEXTS)
# ==========================================
# 严禁修改合同内容
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
# 3. 动态 CSS (V3.9 晶透高亮版)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 1. 背景动画：深海渐变 + 粒子下落 */
    @keyframes move-background {
        from {transform: translate3d(0px, 0px, 0px);}
        to {transform: translate3d(0px, 1000px, 0px);}
    }
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
        /* 全局字体颜色改为极亮白，解决“看不清”问题 */
        color: #f8fafc !important; 
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
    }
    
    /* 星尘粒子层 */
    .stApp::before {
        content: "";
        position: absolute;
        top: -1000px;
        left: 0;
        width: 100%;
        height: 300%;
        background-image: 
            radial-gradient(2px 2px at 100px 50px, #22d3ee, transparent),
            radial-gradient(2px 2px at 300px 450px, #818cf8, transparent),
            radial-gradient(1.5px 1.5px at 600px 100px, #ffffff, transparent);
        background-size: 1000px 1000px;
        animation: move-background 40s linear infinite;
        opacity: 0.4;
        z-index: 0;
        pointer-events: none;
    }

    /* 2. 标题流光 + 字幕浮动 (New Feature) */
    h1 {
        background: linear-gradient(90deg, #22d3ee, #a78bfa, #c084fc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        letter-spacing: -1px;
        animation: gradientText 4s linear infinite;
        text-shadow: 0 0 20px rgba(34, 211, 238, 0.3); /* 增加发光，提高清晰度 */
    }
    
    /* 悬浮动画：用于副标题和说明文字 */
    @keyframes float-text {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0px); }
    }
    .floating-text {
        animation: float-text 6s ease-in-out infinite;
        color: #e2e8f0; /* 亮灰白 */
        text-shadow: 0 2px 4px rgba(0,0,0,0.8); /* 黑色阴影衬托文字 */
    }

    @keyframes gradientText {
        0% {background-position: 0% center;}
        100% {background-position: 200% center;}
    }

    /* 3. 卡片与容器：加深背景色，提高文字对比度 */
    div[data-testid="stMetric"], div.stInfo, div.stWarning, div.stError, div.stSuccess, .login-box {
        background: rgba(2, 6, 23, 0.85) !important; /* 85% 不透明度的深黑背景 */
        backdrop-filter: blur(15px);
        border: 1px solid rgba(148, 163, 184, 0.2); /* 边框调亮 */
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
        color: #ffffff !important; /* 强制纯白文字 */
        border-radius: 16px;
        z-index: 2;
        position: relative;
    }
    
    /* 缅甸语防爆适配 */
    div[data-testid="stNotification"], p, div {
        word-wrap: break-word;
    }

    /* 4. 按钮样式增强 */
    div.stButton > button {
        border: none;
        font-weight: 700;
        letter-spacing: 0.5px;
        transition: all 0.3s;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.6);
    }
    
    /* 谷歌按钮白底适配 */
    button:has(div:contains("Google")) {
        border: 1px solid #e2e8f0 !important;
    }
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
        "back": "⬅️ Back",
        # Login
        "login_title": "Sign in to OriginGuard",
        "login_email": "Enter Access Code / Password",
        "login_btn": "Sign In",
        "login_error": "⚠️ Invalid Access Code. Please contact admin.",
        "login_or": "OR CONTINUE WITH",
        "ph_email": "e.g. origin2026",
    },
    "中文": {
        "slogan": "捍卫你的数字资产",
        "sub_slogan": "Web3 版权保护全球标准 | 自动确权与维权",
        "btn_launch": "🚀 启动控制台",
        "live_status": "🟢 实时连接: Solana 主网区块高度 #",
        "footer_warning": "⚠️ 重要提示：区块链交易均为最终交易。Gas 费概不退款。",
        "footer_copy": "© 2026 OriginGuard Solutions. 泰国暖武里总部.",
        "titles": ["服务条款", "无退款政策", "隐私政策", "SLA承诺", "免责声明"],
        "back": "⬅️ 返回",
        # Login
        "login_title": "登录 OriginGuard",
        "login_email": "输入访问密钥 / 密码",
        "login_btn": "登录",
        "login_error": "⚠️ 密钥错误。请联系管理员获取。",
        "login_or": "或通过以下方式继续",
        "ph_email": "例如：origin2026",
    },
    "Myanmar": {
        "slogan": "ဖန်တီးမှုများကို ကာကွယ်ပါ",
        "sub_slogan": "Web3 မူပိုင်ခွင့် ကာကွယ်ရေး | ကမ္ဘာ့အဆင့်မီ နည်းပညာ",
        "btn_launch": "🚀 စနစ်စတင်မည်",
        "live_status": "🟢 တိုက်ရိုက်: Solana Mainnet Block #",
        "footer_warning": "⚠️ အရေးကြီးသည် - Blockchain ငွေပေးချေမှုများသည် ပြင်ဆင်၍မရပါ။ ငွေပြန်အမ်းမည် မဟုတ်ပါ။",
        "footer_copy": "© 2026 OriginGuard Solutions.",
        "titles": ["စည်းမျဉ်းများ", "ငွေပြန်မအမ်းပါ", "လုံခြုံရေး", "SLA", "ငြင်းဆိုချက်"],
        "back": "⬅️ ပြန်သွားရန်",
        # Login
        "login_title": "အကောင့်ဝင်ပါ",
        "login_email": "စကားဝှက် ထည့်ပါ",
        "login_btn": "ဝင်မည်",
        "login_error": "⚠️ စကားဝှက် မှားယွင်းနေသည်။",
        "login_or": "အခြားနည်းဖြင့် ဝင်မည်",
        "ph_email": "origin2026 ကို ရိုက်ထည့်ပါ",
    }
}

# ==========================================
# 5. 逻辑控制
# ==========================================
lang_choice = st.sidebar.selectbox("🌐 Language / 语言", ["English", "中文", "Myanmar"], index=1)
T = TRANS[lang_choice]
L_TEXT = LEGAL_CONSTANTS[lang_choice]

if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'auth' not in st.session_state: st.session_state.auth = False 

def set_page(name): st.session_state.page = name

# --- 公共底部组件 ---
def render_footer():
    st.write("")
    st.markdown("---")
    st.error(T['footer_warning'])
    cols = st.columns(5)
    labels = T['titles']
    keys = ["tos", "refund", "privacy", "sla", "disclaimer"]
    for i, col in enumerate(cols):
        if col.button(labels[i], key=f"btn_{keys[i]}", use_container_width=True):
            st.session_state.view_legal = keys[i]
            set_page('legal_view')
            st.rerun()
    st.markdown(f"<div style='text-align: center; color: #94a3b8; font-size: 12px; margin-top: 20px; position:relative; z-index:2;'>{T['footer_copy']}</div>", unsafe_allow_html=True)

# --- 1. 官网首页 (Landing) ---
if st.session_state.page == 'landing':
    st.write("")
    
    # 使用 floating-text class 让字幕动起来
    st.markdown(f"""
    <div style="text-align: center; padding: 80px 0; position:relative; z-index:1;">
        <h1 style="font-size: 64px; margin-bottom: 20px;">{T['slogan']}</h1>
        <p class="floating-text" style="font-size: 24px; max-width: 800px; margin: 0 auto; font-weight: 600;">
            {T['sub_slogan']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    block_num = random.randint(245000000, 245999999)
    st.markdown(f"<div style='text-align: center; margin-bottom: 40px; color:#22d3ee; font-weight:bold; position:relative; z-index:1;'>{T['live_status']}{block_num}</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(T['btn_launch'], use_container_width=True):
            set_page('login') 
            st.rerun()
    
    render_footer()

# --- 2. 真实登录页 (Real Login Gate) ---
elif st.session_state.page == 'login':
    st.write("")
    st.write("")
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown(f"""
        <div class="login-box">
            <h2 style="margin-bottom: 10px;">{T['login_title']}</h2>
            <hr style="border-color:rgba(255,255,255,0.2); margin: 20px 0;">
        </div>
        """, unsafe_allow_html=True)
        
        # 密码输入
        password_input = st.text_input(T['login_email'], type="password", placeholder=T['ph_email'])
        
        if st.button(T['login_btn'], use_container_width=True, type="primary"):
            if password_input == "origin2026":
                with st.spinner("Verifying Credentials..."):
                    time.sleep(1.0)
                st.session_state.auth = True 
                set_page('dashboard')
                st.rerun()
            else:
                st.error(T['login_error'])

        st.markdown(f"<div style='text-align: center; color: #cbd5e1; margin: 20px 0; font-size:12px;'>{T['login_or']}</div>", unsafe_allow_html=True)
        
        # 模拟 OAuth 按钮
        col_g, col_a, col_gh = st.columns(3)
        with col_g:
            if st.button("Google", use_container_width=True):
                st.warning("⚠️ API Configuration Required (Production)")
        with col_a:
            if st.button("Apple", use_container_width=True):
                 st.warning("⚠️ API Configuration Required")
        with col_gh:
            if st.button("GitHub", use_container_width=True):
                 st.warning("⚠️ API Configuration Required")
            
        st.write("")
        if st.button(T['back'], use_container_width=True):
            set_page('landing')
            st.rerun()

    render_footer()

# --- 3. 控制台 (Dashboard - Secure) ---
elif st.session_state.page == 'dashboard':
    if not st.session_state.auth:
        set_page('login')
        st.rerun()

    with st.sidebar:
        st.write("👤 **CEO: MNNO**")
        st.success("🟢 Authenticated")
        if st.button(T['back']): 
            st.session_state.auth = False
            set_page('landing')
            st.rerun()

    st.title("📊 Security Dashboard")
    
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Assets", "1,248")
    k2.metric("Threats", "53", "High", delta_color="inverse")
    k3.metric("Legal", "41")
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
    
    render_footer()

# --- 4. 法律详情页 ---
elif st.session_state.page == 'legal_view':
    st.button(T['back'], on_click=lambda: set_page('landing'))
    st.markdown("---")
    view_key = st.session_state.get('view_legal', 'tos')
    content = L_TEXT.get(view_key, "Content not found.")
    st.markdown(f"""
    <div style="background: rgba(2, 6, 23, 0.9); padding: 40px; border-radius: 12px; border: 1px solid #334155; position:relative; z-index:1; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        {content}
    </div>
    """, unsafe_allow_html=True)
    render_footer()
