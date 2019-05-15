import requests


r = requests.get('https://www.google.com/search?q=dataset+on+imagration+of+us+to+canada&rlz=1C1RLNS_enIN830IN830&oq=dataset+on+imagration+of+us+to+canada&aqs=chrome..69i57.28727j0j4&sourceid=chrome&ie=UTF-8')
c = r.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(c,features='html.parser')

