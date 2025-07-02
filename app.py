import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mini Productivity Dashboard", layout="centered")

st.title("🧠 Mini Productivity Dashboard")

# Form to add a task
st.sidebar.header("Add a Task")
task = st.sidebar.text_input("Task Name")
status = st.sidebar.selectbox("Status", ["Pending", "Completed"])
mood = st.sidebar.selectbox("Mood", ["Happy", "Neutral", "Tired", "Stressed"])
focus = st.sidebar.slider("Focus Level", 1, 10)

# Session state for saving data
if "data" not in st.session_state:
    st.session_state.data = []

if st.sidebar.button("Add Task"):
    st.session_state.data.append({
        "Task": task,
        "Status": status,
        "Mood": mood,
        "Focus": focus
    })

df = pd.DataFrame(st.session_state.data)

if not df.empty:
    st.subheader("📋 Task Overview")
    st.dataframe(df)

    st.subheader("📊 Status Distribution")
    st.plotly_chart(px.pie(df, names="Status", title="Tasks Completed vs. Pending"))

    st.subheader("😊 Mood Distribution")
    st.plotly_chart(px.histogram(df, x="Mood", title="Your Mood Trends"))

    st.subheader("🎯 Average Focus Level")
    avg_focus = df["Focus"].mean()
    st.metric("Focus Level", f"{avg_focus:.1f} / 10")
else:
    st.info("Add a task from the sidebar to get started.")

