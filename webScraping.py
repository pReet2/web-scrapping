import requests
import bs4

response = requests.get('https://www.hackthissite.org/')
print(response.status_code)

r = requests.post('https://facebook.com/post', data = {'key':'value'})
print(response.text)

soup_obj = bs4.BeautifulSoup(response.text,'lxml')

print(soup_obj.prettify())

print(soup_obj.select('title')[0].getText())


links = soup_obj.find_all('a')
# find_all() will help to fetch all the details of the selected tag.
for link in links:
    print(link.get('href'))

# get() is used to extract the specific content from the tag

