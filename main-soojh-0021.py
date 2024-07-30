cookie="PHPSESSID=colo3r0736rubr187011qleado; _ga=GA1.1.1489070977.1722333842; _gcl_au=1.1.644558148.1722333842; gads=ID=a7abaace45b6d33c:T=1722333842:RT=1722333842:S=ALNI_MaJ_DEEtom0T_0Dqj7DJ8IYNY96eg; gpi=UID=00000eadaa15dc55:T=1722333842:RT=1722333842:S=ALNI_MbkrbX3IC6CWSQ9AJb21uMJ4kt3eA; __eoi=ID=93555a771f9dc00b:T=1722333842:RT=1722333842:S=AA-AfjbCUDlyDZ0hv_sgwXhLrBPB; FCNEC=%5B%5B%22AKsRol-zFT4erwA3fC0Qw4cfITLh0pCTrHxb4Pt99Om0u8NA8LCRKroZwutUm94VopSonGvDw1WW6bfWreh4K8ktMGjGs3QuoXO3QncEDp51-E4p0usa7Otzlpici6cYcyhMQ5TyNsrdEfmORimNFL7Az1xodnEQ3g%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722333842.1.1.1722333854.48.0.0"
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