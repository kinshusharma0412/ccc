cookie="PHPSESSID=vkl4unlbm3naf44oins4koi03m; _ga=GA1.1.1502841217.1722361887; _gcl_au=1.1.1751367057.1722361887; gads=ID=9977003212c2ddd8:T=1722361886:RT=1722361886:S=ALNI_MYaKUSm1-yY7Um2DQQKpb343C0fLA; gpi=UID=00000eade2fe7203:T=1722361886:RT=1722361886:S=ALNI_MakCUsRo_LxRqHZ8-Zkosa0YChPMw; __eoi=ID=bfa4f566b40d6515:T=1722361886:RT=1722361886:S=AA-AfjbVDIVN1tEORXAiZcs3b7xA; FCNEC=%5B%5B%22AKsRol8huglnwga9B_EQGuzy-1MgzmJJz1_CIDWVhg0P0VvXHcXJCUDzik8dk4v2gV3DOjGxldeKnBuCu2ffH_mOzxpz6Wesv5glC8utLej_mAVIisuo8ObE-hwr2SOr-QOpDJ4HG0DDW6mBJNqTH3mjpNfWW5RlUA%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722361886.1.1.1722361909.37.0.0"
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