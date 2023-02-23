# SuperCare Api Test

> This is a test for SuperCare Api

## Installation requirements

```pip install -r requirements.txt```

## Tips
1. [dynaconf](https://www.dynaconf.com) is used to manage the environment variables
2. 业务决定当前测试不适用数据驱动的方式去验证接口，前期主要关注的是业务逻辑这块，编写用例时无需对入参这块做过多测试

### **测试用例接口定义规范：**

### **目录结构：**
* apis目录：根据页面模块划分apis
* case_excel：测试用例（此处暂时未关联，若后续考虑加入入参的验证，可作为数据驱动入口）
* common：公共方法（业务方法不要放在这里面）
* conf：配置文件（定义各个测试环境配置信息）
* files：测试用例中用到的其他文件（如图片，）
* libs：后续将三方包加入此文件夹做打包
* logs：日志
* report：测试报告
* testcase：实际运行的用例脚本（以页面模块划分，每个页面中定义一个step汇总，添加一些复用较高的一些测试步骤）

主要的思路如下：
* 1.根据模块划分api（易维护）
* 2.所有用例定义接口继承apis.base.Base类，并根据下述模板定义待测接口（统一性）
* 3.单独定义步骤文件集合，分层为：apis（待测接口）->steps（测试步骤）->cases（最终测试用例）

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
* 2.setup以及teardown在传入或调用test中的结果时，使用os环境变量获取