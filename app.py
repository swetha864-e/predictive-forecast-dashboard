import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# PAGE TITLE
# --------------------------------

st.title("Predictive Forecasting of Care Load & Placement Demand")

st.subheader("Live Analytics Dashboard")

# --------------------------------
# LOAD DATASET
# --------------------------------

df = pd.read_csv("HHS_Unaccompanied_Alien_Children_Program.csv")

# --------------------------------
# SHOW DATASET
# --------------------------------

st.subheader("Dataset Preview")

st.write(df.head())

# --------------------------------
# HHS CARE LOAD TREND
# --------------------------------

st.subheader("Children in HHS Care Trend")

st.line_chart(df['Children in HHS Care'])

# --------------------------------
# FORECAST HORIZON SELECTOR
# --------------------------------

days = st.slider(
    "Select Forecast Horizon (Days)",
    1,
    30
)

st.write(f"Forecasting next {days} days")

# --------------------------------
# INTAKE VS DISCHARGE ANALYSIS
# --------------------------------

st.subheader("Intake vs Discharge Analysis")

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(
    df['Children transferred out of CBP custody'],
    label='Transfers from CBP'
)

ax.plot(
    df['Children discharged from HHS Care'],
    label='Discharges from HHS'
)

ax.legend()

st.pyplot(fig)

# --------------------------------
# WARNING INDICATOR
# --------------------------------

st.warning(
    "Capacity stress may increase if intake exceeds discharge."
)

# --------------------------------
# PROJECT SUMMARY
# --------------------------------

st.subheader("Project Objectives")

st.write("""
1. Forecast number of children in HHS care

2. Estimate imbalance between intake and exits

3. Predict short-term discharge demand

4. Provide early warnings for healthcare planners

5. Compare statistical vs machine learning forecasting
""")# --------------------------------
# FORECAST UNCERTAINTY
# --------------------------------

st.subheader("Forecast Uncertainty")

st.write("""
Forecast uncertainty is represented using confidence intervals.
This helps healthcare planners understand possible future variations in HHS care load.
""")

st.info(
    "Higher uncertainty may indicate increased risk of capacity stress."
)
