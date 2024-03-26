import streamlit as st

st.set_page_config(
    page_title="Jiawen Chen - Student, Vlogger",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

#Profile Section
col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 20%;
    }
    </style>

    <div class="profile-img">

    ![](https://github.com/Jaclynjw/technic510-lab1/blob/main/image/profile.jpg?raw=true)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('https://avatars.githubusercontent.com/u/7678108?v=4')
with col2:
    st.markdown(
        """
    # Jiawen Chen (She/Her)
                
    - Master student at [Tsinghua University & UW](https://www.linkedin.com/in/jiawen-chen-43b7ab292/)
    - Vlogger at [Xiaohongshu](https://www.xiaohongshu.com/user/profile/5ac5dceee8ac2b0ecbeab2e2?xhsshare=CopyLink&appuid=5ac5dceee8ac2b0ecbeab2e2&apptime=1711494076)
    """
    )

#Education Section
st.markdown("## Education")
st.markdown("""
- BE @ Tsinghua University, 2018-2022
- Dual MS @ University of Washington & Tsinghua University, 2022-Present
""")

# About Me Section
st.markdown("## About Me")
st.markdown("### Coder | Singer | Vlogger | INFP")
st.markdown("I enjoy coding, singing, photography and travelling. Here are some snapshots of my adventures.")
col1, col2, col3 = st.columns([0.3, 0.3, 0.3])
with col1:
    st.markdown(
        f"""
        <img src="https://github.com/Jaclynjw/technic510-lab1/blob/main/image/photo1.jpg?raw=true" style="border-radius: 10px; width: 100%;">
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        f"""
        <img src="https://github.com/Jaclynjw/technic510-lab1/blob/main/image/photo2.jpg?raw=true" style="border-radius: 10px; width: 100%;">
        """,
        unsafe_allow_html=True
    )   
with col3:
    st.markdown(
        f"""
        <img src="https://github.com/Jaclynjw/technic510-lab1/blob/main/image/photo3.jpg?raw=true" style="border-radius: 10px; width: 100%;">
        """,
        unsafe_allow_html=True
    )

# Contact
st.markdown("## Contact")
st.markdown("""
- Email: [chenjw18@uw.edu]
- LinkedIn: [https://www.linkedin.com/in/jiawen-chen-43b7ab292/] 
""")

ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)