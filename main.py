import urllib.request
import urllib

localDir = "./pic/"

urlList = [
"https://hentaipaw.com/img/1/80/806150/"
]
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
opener = urllib.request.build_opener()#实例化一个OpenerDirector
opener.addheaders = [headers]#添加header,注意格式
urllib.request.install_opener(opener)#将OpenerDirector装进opener

for i in range(159):
    everyURL="https://hentaipaw.com/img/1/80/806150/"+str(i+1)+".webp"
    try:
        urllib.request.urlretrieve(everyURL,localDir+str(i+1)+".webp")
        print("download ok:"+everyURL)
    except:
        print("!!!download error:" + everyURL)

    # for everyFile in urlList:
#     everyURL = everyFile
#     # url split
#     localFileName = everyURL.split('/')[-1]
#     localFile = localDir  +  localFileName
# #     print (localFile)    # test strings
#     urllib.request.urlretrieve(everyURL, localFile)
#     print("download ok:"+localFileName)
