import streamlit as st

# 1. Define your destination
new_url = "golf-swing-analyzer.up.railway.app"  # Replace with your actual destination

st.title("Moving to a New Home 🏠")

st.write("We have officially moved our application.")

# 2. Use a standard HTML link that forces a new tab
# target="_blank" is the key here to stop the "looping"
html_link = f'<a href="{new_url}" target="_blank" style="font-size: 24px; color: #ff4b4b; text-decoration: none; font-weight: bold;">👉 Click here to open the new site</a>'

st.markdown(html_link, unsafe_allow_html=True)

st.info("Note: The new site will open in a separate browser tab.")
