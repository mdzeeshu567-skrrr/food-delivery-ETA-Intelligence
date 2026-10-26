
from pathlib import Path
import glob
import joblib
import pandas as pd
import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="DeliveryIQ | ETA Intelligence",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent

# ==========================================
# LOAD TRAINED MODELS
# ==========================================
@st.cache_resource
def load_models():
    eta_path = BASE_DIR / "tuned_random_forest_eta.pkl"

    if not eta_path.exists():
        raise FileNotFoundError(
            "Cannot find tuned_random_forest_eta.pkl "
            "in the project folder."
        )

    eta_model = joblib.load(eta_path)

    # Find the saved delay-classification model.
    classifier_files = (
        glob.glob(str(BASE_DIR / "delay_classification*.pkl"))
        + glob.glob(str(BASE_DIR / "*delay*classifier*.pkl"))
    )

    # Remove duplicates while preserving order.
    classifier_files = list(dict.fromkeys(classifier_files))

    if not classifier_files:
        raise FileNotFoundError(
            "Cannot find the saved delay-classification model. "
            "Keep its .pkl file in the project folder."
        )

    delay_model = joblib.load(classifier_files[0])

    return eta_model, delay_model


# ==========================================
# CUSTOM DESIGN
# ==========================================
st.markdown("""
<style>
.stApp {
    background-color: #F4F7FC;
    color: #172033;
}
[data-testid="stSidebar"] {
    background-color: #101827;
}
[data-testid="stSidebar"] * {
    color: #F9FAFB;
}
.main-header {
    background: linear-gradient(120deg, #172554, #2563EB);
    padding: 28px 32px;
    border-radius: 16px;
    margin-bottom: 18px;
    color: white;
}
.main-header h1 {
    color: white;
    margin-bottom: 8px;
}
.main-header p {
    color: #DBEAFE;
    margin-bottom: 0;
}
div[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
}
.stButton > button {
    background-color: #2563EB;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.55rem 1rem;
    font-weight: 600;
}
.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# LOAD MODELS SAFELY
# ==========================================
try:
    eta_model, delay_model = load_models()
    models_ready = True
    model_error = None
except Exception as error:
    models_ready = False
    model_error = str(error)


# ==========================================
# SESSION STATE: PREDICTION HISTORY
# ==========================================
if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("## 🍔 DeliveryIQ")
    st.caption("ETA & Delay Intelligence")
    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Choose a page",
        [
            "📊 Dashboard",
            "🚚 Delivery Prediction",
            "📋 Prediction History"
        ],
        index=0,
        label_visibility="collapsed"
    )

    st.divider()
    st.caption("Machine Learning • Random Forest")

    if models_ready:
        st.success("Models Ready")
    else:
        st.error("Models Not Loaded")


# ==========================================
# REUSABLE HEADER
# ==========================================
def show_header():
    st.markdown("""
    <div class="main-header">
        <div style="font-size:12px; letter-spacing:2px;">
            DELIVERY ANALYTICS PLATFORM
        </div>
        <h1>🍔 Food Delivery Intelligence</h1>
        <p>ETA prediction • Delay-risk analysis • Machine learning</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# DASHBOARD
# ==========================================
if page == "📊 Dashboard":
    show_header()

    st.subheader("Smart delivery-time prediction and delay-risk analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📦 **ETA Prediction**\n\nEstimate delivery time in minutes.")

    with col2:
        st.warning("⚠️ **Delay Detection**\n\nEstimate the probability of a delayed delivery.")

    with col3:
        st.info("🤖 **Machine Learning**\n\nPowered by trained Random Forest models.")

    if models_ready:
        st.success("Both machine-learning models loaded successfully!")
    else:
        st.error(f"Model loading error: {model_error}")

    history = st.session_state.prediction_history

    st.subheader("📈 Prediction Summary")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Total Predictions", len(history))

    with m2:
        average_eta = (
            sum(item["Estimated Delivery Time (min)"] for item in history)
            / len(history)
            if history else 0
        )
        st.metric(
            "Average ETA",
            f"{average_eta:.1f} min" if history else "—"
        )

    with m3:
        average_distance = (
            sum(item["Distance (km)"] for item in history)
            / len(history)
            if history else 0
        )
        st.metric(
            "Average Distance",
            f"{average_distance:.2f} km" if history else "—"
        )

    st.caption(
        "Use Delivery Prediction in the sidebar to estimate a new delivery."
    )


# ==========================================
# DELIVERY PREDICTION
# ==========================================
elif page == "🚚 Delivery Prediction":
    show_header()

    st.subheader("📦 Enter Delivery Details")
    st.write("Enter the order, traffic, weather and location information.")

    if not models_ready:
        st.error(f"Cannot make predictions: {model_error}")

    else:
        with st.form("delivery_form"):
            left, right = st.columns(2)

            with left:
                distance = st.number_input(
                    "Delivery distance (km)",
                    min_value=0.1,
                    max_value=100.0,
                    value=5.0,
                    step=0.5
                )

                day_name = st.selectbox(
                    "Day of week",
                    ["Monday", "Tuesday", "Wednesday", "Thursday",
                     "Friday", "Saturday", "Sunday"]
                )
                day_number = [
                    "Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"
                ].index(day_name)

                order_hour = st.slider(
                    "Order hour",
                    min_value=0,
                    max_value=23,
                    value=13
                )

                order_minute = st.slider(
                    "Order minute",
                    min_value=0,
                    max_value=59,
                    value=0
                )

                order_month = st.selectbox(
                    "Order month",
                    list(range(1, 13)),
                    index=0
                )

                weather = st.selectbox(
                    "Weather conditions",
                    [
                        "conditions Sunny",
                        "conditions Cloudy",
                        "conditions Fog",
                        "conditions Sandstorms",
                        "conditions Stormy",
                        "conditions Windy"
                    ]
                )

                traffic = st.selectbox(
                    "Road traffic density",
                    ["Low", "Medium", "High", "Jam"]
                )

                vehicle_condition = st.selectbox(
                    "Vehicle condition",
                    [0, 1, 2]
                )

            with right:
                order_type = st.selectbox(
                    "Order type",
                    ["Snack", "Meal", "Drinks", "Buffet"]
                )

                festival = st.selectbox(
                    "Festival",
                    ["No", "Yes"]
                )

                city = st.selectbox(
                    "City type",
                    ["Metropolitian", "Urban", "Semi-Urban"]
                )

                vehicle_type = st.selectbox(
                    "Vehicle type",
                    ["motorcycle", "scooter", "electric_scooter"]
                )

                st.markdown("### 📍 Location Details")

                restaurant_lat = st.number_input(
                    "Restaurant latitude",
                    value=22.5726,
                    format="%.6f"
                )

                restaurant_lon = st.number_input(
                    "Restaurant longitude",
                    value=88.3639,
                    format="%.6f"
                )

                delivery_lat = st.number_input(
                    "Delivery latitude",
                    value=22.5826,
                    format="%.6f"
                )

                delivery_lon = st.number_input(
                    "Delivery longitude",
                    value=88.3739,
                    format="%.6f"
                )

            submitted = st.form_submit_button(
                "🚀 Predict Delivery",
                use_container_width=True
            )

        if submitted:
            input_data = pd.DataFrame([{
                "Restaurant_latitude": restaurant_lat,
                "Restaurant_longitude": restaurant_lon,
                "Delivery_location_latitude": delivery_lat,
                "Delivery_location_longitude": delivery_lon,
                "Distance_km": distance,
                "Order_DayOfWeek": day_number,
                "Order_Month": order_month,
                "Order_Hour": order_hour,
                "Order_Minute": order_minute,
                "Weatherconditions": weather,
                "Road_traffic_density": traffic,
                "Vehicle_condition": vehicle_condition,
                "Type_of_order": order_type,
                "Type_of_vehicle": vehicle_type,
                "Festival": festival,
                "City": city
            }])

            try:
                eta = float(eta_model.predict(input_data)[0])
                delay_probability = float(
                    delay_model.predict_proba(input_data)[0][1]
                )

                delay_percent = delay_probability * 100

                st.divider()
                st.subheader("🎯 Prediction Results")

                result1, result2 = st.columns(2)

                with result1:
                    st.metric(
                        "Estimated Delivery Time",
                        f"{max(0, eta):.1f} minutes"
                    )

                with result2:
                    st.metric(
                        "Delay Probability",
                        f"{delay_percent:.1f}%"
                    )

                if delay_probability >= 0.5:
                    st.error("⚠️ Higher delay risk predicted.")
                else:
                    st.success("✅ Lower delay risk predicted.")

                st.caption(
                    "Delay probability is the classifier's estimated "
                    "probability of a delivery taking more than 34 minutes. "
                    "The 50% cutoff is the current app decision threshold."
                )

                st.session_state.prediction_history.append({
                    "Estimated Delivery Time (min)": round(max(0, eta), 2),
                    "Delay Probability (%)": round(delay_percent, 2),
                    "Distance (km)": round(distance, 2),
                    "Day": day_name,
                    "Order Hour": order_hour,
                    "Weather": weather,
                    "Traffic": traffic,
                    "Vehicle": vehicle_type,
                    "City": city
                })

            except Exception as error:
                st.error(f"Prediction failed: {error}")


# ==========================================
# PREDICTION HISTORY
# ==========================================
elif page == "📋 Prediction History":
    show_header()

    st.subheader("📋 Prediction History")

    history = st.session_state.prediction_history

    if not history:
        st.info("No predictions yet. Predict a delivery to build your history.")

    else:
        history_df = pd.DataFrame(history)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Predictions", len(history_df))

        with col2:
            st.metric(
                "Average ETA",
                f"{history_df['Estimated Delivery Time (min)'].mean():.1f} min"
            )

        with col3:
            st.metric(
                "Average Distance",
                f"{history_df['Distance (km)'].mean():.2f} km"
            )

        st.dataframe(history_df, use_container_width=True)

        st.download_button(
            "📥 Download Prediction History (CSV)",
            data=history_df.to_csv(index=False).encode("utf-8"),
            file_name="delivery_prediction_history.csv",
            mime="text/csv",
            use_container_width=True
        )

        if st.button("🗑️ Clear Prediction History"):
            st.session_state.prediction_history = []
            st.rerun()







