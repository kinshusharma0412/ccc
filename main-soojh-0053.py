cookie="PHPSESSID=5l4861cvhapeskf86r6deft80l; _ga=GA1.1.2051797857.1722352697; _gcl_au=1.1.1623147430.1722352697; gads=ID=216fbda0620ae86b:T=1722352702:RT=1722352702:S=ALNI_MZNs-fEAlxHCxq6BsaeC_WIgA4-EQ; gpi=UID=00000eadd56cc1d3:T=1722352702:RT=1722352702:S=ALNI_MYebBh12BRKb0UOEFY7WgI6VdQ_3Q; __eoi=ID=c4da445427c9097d:T=1722352702:RT=1722352702:S=AA-AfjY-XJtBJbJeYvwroEivUnkH; _ga_HPSLFXFRWN=GS1.1.1722352696.1.1.1722352814.49.0.0; FCNEC=%5B%5B%22AKsRol8BFX13MVyvSL7OY8ZrSTAebckv8wPfTrCMW1DE1tYr8VEiy7rMBoQcjLY0CRDrvSjn295ntNmsX-LPhWJax0uK6TSIdsJSAv0Ab3-_mdrR_PlHlCxjnHAOI9HOtB9JBR2yOiDhl5vz3VRYZ5pznbx6KldFEQ%3D%3D%22%5D%5D"
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