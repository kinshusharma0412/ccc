cookie="PHPSESSID=rg7m8csi5fc22nrbn27dta1iec; _ga=GA1.1.94883750.1722353166; _gcl_au=1.1.433985217.1722353166; gads=ID=722a03f3b0932111:T=1722353167:RT=1722353167:S=ALNI_Ma1SNEjuPCrcVD5MPLvnMoeHc_8nA; gpi=UID=00000eadd5e73f5d:T=1722353167:RT=1722353167:S=ALNI_Ma2Mp3NNux9_TGkGerMljFeN1-N4g; __eoi=ID=7265f4c951c07ca4:T=1722353167:RT=1722353167:S=AA-Afjam2qoD_xaYoMo5Uexyb2bB; FCNEC=%5B%5B%22AKsRol82yC4SVVVHEYVe0s5Zemz50YG4Scs0VNNAOa8cX-SmyM2ROE1Al6sndER66Uex_k6qWw69x5TNwZ_lqHq-qPUvCz6vU07GOA5aXy5hbeIv2zvNOVT3ebB2vcPNFsKUBOq7zz_ZZucIqZcE8p4aDNNWEDkB5w%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722353166.1.1.1722353183.43.0.0"
import requests,time
import streamlit as st
from bs4 import BeautifulSoup
#@st.cache_data
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
	        st.write(s)
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