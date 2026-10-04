import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Forest AI Monitoring System",
    page_icon="🌲",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #173b2b;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 21px;
        color: #456b58;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #234b36;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .metric-card {
        padding: 22px;
        border-radius: 14px;
        background-color: #f4f8f5;
        border: 1px solid #d9e7dd;
        text-align: center;
        min-height: 135px;
    }

    .metric-label {
        font-size: 17px;
        color: #52675a;
    }

    .metric-value {
        font-size: 35px;
        font-weight: 700;
        color: #173b2b;
        margin-top: 10px;
    }

    .workflow-box {
        padding: 18px 10px;
        border-radius: 12px;
        background-color: #f6faf7;
        border: 1px solid #d5e5da;
        text-align: center;
        min-height: 135px;
    }

    .workflow-number {
        font-size: 22px;
        font-weight: bold;
        color: #2d704b;
    }

    .workflow-name {
        font-size: 16px;
        font-weight: 600;
        color: #263d30;
        margin-top: 10px;
    }

    .info-box {
        padding: 18px;
        border-radius: 12px;
        background-color: #f7faf8;
        border-left: 5px solid #4d8b65;
        margin-bottom: 15px;
    }

    .footer {
        text-align: center;
        color: #6b7770;
        padding: 30px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("🌲 System Modules")

module = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Forest Health Analysis",
        "Encroachment Detection",
        "Recovery Prediction"
    ]
)

st.sidebar.markdown("---")

st.sidebar.subheader("Technology Used")

st.sidebar.write("• Python")
st.sidebar.write("• Streamlit")
st.sidebar.write("• Image Processing")
st.sidebar.write("• U-Net Concept")
st.sidebar.write("• NDVI / NDWI")

st.sidebar.markdown("---")
st.sidebar.info(
    "Satellite-driven AI prototype for forest health, "
    "encroachment monitoring and recovery prediction."
)


# =========================================================
# TITLE
# =========================================================
st.markdown(
    '<div class="main-title">🌲 Satellite-Driven AI System for Forest Health</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Encroachment Detection and Recovery Prediction using U-Net</div>',
    unsafe_allow_html=True
)

st.write(
    "AI-based prototype for satellite image analysis, forest health "
    "assessment, encroachment monitoring and recovery prediction."
)


