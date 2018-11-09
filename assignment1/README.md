# Douban Dataset


## Data Source
This dataset ranks all TV series, which lists the directors and actors, from high to low in the 2010s on Douban website starting page:https://movie.douban.com/tag/#/?sort=S&range=1,10&tags=%E7%94%B5%E8%A7%86%E5%89%A7,%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86,2010%E5%B9%B4%E4%BB%A3&playable=1


## Data fields
* title - string. eg. 父母爱情
* score - float. eg. 9.3
* director - string. eg. 孔笙
* actor - string. eg. 郭涛 / 梅婷 / 王菁华 / 郭广平 / 张延
* url - string. eg. https://movie.douban.com/subject/19965220/


## Data Volume
2151 rows 5 columns 
(Douban can be updated everyday, so the numember of row is possible differnt every time.)


## License
CC 4.0


## Obstacles and solution
1. 我使用driver模拟浏览器的行为，寻找“加载更多”的按钮并且点击它，我使用了两种方法实现这个操作，但是哪种方法会更好？为什么？（个人感觉是第一种）无论是哪种方法都会出现点击到其他无关的链接并且跳转出新窗口的问题，只是出现的次数不同，如果可以避免这种问题的发生？
2. 当无关的页面弹出的时候，如果不返回原本需要爬区的页面是否会停止爬取行为？
3. 爬取出的数据同csv存的时候用了encoding = ‘gbk’，但再用pandas打开却显示有encoding的错误。
4. （已解决）在爬出所有电视剧的列表之后发现豆瓣自带的按照评分高低排序是存在错误的，因此要对这个list按照score进行重新排序，方法一是使用的sorted函数，用lambda进行排序，另一个方法是import一个新的函数operator，用itemgetter对指定的key进行排序，例如，title/director/actor/url都是按照score的高低进行排序，并一起输出（感觉没讲清楚..）


## future work
1. 我之后希望从第一个页面进入到含有更多details的每一个具体电视剧的页面，并且爬取里面相关的信息。但是在执行这一步的时候遇到了问题。
将所有电视剧的链接get之后把网页内容text化，并存进一个txt文件中，花费时常大约两个小时。怎么样可以优化这一步，电脑似乎跑不出来，这个txt文件有127.3MB。在requests.get过程中如果不进行time.sleep()的操作,豆瓣会进行id封号。
2. 我还想从第一个爬取到的页面计算每个演员出演了多少部电视剧分别的评分是多少，得出平均分，每个演员都有对应的分数，我用这个分数进行排名，体现在2010年代这个演员对中国大陆电视剧的贡献程度。

## bonus
1. 计划使用豆瓣的API接口丰富本数据集，可以在豆瓣开发者中看到提供的接口为GET/v2/movie，即我们可以调用 https://api.douban.com/v2/movie 获取更多电影信息
2. enrich数据集打算使用以下方法：在内存足够的情况下，直接append进txt文件中；内存不足时，可以将一定大小（<4GB）的数据存进test(1, 2, 3, ...).txt，使用shell脚本对所有文本进行外部排序，或使用多台pc并发处理。
3. API（Application Programming Interface, 应用程序编程接口）是一些预先定义的函数，目的是提供应用程序与开发人员基于某软件或硬件得以访问一组例程的能力，而又无需访问源码，或理解内部工作机制的细节。