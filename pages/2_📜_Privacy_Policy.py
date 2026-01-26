import streamlit as st

st.set_page_config(
    page_title="隐私政策 - OriginGuard",
    page_icon="📜",
    layout="wide"
)

# Matrix theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    * {
        font-family: 'JetBrains Mono', 'Courier New', monospace !important;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #0a0a0a 100%);
    }
    
    h1, h2, h3 {
        color: #00ff41 !important;
        text-shadow: 0 0 10px #00ff41;
        font-weight: 700 !important;
    }
    
    p, li {
        color: #00ff41 !important;
        font-size: 16px !important;
        line-height: 1.8 !important;
    }
    
    .stMarkdown {
        color: #00ff41 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("📜 隐私政策 Privacy Policy")

st.markdown("""
## 信息收集 Information Collection

**OriginGuard承诺：我们不收集、不存储任何用户数据。**

**OriginGuard Promise: We DO NOT collect or store ANY user data.**

### 我们不收集的信息 What We Don't Collect:
- ❌ 个人身份信息 (姓名、邮箱、电话)
- ❌ IP地址或设备信息
- ❌ 上传的文件或内容
- ❌ 浏览历史或使用数据
- ❌ Cookie或追踪信息

## 数据处理 Data Processing

### 100% 本地处理 100% Local Processing
- ✅ 所有DNA指纹生成在您的浏览器本地完成
- ✅ 文件不会上传到任何服务器
- ✅ 数据不会离开您的设备
- ✅ 处理完成后立即清除

### 零数据存储 Zero Data Storage
- ✅ 不使用数据库
- ✅ 不使用云存储
- ✅ 不保留任何缓存
- ✅ 不记录任何日志

## 区块链隐私 Blockchain Privacy

### Solana区块链记录 Solana Blockchain Records
- DNA指纹哈希值会记录在Solana区块链上
- 区块链记录是公开的、不可篡改的
- 只存储哈希值，不存储原始文件
- 无法从哈希值反推原始内容

### 匿名性保证 Anonymity Guarantee
- 区块链交易不关联个人身份
- 使用匿名钱包地址
- 不要求实名认证

## 第三方服务 Third-Party Services

### Streamlit云托管 Streamlit Cloud Hosting
- 应用托管在Streamlit Community Cloud
- Streamlit可能收集基本访问日志
- 详见Streamlit隐私政策：https://streamlit.io/privacy-policy

### Solana区块链 Solana Blockchain
- 区块链交易公开可查询
- 详见Solana隐私说明：https://solana.com/privacy-policy

## 用户权利 User Rights

### 您的数据控制权 Your Data Control
- ✅ 完全控制上传文件
- ✅ 随时停止使用服务
- ✅ 无需删除账户（因为我们不创建账户）
- ✅ 无需担心数据泄露（因为我们不存储数据）

## 安全措施 Security Measures

### 技术保护 Technical Protection
- ✅ HTTPS加密传输
- ✅ 浏览器端处理
- ✅ 无服务器端存储
- ✅ 定期安全审计

### 零信任架构 Zero Trust Architecture
- 不信任任何中间环节
- 不依赖服务器存储
- 不使用第三方数据处理

## 儿童隐私 Children's Privacy

- 本服务不针对13岁以下儿童
- 我们不主动收集儿童信息
- 如发现儿童数据，将立即删除

## 政策更新 Policy Updates

### 更新通知 Update Notification
- 重大变更将在应用内通知
- 建议定期查看本政策
- 继续使用即表示接受更新

## 联系我们 Contact Us

### 隐私问题咨询 Privacy Inquiries
如有隐私相关问题，请通过GitHub Issues联系：
https://github.com/minnyinyioo/originguard-app/issues

---

## 核心承诺 Core Promise

### 🛡️ OriginGuard隐私承诺

**我们承诺：**
1. 永不收集用户个人信息
2. 永不存储用户上传内容
3. 永不出售或共享用户数据
4. 永不使用追踪技术
5. 永不要求实名认证

**We Promise:**
1. Never collect user personal information
2. Never store user uploaded content
3. Never sell or share user data
4. Never use tracking technologies
5. Never require real-name authentication

---

*最后更新 Last Updated: 2025-01-10*

*本隐私政策符合GDPR、CCPA等国际隐私法规要求*

*This Privacy Policy complies with GDPR, CCPA and international privacy regulations*
""")

st.success("✅ 您的隐私是我们的首要任务 Your Privacy is Our Top Priority")
