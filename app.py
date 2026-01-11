import streamlit as st
import time

# ==========================================
# 1. 页面基础设置 (Page Setup)
# ==========================================
# 浏览器标签页标题通常保持英文通用，或使用品牌名
st.set_page_config(
    page_title="OriginGuard Global",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. 纯净语言包字典 (Strict Language Dictionary)
# ==========================================
# 这里的每一行都严格区分，绝不混用
translations = {
    "English": {
        # Navigation & Sidebar
        "sidebar_title": "OriginGuard® Enterprise",
        "nav_menu_title": "Navigation",
        "nav_home": "Home",
        "nav_dash": "Console",
        "user_role": "Verified User: CEO MNNO",
        "status_active": "Status: ✅ Pro Plan Active",
        "lang_select": "Language / 语言",
        
        # Hero Section (Home)
        "hero_title": "Protect What You Create.",
        "hero_sub": "The world's first AI-powered copyright protection platform backed by Blockchain immutability.",
        "btn_launch": "Launch Enterprise Console",
        "toast_welcome": "Accessing Secure Environment...",
        "sidebar_hint": "Please access the Console via the Sidebar menu.",
        
        # Features
        "feat_title": "Core Technology",
        "f1_title": "Invisible Watermark", "f1_desc": "Military-grade hidden encryption.",
        "f2_title": "Blockchain Evidence", "f2_desc": "Immutable ledger on Solana.",
        "f3_title": "Global Enforcement", "f3_desc": "Automated legal strikes in 180+ countries.",
        
        # Trust Badges
        "trust_soc2": "SOC2 Certified",
        "trust_gdpr": "GDPR Compliant",
        "trust_pay": "Secure Payment",
        "trust_dmca": "DMCA Verified",
        
        # Dashboard
        "dash_header": "Enterprise Dashboard",
        "dash_status": "System Operational",
        "dash_net": "Network: Solana Mainnet",
        "kpi_1": "Assets Protected",
        "kpi_2": "Threats Blocked",
        "kpi_3": "Legal Savings",
        "kpi_4": "Uptime",
        "tab_1": "🛡️ Protect",
        "tab_2": "🔍 Monitor",
        "tab_3": "⚖️ Enforce",
        
        # Functional Areas
        "upload_header": "Secure Asset Upload",
        "upload_label": "Drag and drop files here (End-to-End Encrypted)",
        "upload_btn": "Encrypt & Mint",
        "processing": "Processing...",
        "step_1": "Embedding Invisible DNA...",
        "step_2": "Minting to Blockchain...",
        "success_msg": "Success! Certificate #OG-2026-X99 generated.",
        
        # Footer
        "footer_text": "© 2026 OriginGuard Inc. | Global Privacy Standard | San Francisco • Bangkok • Yangon"
    },
    
    "中文": {
        # 导航与侧边栏
        "sidebar_title": "OriginGuard® 企业版",
        "nav_menu_title": "系统导航",
        "nav_home": "官网首页",
        "nav_dash": "管理控制台",
        "user_role": "已验证用户: CEO MNNO",
        "status_active": "状态: ✅ 专业版已激活",
        "lang_select": "语言 / Language",
        
        # 主视觉 (首页)
        "hero_title": "不仅是保护，更是确权。",
        "hero_sub": "全球首个 AI 驱动的去中心化版权保护平台。为创作者构建的数字长城。",
        "btn_launch": "启动企业控制台",
        "toast_welcome": "正在接入安全环境...",
        "sidebar_hint": "请通过侧边栏菜单进入控制台。",
        
        # 核心功能
        "feat_title": "核心技术引擎",
        "f1_title": "隐形水印矩阵", "f1_desc": "军工级加密，肉眼不可见。",
        "f2_title": "区块链存证", "f2_desc": "Solana 链上永久铭刻证据。",
        "f3_title": "全球自动维权", "f3_desc": "覆盖180+国家的自动法务打击。",
        
        # 信任背书
        "trust_soc2": "SOC2 安全认证",
        "trust_gdpr": "符合欧盟 GDPR",
        "trust_pay": "支付安全保障",
        "trust_dmca": "DMCA 维权认证",
        
        # 控制台
        "dash_header": "企业级管理控制台",
        "dash_status": "系统运行正常",
        "dash_net": "网络: Solana 主网",
        "kpi_1": "已保护资产",
        "kpi_2": "已拦截威胁",
        "kpi_3": "节省律师费",
        "kpi_4": "在线率",
        "tab_1": "🛡️ 资产确权",
        "tab_2": "🔍 全网监控",
        "tab_3": "⚖️ 法务打击",
        
        # 功能区
        "upload_header": "资产安全上传",
        "upload_label": "拖拽文件至此 (端到端加密通道)",
        "upload_btn": "加密并上链",
        "processing": "正在处理中...",
        "step_1": "正在植入隐形 DNA...",
        "step_2": "正在铸造区块链证书...",
        "success_msg": "成功！已生成证书 #OG-2026-X99。",
        
        # 底部
        "footer_text": "© 2026 OriginGuard Inc. | 全球隐私合规标准 | 旧金山 • 曼谷 • 仰光"
    },
    
    "မြန်မာ (Myanmar)": {
        # Navigation
        "sidebar_title": "OriginGuard® Enterprise",
        "nav_menu_title": "မီနူး",
        "nav_home": "ပင်မစာမျက်နှာ",
        "nav_dash": "ဒက်ရှ်ဘုတ်",
        "user_role": "အတည်ပြုပြီး: CEO MNNO",
        "status_active": "အခြေအနေ: ✅ Pro Plan Active",
        "lang_select": "ဘာသာစကား",
        
        # Hero
        "hero_title": "သင်၏ ဖန်တီးမှုများကို ကာကွယ်ပါ။",
        "hero_sub": "AI နှင့် Blockchain နည်းပညာသုံး ကမ္ဘာ့ပထမဆုံး မူပိုင်ခွင့် ကာကွယ်ရေး ပလက်ဖောင်း။",
        "btn_launch": "ဒက်ရှ်ဘုတ် သို့သွားရန်",
        "toast_welcome": "လုံခြုံသော စနစ်သို့ ဝင်ရောက်နေသည်...",
        "sidebar_hint": "ဒက်ရှ်ဘုတ်ကို ဘေးဘက်မီနူးမှတဆင့် ဝင်ရောက်ပါ။",
        
        # Features
        "feat_title": "အဓိက နည်းပညာများ",
        "f1_title": "မမြင်ရသော ရေစာ", "f1_desc": "ပုံရိပ်များတွင် လျှို့ဝှက်စွာ ထည့်သွင်းထားသော လုံခြုံရေး။",
        "f2_title": "Blockchain မှတ်တမ်း", "f2_desc": "Solana ပေါ်တွင် ပြောင်းလဲ၍မရသော ပိုင်ဆိုင်မှု။",
        "f3_title": "ကမ္ဘာလုံးဆိုင်ရာ ဥပဒေ", "f3_desc": "နိုင်ငံပေါင်း ၁၈၀ ကျော်တွင် အလိုအလျောက် အရေးယူဆောင်ရွက်မှု။",
        
        # Trust
        "trust_soc2": "SOC2 လက်မှတ်",
        "trust_gdpr": "GDPR ကိုက်ညီမှု",
        "trust_pay": "လုံခြုံသော ငွေပေးချေမှု",
        "trust_dmca": "DMCA အတည်ပြုချက်",
        
        # Dashboard
        "dash_header": "စီမံခန့်ခွဲမှု ဒက်ရှ်ဘုတ်",
        "dash_status": "စနစ် ပုံမှန်လည်ပတ်နေသည်",
        "dash_net": "ကွန်ရက်: Solana Mainnet",
        "kpi_1": "ကာကွယ်ပြီး",
        "kpi_2": "တားဆီးထားသော",
        "kpi_3": "ချွေတာငွေ",
        "kpi_4": "Uptime",
        "tab_1": "🛡️ ကာကွယ်ရန်",
        "tab_2": "🔍 စောင့်ကြည့်ရန်",
        "tab_3": "⚖️ အရေးယူရန်",
        
        # Functions
        "upload_header": "ဖိုင်တင်သွင်းရန်",
        "upload_label": "ဖိုင်များကို ဤနေရာတွင် ထည့်ပါ (Encrypted)",
        "upload_btn": "Encrypt လုပ်မည်",
        "processing": "ဆောင်ရွက်နေသည်...",
        "step_1": "DNA ထည့်သွင်းနေသည်...",
        "step_2": "Blockchain မှတ်တမ်းတင်နေသည်...",
        "success_msg": "အောင်မြင်သည်! လက်မှတ် #OG-2026-X99 ရရှိပါပြီ။",
        
        # Footer
        "footer_text": "© 2026 OriginGuard Inc. | နိုင်ငံတကာ လုံခြုံရေး စံချိန်စံညွှန်းများ"
    }
}

# ==========================================
# 3. 样式注入 (CSS Styling)
# ==========================================
st.markdown("""
<style>
    /* 引入字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+Myanmar:wght@400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', 'Noto Sans Myanmar', sans-serif; }
    
    /* 按钮样式 */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white; border: none; padding: 0.5rem 1rem; border-radius: 8px; font-weight: 600;
        transition: all 0.2s;
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2); }
    
    /* 信任标识栏 */
    .trust-bar {
        display: flex; justify-content: center; gap: 30px; margin-top: 30px;
        padding: 20px; background: rgba(255,255,255,0.03); border-radius: 12px;
        flex-wrap: wrap;
    }
    .trust-item { font-size: 13px; color: #94a3b8; display: flex; align-items: center; gap: 6px; }
    
    /* 隐藏默认菜单 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. 逻辑控制器 (Main Controller)
# ==========================================

# 4.1 侧边栏 (Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9370/9370126.png", width=60) # 示例Logo
    
    # 语言选择
