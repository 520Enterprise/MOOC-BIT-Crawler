import requests
import bs4
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Exception"


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  # 判断tr是否为bs4库中的Tag类型
            name_cn = tr.find_all(attrs={'class': 'name-cn'}, recursive=True)[0].get_text(strip=True)
            td = tr.find_all('td')
            UnivRank = td[0].get_text(strip=True)
            UnivLocation = td[2].get_text(strip=True)
            UnivType = td[3].get_text(strip=True)
            # 去除空格
            ulist.append([UnivRank, name_cn, UnivLocation, UnivType])


def printUnivList(ulist, num):
    print("{:^10}\t{:^20}\t{:^10}\t{:^10}".format("排名", "学校名称", "所在地", "类型"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^20}\t{:^10}\t{:^10}".format(u[0], u[1], u[2], u[3]))


def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2023"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs


if __name__ == '__main__':
    main()
