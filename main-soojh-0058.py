import os
import streamlit as st
@st.cache_resource
def init_connection1():
	return os.system("/home/adminuser/venv/bin/python main-soojh-0058old.py")
_=init_connection1()