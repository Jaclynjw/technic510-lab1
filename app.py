import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Jiawen Chen - Student, Vlogger",
    page_icon="👨🏻‍💻",
    layout="centered",
    initial_sidebar_state="auto",
)

# Profile Section
col1, col2 = st.columns([0.3, 0.7])
with col1:
    # Display the profile image with rounded corners
    st.image("https://github.com/Jaclynjw/technic510-lab1/blob/main/image/profile.jpg?raw=true", width=200)

with col2:
    # Display the name, education, and vlogging info using modern font
    st.markdown(
        """
        # Jiawen Chen (She/Her)
        
        - Master student at [Tsinghua University & UW](https://www.linkedin.com/in/jiawen-chen-43b7ab292/)
        - Vlogger at [Xiaohongshu](https://www.xiaohongshu.com/user/profile/5ac5dceee8ac2b0ecbeab2e2?xhsshare=CopyLink&appuid=5ac5dceee8ac2b0ecbeab2e2&apptime=1711494076)
        """,
        unsafe_allow_html=True,
    )

# Education Section
st.markdown("## Education", unsafe_allow_html=True)
st.markdown(
    """
    - BE @ Tsinghua University, 2018-2022
    - Dual MS @ University of Washington & Tsinghua University, 2022-Present
    """,
    unsafe_allow_html=True,
)

# About Me Section
st.markdown("## About Me", unsafe_allow_html=True)
st.markdown("### Coder | Singer | Vlogger | INFP", unsafe_allow_html=True)
st.markdown("I enjoy coding, singing, photography and travelling. Here are some snapshots of my adventures.", unsafe_allow_html=True)

# Display images in columns with rounded corners
col1, col2, col3 = st.columns([0.3, 0.3, 0.3])
with col1:
    st.image("https://github.com/Jaclynjw/technic510-lab1/blob/main/image/photo1.jpg?raw=true", caption="Photography", use_column_width=True)
with col2:
    st.image("https://github.com/Jaclynjw/technic510-lab1/blob/main/image/photo2.jpg?raw=true", caption="Hiking", use_column_width=True)  
with col3:
    st.image("https://github.com/Jaclynjw/technic510-lab1/blob/main/image/photo3.jpg?raw=true", caption="Coding Project", use_column_width=True)

# Contact Information
st.markdown("## Contact", unsafe_allow_html=True)
st.markdown(
    """
    - Email: [chenjw18@uw.edu](mailto:chenjw18@uw.edu)
    - LinkedIn: [Jiawen Chen](https://www.linkedin.com/in/jiawen-chen-43b7ab292/)
    """,
    unsafe_allow_html=True,
)

# Apply custom CSS to hide the Streamlit footer and adjust other styles
st.markdown(
    """
    <style>
    /* Hide the Streamlit footer */
    .main footer {visibility: hidden;}
    
    /* Additional custom styles */
    body {
        font-family: Arial, sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: Arial, sans-serif;
    }
    .stMarkdown p {
        font-family: Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
