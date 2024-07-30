cookie="PHPSESSID=l37uijc57q9tg9uk36ahof73pf; _ga=GA1.1.1074972202.1722339193; _gcl_au=1.1.435252123.1722339193; gads=ID=04d53f774650b8c8:T=1722339194:RT=1722339557:S=ALNI_MbXfUtjaCVLdJxypaIVPiq4FLJa5w; gpi=UID=00000eadb4c91514:T=1722339194:RT=1722339557:S=ALNI_MbAgQhReh1ycW0VyrDuyHcPbZ44cw; __eoi=ID=7184da4c5503336f:T=1722339194:RT=1722339557:S=AA-AfjZBM0I1BhnO5lUBSn3y0XjK; FCNEC=%5B%5B%22AKsRol_fzmE0s9YfelpYbflqIDST_HYCiD7MZ2EkPOlP_Er9yV1_i6UoJCfzUwIZxz_T2AUz1sTFhgkJom2uz8E1FK38Rn1f9gE45AezxFPsgqCQnt5d6y4LjaexkWoz-hfnWbt7urJ87YSWtASMAgCl4IiIbpPqiA%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722339192.1.1.1722339673.60.0.0"
import requests,time
import streamlit as st
from bs4 import BeautifulSoup
@st.cache_data
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
	
	        ##st.write(response.text)
	        soup=BeautifulSoup(response.text,"html.parser")
	        try:
	            s=soup.select("h4.v_info")[0].text
	            #st.write(s)
	            print(s)
	        except:
	            pass
	        s=soup.select("meta#token_key")[0]['value']
	        #st.write(s)
	        print(s)
	        open("db.txt","w").write(s)
	    except:
	        try:
	            s="9UyjIsVR"#open("db.txt","r").read(
	        except:
	            s=""
	        ##st.write(s)
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
	
	    #st.write(response.text)
	    print(response.text)
	    time.sleep(5*60)
my()