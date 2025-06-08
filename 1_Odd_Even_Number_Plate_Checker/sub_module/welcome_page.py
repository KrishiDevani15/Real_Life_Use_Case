import streamlit as st

st.set_page_config(page_title="Welcome",page_icon="👋🏻")
st.title("Welcome to Car Number Plate Checker! 🙋🏼‍♂️")
st.markdown(
    """
    # 🚗 Odd-Even Vehicle Rule Checker
    Welcome to the Odd-Even Vehicle System — inspired by real-world traffic control policies!

    👉 Enter your **vehicle number** to check if you're **allowed to drive today** under the odd-even rule.

    ---
    ### 📘 How it Works:
    - ✅ Allowed if the **last digit** of your vehicle **matches the parity** of today’s **date**.
    - ❌ Not allowed if one is odd and the other is even.

    Example:
    - Vehicle ends in `5` (odd) and today is `7` → ✅ Park Right  
    - Vehicle ends in `6` (even) and today is `7` → ⛔ No Parking Left

    ---
    """
)
