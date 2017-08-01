'''
enable 使能够，提供做…的权利[措施]; 使可能; 授予权利或方法;
dedicate  奉献,专注
keep track of 记录状态
retrieve 取回 获取
inspect 检查
propagate 繁衍 扩散
invocation 祈愿 调用
prepended 前缀
prepend 预先考虑 预谋  预置
precedence 优先
specify 指出，说明
manual 手册 指南
spawn   大量生产  卵,子
standard 标准的，一般的   标准，支柱
interpreter 翻译  编译器
hindered 妨碍，阻碍
pointless  无意义
cooperative 合作的协助的
counterparts  对手，同仁
block  阻塞 限制   街区
patched 打补丁
asynchronous 异步的
intensive 强烈的  加强的
dispatch  调度派遣

'''
#https://ronglianun0-PC:8443/svn/hot_news


'''
查看请求信息的网址
http://httpbin.org/get?show_env=1
'''

'''
src/lxml/etree_defs.h:9:31: fatal error: libxml/xmlversion.h: No such file or directory

centos系统
easy_install Cython
yum install libxslt-devel libxml2-devel
'''


'''
djcelery 使用
using django celery beat locally I get error 'PeriodicTask' object has no attribute '_default_manager'

目录: site_packages/djcelery/schedulers.py
把98行改为：
98 Model = type(self.model)
99 obj = Model._default_manager.get(pk=self.model.pk)
'''



'''
根据数据库已有生成model.py
python manage.py inspectdb  --database myapp > models.py
myapp 为setting当中配置的数据库名称
'''
'''
sudo find /var/log/ -type f -mtime +30 -exec rm -f {} \;
删除30天之前的旧文件
'''


