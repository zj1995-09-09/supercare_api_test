# SuperCare Api Test

> This is a test for SuperCare Api

## Installation requirements

```pip install -r requirements.txt```

## Tips
1. [dynaconf](https://www.dynaconf.com) is used to manage the environment variables
2. 业务决定当前测试不适用数据驱动的方式去验证接口，主要关注的是业务逻辑这块，编写用例时无需对入参这块做过多测试

### **测试用例接口定义规范：**

* 根据模块划分子类
* 所有用例定义接口继承apis.base.Base类
* 入参均设置为data=None, params=None, headers=None
* 单独定义步骤文件集合，作为最小操作单位，整体划分：apis->steps->cases

### **接口定义模板：**

	def api_xxx(self, data=None, params=None, headers=None):

		self.headers_default = {
			"Authorization": os.getenv("cookies")	# 必传
		}
		self.data_default = {}	# 可定义默认值
		self.params_default = {}	# 可定义默认值

		method = "xxx"	# 根据实际接口定义
		url = self.url + "/xxx/xxx"	# 根据实际接口定义

		res = self.apis(data=data, params=params, headers=headers, method=method, url=url)

		return res	# 返回原始响应

### **用例编写：**
* 1.区分api单个接口用例测试，场景用例测试，单个接口标签：single，场景用例：scenario
* 2.存在setup时调用用例，不允许单独编写公共方法
* 3.setup中返回的参数使用os.environ进行传参

_single的用例仅仅是为了验证接口的可用性，不作为主要验证点，因此在编写single的用例时要尽可能的为scenario用例提供便捷，若存在多类场景参数不同，建议单个接口文件中，用例与接口分开
所有单个接口的用例命名：test_api_xxx_


### **目录结构：**
* apis目录：根据页面模块划分apis
* case_excel：excel用例
* common：公共业务方法
* conf：配置文件
* files：测试用例中用到的其他文件（如图片，）
* libs：后续将三方包加入此文件夹做打包
* logs：日志
* report：测试报告
* testcase：实际运行的用例脚本

###### _对接口做1次封装，添加默认参数、公共参数等，其中验证分为单个接口的校验，以及各类接口组合场景进行校验；_
