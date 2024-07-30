cookie="PHPSESSID=0cd6o89nhrplqlm5lb498npkkm; _ga=GA1.1.1743848888.1722223810; _gcl_au=1.1.1090976127.1722223810; gads=ID=28381ec8b8e35222:T=1722223812:RT=1722223812:S=ALNI_MaK2BRBY7p4AB0El_oKc033VD8Zmg; gpi=UID=00000eab54a2ee18:T=1722223812:RT=1722223812:S=ALNI_MZi53og7UKTKEBjJ3zobTcipnI0wA; __eoi=ID=0bd4e27d2903b528:T=1722223812:RT=1722223812:S=AA-AfjbCcCKxrbma32f3KeaHOt4E; _ga_HPSLFXFRWN=GS1.1.1722223810.1.1.1722223837.33.0.0; FCNEC=%5B%5B%22AKsRol8CNceacBEFszDIgcu_99aWzZatm4xjvZEBn3_QnlW-0Aij3AAjvS5Nhh-lvNAOS5IUunSDDIgps8gMHdEdksS0SDMPrm05PPW5rQRgBkHwaEfSpSXA9ExPdblhzz-Y1ohrnEib16e9fef7dRY-WVmGWX86PA%3D%3D%22%5D%5D"
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