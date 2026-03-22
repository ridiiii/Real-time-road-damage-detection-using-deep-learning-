import streamlit as st
from PIL import Image
from utils import detect_image, detect_video

# Page configuration
st.set_page_config(
    page_title="AI Road Inspection System",
    page_icon="🚧",
    layout="wide"
)

# ---------- Custom CSS for better UI ----------
st.markdown("""
<style>
.main-title {
    font-size:40px;
    font-weight:bold;
}

.banner {
    background: linear-gradient(90deg,#ff5f6d,#ffc371);
    padding:25px;
    border-radius:12px;
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:25px;
}

.section-text{
    font-size:18px;
}

.stButton>button {
    background-color:#ff5f6d;
    color:white;
    border-radius:10px;
    padding:10px 20px;
    font-size:16px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.title("🚧 Road Inspection")
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🖼 Image Detection", "🎥 Video Detection"]
)

# ---------- HOME PAGE ----------
if page == "🏠 Home":

    st.markdown('<p class="main-title">AI Based Road Inspection System</p>', unsafe_allow_html=True)

    st.markdown(
        '<div class="banner">Welcome to the Future of Road Safety!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-text">

        This platform uses a **YOLOv8 deep learning model** to automatically detect potholes
        and road damage from images and videos.

        ### Key Features
        • Automatic pothole detection  
        • Image based detection  
        • Video based detection  
        • Fast AI powered results  

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- IMAGE DETECTION ----------
elif page == "🖼 Image Detection":

    st.title("Image Detection")

    uploaded_file = st.file_uploader(
        "Upload a road image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Start Detection"):

            with st.spinner("Detecting potholes..."):

                result = detect_image(image)

                st.success("Detection Complete!")

                st.image(result, caption="Detection Result", use_column_width=True)


# ---------- VIDEO DETECTION ----------
elif page == "🎥 Video Detection":

    st.title("Video Detection")

    uploaded_video = st.file_uploader(
        "Upload a road video",
        type=["mp4","avi","mov"]
    )

    if uploaded_video:

        st.video(uploaded_video)

        if st.button("Start Detection"):

            with st.spinner("Processing video..."):

                output_video = detect_video(uploaded_video)

            st.success("Video Processed!")

            st.video(output_video)