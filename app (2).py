import streamlit as st
import joblib
import pandas as pd

# Load model
try:
    model = joblib.load('/content/models/click_prediction_model.pkl')
except FileNotFoundError:
    st.error("Model file 'click_prediction_model.pkl' not found. Run Phase 3 script first.")
    st.stop()

# Pipeline to score users
def score_users(input_data):
    """Score users and return predicted click probabilities."""
    df = input_data.copy()
    for col in ['email_text', 'email_version', 'weekday', 'user_country']:
        df[col] = df[col].astype('category').cat.codes
    df['hour_bin'] = pd.cut(df['hour'], bins=[0, 6, 12, 18, 24],
                           labels=['Night', 'Morning', 'Afternoon', 'Evening']).cat.codes
    df['purchase_bin'] = pd.cut(df['user_past_purchases'], bins=[-1, 0, 2, 5, 10, 25],
                              labels=['0', '1-2', '3-5', '6-10', '11+']).cat.codes
    df = df.drop(['hour', 'user_past_purchases'], axis=1, errors='ignore')
    X = df.drop(['clicked', 'opened'], axis=1, errors='ignore')
    df['pred_proba'] = model.predict_proba(X)[:, 1]
    return df

# Streamlit app
st.title("Email Campaign Targeting App")
st.write("Input user data to predict click probabilities.")
st.info("Tip: For higher click probabilities, try: short_email, personalized, Tuesday/Wednesday, Morning (6–12), US/UK, 6+ past purchases.")

# Input fields
email_text = st.selectbox("Email Text", ["short_email", "long_email"])
email_version = st.selectbox("Email Version", ["personalized", "generic"])
weekday = st.selectbox("Weekday", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
user_country = st.selectbox("User Country", ["US", "UK", "FR", "ES"])
hour = st.slider("Hour (1-24)", 1, 24, 10)
user_past_purchases = st.slider("Past Purchases", 0, 22, 3)

# Check for suboptimal inputs
if user_past_purchases < 6:
    st.warning("Low past purchases (<6) may reduce click probability. Try 6–10 or 11+.")
if email_version == "generic":
    st.warning("Generic emails have lower CTR. Try personalized.")
if hour < 6 or hour > 12:
    st.warning("Non-morning hours (outside 6–12) may lower probability. Try 9–11 AM.")

# Create input dataframe
input_data = pd.DataFrame({
    'email_text': [email_text],
    'email_version': [email_version],
    'weekday': [weekday],
    'user_country': [user_country],
    'hour': [hour],
    'user_past_purchases': [user_past_purchases]
})

# Score user
if st.button("Predict Click Probability"):
    scored_users = score_users(input_data)
    if not scored_users.empty:
        prob = scored_users['pred_proba'].iloc[0]
        st.write(f"Predicted Click Probability: {prob:.4f}")
        if prob >= 0.3:
            st.success("Recommended: Send email to this user!")
        else:
            st.warning("Not recommended: Low click probability.")
    else:
        st.error("No predictions returned. Check model or input data.")
