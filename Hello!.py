import streamlit as st

st.set_page_config(
    page_title="Welcome to Janna's Website!",
    page_icon=":blossom:",
)

st.write("# Welcome to Janna's Website!")

st.sidebar.success("Go Green!")

st.markdown(
    """
    This website was made by me to practice and expand my knowledge of the open-source app framework
    commonly known as Streamlit.  

    **Select the tabs on the sidebar to learn more about me!**
    
""")
st.image("https://images.unsplash.com/photo-1631582053308-40f482e7ace5?q=80&w=1031&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",width = 500)
st.markdown(
     """Want to connect?
    - Check out my [LinkedIn!](https://www.linkedin.com/in/janna-salera-743833237/)
    
    """
)
