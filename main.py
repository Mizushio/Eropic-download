import urllib.request
import urllib

localDir = "./pic/"
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
opener = urllib.request.build_opener()#实例化一个OpenerDirector
opener.addheaders = [headers]#添加header,注意格式
urllib.request.install_opener(opener)#将OpenerDirector装进opener
j=15
for i in range(2000):
    everyURL="https://hentaipaw.com/img/2/225/2254572/"+str(i+1)+".webp"
    # 这边写自己找到的本本的网址+后续格式
    if (j < 0):
        print("over!")
        break
    try:
        urllib.request.urlretrieve(everyURL,localDir+str(i+1)+".jpg")
        print("download ok:"+everyURL)
    except:
        print("!!!download error:" + everyURL)
        j=j-1
