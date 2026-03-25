import streamlit as st
import time
import re

# ─── PAGE CONFIGURATION ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Gostyy Forensic Lab",
    page_icon="🛡️",
    layout="centered"
)

# ─── 🧪 CSS (GLASSY THEME + INTENSE SHAKE) ───────────────────────────────
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=JetBrains+Mono&display=swap');

    .stApp {{
        background-color: #000000 !important;
        color: #ffffff !important;
    }}

    /* 💎 إعادة التأثير الزجاجي للبار العلوي (Glassy Header) */
    header, [data-testid="stHeader"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
    }}

    /* ⚡ INTENSE SCREEN SHAKE ⚡ */
    @keyframes intenseShake {{
        0% {{ transform: translate(0, 0); }}
        10% {{ transform: translate(-15px, -15px); }}
        20% {{ transform: translate(15px, 15px); }}
        30% {{ transform: translate(-15px, 15px); }}
        40% {{ transform: translate(15px, -15px); }}
        50% {{ transform: translate(-15px, -15px); }}
        60% {{ transform: translate(15px, 15px); }}
        100% {{ transform: translate(0, 0); }}
    }}

    .shake-active {{
        animation: intenseShake 0.5s cubic-bezier(.36,.07,.19,.97) both !important;
    }}

    .gostyy-title {{
        font-weight: 700;
        text-align: center;
        font-size: 2.8rem;
        margin-top: 50px;
        text-shadow: 0px 0px 20px rgba(255, 255, 255, 0.2);
    }}

    /* 📄 Input Area Glassy */
    .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.03) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(5px);
    }}

    /* 🔘 Button Highlight & Glow */
    .stButton > button {{
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 700 !important;
        width: 100%;
        height: 55px;
        border-radius: 8px !important;
        border: none !important;
        transition: 0.3s all ease;
    }}

    .stButton > button:hover {{
        background-color: #cccccc !important;
        box-shadow: 0px 0px 25px rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-2px);
    }}

    /* 🛡️ Result Expanders */
    .stExpander {{
        background-color: rgba(255, 75, 75, 0.05) !important;
        border: 1px solid rgba(255, 75, 75, 0.2) !important;
        border-radius: 10px !important;
    }}
</style>
""", unsafe_allow_html=True)

# ─── HIGH PRECISION ENGINE (RE-BUILT) ────────────────────────────────────
def run_audit(code):
    findings = []
    
    # تحسين الأنماط لتكون أكثر دقة وشمولية
    patterns = {
        "Hardcoded Secrets": {
            # يلقط المفاتيح حتى لو كانت بدون علامة = (مثل JSON أو Config)
            "reg": r"(api[_-]?key|password|secret|token|aws[_-]?key|auth|credential|db_pass|access[_-]?key|secret[_-]?key)\s*[:=]?\s*['\"][a-zA-Z0-9/+=_\-]{8,}['\"]",
            "info": "Sensitive credential or token discovered in source code.",
            "fix": "Use environment variables (.env) or a secret manager like Vault."
        },
        "Cross-Site Scripting (XSS)": {
            "reg": r"(\.innerHTML|\.outerHTML|document\.write\(|eval\(|window\.name\s*=|setTimeout\(.*['\"]<script)",
            "info": "Insecure DOM manipulation could lead to malicious script execution.",
            "fix": "Sanitize inputs and use .textContent instead of .innerHTML."
        },
        "SQL Injection": {
            "reg": r"(SELECT|INSERT|UPDATE|DELETE|DROP).*WHERE.*(\+|f['\"]|\.format|%|concat|str\(|\+.*=)",
            "info": "String concatenation in SQL queries detected.",
            "fix": "Switch to parameterized queries to prevent injection."
        },
        "Command Injection": {
            "reg": r"(os\.system|subprocess\.(call|Popen|run|check_output)|eval|exec|shell_exec|system)\s*\(",
            "info": "Direct OS command execution with potential user input.",
            "fix": "Use safe API alternatives and validate all inputs."
        }
    }

    for name, data in patterns.items():
        if re.search(data["reg"], code, re.I):
            findings.append({"type": name, "info": data["info"], "fix": data["fix"]})
            
    return findings

# ─── MAIN INTERFACE ─────────────────────────────────────────────────────
def main():
    st.markdown('<div class="gostyy-title">Gostyy Forensic Lab</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; margin-bottom: 30px;'>v6.1 Global | Advanced Precision & Glassy VFX</p>", unsafe_allow_html=True)

    code_input = st.text_area("Analysis Sandbox", height=300, placeholder="// Drop suspicious code for forensic audit...")

    if st.button("RUN SECURITY AUDIT"):
        if code_input.strip():
            results = run_audit(code_input)
            
            if results:
                # 🛑 إطلاق الاهتزاز فوراً (JS Injection)
                st.markdown("""
                    <script>
                        var el = window.parent.document.querySelector(".stApp");
                        el.classList.remove("shake-active");
                        void el.offsetWidth;
                        el.classList.add("shake-active");
                    </script>
                """, unsafe_allow_html=True)
                
                st.markdown(f"### ⚠️ {len(results)} Vulnerabilities Detected")
                for r in results:
                    with st.expander(f"🚫 {r['type']}"):
                        st.write(f"**Description:** {r['info']}")
                        st.info(f"**Recommendation:** {r['fix']}")
            else:
                st.balloons()
                st.success("✅ Clean Code Detected. No threats found in this segment.")
        else:
            st.info("Please paste some code to begin the analysis.")

if __name__ == "__main__":
    main()
