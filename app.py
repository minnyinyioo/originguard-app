import streamlit as st
import streamlit.components.v1 as components

# --- OriginGuard System Configuration ---
st.set_page_config(
    page_title="OriginGuard App",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- The Super App UI (HTML/CSS/JS Injection) ---
# 这是我们之前设计的“国民级钱包”界面，完美移植到 Streamlit
html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+Myanmar:wght@400;700&display=swap" rel="stylesheet">

<style>
    body { background-color: #000; display: flex; justify-content: center; font-family: 'Inter', 'Noto Sans Myanmar', sans-serif; margin: 0; padding: 0; }
    
    .mobile-screen {
        width: 100%; max-width: 450px; /*稍微调宽一点适配网页*/
        background: #0f172a; min-height: 100vh;
        position: relative; padding-bottom: 80px;
    }

    /* --- Header --- */
    .header {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        padding: 20px 20px 40px 20px;
        border-bottom-left-radius: 25px;
        border-bottom-right-radius: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    
    .user-info { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    .avatar { width: 40px; height: 40px; background: #334155; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #22c55e; border: 2px solid #22c55e; }
    .notif { position: relative; color: #fff; font-size: 20px; cursor:pointer; }
    .badge { position: absolute; top: -5px; right: -5px; background: #ef4444; width: 8px; height: 8px; border-radius: 50%; }

    .balance-area { text-align: center; color: white; margin-top: 10px; }
    .balance-label { font-size: 12px; color: #94a3b8; margin-bottom: 5px; }
    .amount-box { display: flex; justify-content: center; align-items: center; gap: 10px; font-size: 32px; font-weight: 800; }
    .hidden-dots { letter-spacing: 5px; font-size: 24px; display: none; }
    .eye-icon { font-size: 16px; color: #64748b; cursor: pointer; padding: 5px; }

    /* --- Quick Actions --- */
    .quick-actions { display: flex; justify-content: space-around; margin-top: -30px; padding: 0 10px; }
    .action-btn {
        background: #1e293b; border: 1px solid #334155;
        width: 75px; height: 75px; border-radius: 15px;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        box-shadow: 0 10px 15px rgba(0,0,0,0.3); cursor: pointer;
        transition: transform 0.1s;
    }
    .action-btn:active { transform: scale(0.95); }
    .action-icon { font-size: 26px; margin-bottom: 5px; }
    .action-text { font-size: 11px; color: #cbd5e1; font-weight: bold; }
    .scan { color: #22c55e; } .receive { color: #3b82f6; } .topup { color: #facc15; } .history { color: #ef4444; }

    /* --- Grid Section --- */
    .grid-section { padding: 30px 20px; }
    .section-title { color: #fff; font-size: 14px; font-weight: bold; margin-bottom: 15px; border-left: 3px solid #22c55e; padding-left: 10px; }
    .grid-container { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }
    .grid-item { text-align: center; cursor: pointer; }
    .grid-icon-box { 
        width: 50px; height: 50px; background: rgba(255,255,255,0.05); 
        border-radius: 12px; margin: 0 auto 8px auto; 
        display: flex; align-items: center; justify-content: center; font-size: 20px; color: #94a3b8; transition: all 0.2s;
    }
    .grid-item:hover .grid-icon-box { background: rgba(34, 197, 94, 0.1); color: #22c55e; }
    .grid-label { font-size: 10px; color: #94a3b8; line-height: 1.2; }

    /* --- Banner --- */
    .banner { padding: 0 20px; margin-bottom: 20px; }
    .banner-inner { background: linear-gradient(90deg, #22c55e 0%, #15803d 100%); border-radius:12px; padding:15px; display:flex; justify-content:space-between; align-items:center; color:black; cursor: pointer; }

    /* --- Bottom Nav --- */
    .bottom-nav {
        position: fixed; bottom: 0; width: 100%; max-width: 450px;
        background: #1e293b; border-top: 1px solid #334155;
        display: flex; justify-content: space-around; padding: 10px 0 20px 0; z-index: 99;
    }
    .nav-item { text-align: center; color: #64748b; font-size: 10px; cursor: pointer; }
    .nav-item.active { color: #22c55e; }
    .nav-icon { font-size: 20px; margin-bottom: 4px; display: block; }
    .nav-scan-wrapper { position: relative; top: -30px; }
    .nav-scan-btn {
        width: 60px; height: 60px; background: #22c55e; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 20px rgba(34, 197, 94, 0.4); border: 4px solid #0f172a;
        color: #000; font-size: 24px;
    }
</style>
</head>
<body>

<div class="mobile-screen">
    
    <div class="header">
        <div class="user-info">
            <div class="avatar"><i class="fas fa-user-astronaut"></i></div>
            <div style="flex:1; margin-left:10px; color:white;">
                <div style="font-size:12px; opacity:0.8">Hello, CEO</div>
                <div style="font-weight:bold;">MNNO</div>
            </div>
            <div class="notif" onclick="alert('System: All Systems Operational')"><i class="far fa-bell"></i><div class="badge"></div></div>
        </div>

        <div class="balance-area">
            <div class="balance-label">Total Asset Balance (USD)</div>
            <div class="amount-box">
                <span id="bal-txt">$158.00</span>
                <span id="bal-hide" class="hidden-dots">••••••</span>
                <i class="fas fa-eye eye-icon" onclick="toggleBalance()"></i>
            </div>
            <div style="font-size:12px; color:#64748b; margin-top:5px;">≈ 790,000 MMK</div>
        </div>
    </div>

    <div class="quick-actions">
        <div class="action-btn" onclick="alert('Camera Access Request: Scanning Code...')">
            <i class="fas fa-qrcode action-icon scan"></i>
            <div class="action-text">Scan</div>
        </div>
        <div class="action-btn" onclick="alert('Opening KBZ/Stripe Gateway...')">
            <i class="fas fa-wallet action-icon topup"></i>
            <div class="action-text">Cash In</div>
        </div>
        <div class="action-btn" onclick="alert('Generating Payment Link...')">
            <i class="fas fa-hand-holding-usd action-icon receive"></i>
            <div class="action-text">Receive</div>
        </div>
        <div class="action-btn" onclick="alert('Loading Transaction History...')">
            <i class="fas fa-history action-icon history"></i>
            <div class="action-text">History</div>
        </div>
    </div>

    <div class="grid-section">
        <div class="section-title">OriginGuard Core</div>
        <div class="grid-container">
            <div class="grid-item" onclick="alert('Upload your photo to start protection.')">
                <div class="grid-icon-box"><i class="fas fa-copyright"></i></div>
                <div class="grid-label">Upload<br>& Protect</div>
            </div>
            <div class="grid-item" onclick="alert('Fetching Blockchain Certificates...')">
                <div class="grid-icon-box"><i class="fas fa-certificate"></i></div>
                <div class="grid-label">My<br>Certs</div>
            </div>
            <div class="grid-item" onclick="alert('Initiating AI Legal Hammer...')">
                <div class="grid-icon-box"><i class="fas fa-gavel"></i></div>
                <div class="grid-label">Legal<br>Hammer</div>
            </div>
            <div class="grid-item" onclick="alert('Scanning Facebook for stolen images...')">
                <div class="grid-icon-box"><i class="fas fa-search-location"></i></div>
                <div class="grid-label">Radar<br>Scan</div>
            </div>
            <div class="grid-item" onclick="alert('You have 2000 Points! Redeem now.')">
                <div class="grid-icon-box"><i class="fas fa-gift"></i></div>
                <div class="grid-label">Points<br>Rewards</div>
            </div>
            <div class="grid-item" onclick="alert('Connecting to AI Support Bot...')">
                <div class="grid-icon-box"><i class="fas fa-headset"></i></div>
                <div class="grid-label">AI<br>Support</div>
            </div>
            <div class="grid-item">
                <div class="grid-icon-box"><i class="fas fa-file-contract"></i></div>
                <div class="grid-label">Legal<br>Docs</div>
            </div>
            <div class="grid-item">
                <div class="grid-icon-box"><i class="fas fa-ellipsis-h"></i></div>
                <div class="grid-label">More</div>
            </div>
        </div>
    </div>

    <div class="banner">
        <div class="banner-inner" onclick="alert('Referral Link Copied!')">
            <div>
                <div style="font-weight:bold; font-size:14px;">Invite Friend</div>
                <div style="font-size:10px;">Get 500 Points Free!</div>
            </div>
            <i class="fas fa-user-plus" style="font-size:24px;"></i>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-item active">
            <i class="fas fa-home nav-icon"></i> Home
        </div>
        <div class="nav-item">
            <i class="fas fa-wallet nav-icon"></i> Wallet
        </div>
        <div class="nav-scan-wrapper">
            <div class="nav-scan-btn" onclick="alert('Scan...')"><i class="fas fa-expand"></i></div>
        </div>
        <div class="nav-item">
            <i class="fas fa-bell nav-icon"></i> Notify
        </div>
        <div class="nav-item">
            <i class="fas fa-user nav-icon"></i> Me
        </div>
    </div>

</div>

<script>
    let isHidden = false;
    function toggleBalance() {
        const txt = document.getElementById('bal-txt');
        const dots = document.getElementById('bal-hide');
        const icon = document.querySelector('.eye-icon');
        
        isHidden = !isHidden;
        
        if(isHidden) {
            txt.style.display = 'none';
            dots.style.display = 'block';
            icon.classList.remove('fa-eye');
            icon.classList.add('fa-eye-slash');
        } else {
            txt.style.display = 'block';
            dots.style.display = 'none';
            icon.classList.remove('fa-eye-slash');
            icon.classList.add('fa-eye');
        }
    }
</script>

</body>
</html>
"""

# Render the HTML in Streamlit
components.html(html_code, height=850, scrolling=True)

# Add a footer for the CEO
st.caption("OriginGuard v1.0 | System Status: Online 🟢 | Designed for CEO MNNO")
