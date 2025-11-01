import streamlit as st
from collections import deque
from usstates import usa_map
from bfs import bfs_path

st.title("Road Trip Planner-BFS Shortest Route")
st.markdown(
    "<p style=""font-family:Comfortaa; color:black; font-size:18px;"">Welcome to Road Trip Planner!👋🏻👋🏽👋🏿 You choose the starting, destination, and must visit states-and then we find the shortest path and tell you which states you will go through!🗽🙂 </p>",
    unsafe_allow_html=True,
)



states = sorted(list(usa_map.keys()))
start_state = st.selectbox("Start State", states)
end_state = st.selectbox("End State", states)
if start_state==end_state:
    st.warning("Start and destination states are the same!!!")
else:
    path = (bfs_path(usa_map, start_state, end_state))
    if path: 
        st.write(" -> ".join(path))
    else:
        st.error("The system broke down. Just take an airplane!!!!")



