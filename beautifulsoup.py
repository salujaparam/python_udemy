from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML",features="html.parser")
soupp = BeautifulSoup("""<html><p class="subtitle">hi there</p><p>other paragraph</p><ul><li>one</li><li>two</li></ul></html>""", features="html.parser")
# print(soup.find('i').string)
# print(soup.find('i'))
l = soupp.find_all('li')
li = [e.string for e in l]
print(li)

def find_subtitle():
    para = soupp.find('p', {'class': 'subtitle'})
    print(para.string)
find_subtitle()

def find_other():
    paras = soupp.find_all('p')
    print(paras)
    other_para = [p for p in paras if 'subtitle' not in p.attrs.get('class', [])]
    print(other_para[0].string)

find_other()