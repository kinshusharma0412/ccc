cookie="PHPSESSID=duftfgklue9rbldhjb51actt9t; _ga=GA1.1.2044615223.1722346123; _gcl_au=1.1.462248715.1722346123; gads=ID=fd7ad761181efb3b:T=1722346125:RT=1722346125:S=ALNI_MYjYSgMqC7JrvLlIBnBjLEirnq6cg; gpi=UID=00000eadc53f42e4:T=1722346125:RT=1722346125:S=ALNI_MZwEBO2DGngL9b9ivuPl6EWMMP5-g; __eoi=ID=a1137723df5b924b:T=1722346125:RT=1722346125:S=AA-Afjaxt1wp7qLE1AneJCa7O7PB; _ga_HPSLFXFRWN=GS1.1.1722346123.1.0.1722346128.55.0.0; FCNEC=%5B%5B%22AKsRol_qslUc1wg5V4r4Sl_zQFT79aIzgMpf1jE_W5Uu5fNUFfkOAAfJIz1XAhMM5T_I-BXZuabsHOmWzjC24d2oSeE7WL3igY4RYzd7QppnutIdF3uOE5KwCHc_tJjAERVfWrj5NDoqWMEHZtPlBJ-x64gmkKQPLg%3D%3D%22%5D%5D"
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