'''
self.agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
		    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
		        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
			    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
			        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
				    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
				        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
					    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
					        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
						    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
						        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
							    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
							        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
								    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
								        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
									    'IE 9.0User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
									        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
										    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
										        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
											    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
											        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
												    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
												        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
													    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
													        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',
														    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
														        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
															    ]



															    '''



															    '''
															    requests post
															    样例代码：
															    import requests
															    url = 'https://api.github.com/some/endpoint'
															    payload = {'key1': 'value1', 'key2': 'value2'}
															    r = requests.post("http://httpbin.org/post", data=payload)
															    print r.text
															    '''


															    '''
															    django 修改时区
															    修改TIME_ZONE = 'Asia/Shanghai'，重启服务器，时间正常。

															    '''
															    '''
															    fuction() {setInterval( window.scrollTo(0,document.body.scrollHeight),7000 )}
															    '''

															    '''
															    查看程序启动和运行时间
															    ps -A -opid,stime,etime,args | grep phantomjs
															    查看程序开始运行时间
															    ps axo pid,ppid,comm,pmem,lstart | grep phantomjs
															    '''

															    '''
															    from module import 和 import module之间的不同。使用 import module，模块自身被导入，
															    但是它保持着自已的名字空间，这就是为什么你需要使用模块名来访问它的函数或属性（module.function）
															    的原因。但是使用 from module import，实际上是从另一个模块中将指定的函数和属性导入到你自己的名字
															    空间，这就是为什么你可以直接访问它们却不需要引用它们所来源的模块的原因。
															    '''


															    '''
															    查看linux版本
															    uname -a           #查看centos版本信息
															    file /bin/ls       #显示系统程序信息，就能看出多少位
															    get LONG_BIT       #获得机器字长
															    cat /proc/version  #查看os版本

															    修改环境变量
															    1、#临时修改
															    export PATH=$PATH:/etc/apache/bin  
															    2、针对用户修改
															    修改~/.bashrc或./bash_profile
															    加入
															    export PATH=$PATH:/etc/apache/bin
															    3、全局修改
															    修改/etc/profile文件,加入:
															    export PATH=$PATH:/etc/apache/bin
															    '''



															    #soup结果正则替换
															    reg = '''re.sub('(?isu)文章来源：|更新时间.*','',soup.find('div',attrs={'class':'sub_bt'}).find('span').text.encode('utf8','ignore'))'''


															    '''
															    selenium 操作cookies
															    driver.
															    get_cookies（） 获得cookie信息
															    add_cookie(cookie_dict)  向cookie添加会话信息
															    delete_cookie(name)   删除特定(部分)的cookie
															    delete_all_cookies()    删除所有cookie
															    '''




															    '''
															    产生相乘列表，结果为map
															    url_args = ["first_type":[1,2,3],"second_type":["a","b","c"]]
															    c_map_list=map(dict,product(*[list(product([k], v)) for k, v in url_args.items()]))
															    '''


															    '''
															    linux查找含有字符串的所有文件
															    grep -rn "hello,world!" *
															    *: 标示当前目录所有文件，也可以是某个文件名
															    -r 递归查找
															    -n 显示行号
															    -R 查找所有文件，包含子目录
															    -i 忽略大小写

															    \< 和 \> 分别标注单词的开始与结尾。

															    例如： 
															    grep man * 会匹配 ‘Batman’、‘manic’、‘man’等， 

															    grep '\<man' * 匹配‘manic’和‘man’，但不是‘Batman’， 

															    grep '\<man\>' 只匹配‘man’，而不是‘Batman’或‘manic’等其他的字符串。 

															    '^'：指匹配的字符串在行首， 

															    '$'：指匹配的字符串在行尾，


															    或者xargs配合grep查找
															    find -type f -name '*.php'|xargs grep 'GroupRecord'


															    查找多个字符串
															    grep -E   'aaaaa|bbbbbb'
															    '''
															    '''
															    redis批量删除键值
															    redis-cli keys "*" | xargs redis-cli del  
															    redis-cli -a password keys "*" | xargs redis-cli -a password del  
															    redis-cli -n 0 keys "*" | xargs redis-cli -n 0 del  
															    '''



															    '''
															    celery使用
															    @app.task(bind=True)
															    bind = True  task对象会作为第一个参数传入
															    加上filter=task_method, bind=True, task对象会作为第一个，实例(self)会作为第二个参数自动传入。
															    '''


															    '''
															    linux复制文件
															     for i in `ls | grep -v log`; do cp -r $i /home/spiderManager/kcy/tt/;done
															     或
															     find . ! -name "2.txt" -exec cp {} /target_dir \;
															     '''


															     '''
															     BeautifulSoup添加标签属性与删除标签属性
															     del a['class'] 
															     a['old_src']='http://www.baidu.com'
															     '''

															     '''
															     MySQL配置
															     编辑my.cnf，默认为/etc/mydql/my.cnf，
															     修改max_connections的值为10000，默认为100，实际MySQL服务器允许的最大连接数16384。
															     '''

															     '''
															     pyspider源码注释
															     首先，我用的分支是 https://github.com/tdifg/pyspider/tree/reading
															     '''

															     '''
															     使用lambda和filter、map操作字典类型数据
															     exam = { 'math': '95', 'eng': '96', 'chn': '90', 'phy': '', 'chem': '' }
															     t=['phy']
															     #筛选出非t的内容项
															     a=dict(filter(lambda x:x[0] not in t,exam.items()))
															     #对于a的每个元素加10后返回
															     b=dict(map(lambda (x,y): (x, int(y or 0)+10), a.items()))
															     '''



															     '''
															     #compile()  
															     str = "for i in range(0,10): print(i)"  
															     c = compile(str,'','exec')   # 编译为字节代码对象  
															     exec(c)                          # 执行  
															     str2 = "3*x + 4*y"  
															     c2 = compile(str2, '', 'eval')  # 编译为表达式

															     内置函数compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
															     这个函数用来编译一段字符串的源码，结果可以生成字节码或者AST（抽像语法树），字节码可以使用函数exec()来执行，而AST可以使用eval()来继续编译。

															     参数source是一串字符串的源码，或者是AST对象数组。

															     参数filename是读取字符串的文件对象，如果不是从文件里读取源码来编译，那么这里可以放一些用来标识这些代码的字符串。

															     参数mode是用来指明那种表示的源码类型；如果是exec类型，表示这是一个序列语句，可以进行运行；如果是eval类型，表示这是一个单一的表达式语句，可以用来计算相应的值出来；如果是single类型，表示这是一个单一语句，采用交互模式执行，在这种情况下，如果是一个表达式，一般会输出结果，而不是打印为None输出。

															     可选参数flags和dont_inherit是用来控制编译源码时的标志，可以查看PEP236文档来了解这些参数，以及相关编译的说明。如果两者使用缺省参数（也即两者都是零值），在调用本函数编译时，主要使用代码中指明的编译特征来对待；如果flags参数设置有值，而dont_inherit没有设置（即是零值），那么编译代码时，不仅源码的编译特征起作用，而且flags指明的特征也起作用，相当两者的并集；如果参数dont_inherit设置有值（即是非零值），编译语句时只有参数flags指明的编译特征值起作用，即是不使用源码里指明的特征。

															     编译特征是按位图的方式设置到参数里，可以查看__future__。

															     可选参数optimize是用来指明编译器使用优化的等级；缺省值是-1，表示使用命令行参数-O中获取的优化等级为准；如果设置值为0（即是不用优化，__debug__是设置true），是没有优化；如果设置值为1，assert语句被删除，__debug__设置为false；如果设置值为2，除了设置值为1的功能之外，还会把代码里文档说明也删除掉，达到最佳优化结果。

															     本函数编译代码时，如果语法出错会返回SyntaxError；如果代码包含一些空字节，则返回类型错误TypeError。

															     注意事项：当采用single或eval类型编译时，如果有多行代码，每行代码后面至少有一个换行符，否则在code模块编译时就会提示编译的源码不完整错误。在Python 3.2版本之后，允许输入Windows或Mac的换行符；当采用exec模式时，不需要在每个行后面输入换行符；在这个版本之后增加了优化参数。


															     '''



															     '''
															     selenium 操作实例
															     下载chromedriver.exe驱动程序放到c://python27目录下(该目录是path目录)

															     from selenium import webdriver
															     from selenium.webdriver.common.keys import Keys

															     driver=webdriver.Chrome(executable_path="chromedriver.exe")
															     driver.get("http://eastmoney.com")
															     content=driver.page_source   #获取网页源码
															     t=driver.find_element_by_id("su") #百度输入框的id内容
															     t.send_keys("kcy")  #输入框自动输入kcy
															     t.send_keys(Keys.RETURN)  #出发自动点击
															     s=driver.find_element_by_id("kw") #百度的click按钮
															     s.click()           #提交后页面



															     driver.implicitly_wait(10) # seconds     #等待10s

															     前进和后退功能
															     driver.forward()
															     driver.back()

															     清除输入的内容
															     element.clear()

															     '''


															     '''
															     获取dir的元素
															     _signames = dict((getattr(signal, signame), signame)
															                      for signame in dir(signal)
																	                       if signame.startswith('SIG') and '_' not in signame)
																			       '''

																			       '''
																			       selenium的webdriver等待
																			       显式等待

																			       显式等待指定某个条件，然后设置最长等待时间。如果在这个时间还没有找到元素，那么便会抛出异常了。

																			       from selenium import webdriver
																			       from selenium.webdriver.common.by import By
																			       from selenium.webdriver.support.ui import WebDriverWait
																			       from selenium.webdriver.support import expected_conditions as EC
																			        
																				driver = webdriver.Chrome()
																				driver.get("http://somedomain/url_that_delays_loading")
																				try:
																				    element = WebDriverWait(driver, 10).until(
																				            EC.presence_of_element_located((By.ID, "myDynamicElement"))
																					        )
																						finally:
																						    driver.quit()
																						    程序默认会 500ms 调用一次来查看元素是否已经生成，如果本来元素就是存在的，那么会立即返回。

																						    隐试等待
																						    driver = webdriver.Chrome()
																						    driver.implicitly_wait(10) # seconds
																						    driver.get("http://somedomain/url_that_delays_loading")
																						    myDynamicElement = driver.find_element_by_id("myDynamicElement")


																						    '''


																						    '''
																						    win7查看端口使用情况
																						    netstat -aon|findstr “提示的端口”
																						    '''


																						    '''
																						    redis-cli keys "*" | xargs redis-cli del  
																						    '''

																						    '''
																						    从网页中删除一个标签

																						    删除标签的方法有decomose()和extract()方法


																						    使用decompose()删除生产者


																						    我们现在移去class="name"属性的div标签，使用decompose()方法。

																						    [python] view plain copy
																						    在CODE上查看代码片派生到我的代码片

																						        third_producer = soup.find_all("li")[2]  
																							    div_name = third_producer.div  
																							        div_name.decompose()  
																								    print(third_producer.prettify())  

																								    decompose()方法会移去标签及标签的子代。
																								    使用extract()删除生产者

																								    extract()用于删除一个HTMNL文档中昂的标签或者字符串，另外，它还返回一个被删除掉的标签或字符串的句柄。
																								    不同于decompose()，extract也可以用于字符串。

																								    [python] view plain copy
																								    在CODE上查看代码片派生到我的代码片

																								        third_producer_removed=third_producer.extract()  
																									    print(soup.prettify())  

																									    '''

																									    '''
																									     Python解析非标准JSON（Key值非字符串）

																									     采集数据的时候经常碰到一些JSON数据的Key值不是字符串，这些数据在JavaScript的上下文中是可以解析的，
																									     但在Python中，没有该部分数据的上下文，无法采用json.loads(JSON)的形式导入。在网上搜集来一些方法以便日后使用。
																									     方法一：

																									     def parse_js(expr):
																									         """
																										     解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
																										         :param expr:非标准JSON的Javascript字符串
																											     :return:Python字典
																											         """
																												     obj = eval(expr, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
																												         return obj

																													 方法二(推荐)

																													 def parse_js(expr):
																													     """
																													         解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
																														     :param expr:非标准JSON的Javascript字符串
																														         :return:Python字典
																															     """
																															         import ast
																																     m = ast.parse(expr)
																																         a = m.body[0]

																																	     def parse(node):
																																	             if isinstance(node, ast.Expr):
																																		                 return parse(node.value)
																																				         elif isinstance(node, ast.Num):
																																					             return node.n
																																						             elif isinstance(node, ast.Str):
																																							                 return node.s
																																									         elif isinstance(node, ast.Name):
																																										             return node.id
																																											             elif isinstance(node, ast.Dict):
																																												                 return dict(zip(map(parse, node.keys), map(parse, node.values)))
																																														         elif isinstance(node, ast.List):
																																															             return map(parse, node.elts)
																																																             else:
																																																	                 raise NotImplementedError(node.__class__)

																																																			     return parse(a)

																																																			     '''

																																																			     '''
																																																			     linux 不能使用回退键
																																																			     stty命令设置一下：
																																																			     stty erase ^h

																																																			     '''


																																																			     '''
																																																			     DBUtils是一套Python数据库连接池包，并允许对非线程安全的数据库接口进行线程安全包装。DBUtils来自Webware for Python。

																																																			     DBUtils提供两种外部接口：
																																																			     * PersistentDB ：提供线程专用的数据库连接，并自动管理连接。
																																																			     * PooledDB ：提供线程间可共享的数据库连接，并自动管理连接。

																																																			     PooledDB的参数：
																																																			     1. mincached，最少的空闲连接数，如果空闲连接数小于这个数，pool会创建一个新的连接
																																																			     2. maxcached，最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接
																																																			     3. maxconnections，最大的连接数，
																																																			     4. blocking，当连接数达到最大的连接数时，在请求连接的时候，如果这个值是True，请求连接的程序会一直等待，直到当前连接数小于最大连接数，如果这个值是False，会报错，
																																																			     5. maxshared 当连接数达到这个数，新请求的连接会分享已经分配出去的连接在uwsgi中，每个http请求都会分发给一个进程，连接池中配置的连接数都是一个进程为单位的（即上面的最大连接数，都是在一个进程中的连接数），而如果业务中，一个http请求中需要的sql连接数不是很多的话（其实大多数都只需要创建一个连接），配置的连接数配置都不需要太大。
																																																			     连接池对性能的提升表现在：
																																																			     1.在程序创建连接的时候，可以从一个空闲的连接中获取，不需要重新初始化连接，提升获取连接的速度
																																																			     2.关闭连接的时候，把连接放回连接池，而不是真正的关闭，所以可以减少频繁地打开和关闭连接


																																																			     PooledDB有这么几个参数：

																																																			     * creator
																																																			         可以生成 DB-API 2 连接的任何函数或 DB-API 2 兼容的数据库连接模块。
																																																				 * mincached
																																																				     启动时开启的空连接数量(缺省值 0 意味着开始时不创建连接)
																																																				     * maxcached
																																																				         连接池使用的最多连接数量(缺省值 0 代表不限制连接池大小)
																																																					 * maxshared
																																																					     最大允许的共享连接数量(缺省值 0 代表所有连接都是专用的)
																																																					     * maxconnections
																																																					         最大允许连接数量(缺省值 0 代表不限制)
																																																						 * blocking
																																																						     设置在达到最大数量时的行为(缺省值 0 或 False)
																																																						     * maxusage
																																																						         单个连接的最大允许复用次数(缺省值 0 或 False 代表不限制的复用)
																																																							 * setsession:
																																																							     一个可选的SQL命令列表用于准备每个会话，如 ["set datestyle to german", ...]


																																																							     '''

																																																							     '''
																																																							     centos查看时区
																																																							     date -R

																																																							     修改东八区
																																																							     （将Asia/shanghai-上海时区写入当前时区）
																																																							     #cp -f /usr/share/zoneinfo/Asia/Shanghai     /etc/localtime

																																																							     '''

																																																							     '''
																																																							     (1)按位与运算符(&)
																																																							         按位与运算将两个运算分量的对应位按位遵照以下规则进行计算：
																																																								      0 & 0 = 0, 0 & 1 = 0, 1 & 0 = 0, 1 & 1 = 1。
																																																								      即同为 1 的位，结果为 1，否则结果为 0。
																																																								      (2)按位或运算符(|)
																																																								          按位或运算将两个运算分量的对应位按位遵照以下规则进行计算：
																																																									       0 | 0 = 0, 0 | 1 = 1, 1 | 0 = 1, 1 | 1 = 1
																																																									       即只要有1个是1的位，结果为1，否则为0。
																																																									       (3)按位异或运算符(^)
																																																									           按位异或运算将两个运算分量的对应位按位遵照以下规则进行计算：
																																																										        0 ^ 0 = 0, 0 ^ 1 = 1, 1 ^ 0 = 1, 1 ^ 1 = 0
																																																											即相应位的值相同的，结果为 0，不相同的结果为 1。
																																																											(4)按位取反运算符(~)
																																																											    按位取反运算是单目运算，用来求一个位串信息按位的反，
																																																											        即哪些为0的位，结果是1，
																																																												    而哪些为1的位，结果是0。
																																																												        例如, ~7的结果为0xfff8。
																																																													(1)左移运算符(<<)
																																																													每左移1位相当于乘2。如4 << 2，结果为16
																																																													(2)右移运算符(>>)
																																																													右端移出的位的信息被丢弃。例如12>>2,结果为3
																																																													'''


																																																													'''
																																																													python里面的字符，如果开头处有个r，说明字符串r"XXX"中的XXX是普通字符
																																																													python3.x里默认的str是(py2.x里的)unicode,  bytes是(py2.x)的str, b""前缀代表的就是bytes
																																																													python2.x里, b前缀没什么具体意义， 只是为了兼容python3.x的这种写法
																																																													'''


																																																													'''
																																																													链表做文本处理矩阵计算：交换行列

																																																													#由三个长度为 4 的列表组成的 3x4 矩阵,交换行列 
																																																													>>> matrix = [
																																																													... [1, 2, 3, 4],
																																																													... [5, 6, 7, 8],
																																																													... [9, 10, 11, 12],
																																																													... ]
																																																													>>> [[row[i] for row in matrix] for i in range(4)]
																																																													[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
																																																													等于
																																																													>>> transposed = []
																																																													>>> for i in range(4):
																																																													... transposed.append([row[i] for row in matrix])
																																																													...
																																																													>>> transposed
																																																													[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
																																																													'''
																																																													'''
																																																													.encode("raw_unicode_escape") 不用转那么多次，直接用这个就行
																																																													'''
																																																													getattr(e, 'value', None)


																																																													'''
																																																													查看mysql连接数
																																																													select SUBSTRING_INDEX(host,':',1) as ip , count(*) 
																																																													from information_schema.processlist 
																																																													group by ip;
																																																													'''

																																																													'''
																																																													根据传入的参数生成变量
																																																													s={"a":0}
																																																													globals().update(s)
																																																													print a  #0
																																																													或
																																																													def f(name):
																																																													    exec "%s = 0"%(name)
																																																													        return name
																																																														'''
																																																														'''
																																																														#新建目录  删除目录
																																																														import os
																																																														import shutil
																																																														# shutil.rmtree('result/detail')
																																																														# os.rmdir('result/list')
																																																														os.mkdir('result/list')
																																																														os.mkdir('result/detail')

																																																														'''

																																																														'''
																																																														from module import 和 import module之间的不同。
																																																														使用 import module，模块自身被导入，但是它保持着自已的名字空间，
																																																														这就是为什么你需要使用模块名来访问它的函数或属性（module.function）的原因。
																																																														但是使用 from module import，实际上是从另一个模块中将指定的函数和属性导入到你自己的名字空间，
																																																														这就是为什么你可以直接访问它们却不需要引用它们所来源的模块的原因
																																																														'''



																																																														'''

																																																														# DB Config
																																																														DB_CONFIG = { 
																																																														    "host" : "localhost",
																																																														        "port" : 3306,
																																																															    "user" : "coder4",
																																																															        "passwd" : "password",
																																																																    "db" : "db",
																																																																        "use_unicode" : True,
																																																																	    "charset" : "utf8"
																																																																	    }
																																																																	     
																																																																	     # Init conn
																																																																	     self.conn = MySQLdb.connect(**DB_CONFIG)
																																																																	     '''


																																																																	     '''
																																																																	         # re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
																																																																		     # re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
																																																																		         # re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
																																																																			     # re_br=re.compile('<br\s*?/?>')#处理换行
																																																																			         # re_h=re.compile('</?\w+[^>]*>')#HTML标签
																																																																				     # re_comment=re.compile('<!--[^>]*-->')#HTML注释
																																																																				         # s=re_cdata.sub('',htmlstr)#去掉CDATA
																																																																					     # s=re_script.sub('',s) #去掉SCRIPT
																																																																					         # s=re_style.sub('',s)#去掉style
																																																																						     # s=re_br.sub('\n',s)#将br转换为换行
																																																																						         # s=re_h.sub('',s) #去掉HTML 标签
																																																																							     # s=re_comment.sub('',s)#去掉HTML注释
																																																																							         # blank_line=re.compile('\n+')
																																																																								     # s=blank_line.sub('\n',s)
																																																																								         # # s=replaceCharEntity(s)#替换实体
																																																																									     s=htmlstr
																																																																									         # s=re.sub("(?isu)<script[^>]*>.*?</script>","",s)
																																																																										     # s=re.sub("(?isu)<style[^>]*>.*?</style>","",s)
																																																																										         s=re.sub("(?isu)<!--[^>]*-->","",s)
																																																																											     s=re.sub("(?isu)<!--\[[^>]*\][^>]*>.*?<[^>]*\[[^>]*\]-->","",s)
																																																																											     '''

																																																																											     '''
																																																																											     查找/opt/web/blog目录下所有包含 demo.fity.cn的文件 
																																																																											     grep -lr "demo.fity.cn" /opt/web/blog/*

																																																																											     vim替换单个文件中所有字符串的方法
																																																																											     :%s/demo/blog/g   #注释  %表示替换所有行，g表示替换一行中所有的匹配点

																																																																											     替换文件夹下包含字符串的文件
																																																																											     #sed与grep结合，将目录/opt/web/blog下所有的文件中demo.fity.cn替换为fity.cn
																																																																											     sed -i "s/demo.fity.cn/fity.cn/g" `grep demo.fity.cn -lr /opt/web/blog/*`
																																																																											     '''

																																																																											     '''
																																																																											     key_words 提取
																																																																											         try:
																																																																												         keywords=soup.find(attrs={"name":"keywords"})['content']
																																																																													         content_map['keywords']=keywords.strip()
																																																																														     except Exception,e:
																																																																														             print "has no keywords, "+str(e)

																																																																															     '''


																																																																															     '''
																																																																															     centos查看环境变量
																																																																															     $echo $PATH  
																																																																															     系统中所有bin,sbin目录
																																																																															     find / -type d -name *bin 
																																																																															     .修改/etc/profile文件
																																																																															     将没有包含在PATH变量中的bin,sbin目录加入到PATH中。比如profile文件中末尾加入
																																																																															     export   PATH=/usr/sbin:/bin:/usr/local/sbin:/usr/local/share/bin:$PATH

																																																																															     执行source /etc/profile
																																																																															     '''


																																																																															     '''
																																																																															     No module named setuptools 解决方案 2013-11-14 12:55:03
																																																																															     分类： Python/Ruby
																																																																															     ImportError: No module named setuptools 解决方案  
																																																																															     shell中输入：
																																																																															     wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz
																																																																															     tar zxvf setuptools-0.6c11.tar.gz
																																																																															     cd setuptools-0.6c11
																																																																															     python setup.py build
																																																																															     python setup.py install

																																																																															     '''



																																																																															     '''
																																																																															     了解异步IO模型及常用异步IO框架

																																																																															     同步 异步  阻塞  非阻塞
																																																																															     同步是指：发送方发出数据后，等接收方发回响应以后才发下一个数据包的通讯方式。  
																																																																															     异步是指：发送方发出数据后，不等接收方发回响应，接着发送下个数据包的通讯方式。  
																																																																															     ---------------------------------------------------------------  
																																																																															      
																																																																															      举个不太恰当的例子,就像:  
																																																																															      SendMessage(...)  
																																																																															      TRACE0("just  like  send");  
																																																																															       
																																																																															       PostMessage(...)  
																																																																															       TRACE0("just  like  WSASend  using  overlapped");  
																																																																															        
																																																																																SendMessage是调用的时候不返回,等消息响应后才执行TRACE0,这就是同步.  
																																																																																PostMessage是调用后马上返回,不用消息响应就执行TRACE0,这就是异步.
																																																																																答案三：
																																																																																 同步和异步的区别 
																																																																																  举个例子：普通B/S模式（同步）AJAX技术（异步）
																																																																																  同步：提交请求->等待服务器处理->处理完毕返回 这个期间客户端浏览器不能干任何事
																																																																																  异步: 请求通过事件触发->服务器处理（这是浏览器仍然可以作其他事情）->处理完毕
																																																																																  --------------------------------------------------------------------------------------------------------------------
																																																																																  同步就是你叫我去吃饭，我听到了就和你去吃饭；如果没有听到，你就不停的叫，直到我告诉你听到了，才一起去吃饭。
																																																																																  异步就是你叫我，然后自己去吃饭，我得到消息后可能立即走，也可能等到下班才去吃饭。
																																																																																  所以，要我请你吃饭就用同步的方法，要请我吃饭就用异步的方法，这样你可以省钱。
																																																																																  --------------------------------------------------------------------------------------------------------------------
																																																																																  举个例子 打电话时同步 发消息是异步
																																																																																  -------------------------------------------------------------
																																																																																  同步、异步、阻塞和非阻塞的概念

																																																																																  在进行网络编程时，我们常常见到同步、异步、阻塞和非阻塞四种调用方式。这些方式彼此概念并不好理解。下面是我对这些术语的理解。
																																																																																  同步

																																																																																  所谓同步，就是在发出一个功能调用时，在没有得到结果之前，该调用就不返回。按照这个定义，其实绝大多数函数都是同步调用（例如sin, isdigit等）。但是一般而言，我们在说同步、异步的时候，特指那些需要其他部件协作或者需要一定时间完成的任务。最常见的例子就是 SendMessage。该函数发送一个消息给某个窗口，在对方处理完消息之前，这个函数不返回。当对方处理完毕以后，该函数才把消息处理函数所返回的 LRESULT值返回给调用者。
																																																																																  异步

																																																																																  异步的概念和同步相对。当一个异步过程调用发出后，调用者不能立刻得到结果。实际处理这个调用的部件在完成后，通过状态、通知和回调来通知调用者。以CAsycSocket类为例（注意，CSocket从CAsyncSocket派生，但是起功能已经由异步转化为同步），当一个客户端通过调用 Connect函数发出一个连接请求后，调用者线程立刻可以朝下运行。当连接真正建立起来以后，socket底层会发送一个消息通知该对象。这里提到执行部件和调用者通过三种途径返回结果：状态、通知和回调。可以使用哪一种依赖于执行部件的实现，除非执行部件提供多种选择，否则不受调用者控制。如果执行部件用状态来通知，那么调用者就需要每隔一定时间检查一次，效率就很低（有些初学多线程编程的人，总喜欢用一个循环去检查某个变量的值，这其实是一种很严重的错误）。如果是使用通知的方式，效率则很高，因为执行部件几乎不需要做额外的操作。至于回调函数，其实和通知没太多区别。
																																																																																  阻塞

																																																																																  阻塞调用是指调用结果返回之前，当前线程会被挂起。函数只有在得到结果之后才会返回。有人也许会把阻塞调用和同步调用等同起来，实际上他是不同的。对于同步调用来说，很多时候当前线程还是激活的，只是从逻辑上当前函数没有返回而已。例如，我们在CSocket中调用Receive函数，如果缓冲区中没有数据，这个函数就会一直等待，直到有数据才返回。而此时，当前线程还会继续处理各种各样的消息。如果主窗口和调用函数在同一个线程中，除非你在特殊的界面操作函数中调用，其实主界面还是应该可以刷新。socket接收数据的另外一个函数recv则是一个阻塞调用的例子。当socket工作在阻塞模式的时候，如果没有数据的情况下调用该函数，则当前线程就会被挂起，直到有数据为止。
																																																																																  非阻塞

																																																																																  非阻塞和阻塞的概念相对应，指在不能立刻得到结果之前，该函数不会阻塞当前线程，而会立刻返回。
																																																																																  对象的阻塞模式和阻塞函数调用
																																																																																  对象是否处于阻塞模式和函数是不是阻塞调用有很强的相关性，但是并不是一一对应的。阻塞对象上可以有非阻塞的调用方式，我们可以通过一定的API去轮询状态，在适当的时候调用阻塞函数，就可以避免阻塞。而对于非阻塞对象，调用特殊的函数也可以进入阻塞调用。函数select就是这样的一个例子
																																																																																  '''

																																																																																  '''
																																																																																  后端启动含有100个线程的线程池。
																																																																																  celery -A tasks worker  -c 100 --loglevel=info

																																																																																  异步的celery获取任务执行状态
																																																																																  @app.route("/") 
																																																																																  def index(): 
																																																																																       return "hello" 
																																																																																       @app.route("/test") 
																																																																																       def test(x=10, y=12): 
																																																																																            x = int(request.args.get("x", x)) 
																																																																																	         y = int(request.args.get("y", y)) 
																																																																																		      res = add.apply_async((x, y)) 
																																																																																		           retval = add.AsyncResult(res.task_id).get(timeout=7.0) 
																																																																																			        return repr(retval) 
																																																																																				'''

																																																																																				'''
																																																																																				#多个dict组成的list列表，根据dict的键值进行排序
																																																																																				from operator import itemgetter
																																																																																				aa=[{'a':1,'b':2},{'a':10,'b':1}]
																																																																																				sorted(aa,key=itemgetter('b'))    # 根据b的值进行排序
																																																																																				'''

																																																																																				'''
																																																																																				#查询ip的登录链接数据
																																																																																				SELECT SUBSTRING_INDEX(HOST,':',1) AS ip , COUNT(*) FROM information_schema.processlist 
																																																																																				GROUP BY ip;
																																																																																				mysql添加唯一索引
																																																																																				ALTER TABLE `t_user` ADD unique(`username`);

																																																																																				#查看链接
																																																																																				SHOW PROCESSLIST
																																																																																				'''

																																																																																				'''
																																																																																				#替换img和p以外 的所有标签为空
																																																																																				import re
																																																																																				t = '<html>asdfasdf<head>1111111111<body><p>asdfasdfasdf</p> <img herf="fff">'
																																																																																				def replace_two(m):
																																																																																				    """
																																																																																				        #过滤掉页面中除了<p></p>和<img>以外所有的标签
																																																																																					    """
																																																																																					        all = re.findall(r'</?.*?>',m)
																																																																																						    save = re.findall(r'</?(?:img).*?>|</?[pP]*?>',m)
																																																																																						     
																																																																																						         for e in all:
																																																																																							         if e not in save:
																																																																																								             m1 = m.replace(e, '')
																																																																																									                 m = m1
																																																																																											     return m
																																																																																											     print replace_two(t)

																																																																																											     []的用法是匹配[]中的任意一个字符，加^是不匹配的意思，你这样写会把以i、m和g开头标签都会过滤掉的

																																																																																											     '''



																																																																																											     '''
																																																																																											     t='2016-08-23 19:00'
																																																																																											     #把字符串格式化为日期格式
																																																																																											     def formattime(t_str):
																																																																																											       format_time = datetime.datetime(*time.strptime(t_str,'%Y-%m-%d %H:%M')[:5]).strftime('%Y-%m-%d %H:%M')
																																																																																											         return format_time
																																																																																												 '''
																																																																																												 '''
																																																																																												 linux定时任务重启
																																																																																												 1.在系统中有service这个命令时：
																																																																																												 这个命令在red hat当中常用,有的linux发行版本中没有这个命令.
																																																																																												 $ service crond start //启动服务
																																																																																												 $ service crond stop //关闭服务
																																																																																												 $ service crond restart //重启服务

																																																																																												 2.linux发行版本没有service这个命令时：
																																																																																												 /etc/init.d/cron stop
																																																																																												 /etc/init.d/cron start
																																																																																												 '''


																																																																																												 '''
																																																																																												 开放端口：/sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT
																																																																																												 关闭端口：/sbin/iptables -I INPUT -p tcp --dport 80 -j DROP
																																																																																												 保存修改：/etc/rc.d/init.d/iptables save
																																																																																												 查看状态：/etc/init.d/iptables status
																																																																																												 重启防火墙：/etc/init.d/iptables restart
																																																																																												 关闭防火墙：/etc/init.d/iptables stop
																																																																																												 启动防火墙：/etc/init.d/iptables stop
																																																																																												 '''

																																																																																												 '''
																																																																																												 shutil.rmtree(filepath,True) #删除非空文件夹
																																																																																												 os.remove(filepath)  #删除空目录
																																																																																												 os.mkdir(filepath)   #创建目录
																																																																																												 >>> a = {'1':'2'}
																																																																																												 >>> b = {'3':'4'}
																																																																																												 >>> a.update(b)
																																																																																												 该方法把b的元素加入到a中去，键字重复时会覆盖a中的键值
																																																																																												  '''

																																																																																												  '''
																																																																																												  django 
																																																																																												  session的超时时间设置
																																																																																												  settings中
																																																																																												  SESSION_COOKIE_AGE=60*30 30分钟。
																																																																																												  SESSION_EXPIRE_AT_BROWSER_CLOSE False：会话cookie可以在用户浏览器中保持有效期。True：关闭浏览器，则Cookie失效。
																																																																																												  SESSION_COOKIE_DOMAIN 生效站点
																																																																																												  SESSION_COOKIE_NAME cookie中保存session的名称
																																																																																												  Session使用比较简单，在request.session是一个字典类。session是保存在数据库中的。

																																																																																												  '''



																																																																																												  '''
																																																																																												  1、查看时间和日期
																																																																																												  date
																																																																																												  2、设置时间和日期
																																																																																												  将系统日期设定成1996年6月10日的命令
																																																																																												  date -s 06/22/96
																																																																																												  将系统时间设定成下午1点52分0秒的命令
																																																																																												  date -s 13:52:00
																																																																																												  3. 将当前时间和日期写入BIOS，避免重启后失效
																																																																																												  hwclock -w
																																																																																												  三、定时同步时间
																																																																																												  * * * * * /usr/sbin/ntpdate 210.72.145.44 > /dev/null 2>&1
																																																																																												  Linux中用于时钟查看和设置的命令主要有date、hwclock和clock。
																																																																																												  其中，clock和hwclock用法相近，只用一个就行，只不过clock命令除了支持x86硬件体系外，还支持Alpha硬件体系。

																																																																																												  '''


																																																																																												  '''
																																																																																												  用Curl测试POST 
																																																																																												   POST请求  

																																																																																												   http://172.16.102.208:8089/wiapi/score?leaderboard_id=1&score=36&app_key=66 

																																																																																												     目的1：通过脚本发送post请求。
																																																																																												       答案： 

																																																																																												       curl -d "leaderboard_id=7778a8143f111272&score=19&app_key=8d49f16fe034b98b&_test_user=test01" "http://172.16.102.208:8089/wiapi/score" 

																																																																																												         目的2：通过脚本发送post请求，顺便附带文本数据，比如通过"浏览"选择本地的card.txt并上传发送post请求
																																																																																													   答案：  

																																																																																													   curl  -F "blob=@card.txt;type=text/plain"  "http://172.16.102.208:8089/wiapi/score?leaderboard_id=7778a8143f111272&score=40&app_key=8d49f16fe034b98b&_test_user=test01" 
																																																																																													   其中-F 为带文件的形式发送post请求，   blob为文本框中的name元素对应的属性值。<type="text" name="blob">

																																																																																													   '''





																																																																																													   '''
																																																																																													   win7 安装 pyspider
																																																																																													   windows下安装

																																																																																													   需要安装如下两个exe之后再执行pip： 
																																																																																													   - lxml 
																																																																																													   - pycurl
																																																																																													   然后执行
																																																																																													   easy_install pyspider
																																																																																													   '''


																																																																																													   '''
																																																																																													    ps -Lf pid 查看对应进程下的线程数
																																																																																													    '''

																																																																																													    '''
																																																																																													    ubuntu 安装更新
																																																																																													    安装server的时候选择自动安装更新
																																																																																													    更换更新源  /etc/apt/sources.list

																																																																																													    遇到问题
																																																																																													    ubuntu
																																																																																													    sudo apt-get update
																																																																																													    错误：
																																																																																													    W: GPG error: http://extras.ubuntu.com precise Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 16126D3A3E5C1192

																																																																																													    解决：
																																																																																													    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 16126D3A3E5C1192

																																																																																													    '''

																																																																																													    '''
																																																																																													    首先，gevent是一个网络库：libevent是一个事件分发引擎，greenlet提供了轻量级线程的支持。
																																																																																													    所以它不适合处理有长时间阻塞IO的情况。
																																																																																													    gevent就是基于这两个东西的一个专门处理网络逻辑的并行库。

																																																																																													    1. gevent.spawn启动的所有协程，都是运行在同一个线程之中，所以协程不能跨线程同步数据。
																																																																																													    2. gevent.queue.Queue 是协程安全的。
																																																																																													    3. gevent启动的并发协程，具体到task function，不能有长时间阻塞的IO操作。因为gevent的协程的特点是，当前协程阻塞了才会切换到别的协程。
																																																																																													    如果当前协程长时间阻塞，则不能显示（gevent.sleep(0)，或隐式，由gevent来做）切换到别的协程。导致程序出问题。
																																																																																													    4. 如果有长时间阻塞的IO操作，还是用传统的线程模型比较好。
																																																																																													    5. 因为gevent的特点总结是：事件驱动+协程+非阻塞IO，事件驱动值得是libvent对epool的封装，来基于事件的方式处理IO。
																																																																																													    协程指的是greenlet，非阻塞IO指的是gevent已经patch过的各种库，例如socket和select等等。
																																																																																													    6. 使用gevent的协程，最好要用gevent自身的非阻塞的库。如httplib, socket, select等等。
																																																																																													    7. gevent适合处理大量无阻塞的任务，如果有实在不能把阻塞的部分变为非阻塞再交给gevent处理，就把阻塞的部分改为异步吧。
																																																																																													    '''







																																																																																													    '''
																																																																																													    1）多进程能够利用多核优势，但是进程间通信比较麻烦，另外，进程数目的增加会使性能下降，进程切换的成本较高。
																																																																																													       程序流程复杂度相对I/O多路复用要低。
																																																																																													       2）I/O多路复用是在一个进程内部处理多个逻辑流程，不用进行进程切换，性能较高，另外流程间共享信息简单。
																																																																																													          但是无法利用多核优势，另外，程序流程被事件处理切割成一个个小块，程序比较复杂，难于理解。
																																																																																														  3）线程运行在一个进程内部，由操作系统调度，切换成本较低，另外，他们共享进程的虚拟地址空间，线程间共享信息简单。但是线程安全问题导致线程学习曲线陡峭，而且易出错。
																																																																																														  4）协程有编程语言提供，由程序员控制进行切换，所以没有线程安全问题，可以用来处理状态机，并发请求等。
																																																																																														     但是无法利用多核优势。
																																																																																														     上面的四种方案可以配合使用，我比较看好的是进程+协程的模式。
																																																																																														     '''


																																																																																														     '''
																																																																																														     接着您需要将 /home/projects/mysite 加入到 PYTHONPATH 环境变量中并将 mysite.settings 
																																																																																														     设置为 DJANGO_SETTINGS_MODULE 环境变量。 这可以在Scrapy设置文件中添加下列代码:

																																																																																														     import sys
																																																																																														     sys.path.append('/home/projects/mysite')

																																																																																														     import os
																																																																																														     os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


																																																																																														     '''


																																																																																														     '''
																																																																																														     查看端口是否被占用
																																																																																														     netstat -ap | grep 8077
																																																																																														     '''

																																																																																														     '''
																																																																																														     安装
																																																																																														     sudo apt-get install nginx
																																																																																														     卸载
																																																																																														     sudo apt-get remove nginx
																																																																																														     '''



																																																																																														     '''字典操作'''
																																																																																														     mm={"a":1,"b":2,"c":3}
																																																																																														     mm.clear()  #清空字典
																																																																																														     mm.pop('a') #取出a并删除a
																																																																																														     mm.popitem() #随机取出一个元素并删除该元素


																																																																																														     '''tornado'''
																																																																																														     '''
																																																																																														     Tornado 的 Web 程序会将 URL 或者 URL 范式映射到 tornado.web.RequestHandler 的子类上去。
																																																																																														     在其子类中定义了 get() 或 post() 方法，用以处理不同的 HTTP 请求
																																																																																														     可以使用 get_argument() 方法来获取查询字符串参数，以及解析 POST 的内容：
																																																																																														     def post(self):
																																																																																														             self.set_header("Content-Type", "text/plain")
																																																																																															             self.write("You wrote " + self.get_argument("message"))

																																																																																																     上传的文件可以通过 self.request.files 访问到，该对象将名称（HTML元素 <input type="file">的 name 属性）
																																																																																																     对应到一个文件列表。每一个文件都以字典的形式 存在，
																																																																																																     其格式为 {"filename":..., "content_type":..., "body":...}。

																																																																																																     请求处理程序可以通过 self.request 访问到代表当前请求的对象。该 HTTPRequest 对象包含了一些有用的属性，包括：
																																																																																																     arguments - 所有的 GET 或 POST 的参数
																																																																																																     files - 所有通过 multipart/form-data POST 请求上传的文件
																																																																																																     path - 请求的路径（ ? 之前的所有内容）
																																																																																																     headers - 请求的开头信息
																																																																																																     可以通过查看源代码 httpserver 模组中 HTTPRequest 的定义，从而了解到它的 所有属性

																																																																																																     Tornado 中的重定向有两种主要方法：self.redirect，或者使用 RedirectHandler。
																																																																																																     permanent 的默认值是 False，这是为了适用于常见的操作，例如用户端在成功发送 POST 请求 以后的重定向。
																																																																																																     例如:
																																																																																																         self.redirect('/some-canonical-page', permanent=True)
																																																																																																	 RedirectHandler 会在你初始化 Application 时自动生成。
																																																																																																	 例如本站的下载 URL，由较短的 URL 重定向到较长的 URL 的方式是这样的：
																																																																																																	 application = tornado.wsgi.WSGIApplication([
																																																																																																	     (r"/([a-z]*)", ContentHandler),
																																																																																																	         (r"/static/tornado-0.2.tar.gz", tornado.web.RedirectHandler,
																																																																																																		      dict(url="http://github.com/downloads/facebook/tornado/tornado-0.2.tar.gz")),
																																																																																																		      ], **settings)
																																																																																																		      RedirectHandler 的默认状态码是 301 Moved Permanently，不过如果你想使用 302 Found 状态码，
																																																																																																		      你需要将 permanent 设置为 False。
																																																																																																		      application = tornado.wsgi.WSGIApplication(
																																																																																																		          [(r"/foo", tornado.web.RedirectHandler, {"url":"/bar", "permanent":False}),], **settings)
																																																																																																			  注意，在 self.redirect 和 RedirectHandler 中，permanent 的默认值是不同的。 这样做是有一定道理的，
																																																																																																			  self.redirect 通常会被用在自定义方法中，是由逻辑事件触发 的（例如环境变更、用户认证、以及表单提交）。
																																																																																																			  而 RedirectHandler 是在每次匹配到请求 URL 时被触发

																																																																																																			  所有的模板输出都已经通过 tornado.escape.xhtml_escape 自动转义(escape)，
																																																																																																			  这种默认行为， 可以通过以下几种方式修改：将 autoescape=None 传递给 Application 或者 TemplateLoader、 在模板文件中加入 {% autoescape None %}、或者在简单表达语句 {{ ... }} 写成 {% raw ...%}。
																																																																																																			  另外你可以在上述位置将 autoescape 设为一个自定义函数，而不仅仅是 None。

																																																																																																			  Cookie 和安全 Cookie
																																																																																																			  你可以使用 set_cookie 方法在用户的浏览中设置 cookie：

																																																																																																			  class MainHandler(tornado.web.RequestHandler):
																																																																																																			      def get(self):
																																																																																																			              if not self.get_cookie("mycookie"):
																																																																																																				                  self.set_cookie("mycookie", "myvalue")
																																																																																																						              self.write("Your cookie was not set yet!")
																																																																																																							              else:
																																																																																																								                  self.write("Your cookie was set!")
																																																																																																										  Cookie 很容易被恶意的客户端伪造。加入你想在 cookie 中保存当前登陆用户的 id 之类的信息，
																																																																																																										  你需要对 cookie 作签名以防止伪造。
																																																																																																										  Tornado 通过 set_secure_cookie 和 get_secure_cookie 方法直接支持了这种功能。 
																																																																																																										  要使用这些方法，你需要在创建应用时提供一个密钥，名字为 cookie_secret。你可以把它作为一个关键词参数传入应用的设置中：
																																																																																																										  application = tornado.web.Application([
																																																																																																										      (r"/", MainHandler),
																																																																																																										      ], cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")
																																																																																																										      签名过的 cookie 中包含了编码过的 cookie 值，另外还有一个时间戳和一个 HMAC 签名。
																																																																																																										      如果 cookie 已经过期或者 签名不匹配，get_secure_cookie 将返回 None，这和没有设置 cookie 时的 返回值是一样的。
																																																																																																										      上面例子的安全 cookie 版本如下：

																																																																																																										      class MainHandler(tornado.web.RequestHandler):
																																																																																																										          def get(self):
																																																																																																											          if not self.get_secure_cookie("mycookie"):
																																																																																																												              self.set_secure_cookie("mycookie", "myvalue")
																																																																																																													                  self.write("Your cookie was not set yet!")
																																																																																																															          else:
																																																																																																																              self.write("Your cookie was set!")




																																																																																																																	      '''

																																																																																																																	      '''
																																																																																																																	      from uuid import uuid4
																																																																																																																	      def uuid():
																																																																																																																	          Generate a new UUID.
																																																																																																																		      return uuid4().hex
																																																																																																																		      '''

																																																																																																																		      '''
																																																																																																																		      安装 uwsgi
																																																																																																																		      sudo apt-get install python-dev
																																																																																																																		      pip install uwsgi
																																																																																																																		      '''

																																																																																																																		      '''
																																																																																																																		      大文件上传到linux环境速度10M/s
																																																																																																																		      yum install lrzsz
																																																																																																																		      敲入rz命令，选中文件夹

																																																																																																																		      '''



																																																																																																																		      '''
																																																																																																																		      django
																																																																																																																		          #获取非json格式数据时候，能够检测是否包含data项
																																																																																																																			      # print request.POST.has_key('data')
																																																																																																																			      '''

																																																																																																																			      '''
																																																																																																																			      在python中，模拟http客户端发送get和post请求，主要用httplib模块的功能。
																																																																																																																			      '''


																																																																																																																			      '''
																																																																																																																			      设置eclipse字体大小
																																																																																																																			      windows--perference--basic--general--appearence--colors and fonts -- text font -- edit
																																																																																																																			      一般设置为12号字体就够用的了

																																																																																																																			      '''

																																																																																																																			      '''
																																																																																																																			       在Windows下常用的有两种方式修改最大连接数。

																																																																																																																			            第一种：命令行修改。

																																																																																																																				        >mysql -uuser -ppassword(命令行登录MySQL)

																																																																																																																					    mysql>show variables like 'max_connections';(查可以看当前的最大连接数)

																																																																																																																					        msyql>set global max_connections=1000;(设置最大连接数为1000，可以再次查看是否设置成功)

																																																																																																																						    mysql>exit(退出)

																																																																																																																						        这种方式有个问题，就是设置的最大连接数只在mysql当前服务进程有效，一旦mysql重启，又会恢复到初始状态。
																																																																																																																							    因为mysql启动后的初始化工作是从其配置文件中读取数据的，而这种方式没有对其配置文件做更改。

																																																																																																																							        第二种：修改配置文件。
																																																																																																																								   这 种方式说来很简单，只要修改MySQL配置文件my.ini 或 my.cnf的参数max_connections，将其改为max_connections=1000，然后重启MySQL即可。但是有一点最难的就是my.ini这个文件在哪找。
																																																																																																																								      通常有两种可能，一个是在安装目录下（这是比较理想的情况），
																																																																																																																								         另一种是在数据文件的目录下，安装的时候如果没有人为改变目录的话，一般就在C:/ProgramData/MySQL往下的目录下。
																																																																																																																									 '''


																																																																																																																									 '''
																																																																																																																									 问题描述：spynner下载后的browser.html 乱码问题，处理方式为lib\site_packages\spynner.egg  解压缩后，spynner文件放到site_packages目录下
																																																																																																																									 接下来按照下面处理

																																																																																																																									 这个是底层的QtWebKit相关库里 用的是Qt的QString  spynner在将QString转为Python的通用字符串时，没有考虑到中文编码这一块的问题。

																																																																																																																									 原创声明：我这两天抓取动态页面，也遇到这个问题，通过调试发现是QString问题后从google找到了QString的正确转换方法。
																																																																																																																									 你把Python27\Lib\site-packages\spynner\browser.py 下的函数 (大概是477行)
																																																																																																																									 def _get_html(self):
																																																																																																																									     return six.u(self.webframe.toHtml())
																																																																																																																									     改成下面这样
																																																																																																																									     def _get_html(self):
																																																																																																																									         return unicode(self.webframe.toHtml().toUtf8(), 'utf-8', 'ignore')
																																																																																																																										 '''

																																																																																																																										 '''
																																																																																																																										 虚拟机与本机ip不在同一个网段，设置虚拟机连接为桥接模式

																																																																																																																										 '''

																																																																																																																										 '''
																																																																																																																										 安装文件内的包
																																																																																																																										 pip install -r requirements.txt
																																																																																																																										 '''

																																																																																																																										 '''
																																																																																																																										 大多数Django教程都是将models放在models.py文件(模块)中, 然而随着models类的增加, 将类放在一个文件中太混乱了, 
																																																																																																																										 于是将models做成一个package:

																																																																																																																										 models/
																																																																																																																										     __init__.py
																																																																																																																										         usermodels.py
																																																																																																																											     othermodel.py

																																																																																																																											     这样就可以将models定义拆分到多个模块中,  但是当用命令同步数据时发现不可用: 
																																																																																																																											     manage.py sqlall blog
																																																																																																																											     不会生成数据库创建命令(APP的名字是blog)

																																																																																																																											     需要做如下更改:

																																																																																																																											     在__init__.py中import模块:
																																																																																																																											     from usermodels import *
																																																																																																																											     from othermodel import *
																																																																																																																											     在定义model的类中加一个内部类Meta:
																																																																																																																											     class User(models.Model):
																																																																																																																											         title = models.CharField(max_length = 100)
																																																																																																																												     class Meta:
																																																																																																																												             app_label = 'blog'
																																																																																																																													     app_lable的值为APP的名称
																																																																																																																													     这样就可以将models定义到多个文件中了

																																																																																																																													     '''


																																																																																																																													     '''
																																																																																																																													     mysql 表添加外键，在表中外键字段已经存在
																																																																																																																													     添加外键 
																																																																																																																													     alter table locstock add foreign key locstock_ibfk2(stockid) references product(stockid) 
																																																																																																																													     locstock 为表名, locstock_ibfk2 为外键名 第一个括号里填写外键列名, product为表名,第二个括号里是写外键关联的列名 
																																																																																																																													     删除外键  
																																																																																																																													     alter table locstock drop foreign key locstock_ibfk2 
																																																																																																																													     查看表有哪些外键 
																																																																																																																													     show create table locstock 
																																																																																																																													     '''
																																																																																																																													     ALTER TABLE product ADD CONSTRAINT FK_ID FOREIGN KEY(company) REFERENCES company(NAME); 
																																																																																																																													     '''
																																																																																																																													     django models 当中 
																																																																																																																													     unicode是和编码有关系的
																																																																																																																													     meta的作用
																																																																																																																													     一般我们用它来归纳一些公共属性字段，然后继承它的子类可以继承这些字段。
																																																																																																																													     就是继承你上面写的class再写些内容
																																																																																																																													     另外还有排序功能


																																																																																																																													     django使用mysql已有表
																																																																																																																													     在命令行下使用  python manage.py inspectdb > models.py 根据数据库生成models文件，然后代码调用
																																																																																																																													     '''



																																																																																																																													     '''文件当前目录'''
																																																																																																																													     import os
																																																																																																																													     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
																																																																																																																													     pirnt BASE_DIR
																																																																																																																													     '''
																																																																																																																													     raise ValueError('Expected a bytes object, not a unicode object')
																																																																																																																													     解决方案
																																																																																																																													     '''
																																																																																																																													     words = search_words.encode('utf8')
																																																																																																																													     urllib.quote(words)

																																																																																																																													     '''
																																																																																																																													     threading
																																																																																																																													     threading模块，里面有一个Thread类。
																																																																																																																													     Thread类里有很多方法，包括run(),start(),getName(),setName()，join()等。
																																																																																																																													     run()可以通过继承重写，是线程运行时执行的内容。
																																																																																																																													     start()方法是启动一个线程，如定义继承Thread类的一个对象t，t.start()就启动这个线程，并自动执行run()方法。getName()是得到此线程的名字，setName是设置这个线程的名字，join()方法比较重要，如果代码中加入join()，是等待t这个线程执行完，才执行下一个线程。

																																																																																																																													     threading.currentThread().getName()
																																																																																																																													     start()
																																																																																																																													     开始线程活动
																																																																																																																													     join()
																																																																																																																													     等待线程终止
																																																																																																																													     tt = threading.Thread(target=AA,args=(参数1,参数2))
																																																																																																																													     threading.activeCount()的使用，此方法返回当前进程中线程的个数。返回的个数中包含主线程。
																																																																																																																													     exp:
																																																																																																																													     '''
																																																																																																																													     import threading
																																																																																																																													     import time
																																																																																																																													      
																																																																																																																													      def worker():
																																																																																																																													          print "test"
																																																																																																																														      time.sleep(1)
																																																																																																																														       
																																																																																																																														       for i in xrange(5):
																																																																																																																														           t = threading.Thread(target=worker)
																																																																																																																															       t.start()
																																																																																																																															        
																																																																																																																																print "current has %d threads" % (threading.activeCount() - 1)
																																																																																																																																'''threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表。
																																																																																																																																代码如下：'''
																																																																																																																																#!/usr/bin/python
																																																																																																																																#test the variable threading.enumerate()
																																																																																																																																import threading
																																																																																																																																import time
																																																																																																																																 
																																																																																																																																 def worker():
																																																																																																																																     print "test"
																																																																																																																																         time.sleep(2)
																																																																																																																																	  
																																																																																																																																	  threads = []
																																																																																																																																	  for i in xrange(5):
																																																																																																																																	      t = threading.Thread(target=worker)
																																																																																																																																	          threads.append(t)
																																																																																																																																		      t.start()
																																																																																																																																		       
																																																																																																																																		       for item in threading.enumerate():
																																																																																																																																		           print item
																																																																																																																																			    
																																																																																																																																			    print
																																																																																																																																			     
																																																																																																																																			     for item in threads:
																																																																																																																																			         print item




																																																																																																																																				 '''
																																																																																																																																				 str 转换为 dict
																																																																																																																																				 '''
																																																																																																																																				 aa = "{'a':'a','b':'b'}" 
																																																																																																																																				 tt = eval(aa)
																																																																																																																																				 for k,v in tt.items():
																																																																																																																																				     print k,'-'*10,v


																																																																																																																																				     '''
																																																																																																																																				     Path配置好后能够让我们在系统中的任何地方运行java应用程序。比如：javac、java命令。
																																																																																																																																				     CLASS_PATH  前面有个  .;  这个是告诉JDK，搜索CLASS时先查找当前目录的CLASS文件 )
																																																																																																																																				      配置java_home的原因是：我们写java程序时需要引用已经开发好的类，所以应该让java解释器知道引用的类的位置啊。
																																																																																																																																				       否则会提示：所引用的类找不到的
																																																																																																																																				       '''

																																																																																																																																				       '''BeautifulSoup解析<th class="hot">或<th class="common">'''
																																																																																																																																				       from BeautifulSoup import BeautifulSoup
																																																																																																																																				       soup = BeautifulSoup(open('a.html'))
																																																																																																																																				       thOrCommonSoup = soup.findAll(name="th", attrs={"class":re.compile("(hot)|(common)")})
																																																																																																																																				       soup.findAll("th",{'class':['hot','common'],})
																																																																																																																																				       '''
																																																																																																																																				       getContent = soup.find('div',id='doc').find('div',id='scontainer').find....
																																																																																																																																				       这样一级级的找，定点打击！特别准确
																																																																																																																																				       使用Beautifulsoup怎么样来获取div 下面的li  里的URL和文本啊
																																																																																																																																				       soup.div.li.a.get_text(), soup.div.li.a['href']
																																																																																																																																				       '''
																																																																																																																																				       '''格式化输出时间'''
																																																																																																																																				       t = str(time.time())
																																																																																																																																				       time.strftime('%Y-%m-%d',time.localtime(float(t)))

																																																																																																																																				       '''
																																																																																																																																				       "单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
																																																																																																																																				       "双下划线" 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据
																																																																																																																																				       Python 用下划线作为变量前缀和后缀指定特殊变量。
																																																																																																																																				       _xxx      不能用'from module import *'导入
																																																																																																																																				       __xxx__ 系统定义名字
																																																																																																																																				       __xxx    类中的私有变量名
																																																																																																																																				       '''

																																																																																																																																				       '''lambda put 含义'''
																																																																																																																																				       def http_put():
																																																																																																																																				           url='http://192.168.1.13:9999/test'
																																																																																																																																					       values={'':''}

																																																																																																																																					           jdata = json.dumps(values)                  # 对数据进行JSON格式化编码
																																																																																																																																						       request = urllib2.Request(url, jdata)
																																																																																																																																						           request.add_header('Content-Type', 'your/conntenttype')
																																																																																																																																							       request.get_method = lambda:'PUT'           # 设置HTTP的访问方式
																																																																																																																																							           request = urllib2.urlopen(request)
																																																																																																																																								       return request.read()



																																																																																																																																								       '''
																																																																																																																																								       restful理解  来自于qq群友 
																																																																																																																																								       restful主要是提供的服务都看成资源
																																																																																																																																								       使用get获取资源, post创建资源, put覆盖原来的资源, delete删除资源, patch就是修改资源属性
																																																																																																																																								       '''

																																																																																																																																								       '''
																																																																																																																																								       str repr 和``的区别
																																																																																																																																								       虫大：str一个是把数值转字符串，repr一个是把对象转字符串
																																																																																																																																								       尽管str(),repr()和``运算在特性和功能方面都非常相似，事实上repr()和``做的是完全一样的事情，
																																																																																																																																								       它们返回的是一个对象的“官方”字符串表示，也就是说绝大多数情况下可以通过求值运算（使用内建函数eval()）重新得到该对象，
																																																																																																																																								       但str()则有所不同。str()致力于生成一个对象的可读性好的字符串表示，它的返回结果通常无法用于eval()求值，但很适合用于print语句输出。需要再次提醒的是，并不是所有repr()返回的字符串都能够用 eval()内建函数得到原来的对象。 
																																																																																																																																								       也就是说 repr() 输出对 Python比较友好，而str()的输出对用户比较友好。虽然如此，很多情况下这三者的输出仍然都是完全一样的。 
																																																																																																																																								       '''


																																																																																																																																								       '''
																																																																																																																																								       c++安装包直接在python有VCForPython,下载后安装
																																																																																																																																								       mysql-python 安装
																																																																																																																																								       下载64位安装文件exe，直接点击下载
																																																																																																																																								       http://www.codegood.com/downloads
																																																																																																																																								       '''

																																																																																																																																								       #mysqldb      
																																																																																																																																								       import time, MySQLdb        
																																																																																																																																								       #连接      
																																																																																																																																								       conn=MySQLdb.connect(host="localhost",user="root",passwd="root",db="test",charset="utf8")    
																																																																																																																																								       cursor = conn.cursor()      
																																																																																																																																								       #删除表  
																																																																																																																																								       sql = "drop table if exists user"  
																																																																																																																																								       cursor.execute(sql)  
																																																																																																																																								       #创建  
																																																																																																																																								       sql = "create table if not exists user(name varchar(128) primary key, created int(10))"  
																																																																																																																																								       cursor.execute(sql)  
																																																																																																																																								       #写入      
																																																																																																																																								       sql = "insert into user(name,created) values(%s,%s)"     
																																																																																																																																								       param = ("aaa",int(time.time()))      
																																																																																																																																								       n = cursor.execute(sql,param)      
																																																																																																																																								       print 'insert',n        
																																																																																																																																								       #写入多行      
																																																																																																																																								       sql = "insert into user(name,created) values(%s,%s)"     
																																																																																																																																								       param = (("bbb",int(time.time())), ("ccc",33), ("ddd",44) )  
																																																																																																																																								       n = cursor.executemany(sql,param)      
																																																																																																																																								       print 'insertmany',n      
																																																																																																																																								       #更新      
																																																																																																																																								       sql = "update user set name=%s where name='aaa'"     
																																																																																																																																								       param = ("zzz")      
																																																																																																																																								       n = cursor.execute(sql,param)      
																																																																																																																																								       print 'update',n        
																																																																																																																																								       #查询      
																																																																																																																																								       n = cursor.execute("select * from user")      
																																																																																																																																								       for row in cursor.fetchall():      
																																																																																																																																								           print row  
																																																																																																																																									       for r in row:      
																																																																																																																																									               print r       
																																																																																																																																										       #删除      
																																																																																																																																										       sql = "delete from user where name=%s"     
																																																																																																																																										       param =("bbb")      
																																																																																																																																										       n = cursor.execute(sql,param)      
																																																																																																																																										       print 'delete',n      
																																																																																																																																										       #查询      
																																																																																																																																										       n = cursor.execute("select * from user")      
																																																																																																																																										       print cursor.fetchall()      
																																																																																																																																										       cursor.close()      
																																																																																																																																										       #提交      
																																																																																																																																										       conn.commit()  
																																																																																																																																										       #关闭      
																																																																																																																																										       conn.close() 

																																																																																																																																										       '''通用headers'''
																																																																																																																																										               ip = ''
																																																																																																																																											               if ip:
																																																																																																																																												                   proxy_handler = urllib2.ProxyHandler({'http':ip})
																																																																																																																																														           else:
																																																																																																																																															               proxy_handler = urllib2.ProxyHandler()
																																																																																																																																																               opener = urllib2.build_opener(proxy_handler)
																																																																																																																																																	               req_headers = [('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
																																																																																																																																																		                             ('Accept-Encoding', 'gzip, deflate'),
																																																																																																																																																					                           ('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
																																																																																																																																																								                         ('Connection','keep-alive'),
																																																																																																																																																											                       ('Referer',url),
																																																																																																																																																													                             ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'),]
																																																																																																																																																																             opener.addheaders = req_headers
																																																																																																																																																																	             urllib2.install_opener(opener)


																																																																																																																																																																		     '''
																																																																																																																																																																		     myqueue = Queue.Queue(maxsize = 10)
																																																																																																																																																																		     Queue.Queue类即是一个队列的同步实现,如果maxsize小于1就表示队列长度无限
																																																																																																																																																																		     myqueue.put(10)
																																																																																																																																																																		     调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。
																																																																																																																																																																		     myqueue.get()
																																																																																																																																																																		     调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。
																																																																																																																																																																		     如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常

																																																																																																																																																																		     Queue.qsize() 返回队列的大小 
																																																																																																																																																																		     Queue.empty() 如果队列为空，返回True,反之False 
																																																																																																																																																																		     Queue.full() 如果队列满了，返回True,反之False
																																																																																																																																																																		     Queue.full 与 maxsize 大小对应 
																																																																																																																																																																		     Queue.get([block[, timeout]])获取队列，timeout等待时间 
																																																																																																																																																																		     Queue.get_nowait() 相当Queue.get(False)
																																																																																																																																																																		     非阻塞 Queue.put(item) 写入队列，timeout等待时间 
																																																																																																																																																																		     Queue.put_nowait(item) 相当Queue.put(item, False)
																																																																																																																																																																		     Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
																																																																																																																																																																		     Queue.join() 实际上意味着等到队列为空，再执行别的操作

																																																																																																																																																																		     针对这三种队列分别有三个构造函数:
																																																																																																																																																																		     1、class Queue.Queue(maxsize) FIFO     先进先出
																																																																																																																																																																		     2、class Queue.LifoQueue(maxsize) LIFO 先进后出
																																																																																																																																																																		     3、class Queue.PriorityQueue(maxsize)  优先级队列 

																																																																																																																																																																		     '''

																																																																																																																																																																		     '''时间格式化输出
																																																																																																																																																																		     time.strftime(…)
																																																																																																																																																																		     strftime(format[, tuple]) -> string
																																																																																																																																																																		     将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
																																																																																																																																																																		     python中时间日期格式化符号：
																																																																																																																																																																		     %y 两位数的年份表示（00-99）
																																																																																																																																																																		     %Y 四位数的年份表示（000-9999）
																																																																																																																																																																		     %m 月份（01-12）
																																																																																																																																																																		     %d 月内中的一天（0-31）
																																																																																																																																																																		     %H 24小时制小时数（0-23）
																																																																																																																																																																		     %I 12小时制小时数（01-12）
																																																																																																																																																																		     %M 分钟数（00=59）
																																																																																																																																																																		     %S 秒（00-59）
																																																																																																																																																																		     %a 本地简化星期名称
																																																																																																																																																																		     %A 本地完整星期名称
																																																																																																																																																																		     %b 本地简化的月份名称
																																																																																																																																																																		     %B 本地完整的月份名称
																																																																																																																																																																		     %c 本地相应的日期表示和时间表示
																																																																																																																																																																		     %j 年内的一天（001-366）
																																																																																																																																																																		     %p 本地A.M.或P.M.的等价符
																																																																																																																																																																		     %U 一年中的星期数（00-53）星期天为星期的开始
																																																																																																																																																																		     %w 星期（0-6），星期天为星期的开始
																																																																																																																																																																		     %W 一年中的星期数（00-53）星期一为星期的开始
																																																																																																																																																																		     %x 本地相应的日期表示
																																																																																																																																																																		     %X 本地相应的时间表示
																																																																																																																																																																		     %Z 当前时区的名称
																																																																																																																																																																		     %% %号本身
																																																																																																																																																																		     例： time.strftime(’%Y%m%d%H%M%S’)
																																																																																																																																																																		     20090805092348
																																																																																																																																																																		     '''


																																																																																																																																																																		     '''
																																																																																																																																																																		     以下的文章就是对python 读写配置文件的具体方案的介绍
																																																																																																																																																																		     1，函数介绍
																																																																																																																																																																		     1.1.读取配置文件
																																																																																																																																																																		     -read(filename) 直接读取ini文件内容
																																																																																																																																																																		     -sections() 得到所有的section，并以列表的形式返回
																																																																																																																																																																		     -options(section) 得到该section的所有option
																																																																																																																																																																		     -items(section) 得到该section的所有键值对
																																																																																																																																																																		     -get(section,option) 得到section中option的值，返回为string类型
																																																																																																																																																																		     -getint(section,option) 得到section中option的值，返回为int类型
																																																																																																																																																																		      
																																																																																																																																																																		      1.2.写入配置文件
																																																																																																																																																																		      -add_section(section) 添加一个新的section
																																																																																																																																																																		      -set( section, option, value) 对section中的option进行设置
																																																																																																																																																																		        需要调用write将内容写入配置文件。
																																																																																																																																																																			2，测试实例
																																																																																																																																																																			2.1，测试1
																																																																																																																																																																			配置文件test.cfg
																																																																																																																																																																			[plain] view plain copy
																																																																																																																																																																			[sec_a]  
																																																																																																																																																																			a_key1 = 20  
																																																																																																																																																																			a_key2 = 10  
																																																																																																																																																																			  
																																																																																																																																																																			  [sec_b]  
																																																																																																																																																																			  b_key1 = 121  
																																																																																																																																																																			  b_key2 = b_value2  
																																																																																																																																																																			  b_key3 = $r  
																																																																																																																																																																			  b_key4 = 127.0.0.1  
																																																																																																																																																																			  测试文件test.py
																																																																																																																																																																			  [python] view plain copy
																																																																																																																																																																			  # -* - coding: UTF-8 -* -  
																																																																																																																																																																			  import ConfigParser  
																																																																																																																																																																			  #生成config对象  
																																																																																																																																																																			  conf = ConfigParser.ConfigParser()  
																																																																																																																																																																			  #用config对象读取配置文件  
																																																																																																																																																																			  conf.read("test.cfg")  
																																																																																																																																																																			  #以列表形式返回所有的section  
																																																																																																																																																																			  sections = conf.sections()  
																																																																																																																																																																			  print 'sections:', sections         #sections: ['sec_b', 'sec_a']  
																																																																																																																																																																			  #得到指定section的所有option  
																																																																																																																																																																			  options = conf.options("sec_a")  
																																																																																																																																																																			  print 'options:', options           #options: ['a_key1', 'a_key2']  
																																																																																																																																																																			  #得到指定section的所有键值对  
																																																																																																																																																																			  kvs = conf.items("sec_a")  
																																																																																																																																																																			  print 'sec_a:', kvs                 #sec_a: [('a_key1', '20'), ('a_key2', '10')]  
																																																																																																																																																																			  #指定section，option读取值  
																																																																																																																																																																			  str_val = conf.get("sec_a", "a_key1")  
																																																																																																																																																																			  int_val = conf.getint("sec_a", "a_key2")  
																																																																																																																																																																			    
																																																																																																																																																																			    print "value for sec_a's a_key1:", str_val   #value for sec_a's a_key1: 20  
																																																																																																																																																																			    print "value for sec_a's a_key2:", int_val   #value for sec_a's a_key2: 10  
																																																																																																																																																																			      
																																																																																																																																																																			      #写配置文件  
																																																																																																																																																																			      #更新指定section，option的值  
																																																																																																																																																																			      conf.set("sec_b", "b_key3", "new-$r")  
																																																																																																																																																																			      #写入指定section增加新option和值  
																																																																																																																																																																			      conf.set("sec_b", "b_newkey", "new-value")  
																																																																																																																																																																			      #增加新的section  
																																																																																																																																																																			      conf.add_section('a_new_section')  
																																																																																																																																																																			      conf.set('a_new_section', 'new_key', 'new_value')  
																																																																																																																																																																			      #写回配置文件  
																																																																																																																																																																			      conf.write(open("test.cfg", "w"))  

																																																																																																																																																																			      2.2，测试2
																																																																																																																																																																			      配置文件test.cfg
																																																																																																																																																																			      [plain] view plain copy
																																																																																																																																																																			      [info]  
																																																																																																																																																																			      age = 21  
																																																																																																																																																																			      name = chen  
																																																																																																																																																																			      sex = male  
																																																																																																																																																																			      测试文件test.py
																																																																																																																																																																			      [python] view plain copy
																																																																																																																																																																			      from __future__ import with_statement  
																																																																																																																																																																			      import ConfigParser  
																																																																																																																																																																			      config=ConfigParser.ConfigParser()  
																																																																																																																																																																			      with open("test.cfg","rw") as cfgfile:  
																																																																																																																																																																			          config.readfp(cfgfile)  
																																																																																																																																																																				      name=config.get("info","name")  
																																																																																																																																																																				          age=config.get("info","age")  
																																																																																																																																																																					      print name  
																																																																																																																																																																					          print age  
																																																																																																																																																																						      config.set("info","sex","male")  
																																																																																																																																																																						          config.set("info","age","55")  
																																																																																																																																																																							      age=config.getint("info","age")  
																																																																																																																																																																							          print name  
																																																																																																																																																																								      print type(age)  
																																																																																																																																																																								          print age  
																																																																																																																																																																									  分析
																																																																																																																																																																									  其中[ ] 中的info是这段配置的名字。
																																																																																																																																																																									  其中age,name都是属性。
																																																																																																																																																																									  首先，config=ConfigParser.ConfigParser() 得到一个配置config对象.下面打开一个配置文件 cfgfile. 用readfp()读取这个文件.这样配置的内容就读到config对象里面了。
																																																																																																																																																																									  接下来一个问题是如何读取值.常用的方法是get() 和getint() . get()返回文本. getint()返回整数。
																																																																																																																																																																									  其次，name=config.get(''info'',''name'')  意思就是.读取config中info段中的name变量值。
																																																																																																																																																																									  最后讲讲如何设置值.使用set(段名,变量名,值) 来设置变量.config.set(''info'',''age'',''21'') 表示把info段中age变量设置为21。

																																																																																																																																																																									  2.3，测试3
																																																																																																																																																																									  Python的ConfigParser Module中定义了3个类对INI文件进行操作。
																																																																																																																																																																									  分别是RawConfigParser、ConfigParser、SafeConfigParser。
																																																																																																																																																																									  RawCnfigParser是最基础的INI文件读取类，ConfigParser、SafeConfigParser支持对%(value)s变量的解析。 
																																																																																																																																																																									  配置文件test.cfg
																																																																																																																																																																									  [plain] view plain copy
																																																																																																																																																																									  [portal]  
																																																																																																																																																																									  url = http://%(host)s:%(port)s/Portal  
																																																																																																																																																																									  host = localhost  
																																																																																																																																																																									  port = 8080  
																																																																																																																																																																									  使用RawConfigParser：
																																																																																																																																																																									  [python] view plain copy
																																																																																																																																																																									  import ConfigParser  
																																																																																																																																																																									    
																																																																																																																																																																									    conf = ConfigParser.RawConfigParser()  
																																																																																																																																																																									    print "use RawConfigParser() read"  
																																																																																																																																																																									    conf.read("test.cfg")  
																																																																																																																																																																									    print conf.get("portal", "url")  
																																																																																																																																																																									      
																																																																																																																																																																									      print "use RawConfigParser() write"  
																																																																																																																																																																									      conf.set("portal", "url2", "%(host)s:%(port)s")  
																																																																																																																																																																									      print conf.get("portal", "url2")  
																																																																																																																																																																									      得到输出
																																																																																																																																																																									      [plain] view plain copy
																																																																																																																																																																									      use RawConfigParser() read  
																																																																																																																																																																									      http://%(host)s:%(port)s/Portal  
																																																																																																																																																																									      use RawConfigParser() write  
																																																																																																																																																																									      %(host)s:%(port)s  

																																																																																																																																																																									      改用ConfigParser
																																																																																																																																																																									      [python] view plain copy
																																																																																																																																																																									      import ConfigParser  
																																																																																																																																																																									        
																																																																																																																																																																										conf = ConfigParser.ConfigParser()  
																																																																																																																																																																										print "use RawConfigParser() read"  
																																																																																																																																																																										conf.read("test.cfg")  
																																																																																																																																																																										print conf.get("portal", "url")  
																																																																																																																																																																										  
																																																																																																																																																																										  print "use RawConfigParser() write"  
																																																																																																																																																																										  conf.set("portal", "url2", "%(host)s:%(port)s")  
																																																																																																																																																																										  print conf.get("portal", "url2")  
																																																																																																																																																																										  得到输出
																																																																																																																																																																										  [plain] view plain copy
																																																																																																																																																																										  use RawConfigParser() read  
																																																																																																																																																																										  http://localhost:8080/Portal  
																																																																																																																																																																										  use RawConfigParser() write  
																																																																																																																																																																										  localhost:8080  

																																																																																																																																																																										  改用SafeConfigParser，效果与ConfigParser相同
																																																																																																																																																																										  [python] view plain copy
																																																																																																																																																																										  import ConfigParser  
																																																																																																																																																																										    
																																																																																																																																																																										    conf = ConfigParser.SafeConfigParser()  
																																																																																																																																																																										    print "use RawConfigParser() read"  
																																																																																																																																																																										    conf.read("test.cfg")  
																																																																																																																																																																										    print conf.get("portal", "url")  
																																																																																																																																																																										      
																																																																																																																																																																										      print "use RawConfigParser() write"  
																																																																																																																																																																										      conf.set("portal", "url2", "%(host)s:%(port)s")  
																																																																																																																																																																										      print conf.get("portal", "url2")  

																																																																																																																																																																										      结论：
																																																																																																																																																																										      还是用ConfigParser


																																																																																																																																																																										      '''


																																																																																																																																																																										      '''
																																																																																																																																																																										      字段唯一值设置
																																																																																																																																																																										      #http://blog.163.com/leiliuxing2010@126/blog/static/298693542011125235887/

																																																																																																																																																																										      CREATE TABLE myset (id INT(11),col SET('a','b','c','d'))

																																																																																																																																																																										      SELECT * FROM myset

																																																																																																																																																																										      INSERT INTO myset (col) VALUES  ('a,d'), ('d,a'), ('a,d,a'), ('a,d,d'), ('d,a,d')

																																																																																																																																																																										      SELECT * FROM myset;
																																																																																																																																																																										      a,b,c
																																																																																																																																																																										      a,b,c,d
																																																																																																																																																																										      UPDATE myset SET col=CONCAT(col,',a,d') WHERE id=1;


																																																																																																																																																																										      '''




																																																																																																																																																																										      '''cookie'''
																																																																																																																																																																										      '''test1
																																																																																																																																																																										      注意这个例子经过测试，发现只有人人网和开心网之类的网站可以，
																																																																																																																																																																										      而像支付宝，百度网盘，甚至是我们学校的教务系统都不能成功登录
																																																																																																																																																																										      可能是这些网站在编写时不接受客户端请求该方法，具体原因我也不知道为什么。
																																																																																																																																																																										      而且这个程序不能自动通过有验证码验证的网站，所以纯粹学习它的原理吧
																																																																																																																																																																										      '''
																																																																																																																																																																										      #! /usr/bin/env python
																																																																																																																																																																										      #coding=utf-8

																																																																																																																																																																										      import urllib2
																																																																																																																																																																										      import urllib
																																																																																																																																																																										      import cookielib

																																																																																																																																																																										      def login():
																																																																																																																																																																										          email = raw_input("请输入用户名:")
																																																																																																																																																																											      pwd = raw_input("请输入密码:")
																																																																																																																																																																											          data={"email":email,"password":pwd}  #登陆用户名和密码
																																																																																																																																																																												      post_data=urllib.urlencode(data)   #将post消息化成可以让服务器编码的方式
																																																																																																																																																																												          cj=cookielib.CookieJar()   #获取cookiejar实例
																																																																																																																																																																													      opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
																																																																																																																																																																													          #自己设置User-Agent（可用于伪造获取，防止某些网站防ip注入）
																																																																																																																																																																														      headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
																																																																																																																																																																														          website = raw_input('请输入网址:')
																																																																																																																																																																															      req=urllib2.Request(website,post_data,headers)
																																																																																																																																																																															          content=opener.open(req)
																																																																																																																																																																																      print content.read()    #linux下没有gbk编码，只有utf-8编码

																																																																																																																																																																																      if __name__ == '__main__':
																																																																																																																																																																																          login()


																																																																																																																																																																																	  '''test2'''

																																																																																																																																																																																	  #获取Cookiejar对象（存在本机的cookie消息）
																																																																																																																																																																																	  cookie = cookielib.CookieJar()
																																																																																																																																																																																	  #自定义opener,并将opener跟CookieJar对象绑定
																																																																																																																																																																																	  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
																																																																																																																																																																																	  #安装opener,此后调用urlopen()时都会使用安装过的opener对象
																																																																																																																																																																																	  urllib2.install_opener(opener)

																																																																																																																																																																																	  url = "http://www.baidu.com"   
																																																																																																																																																																																	  urllib2.urlopen(url)

																																																																																																																																																																																	  '''
																																																																																																																																																																																	  python装饰器（decorator）在实现的时候，有一些细节需要被注意。
																																																																																																																																																																																	  例如，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）。
																																																																																																																																																																																	  这样有时候会对程序造成一些不便，例如笔者想对unittest框架中的一些函数添加自定义的decorator，
																																																																																																																																																																																	  添加后由于函数名和函数的doc发生了改变，对测试结果有一些影响。
																																																																																																																																																																																	  所以，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。
																																																																																																																																																																																	  写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring。例如：
																																																																																																																																																																																	  test_decorator.py
																																																																																																																																																																																	  # -*- coding=utf-8 -*- 

																																																																																																																																																																																	   
																																																																																																																																																																																	   打印出：example Docstring
																																																																																																																																																																																	   '''
																																																																																																																																																																																	   from functools import wraps   
																																																																																																																																																																																	   def my_decorator(func):
																																																																																																																																																																																	       @wraps(func)
																																																																																																																																																																																	           def wrapper(*args, **kwargs):
																																																																																																																																																																																		           print('Calling decorated function...')
																																																																																																																																																																																			           return func(*args, **kwargs)
																																																																																																																																																																																				       return wrapper  
																																																																																																																																																																																				       @my_decorator 
																																																																																																																																																																																				       def example():
																																																																																																																																																																																				           """Docstring""" 
																																																																																																																																																																																					       print('Called example function')
																																																																																																																																																																																					       print(example.__name__, example.__doc__)




																																																																																																																																																																																					       '''
																																																																																																																																																																																					       这几天在折腾Python使用QtWebKit的实验，算是刚刚摸清了一些门道.
																																																																																																																																																																																					       以下是python使用QtWebKit代码记录
																																																																																																																																																																																					       '''
																																																																																																																																																																																					       import sys
																																																																																																																																																																																					       import time
																																																																																																																																																																																					       from PyQt4 import QtGui, QtCore, QtWebKit
																																																																																																																																																																																					        
																																																																																																																																																																																						class Sp():
																																																																																																																																																																																						    def save(self):
																																																																																																																																																																																						            print "call"
																																																																																																																																																																																							            data = self.webView.page().currentFrame().documentElement().toInnerXml()
																																																																																																																																																																																								            open("htm.txt","w").write(data)
																																																																																																																																																																																									            print 'finished'
																																																																																																																																																																																										            time.sleep(5)
																																																																																																																																																																																											            print 'finisheed......2'
																																																																																																																																																																																												            #sys.exit()
																																																																																																																																																																																													            
																																																																																																																																																																																														        def txtfile(self):
																																																																																																																																																																																															        print "starting..."   
																																																																																																																																																																																																 
																																																																																																																																																																																																     def main(self):
																																																																																																																																																																																																             self.webView = QtWebKit.QWebView()

																																																																																																																																																																																																	             self.webView.load(QtCore.QUrl("http://www.neiyiwangzhan.com"))
																																																																																																																																																																																																		             self.webView.show()
																																																																																																																																																																																																			             QtCore.QObject.connect(self.webView,QtCore.SIGNAL("loadFinished(bool)"),self.save)
																																																																																																																																																																																																				      
																																																																																																																																																																																																				      app = QtGui.QApplication(sys.argv)
																																																																																																																																																																																																				      s = Sp()
																																																																																																																																																																																																				      s.main()
																																																																																																																																																																																																				      sys.exit(app.exec_())




																																																																																																																																																																																																				      '''
																																																																																																																																																																																																				      在django的view当中使用线程
																																																																																																																																																																																																				      '''
																																																																																																																																																																																																				      @login_required 
																																																																																																																																																																																																				      def search_area(request):
																																																																																																																																																																																																				              prints = PrintThread()
																																																																																																																																																																																																					              prints.start()      
																																																																																																																																																																																																						              return retrieve(request, 'Area', 'areasearche.html', [{'name':'areaname', 'mode': 'contains'}]) 
																																																																																																																																																																																																							      ##通过thread 实现django中    
																																																																																																																																																																																																							      import threading    
																																																																																																																																																																																																							      import time 
																																																																																																																																																																																																							      class PrintThread(threading.Thread):
																																																																																																																																																																																																							              def run(self):
																																																																																																																																																																																																								                          print "start.... %s"%(self.getName(),)          
																																																																																																																																																																																																											                      for i in range(30):
																																																																																																																																																																																																													                                          time.sleep(1)               
																																																																																																																																																																																																																		                                      print i         
																																																																																																																																																																																																																						                          print "end.... %s"%(self.getName(),)

																																																																																																																																																																																																																									  '''
																																																																																																																																																																																																																									  关闭csrf保护功能。为视图函数添加@csrf_exempt修饰符

																																																																																																																																																																																																																									  '''

																																																																																																																																																																																																																									  '''
																																																																																																																																																																																																																									  python字符串转json对象，需要使用json模块的loads函数，如下所示：
																																																																																																																																																																																																																									  >>> import json
																																																																																																																																																																																																																									  >>> s = '{"skey":"val","ikey":10}'
																																																																																																																																																																																																																									  >>> jo = json.loads(s)
																																																																																																																																																																																																																									  >>> jo
																																																																																																																																																																																																																									  {'ikey': 10, 'skey': 'val'}
																																																																																																																																																																																																																									  >>> jo['ikey']
																																																																																																																																																																																																																									  10
																																																																																																																																																																																																																									  >>> jo['skey']
																																																																																																																																																																																																																									  'val'

																																																																																																																																																																																																																									  json.loads介绍：
																																																																																																																																																																																																																									  json.loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
																																																																																																																																																																																																																									  Deserialize s (a str instance containing a JSON document) to a Python object using this conversion table.
																																																																																																																																																																																																																									  The other arguments have the same meaning as in load(), except encoding which is ignored and deprecated.
																																																																																																																																																																																																																									  If the data being deserialized is not a valid JSON document, a JSONDecodeError will be raised
																																																																																																																																																																																																																									  '''

																																																																																																																																																																																																																									  '''
																																																																																																																																																																																																																									  json中文乱码
																																																																																																																																																																																																																									  中文以 unicode 编码了，而默认是以ASCII解析的，中文不在ASCII编码中，所以无法显示。
																																																																																																																																																																																																																									  import json  
																																																																																																																																																																																																																									  myjson=json.loads(data) #data是向 api请求的响应数据，data必须是字符串类型的  
																																																																																																																																																																																																																									  #ensure_ascii=False 就不会用 ASCII 编码，中文就可以正常显示了  
																																																																																																																																																																																																																									  newjson=json.dumps(myjson,ensure_ascii=False)   
																																																																																																																																																																																																																									     
																																																																																																																																																																																																																									     print newjson  
																																																																																																																																																																																																																									     '''
