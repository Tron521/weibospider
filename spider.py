import requests
import csv
from bs4 import BeautifulSoup as bs
from time import sleep
import os
def post_ajax(page):
    url = f"https://m.weibo.cn/api/container/getIndex?containerid=2304133963209263_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=2302833963209263&page_type=03&page={page}"
    header = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64;rv: 73.0) Gecko / 20100101Firefox / 73.0",
        "Referer": "https: // m.weibo.cn / u / 6617213711",
        "Accept - Encoding": "gzip, deflate, br",
        "X - Requested - With": "XMLHttpRequest"
    }
    request = requests.get(url,headers=header,timeout=3)
    return request.json()
def get_data(json):
	items = json.get("data").get("cards")
	for item in items:
		result = []
		item = item.get("mblog")
		if item == None:
			continue
		print(item)
		result.append(bs(item.get("text"),"html.parser").get_text())
		result.append(item.get("created_at"))
		result.append(item.get("attitudes_count"))
		result.append(item.get("comments_count"))
		result.append(item.get("reposts_count"))
		yield result
def main():
	file = open("双笙0.0.csv","a",encoding="utf-8")
	writer = csv.writer(file)
	writer.writerow(["正文","日期","点赞","评论","转发"])
	for num in range(1,11):
		print("*"*5,f"正在爬取第{num}页","*"*5)
		json = post_ajax(str(num))
		for data in get_data(json):
			writer.writerow(data)
			sleep(5)
		os.system("cls")
	file.close()

if __name__ == "__main__":
	main()
