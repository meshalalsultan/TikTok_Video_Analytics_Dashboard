import streamlit as st
import pandas as pd
import numpy as np

def load_data_file(data_file):
    # Load the data file into a Pandas DataFrame
    df = pd.read_csv(data_file)

    return df

def calculate_analytics_metrics(df):
    # Calculate the analytics metrics
    dashboard_data = {}

    # Calculate the total views
    total_views = df['total_views'].sum()

    # Calculate the average views per video
    average_views_per_video = total_views / df['video_id'].nunique()

    # Calculate the total likes
    total_likes = df['likes_count'].sum()

    # Calculate the average likes per video
    average_likes_per_video = total_likes / df['video_id'].nunique()

    # Calculate the total comments
    total_comments = df['comments_count'].sum()

    # Calculate the average comments per video
    average_comments_per_video = total_comments / df['video_id'].nunique()

    # Calculate the total followers
    total_followers = len(df['video_id'].unique())

    # Add the analytics metrics to the dashboard data dictionary
    dashboard_data['total_views'] = total_views
    dashboard_data['average_views_per_video'] = average_views_per_video
    dashboard_data['total_likes'] = total_likes
    dashboard_data['average_likes_per_video'] = average_likes_per_video
    dashboard_data['total_comments'] = total_comments
    dashboard_data['average_comments_per_video'] = average_comments_per_video
    dashboard_data['total_followers'] = total_followers

    return dashboard_data

def create_charts(dashboard_data):
    # Create the analytics charts
    st.metric(label="Total views", value=dashboard_data['total_views'], delta="+10% (24h)")
    st.line_chart(df['total_views'])
    st.metric(label="Average views per video", value=dashboard_data['average_views_per_video'], delta="-5% (24h)")
    st.metric(label="Total likes", value=dashboard_data['total_likes'], delta="+20% (24h)")
    st.metric(label="Average likes per video", value=dashboard_data['average_likes_per_video'], delta="-10% (24h)")
    st.metric(label="Total comments", value=dashboard_data['total_comments'], delta="+30% (24h)")
    st.metric(label="Average comments per video", value=dashboard_data['average_comments_per_video'], delta="-15% (24h)")
    st.metric(label="Total followers", value=dashboard_data['total_followers'], delta="+40% (24h)")

st.title('TikTok Video Analytics Dashboard')

# Upload the data file
data_file = st.file_uploader('Upload data file')

# Load the data file
df = load_data_file(data_file)

# Calculate the analytics metrics
dashboard_data = calculate_analytics_metrics(df)
st.dataframe(df)

# Create the charts
create_charts(dashboard_data)


