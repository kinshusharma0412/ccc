cookie="PHPSESSID=fvib42kjfp5m9m8751gah2pigr; _ga=GA1.1.625064203.1722225953; _gcl_au=1.1.694222700.1722225953; gads=ID=8fa7c785e3efcbea:T=1722225954:RT=1722225954:S=ALNI_MZyVsK-MDAIJNT9O4rXPe7fZCRGjw; gpi=UID=00000eab5b141d72:T=1722225954:RT=1722225954:S=ALNI_MZJeEcsweWeFF5Zn5ZEEyoERkHvew; __eoi=ID=25b20acac13b0708:T=1722225954:RT=1722225954:S=AA-AfjYbZ3zOFnR4HIWins25gdmk; FCNEC=%5B%5B%22AKsRol8X9OsC2SGHcwAh9cH-auJ01bvRQa1Z9aM66m67czYhcz8Fc8l-P7q7ePXW2aIchX0a-Rq1wngj3whczhTQZcUsOzVTxqVkv3mi5uTGiXNVvJHWTD0T-gaaaxRXHEdFiy6zLnFFcwQF20atDruJPbEvJBrcVA%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722225952.1.1.1722226019.60.0.0"
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