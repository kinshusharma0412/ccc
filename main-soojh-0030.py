cookie="PHPSESSID=lbhde73bfgh3k52uq87ju80t4p; _ga=GA1.1.1742008941.1722338263; _gcl_au=1.1.1814127646.1722338263; gads=ID=4a6c91edb5ed9efe:T=1722338264:RT=1722343865:S=ALNI_MY6w8edtmC_Lt4PjaJ7mDazyNvwfg; gpi=UID=00000eadb31182e0:T=1722338264:RT=1722343865:S=ALNI_MavHxmJnk3taaorC6h1unx4t5eNHw; __eoi=ID=6c5e7cde4f5c52ef:T=1722338264:RT=1722343865:S=AA-AfjYscSnXRFiGI37XpTOpVtbn; FCNEC=%5B%5B%22AKsRol898EUndDcJrJPM60Ln1MDY46aVM15u4JYI-Xp695p6o8FykTJRPjcMtE7g5Dus6rdt8uvlkhJCWJHV--1gS3X9Mn3_YIVUsykqIA1y-BGcEPWmdnmNoXH9WWsMirnBLTQEwGXxyUNoqgmMHbfIroxsXn19bw%3D%3D%22%5D%5D; popup_fb=yes; _ga_HPSLFXFRWN=GS1.1.1722343864.2.1.1722343996.60.0.0"
import requests,time
import streamlit as st
from bs4 import BeautifulSoup
@st.cache
def my():
	while True:
	    try:
	        url = "https://mycutebaby.in/contest/participant/669bc381bf80d"
	
	        params = {
	          'utm_medium': "w_7_24"
	        }
	
	        headers = {
	          'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	          'Cookie': cookie
	        }
	
	        response = requests.get(url, params=params, headers=headers)
	
	        #st.write(response.text)
	        soup=BeautifulSoup(response.text,"html.parser")
	        try:
	            s=soup.select("h4.v_info")[0].text
	            st.write(s)
	            print(s)
	        except:
	            pass
	        s=soup.select("meta#token_key")[0]['value']
	        st.write(s)
	        print(s)
	        open("db.txt","w").write(s)
	    except:
	        try:
	            s="9UyjIsVR"#open("db.txt","r").read(
	        except:
	            s=""
	        #st.write(s)
	    url = "https://mycutebaby.in/contest/daily_vote/"
	
	
	    params = {
	              'n': "669bc381bf80d",
	              'captcha': "asdsdad",
	              'key': s,
	              'v': "Sharma ab"
	            }
	    headers = {
	              'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	            #  'Accept-Language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	              'Referer': "https://mycutebaby.in/contest/participant/669bc381bf80d",
	            #  'Sec-Fetch-Dest': "empty",
	            #  'Sec-Fetch-Mode': "cors",
	            #  'Sec-Fetch-Site': "same-origin",
	              'X-Requested-With': "XMLHttpRequest",
	            #  'sec-ch-ua': ""Not-A.Brand";v="99", "Chromium";v="124"",
	            #  'sec-ch-ua-full-version-list': ""Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"",
	            #  'sec-ch-ua-mobile': "?1",
	            #  'sec-ch-ua-model': ""M2102J20SI"",
	            #  'sec-ch-ua-platform': ""Android"",
	            #  'sec-ch-ua-platform-version': ""12.0.0"",
	              'Cookie': cookie
	            }
	
	    response = requests.get(url, params=params, headers=headers)
	
	    st.write(response.text)
	    print(response.text)
	    time.sleep(5*60)
my()