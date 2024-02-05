import streamlit as st


st.header("For starters, my name is **Janna Salera**")
st.markdown("""I am currently a Freshman at :green[*Michigan State University*],
            where I study Electrical Engineering (and not Computer Science).
            Now, get to know each other better by checking off similar hobbies.
            """)
st.divider()
st.markdown("**My Hobbies and Interests!**")

cats = st.checkbox('Cats')
seafood = st.checkbox('Seafood')
ghibli = st.checkbox('Studio Ghibli')

if ghibli:
    st.markdown("""Could not agree more! From music to animation, Studio Ghibli movies are just the best.
                My personal favorite is Ponyo. Additional fun fact: I have Studio Ghibli wallpapers on *all* of my devices.""")
    st.image("https://i.pinimg.com/originals/5b/da/71/5bda710b17751fd6611537b839938162.jpg")

if seafood:
    st.markdown("""Nothing is better than a good old seafood boil! 
                I love all types of seafood from lobster to mussels but,
                if I had to choose, I would pick crabs as my favorite seafood dish.""")
    st.image("https://i.pinimg.com/564x/33/88/08/338808aa54d28b8037fd6e8a16d4f84f.jpg", width = 500)
if cats:
    st.markdown("""Wow, I love cats as well! I plan to get an orange cat sometime in the future
                and we would take the best naps together.""")
    st.image("https://i.pinimg.com/564x/4c/43/d2/4c43d27dd0b4f5737aac6bb1fe189a4b.jpg", width = 650)