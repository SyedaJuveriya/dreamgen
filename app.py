import streamlit as st

st.set_page_config(page_title="DreamGen", layout="centered")

st.title("🎬 DreamGen")
st.subheader("Turn your ideas into AI-generated videos")

prompt = st.text_area("Describe your video idea:")

if st.button("Generate Video"):
    if prompt.strip() == "":
        st.warning("Please enter a video idea.")
    else:
        with st.spinner("Generating video using AI..."):
            st.success("Video generated successfully!")

            st.write("**Your Prompt:**")
            st.info(prompt)

            st.write("**Generated Video (Preview):**")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
