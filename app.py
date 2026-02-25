import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Page Moved", page_icon="🚀")

# Center the content using columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2983/2983780.png", width=100)
    st.title("We have moved!")
    
    st.info("Our application has been relocated to a new web address to provide a better experience.")
    
    # Define your new URL
    new_url = "golf-swing-analyzer.up.railway.app"
    
    # Use a large Link Button for the redirect
    st.link_button(f"Go to {new_url}", new_url, type="primary", use_container_width=True)
    
    st.write("---")
    st.caption("Please update your bookmarks. You will be redirected manually by clicking the button above.")
