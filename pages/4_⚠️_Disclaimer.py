import streamlit as st

st.set_page_config(
    page_title="免责声明 - OriginGuard",
    page_icon="⚠️",
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

st.title("⚠️ 免责声明 Disclaimer")

st.markdown("""
## 重要通知 Important Notice

**在使用OriginGuard服务之前，请务必仔细阅读本免责声明。使用本服务即表示您已阅读、理解并接受本声明的所有内容。**

**Please read this Disclaimer carefully before using OriginGuard. By using our service, you acknowledge that you have read, understood, and accepted all terms herein.**

---

## 1. 服务性质声明 Service Nature Disclaimer

### 1.1 技术证明而非法律结论 Technical Proof, Not Legal Conclusion
OriginGuard提供的DNA指纹和区块链存证记录属于**技术性证据**。虽然我们采用先进的AI和区块链技术，但这些记录：
- ❌ 不等同于法律上的著作权登记证书
- ❌ 不保证在所有国家的法律体系中被自动采纳为决定性证据
- ❌ 不构成任何形式的法律意见或专业建议

### 1.2 "按原样"提供 "As-Is" Provision
本服务按"按原样"（As-Is）和"按可用性"（As-Available）基础提供。我们不提供任何形式的明示或暗示保证。

---

## 2. 内容真实性免责 Authenticity Disclaimer

### 2.1 用户上传内容责任 User Responsibility
OriginGuard**不负责审核**用户上传内容的原创性、合法性或真实性。
- ✅ 如果用户上传他人的作品进行认证，该认证在法律上是无效的。
- ✅ 用户应对其上传的所有内容承担全部法律责任。

### 2.2 冒名顶替风险 Impersonation Risks
如果他人窃取您的作品并在您之前进行认证，OriginGuard无法自动识别谁才是真正的原作者。我们建议您在作品创作完成后**第一时间**进行存证。

---

## 3. 技术限制免责 Technical Limitations Disclaimer

### 3.1 AI识别限制 AI Identification Limits
尽管我们的AI DNA指纹技术具有极高的精确度，但在以下极端情况下可能存在偏差：
- 极微小的修改或高度重合的通用素材。
- AI生成内容的混淆。
- 图像或视频质量极差导致的识别误差。

### 3.2 区块链风险 Blockchain Risks
OriginGuard基于Solana区块链。我们不对以下区块链相关风险承担责任：
- 网络拥堵导致的延迟。
- 节点故障。
- 区块链本身的技术性风险。

### 3.3 数据持久性 Data Persistence
由于我们实行**零数据存储政策**，如果您丢失了本地保存的认证报告，我们**无法**为您找回或恢复任何数据。

---

## 4. 法律锤与监控免责 Legal Hammer & Monitoring Disclaimer

### 4.1 监控覆盖范围 Monitoring Coverage
24/7实时监控覆盖主流视频及社交平台，但由于互联网的庞大和封闭平台的限制，我们不保证能监测到100%的侵权行为。

### 4.2 法律锤效果 Legal Hammer Effectiveness
"法律锤"（Legal Hammer）功能旨在提供维权协助和证据支持。
- ❌ 我们不代表您提起诉讼。
- ❌ 我们不保证维权一定成功。
- ❌ 最终的维权结果取决于司法机关或平台方的裁决。

---

## 5. 责任限制 Limitation of Liability

在任何情况下，OriginGuard及其开发者不对因使用或无法使用本服务而产生的以下损失承担责任：
- ❌ 利润损失、业务中断。
- ❌ 任何间接、附带、特别或后果性损害。
- ❌ 由于第三方侵权行为造成的任何损失。

---

## 6. 核心承诺 Core Commitment

**虽然有上述免责条款，但我们郑重承诺：**
1. ✅ **100% 安全**：我们不存储您的任何原始数据。
2. ✅ **100% 公正**：技术逻辑对所有用户一视同仁。
3. ✅ **持续更新**：我们将不断优化算法以提高保护力度。

---

## 🛡️ 保护您的原创，我们是认真的

OriginGuard致力于成为全球创作者的坚强后盾。我们通过技术手段大幅降低维权成本，提高侵权代价。

---

*最后更新 Last Updated: 2025-01-10*

*Version 1.0*

**如果您不同意本声明的任何内容，请立即停止使用本服务。**

**If you do not agree with any part of this disclaimer, please stop using the service immediately.**
""")
