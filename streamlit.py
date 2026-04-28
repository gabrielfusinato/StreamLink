import streamlit as st
from app import store_long_url, get_full_url
import webbrowser
import streamlit.components.v1 as components

params = st.query_params
hash = params.get("sl")

site = get_full_url(hash)

current_url = st.context.url

if site:
    if not site.startswith("http"):
        site = "https://" + site
    print("opening new tab: " + site)
    webbrowser.open(site, new = 0, autoraise=True)
    st.stop()

st.title("Stream:blue[Link]")
st.divider()

url_input = st.text_input("Enter your link below:")

if st.button("Type here to get link.", type="primary"):
    if url_input.strip() == "":
        st.warning("Please, input a valid URL.")

    else:
        tiny_alias = store_long_url(url_input)
        st.divider()
        st.write("Click to copy your compressed link:")
        st.code(current_url + "?sl=" + tiny_alias)
        st.success("Done!")





