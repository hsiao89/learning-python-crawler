import requests
import bs4

def getData(infor):
    headers = {"cookie": "over18=1"}
    page = requests.get(infor[0], headers=headers)
    data = bs4.BeautifulSoup(page.text, "html.parser")
    titles = data.find_all("div", class_= "title")

    infor = [""]
    i = 1
    for title in titles:
        if title.a != None:
            if "兔子" not in title.a.text:
            # print(title.a.text)
                infor.insert(i, "https://www.ptt.cc" + title.a["href"] + " " + title.a.text+ "\n")
                i = i + 1
    prePage = data.find("a", class_ = "btn wide", string = "‹ 上頁")
    newUrl = "https://www.ptt.cc"+prePage["href"]
    infor[0] = newUrl
    return infor

infor = ['https://www.ptt.cc/bbs/Gossiping/index.html']

num_of_files = 3
num_of_pages = 5

for x in range(1, num_of_files+1,1):
    file = open("gossiping"+str(x)+".txt", "w", encoding="utf-8")
    for i in range(1,num_of_pages,1):
        file.write("---------第"+ str(num_of_pages * (x-1) + i)+ "頁---------------- \n")
        file.write(infor[0] + '\n')
        infor = getData(infor)
        for inf in infor:
            file.write(inf)
file.close()

for x in range(1, num_of_files+ 1, 1):
    read = open("gossiping" + str(x) + ".txt", encoding="utf-8")
    print(read.read())
    read.close()
# print(titles.a.text)