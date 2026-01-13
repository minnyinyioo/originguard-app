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
        "tos": """### 1. Acceptance of Terms
By accessing OriginGuard, you agree to be bound by these Terms.

### 2. Authorized Use
You affirm that you are the lawful copyright owner of uploaded content. Uploading stolen content will result in immediate ban.

### 3. Limitation
We provide blockchain evidence, not legal outcomes.""",
        "refund": """### NO REFUND POLICY (STRICT)
**Gas fees are paid instantly to the Solana network.**

**ALL SALES ARE FINAL.**
Once a transaction is initiated, it cannot be canceled, reversed, or refunded.
By using this service, you waive your right to a cooling-off period.""",
        "privacy": """### Data Privacy
1. **Data Minimization:** We only hash files.
2. **No Storage:** We do not store original images.
3. **Ownership:** Your data remains yours.""",
        "sla": """### Enterprise SLA
We guarantee **99.9%** API Uptime for Enterprise subscribers.
Credits are issued for downtime exceeding limits.""",
        "disclaimer": """### Legal Disclaimer
OriginGuard is a technology provider, **not a law firm**.
The "Legal Hammer" tools are for reference only."""
    },
    "中文": {
        "tos": """### 1. 服务条款
访问即表示同意本条款。如果您不同意，请立即停止使用。

### 2. 授权使用
严禁上传盗版内容。一旦发现，我们将立即封禁账号。

### 3. 责任限制
我们提供区块链技术证据，但不承诺特定的法庭判决结果。""",
        "refund": """### 🚫 无退款政策 (No Refund)
**Gas 费已实时支付给区块链网络。**

**所有交易均为最终交易。**
OriginGuard 不支持任何形式的退款、撤销或回滚操作。
请在支付前仔细确认。""",
        "privacy": """### 🔒 隐私政策
1. **数据最小化**：我们只存储文件的数字哈希值。
2. **不存原图**：您的原始高清图片从未上传到我们的服务器。
3. **数据主权**：数据归您所有。""",
        "sla": """### ⚡ SLA 服务承诺
对于企业版订阅用户，我们承诺 **99.9%** 的 API 在线率。
如未达标，我们将按照合同约定进行赔偿。""",
        "disclaimer": """### ⚠️ 免责声明
OriginGuard 是一家技术提供商，而**非律师事务所**。
我们提供的“自动律师函”仅供参考，不构成法律建议。"""
    },
    "Myanmar": {
        "tos": """### စည်းမျဉ်းများ
ဤဝန်ဆောင်မှုကို အသုံးပြုခြင်းဖြင့် စည်းကမ်းများကို လိုက်နာရန် သဘောတူပါသည်။""",
        "refund": """### ငွေပြန်မအမ်းပါ (No Refund)
Blockchain ငွေပေးချေမှုများသည် ပြင်ဆင်၍မရပါ။
**ငွေပြန်အမ်းခြင်း မပြုလုပ်နိုင်ပါ။**""",
        "privacy": """### လုံခြုံရေး
သင့်ပုံများကို ကျွန်ုပ်တို့ သိမ်းဆည်းမထားပါ။""",
        "sla": """### SLA အာမခံချက်
၉၉.၉% အချိန်ပြည့် အလုပ်လုပ်မည်။""",
        "disclaimer": """### ငြင်းဆိုချက်
ကျွန်ုပ်တို့သည် နည်းပညာကိုသာ ပံ့ပိုးပေးသည်။"""
    }
}

# ==========================================
# 3. 动态 CSS (V4.2: 高对比度 + 真实组件)
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
        color: #ffffff !important; 
        font-family: 'Inter', 'Padauk', 'Noto Sans Myanmar', sans-serif !important;
    }
    
    .stApp::before {
        content
