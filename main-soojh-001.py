cookie="PHPSESSID=q9h1e1es54c6ch5f5bcojtq0g5; _ga=GA1.1.1668349273.1722088675; _gcl_au=1.1.1706235565.1722088675; gpi=UID=00000ea97fd6499d:T=1722089555:RT=1722089555:S=ALNI_MZPq5CHxntiEIHHAmdVhwIj-ghsEQ; popup_fb=yes; gads=ID=5ad943fc012a4884:T=1722089555:RT=1722090431:S=ALNI_MZ2i4Z7EvCqAiUfG01SsJ2HS9N2Zw; __eoi=ID=a2413e9208bca4db:T=1722089555:RT=1722090431:S=AA-Afja2krhp-91l7vM23tni0i5D; _ga_HPSLFXFRWN=GS1.1.1722090377.3.1.1722090433.4.0.0; FCNEC=%5B%5B%22AKsRol9RyTkAi1KtDMJPO3BbV1_CnOdfHkTusVBGgVJRCfBWD668NJKhB1mc_cPV16JWaMyIKhStwUG5rNFUAHaB1ZYhrhy0rP5OMAaFZJTQ1PD8nOzKVZAUh9eH8KhL6uDJPCv_jolwNiNfmfcKlH-Dy5NRntyDNA%3D%3D%22%5D%5D"
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