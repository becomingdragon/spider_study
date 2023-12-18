import urllib.request
import urllib.parse

def create_request(page):
    url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '海口',
        'pid':'',
        'pageIndex': page,
        'pageSize': 10,
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers={
           'User-Agent':
         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    request = urllib.request.Request(url = url,data= data,headers = headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page, content):
    with open('kendeji_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

# 程序入口
if __name__ == '__main__':
    start_page = int(input('请输入开始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page,end_page+1):
#        请求对象定制
        request = create_request(page)
#       内容获取
        content = get_content(request)
#       将获取的内容下载到本地
        down_load(page,content)
