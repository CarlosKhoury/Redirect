import streamlit as st

def redirect_to(url):
    """
    Redirects the user using an HTML meta refresh tag.
    This bypasses Streamlit Cloud's iframe sandbox restrictions.
    """
    nav_script = f"""
        <meta http-equiv="refresh" content="0; url='{url}'">
    """
    st.markdown(nav_script, unsafe_allow_html=True)

st.title("Redirecting...")

# Call the function with your target URL
target_website = "golf-swing-analyzer.up.railway.app" 
redirect_to(target_website)
