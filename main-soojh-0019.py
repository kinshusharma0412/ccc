cookie="PHPSESSID=kqq8d459njm9ns99vnp9f956fe; _ga=GA1.1.1298863126.1722326947; _gcl_au=1.1.842499643.1722326947; gads=ID=0c9e3f5132bacf38:T=1722326946:RT=1722326946:S=ALNI_MZ2kddfxKxJ9a2pZWLV1gdK_te6HQ; gpi=UID=00000ead18265546:T=1722326946:RT=1722326946:S=ALNI_MaGps6Y9UH2Z8SvFut1yxDUt295Ag; __eoi=ID=07a222d47c4654a1:T=1722326946:RT=1722326946:S=AA-AfjYk4DyikP6fJ94cpbXY4FN-; _ga_HPSLFXFRWN=GS1.1.1722326947.1.0.1722326954.53.0.0; FCNEC=%5B%5B%22AKsRol9yHHfdHFVGAlCAoyzd8QiGM2sF9MW6krQrioIOwhvSoUzp89UjVsdFigoqdZTa2F342qpmBIOU0IBLnkFFKfBfGdQP6rV6EzdhVMv6IN6X3mnA3gIe-Ad4FNav2MPkIkz3vJUEO_Df2Uf_mW1yvSlAbu5aNA%3D%3D%22%5D%5D"
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