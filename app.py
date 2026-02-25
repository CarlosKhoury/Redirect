import streamlit as st

# 1. Set the page configuration
st.set_page_config(page_title="Moved", layout="centered")

# 2. Define your URL
new_url = "golf-swing-analyzer.up.railway.app"

# 3. Create the "We have moved" message
st.title("📢 We have moved!")

st.write(f"""
Our application is now hosted at a new address. 
Please update your bookmarks to stay connected.
""")

# 4. The Hyperlink
# Markdown syntax: [Text](URL)
st.markdown(f"### 👉 [Click here to go to {new_url}]({new_url})")

# Optional: Add a visual divider
st.divider()

st.caption("If the link doesn't work, please copy and paste it into your browser address bar.")
