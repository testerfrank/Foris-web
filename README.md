#整体结构目录说明

**base：基类封装包** 
* basepage：page类的基类，主要是对selenium常用方法做二次封装

**common：通用方法的封装**
* readconfig：读取config.ini配置文件
* readelement：读取yaml文件中的页面元素

**config：目录管理**
* conf：目录管理
* config.ini：存放环境链接等配置数据

**data：存放测试数据**

**driver：存放浏览器驱动**

**logs：存放日志文件**

**page：page类封装包**

**page_element：以yaml文件的形式存放页面元素**

**report：存放测试报告**

**screen_record：存放视频文件**

**screen_shot：存放截图文件**

**test_case：测试用例封装包**

**utils：第三方工具类的封装包**
* utils_config：ini配置文件相关方法封装
* utils_logger：logging日志的封装
* utils_time：time与datetime相关方法的封装

**conftest.py：包含初始化的fixture，以及hook函数的重写**

**pytest.ini：pytest的配置文件**

**run_case.py：测试用例运行主入口**
