cookie="PHPSESSID=gb2r5coe28nehse18a6lc590ah; _ga=GA1.1.598967275.1722343150; _gcl_au=1.1.926023953.1722343150; gads=ID=efbb1aa1161685db:T=1722343152:RT=1722345350:S=ALNI_MbW77AxYhFv_1mlZi1ZOzLaKx-rag; gpi=UID=00000eadbe9f5d9e:T=1722343152:RT=1722345350:S=ALNI_MbKgA5p5um4pe9yIAvZlCM6f07hVg; __eoi=ID=5855a3614e4f7861:T=1722343152:RT=1722345350:S=AA-AfjZGGWqMtC0pCd6cPpfRvuMo; FCNEC=%5B%5B%22AKsRol8MA_tW8hNE1lQwx-aB8XqnIlc_z9ohkpIY-BY09qMcwnLF24FgW_bgVR30oKZMOsAAkaaqDsgrjUQ_gTSFJjWH1LpD1yra6FCUNAn1YUfURe6m-0kmsgJXx6Tuwff_O02Ky2MXFbwlUCiwsjFVnmXW9DIATQ%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722345343.4.1.1722345561.60.0.0"
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