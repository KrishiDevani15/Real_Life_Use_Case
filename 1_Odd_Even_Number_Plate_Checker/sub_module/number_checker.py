import streamlit as st
import time
from datetime import datetime
st.set_page_config(page_title="Parking Checker",page_icon="🅿️")
st.title("Welcome to Car Number Plate Checker! 🙋🏼‍♂️")
vehicle_number = st.text_input("🔢 Enter your vehicle number (e.g. DL3CAF1234)")


def numberChecker(last_digit,today_day):
    if (last_digit % 2 == 0 and today_day % 2 == 0):
        return st.success(f"🎉 Even number vehicle `{vehicle_number}` detected. You are **ALLOWED** to drive today 😁.")
    elif (last_digit % 2 != 0 and today_day % 2 != 0):
        return st.success(f"🎉 Odd number vehicle `{vehicle_number}` detected. You are **ALLOWED** to drive today 😁.")
    else:
        return st.warning(f"👀 Vehicle `{vehicle_number}` is **NOT ALLOWED** to drive today 😩.")


if st.button("Check Parking 🅿️"):
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    if not vehicle_number or not vehicle_number[-1].isdigit():
        st.error("❌ Please enter a valid vehicle number ending with a digit.")

    else:
        last_digit = int(vehicle_number[-1])
        today_day = datetime.now().day

        result = numberChecker(last_digit,today_day)

    
    

