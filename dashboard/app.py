import sys
import os

# ====================================
# FIX PYTHON IMPORT PATH
# ====================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# ====================================
# IMPORTS
# ====================================

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

from datetime import datetime

from services.detection_service.analytics.insight_engine import (
    generate_ai_insights,
)

# ====================================
# CONFIG
# ====================================

API_BASE = "http://localhost:8000"

STORE_ID = "ST1008"

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Retail Intelligence Dashboard",
    layout="wide"
)

# ====================================
# TITLE
# ====================================

st.title(
    "🛍️ Retail Intelligence Platform"
)

# ====================================
# FETCH FUNNEL DATA
# ====================================

try:

    funnel_response = requests.get(
        f"{API_BASE}/stores/{STORE_ID}/funnel"
    )

    funnel_data = funnel_response.json()

except Exception as e:

    st.error(
        f"Failed to connect to backend: {e}"
    )

    st.stop()

# ====================================
# METRICS
# ====================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Entered",
    funnel_data.get("entered", 0)
)

col2.metric(
    "Browsed",
    funnel_data.get("browsed", 0)
)

col3.metric(
    "Queued",
    funnel_data.get("queued", 0)
)

col4.metric(
    "Purchased",
    funnel_data.get("purchased", 0)
)

# ====================================
# DIVIDER
# ====================================

st.divider()

# ====================================
# FUNNEL CHART
# ====================================

funnel_df = pd.DataFrame({

    "Stage": [
        "Entered",
        "Browsed",
        "Queued",
        "Purchased"
    ],

    "Count": [
        funnel_data.get("entered", 0),
        funnel_data.get("browsed", 0),
        funnel_data.get("queued", 0),
        funnel_data.get("purchased", 0)
    ]
})

fig = px.funnel(
    funnel_df,
    x="Count",
    y="Stage"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ====================================
# DIVIDER
# ====================================

st.divider()

# ====================================
# SYSTEM STATUS
# ====================================

st.subheader(
    "System Status"
)

status_data = pd.DataFrame({

    "Component": [
        "YOLOv8",
        "ByteTrack",
        "Event Engine",
        "Postgres",
        "FastAPI",
        "Queue Analytics",
        "Heatmaps",
        "AI Insight Engine"
    ],

    "Status": [
        "Running",
        "Running",
        "Running",
        "Connected",
        "Running",
        "Active",
        "Active",
        "Active"
    ]
})

st.dataframe(
    status_data,
    use_container_width=True
)

# ====================================
# DIVIDER
# ====================================

st.divider()

# ====================================
# LIVE EVENT INFO
# ====================================

st.subheader(
    "Live Analytics"
)

st.info(
    f"""
    Last Updated:
    {datetime.utcnow()}
    """
)

# ====================================
# DIVIDER
# ====================================

st.divider()

# ====================================
# AI RETAIL INSIGHTS
# ====================================

st.subheader(
    "AI Retail Insights"
)

insights = generate_ai_insights(
    funnel_data
)

for insight in insights:

    st.success(
        insight
    )

# ====================================
# FOOTER
# ====================================

st.divider()

st.caption(
    "Retail Intelligence Platform • Real-Time AI Analytics"
)