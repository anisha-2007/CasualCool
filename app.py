import streamlit as st

st.set_page_config(
    page_title="CausalCool",
    page_icon="🌳",
    layout="wide"
)

st.title("🌳 CausalCool")
st.subheader("AI-Powered Neighbourhood Urban Heat What-If Analysis")

st.write(
    "Explore how a proposed urban intervention could affect "
    "local heat conditions using a model-based counterfactual estimate."
)

st.divider()

# Input section
col1, col2 = st.columns(2)

with col1:
    neighbourhood = st.selectbox(
        "Select Neighbourhood",
        ["Neighbourhood A", "Neighbourhood B", "Neighbourhood C"]
    )

with col2:
    intervention = st.selectbox(
        "Select Intervention",
        [
            "Increase Tree Cover",
            "Increase Cool Surface",
            "Reduce Built-up Surface"
        ]
    )

change = st.slider(
    "Intervention Change (%)",
    min_value=5,
    max_value=50,
    value=20,
    step=5
)

if st.button("🔍 Run What-If Analysis"):
    st.divider()

    st.success("What-If Analysis Completed")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Baseline Heat Indicator", "38.2")

    with col2:
        st.metric("Estimated Change", "-1.4 °C")

    with col3:
        st.metric("Uncertainty", "±0.6 °C")

    st.subheader("Key Drivers")

    st.write("🌳 Vegetation")
    st.write("🏢 Built-up Surface")
    st.write("🛣️ Road Coverage")
    st.write("🚗 Traffic")
    st.write("🌤️ Weather Conditions")

    st.subheader("Causal Explanation")

    st.info(
        f"For **{neighbourhood}**, the proposed intervention "
        f"**{intervention} (+{change}%)** is estimated to reduce "
        "the local heat indicator under the model assumptions."
    )

    st.warning(
        "This is a model-based intervention estimate, not a guaranteed "
        "real-world outcome. Field validation is required."
    )