# =========================================================
# IMAGE UPLOAD
# =========================================================
st.markdown(
    '<div class="section-title">📤 Upload Satellite / Forest Image</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


# =========================================================
# DEMO ANALYSIS FUNCTION
# =========================================================
def analyze_image(image):

    img = image.convert("RGB")
    arr = np.array(img).astype(np.float32)

    # Normalize
    arr = arr / 255.0

    red = arr[:, :, 0]
    green = arr[:, :, 1]
    blue = arr[:, :, 2]

    # Simple green vegetation estimation
    green_ratio = np.mean(green > red * 1.05)

    # Vegetation index-like demo calculation
    ndvi_demo = (green - red) / (green + red + 0.001)
    ndvi_value = float(np.mean(ndvi_demo))

    # Water-like estimation
    ndwi_demo = (green - blue) / (green + blue + 0.001)
    ndwi_value = float(np.mean(ndwi_demo))

    # Convert vegetation percentage
    vegetation = green_ratio * 100

    # Demo forest health
    forest_health = int(np.clip(vegetation + 30, 20, 95))

    # Demo encroachment risk
    encroachment_risk = int(np.clip(100 - forest_health + 10, 5, 85))

    # Recovery prediction
    if forest_health >= 70:
        recovery = "High"
    elif forest_health >= 45:
        recovery = "Medium"
    else:
        recovery = "Low"

    # Health classification
    if forest_health >= 70:
        healthy = 65
        stressed = 25
        deforested = 10
    elif forest_health >= 45:
        healthy = 40
        stressed = 35
        deforested = 25
    else:
        healthy = 20
        stressed = 35
        deforested = 45

    return {
        "health": forest_health,
        "encroachment": encroachment_risk,
        "recovery": recovery,
        "healthy": healthy,
        "stressed": stressed,
        "deforested": deforested,
        "ndvi": ndvi_value,
        "ndwi": ndwi_value
    }


# =========================================================
# DASHBOARD
# =========================================================
if module == "Dashboard":

    if uploaded_file is None:

        st.markdown(
            '<div class="section-title">📊 Forest Monitoring Dashboard</div>',
            unsafe_allow_html=True
        )

        st.info(
            "Upload a forest/satellite image above to start the analysis."
        )

        st.markdown(
            """
            **Demo Workflow**

            Satellite Image → Preprocessing → U-Net Segmentation →
            Health Assessment → Encroachment Detection → Recovery Prediction
            """
        )

    else:

        image = Image.open(uploaded_file)
        result = analyze_image(image)

        # ---------------------------------------------
        # IMAGE PREVIEW
        # ---------------------------------------------
        st.markdown(
            '<div class="section-title">🛰️ Uploaded Satellite Image</div>',
            unsafe_allow_html=True
        )

        col_img, col_text = st.columns([1.3, 1])

        with col_img:
            st.image(
                image,
                caption="Uploaded Satellite / Forest Image",
                width="stretch"
            )

        with col_text:
            st.markdown("### 🔍 Analysis Summary")

            st.write(
                "The uploaded image is processed using a "
                "demonstration image-analysis pipeline."
            )

            st.write("**Processing stages:**")
            st.write("✓ Image preprocessing")
            st.write("✓ Vegetation feature extraction")
            st.write("✓ U-Net concept segmentation")
            st.write("✓ Forest health assessment")
            st.write("✓ Encroachment risk estimation")
            st.write("✓ Recovery prediction")


        # ---------------------------------------------
        # MAIN METRICS
        # ---------------------------------------------
        st.markdown(
            '<div class="section-title">📊 Forest Monitoring Dashboard</div>',
            unsafe_allow_html=True
        )

        m1, m2, m3 = st.columns(3)

        with m1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">🌲 Forest Health</div>
                    <div class="metric-value">{result["health"]}%</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with m2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">⚠️ Encroachment Risk</div>
                    <div class="metric-value">{result["encroachment"]}%</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with m3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">🌱 Recovery Potential</div>
                    <div class="metric-value">{result["recovery"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ---------------------------------------------
        # WORKFLOW
        # ---------------------------------------------
        st.markdown(
            '<div class="section-title">🔄 Custom Workflow</div>',
            unsafe_allow_html=True
        )

        workflow = [
            ("1", "🛰️", "Satellite Image"),
            ("2", "⚙️", "Preprocessing"),
            ("3", "🧠", "U-Net Segmentation"),
            ("4", "🌲", "Health Assessment"),
            ("5", "⚠️", "Encroachment Detection"),
            ("6", "🌱", "Recovery Prediction")
        ]

        cols = st.columns(6)

        for col, item in zip(cols, workflow):
            with col:
                st.markdown(
                    f"""
                    <div class="workflow-box">
                        <div class="workflow-number">
                            {item[0]} {item[1]}
                        </div>
                        <div class="workflow-name">
                            {item[2]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # ---------------------------------------------
        # HEALTH CLASSIFICATION
        # ---------------------------------------------
        st.markdown(
            '<div class="section-title">🌳 Health Classification</div>',
            unsafe_allow_html=True
        )

        health_data = pd.DataFrame({
            "Forest Condition": [
                "Healthy Forest",
                "Stressed Forest",
                "Deforested / Barren"
            ],
            "Percentage": [
                result["healthy"],
                result["stressed"],
                result["deforested"]
            ]
        })

        c1, c2 = st.columns([1, 1.5])

        with c1:
            st.write("### Classification")
            st.write(
                f"🟢 **Healthy Forest:** {result['healthy']}%"
            )
            st.write(
                f"🟡 **Stressed Forest:** {result['stressed']}%"
            )
            st.write(
                f"🔴 **Deforested / Barren:** {result['deforested']}%"
            )

        with c2:
            st.bar_chart(
                health_data.set_index("Forest Condition")
            )


        # ---------------------------------------------
        # NDVI / NDWI
        # ---------------------------------------------
        st.markdown(
            '<div class="section-title">📡 Vegetation Indicators</div>',
            unsafe_allow_html=True
        )

        n1, n2 = st.columns(2)

        with n1:
            st.metric(
                "NDVI (Demo)",
                f"{result['ndvi']:.3f}"
            )

        with n2:
            st.metric(
                "NDWI (Demo)",
                f"{result['ndwi']:.3f}"
            )


        # ---------------------------------------------
        # CONCLUSION
        # ---------------------------------------------
        st.markdown(
            '<div class="section-title">📝 Analysis Conclusion</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="info-box">
                <b>Forest Health:</b> {result["health"]}%<br><br>
                <b>Encroachment Risk:</b> {result["encroachment"]}%<br><br>
                <b>Recovery Potential:</b> {result["recovery"]}<br><br>
                The prototype demonstrates how satellite imagery can be
                processed to support forest monitoring, encroachment
                assessment and recovery prediction.
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FOREST HEALTH MODULE
# =========================================================
elif module == "Forest Health Analysis":

    st.markdown(
        '<div class="section-title">🌳 Forest Health Analysis</div>',
        unsafe_allow_html=True
    )

    if uploaded_file is None:
        st.warning("Please upload a satellite/forest image first.")
    else:

        image = Image.open(uploaded_file)
        result = analyze_image(image)

        col1, col2 = st.columns(2)

        with col1:
            st.image(
                image,
                caption="Forest Image",
                width="stretch"
            )

        with col2:
            st.subheader("Health Classification")

            st.success(
                f"Healthy Forest: {result['healthy']}%"
            )

            st.warning(
                f"Stressed Forest: {result['stressed']}%"
            )

            st.error(
                f"Deforested / Barren: {result['deforested']}%"
            )

            st.metric(
                "Overall Forest Health",
                f"{result['health']}%"
            )

            st.write(
                "The health assessment uses vegetation-related "
                "image features as a prototype demonstration."
            )


# =========================================================
# ENCROACHMENT MODULE
# =========================================================
elif module == "Encroachment Detection":

    st.markdown(
        '<div class="section-title">⚠️ Encroachment Detection</div>',
        unsafe_allow_html=True
    )

    if uploaded_file is None:
        st.warning("Please upload a satellite/forest image first.")
    else:

        image = Image.open(uploaded_file)
        result = analyze_image(image)

        st.image(
            image,
            caption="Image Used for Encroachment Analysis",
            width="stretch"
        )

        st.metric(
            "Estimated Encroachment Risk",
            f"{result['encroachment']}%"
        )

        if result["encroachment"] >= 60:
            st.error(
                "High encroachment risk detected in the demonstration analysis."
            )
        elif result["encroachment"] >= 30:
            st.warning(
                "Moderate encroachment risk detected in the demonstration analysis."
            )
        else:
            st.success(
                "Low encroachment risk detected in the demonstration analysis."
            )

        st.info(
            "In the complete U-Net system, segmentation masks can be used "
            "to identify forest boundaries and possible agricultural or "
            "infrastructure encroachment."
        )


# =========================================================
# RECOVERY MODULE
# =========================================================
elif module == "Recovery Prediction":

    st.markdown(
        '<div class="section-title">🌱 Forest Recovery Prediction</div>',
        unsafe_allow_html=True
    )

    if uploaded_file is None:
        st.warning("Please upload a satellite/forest image first.")
    else:

        image = Image.open(uploaded_file)
        result = analyze_image(image)

        st.image(
            image,
            caption="Image Used for Recovery Prediction",
            width="stretch"
        )

        st.metric(
            "Recovery Potential",
            result["recovery"]
        )

        st.subheader("Recovery Assessment")

        if result["recovery"] == "High":
            st.success(
                "The area shows high recovery potential based on the "
                "demonstration vegetation analysis."
            )
        elif result["recovery"] == "Medium":
            st.warning(
                "The area shows moderate recovery potential."
            )
        else:
            st.error(
                "The area shows low recovery potential and may require "
                "restoration attention."
            )

        st.info(
            "A full temporal prediction system would compare satellite "
            "images from multiple dates and analyse NDVI trends to "
            "forecast forest regrowth."
        )


# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.markdown(
    """
    <div class="footer">
        Satellite-Driven AI System for Forest Health,
        Encroachment and Recovery Prediction | Mini Project Prototype
    </div>
    """,
    unsafe_allow_html=True
)