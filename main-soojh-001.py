import socket
import streamlit as st

## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
st.write(f"Hostname: {hostname}")
st.write(f"IP Address: {ip_address}")
import os,sys
import time 
time.sleep(5)
os.execv(sys.executable, ['python'] + sys.argv)