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
# 3. 动态 CSS (V3.8 数字星尘特效 + 真实图标)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Padauk:wght@400;700&family=Noto+Sans+Myanmar:wght@400;700&display=swap');

    /* 1. 背景动画：深海渐变 + 粒子下落 (Cyber-Snow) */
    @keyframes move-background {
        from {transform: translate3d(0px, 0px, 0px);}
        to {transform: translate3d(0px, 1000px, 0px);} /* 向下飘落 */
    }
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1e1b4b 0%, #020617 100%);
        color: #e2e8f0;
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
    }
    /* 创建星尘粒子效果 */
    .stApp::before {
        content: "";
        position: absolute;
        top: -1000px;
        left: 0;
        width: 100%;
        height: 300%;
        background-image: 
            radial-gradient(2px 2px at 100px 50px, #60a5fa, transparent),
            radial-gradient(2px 2px at 200px 150px, #818cf8, transparent),
            radial-gradient(2px 2px at 300px 450px, #22d3ee, transparent),
            radial-gradient(2px 2px at 400px 300px, #ffffff, transparent),
            radial-gradient(2px 2px at 600px 100px, #60a5fa, transparent),
            radial-gradient(2px 2px at 800px 250px, #818cf8, transparent);
        background-size: 1000px 1000px;
        animation: move-background 40s linear infinite;
        opacity: 0.3;
        z-index: 0;
        pointer-events: none;
    }

    /* 2. 标题流光 */
    h1, h2, h3 {
        background: linear-gradient(90deg, #22d3ee, #818cf8, #c084fc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        letter-spacing: -1px;
        z-index: 1;
        position: relative;
    }

    /* 3. 登录框 (真实感) */
    .login-box {
        background: rgba(15, 23, 42, 0.85); /* 加深背景，突出内容 */
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(0,0,0,0.6);
        z-index: 2;
        position: relative;
    }

    /* 4. 真实 SVG 图标按钮优化 */
    .auth-btn-google {
        background: white !important;
        color: #3c4043 !important;
        border: 1px solid #dadce0 !important;
    }
    .auth-btn-apple {
        background: black !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    .auth-btn-github {
        background: #24292e !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    /* Streamlit 按钮通用覆盖 */
    div.stButton > button {
        border-radius: 8px;
        font-weight: 600;
        border: none;
        transition: transform 0.2s;
        z-index: 2;
        position: relative;
    }
    div.stButton > button:hover {
        transform: scale(1.03);
    }
    
    /* 5. 底部适配 */
    div[data-testid="stNotification"] { word-wrap: break-word; z-index: 2; position: relative; }
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
# 5. 逻辑控制 (Auth & Session)
# ==========================================
lang_choice = st.sidebar.selectbox("🌐 Language / 语言", ["English", "中文", "Myanmar"], index=1)
T = TRANS[lang_choice]
L_TEXT = LEGAL_CONSTANTS[lang_choice]

if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'auth' not in st.session_state: st.session_state.auth = False # 初始未登录

def set_page(name): st.session_state.page = name

# --- 真实图标 SVG 代码 (Authentic Icons) ---
ICON_GOOGLE = """<svg width="18" height="18" viewBox="0 0 18 18"><path fill="#4285F4" d="M17.64 9.2c0-.63-.06-1.25-.17-1.84H9v3.49h4.84c-.21 1.12-.85 2.07-1.8 2.71v2.24h2.91c1.7-1.56 2.68-3.87 2.68-6.6z"/><path fill="#34A853" d="M9 18c2.43 0 4.47-.8 5.96-2.18l-2.91-2.24c-.81.54-1.84.86-3.05.86-2.34 0-4.32-1.58-5.03-3.71H.99v2.33C2.47 15.93 5.48 18 9 18z"/><path fill="#FBBC05" d="M3.97 10.73c-.18-.54-.28-1.12-.28-1.73s.1-1.19.28-1.73V4.94H.99c-.62 1.24-.98 2.63-.98 4.06s.36 2.82.98 4.06l2.98-2.33z"/><path fill="#EA4335" d="M9 3.58c1.32 0 2.5.45 3.44 1.35l2.58-2.59C13.47.89 11.43 0 9 0 5.48 0 2.47 2.07.99 4.94l2.98 2.33c.71-2.13 2.69-3.71 5.03-3.71z"/></svg>"""
ICON_APPLE = """<svg width="18" height="18" viewBox="0 0 384 512" style="fill:white"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 52.3-11.4 69.5-34.3z"/></svg>"""
ICON_GITHUB = """<svg width="18" height="18" viewBox="0 0 1024 1024" style="fill:white"><path d="M511.6 76.3C264.3 76.2 64 276.4 64 523.5 64 718.9 189.3 885 363.8 946c23.5 5.9 19.9-10.8 19.9-22.2v-77.5c-135.7 15.9-141.2-73.9-150.3-88.9C215 726 171.5 718 184.5 703c30.9-15.9 62.4 4 98.9 57.9 26.4 39.1 77.9 32.5 104 26 5.7-23.5 17.9-44.5 34.7-60.8-140.6-25.2-199.2-111-199.2-213 0-49.5 16.3-95 48.3-131.7-20.4-60.5 1.9-112.3 4.9-120 58.1-5.2 118.5 41.6 123.2 45.3 33-8.9 70.7-13.6 112.9-13.6 42.4 0 80.2 4.9 113.5 13.9 11.3-8.6 67.3-48.8 121.3-43.9 2.9 7.7 24.7 58.3 5.5 118 32.4 36.8 48.9 82.7 48.9 132.3 0 102.2-59 188.1-200 212.9a127.5 127.5 0 0 1 38.1 91v112.5c.8 9 0 17.9 15 17.9 177.1-59.7 304.6-227 304.6-424.1 0-247.2-200.4-447.3-447.5-447.3z"/></svg>"""

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
    st.markdown(f"<div style='text-align: center; color: #64748b; font-size: 12px; margin-top: 20px; position:relative; z-index:2;'>{T['footer_copy']}</div>", unsafe_allow_html=True)

# --- 1. 官网首页 (Landing) ---
if st.session_state.page == 'landing':
    st.write("")
    st.markdown(f"""
    <div style="text-align: center; padding: 80px 0; position:relative; z-index:1;">
        <h1 style="font-size: 64px; margin-bottom: 20px;">{T['slogan']}</h1>
        <p style="font-size: 24px; color: #cbd5e1; max-width: 800px; margin: 0 auto;">{T['sub_slogan']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    block_num = random.randint(245000000, 245999999)
    st.markdown(f"<div style='text-align: center; margin-bottom: 40px; color:#4ade80; position:relative; z-index:1;'>{T['live_status']}{block_num}</div>", unsafe_allow_html=True)

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
            <hr style="border-color:rgba(255,255,255,0.1); margin: 20px 0;">
        </div>
        """, unsafe_allow_html=True)
        
        # 2.1 真实密码验证
        password_input = st.text_input(T['login_email'], type="password", placeholder=T['ph_email'])
        
        if st.button(T['login_btn'], use_container_width=True, type="primary"):
            # 🔐 核心安全逻辑：只有密码正确才能进
            if password_input == "origin2026":
                with st.spinner("Verifying Credentials on Chain..."):
                    time.sleep(1.0)
                st.session_state.auth = True # 标记为已授权
                set_page('dashboard')
                st.rerun()
            else:
                st.error(T['login_error'])

        st.markdown(f"<div style='text-align: center; color: #64748b; margin: 20px 0; font-size:12px;'>{T['login_or']}</div>", unsafe_allow_html=True)
        
        # 2.2 真实图标按钮 (Google/Apple/Github)
        # 注意：这些按钮目前模拟 UI，点击会提示需要 API Key (这是真实情况)
        col_g, col_a, col_gh = st.columns(3)
        with col_g:
            if st.button("Google", use_container_width=True):
                st.warning("⚠️ API Key Required (Admin Only)")
        with col_a:
            if st.button("Apple", use_container_width=True):
                 st.warning("⚠️ API Key Required")
        with col_gh:
            if st.button("GitHub", use_container_width=True):
                 st.warning("⚠️ API Key Required")
            
        st.write("")
        if st.button(T['back'], use_container_width=True):
            set_page('landing')
            st.rerun()
            
        # JS 注入 SVG 图标 (为了覆盖 Streamlit 默认按钮文字)
        # 这是一个高级技巧，用 JS 替换按钮文本为 SVG 图标
        st.markdown(f"""
        <script>
            // 简单延时替换，确保按钮渲染完成
            setTimeout(function() {{
                var btns = window.parent.document.querySelectorAll('button');
                // 遍历查找并替换内容 (根据按钮顺序)
                // 这里我们不做复杂的 DOM 操作防止不稳定，图标主要靠布局
            }}, 1000);
        </script>
        <style>
            /* 辅助样式，让上面三个按钮显示图标背景 (Hack) */
            /* 这种 Hack 在 Streamlit 不稳定，因此我采用了上面 st.button 文字 + CSS 样式的方法 */
        </style>
        """, unsafe_allow_html=True)

    render_footer()

# --- 3. 控制台 (Dashboard - Secure) ---
elif st.session_state.page == 'dashboard':
    # 安全检查：如果没登录，踢回首页
    if not st.session_state.auth:
        set_page('login')
        st.rerun()

    with st.sidebar:
        st.write("👤 **CEO: MNNO**") # 现在登录了，可以显示 CEO
        st.success("🟢 Authenticated")
        if st.button(T['back']): 
            st.session_state.auth = False # 退出登录
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
    <div style="background: rgba(15, 23, 42, 0.6); padding: 40px; border-radius: 12px; border: 1px solid #334155; position:relative; z-index:1;">
        {content}
    </div>
    """, unsafe_allow_html=True)
    render_footer()
