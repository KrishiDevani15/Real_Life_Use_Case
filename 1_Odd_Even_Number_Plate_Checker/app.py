import streamlit as st
# Main Ui
about_page = st.Page("./sub_module/welcome_page.py", title="Welcome 👋🏻")
number_checker_page = st.Page("./sub_module/number_checker.py", title="Vehicle Number Checker 🅿️")

pg = st.navigation([about_page, number_checker_page])
pg.run()

st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    ---
    👨‍💻 Made by [Krishi Devani](https://github.com/KrishiDevani15)

    ☕ If this app helped you, consider buying me a virtual coffee.  
    Or just enjoy a real one while coding!

    ---
    """
)