import streamlit as st
from app import store_long_url

#DEIXAR MAIS BONITINNHO DEPOIS
st.title("Stream:blue[Link]")
st.divider()

#INTEGRAR COM BACK
url_input = st.text_input("Enter your link below:")

if st.button("Type here to get link.", type="primary"):
    if url_input.strip() == "":
        st.warning("Please, input a valid URL.")

    else:
        tiny_alias = store_long_url(url_input)
        st.divider()
        st.write("Click to copy your compressed link:")
        st.code("https://streamlink/" + tiny_alias)
        st.success("Done!")

