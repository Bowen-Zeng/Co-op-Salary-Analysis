"""
Dashboard Application in StreamLit
Placeholder for dashboard functionality - framework agnostic.
"""

import pandas as pd
import streamlit as st
import plotly.express as px

# ---------- Page config ----------
st.set_page_config(
    page_title="Co-op Salary Insights",
    page_icon="📊",
    layout="wide"
)

# ---------- Load data ----------
@st.cache_data
def load_data():
    return pd.read_csv("Processed/cleaned_salaries.csv")

df = load_data()

# ---------- Header ----------
st.markdown(
    """
    <h1 style='margin-bottom:0'>Co-op Salary Insights</h1>
    <p style='color:gray; margin-top:0'>
    An analysis of co-op compensation across companies and roles
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- Sidebar ----------
st.sidebar.header("Filters")

company = st.sidebar.selectbox(
    "Company",
    ["All"] + sorted(df["company"].unique())
)

if company != "All":
    df = df[df["company"] == company]

# ---------- KPI Section ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average Salary (USD)",
    f"${df['salary_annual_usd'].mean():,.0f}"
)

col2.metric(
    "Median Salary (USD)",
    f"${df['salary_annual_usd'].median():,.0f}"
)

col3.metric(
    "Max Salary",
    f"${df['salary_annual_usd'].max():,.0f}"
)

col4.metric(
    "Observations",
    f"{len(df):,}"
)

st.markdown("## Salary Distribution")

# ---------- Main Chart ----------
fig = px.histogram(
    df,
    x="salary_annual_usd",
    nbins=40,
    title="Distribution of Annualized Salaries",
    labels={"salary_annual_usd": "Annual Salary (USD)"},
    template="simple_white"
)

fig.update_layout(
    title_x=0.5,
    height=450
)

st.plotly_chart(fig, use_container_width=True)

# ---------- Secondary Section ----------
left, right = st.columns([2, 1])

with left:
    st.markdown("### Top Paying Companies")
    top_companies = (
        df.groupby("company")["salary_annual_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    bar = px.bar(
        top_companies,
        x="salary_annual_usd",
        y="company",
        orientation="h",
        template="simple_white",
        labels={
            "salary_annual_usd": "Avg Salary (USD)",
            "company": ""
        }
    )

    bar.update_layout(height=400)
    st.plotly_chart(bar, use_container_width=True)

with right:
    st.markdown("### Sample Data")
    st.dataframe(
        df[["company", "salary_annual_usd"]]
        .sort_values("salary_annual_usd", ascending=False)
        .head(10),
        height=400
    )

# ---------- Footer ----------
st.markdown("---")
st.caption(
    "Salaries normalized to annual USD values. "
    "Data cleaned and processed in Python."
)
