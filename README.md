# SuperCare Api Test

> This is a test for SuperCare Api

## Installation requirements

```pip install -r requirements.txt```

## Tips
1. [dynaconf](https://www.dynaconf.com) is used to manage the environment variables

当前Supercare业务测试不适用数据驱动的方式去验证接口，因此前期主要关注的是业务逻辑这块，编写用例时无需对入参这块做过多测试验证

### **测试用例接口定义规范：**

### **目录结构：**
```
|-- apis
    |-- page_modules1
    |-- page_modules2
    ...
|-- case_excel
|-- common
|-- conf
|-- files
|-- libs
|-- logs
|-- testcase
    |-- page1_cases
    page1_case_steps.py
    |-- page2_cases
    page2_case_steps.py
    ...
conftest.py
```
- apis目录：根据页面模块划分apis
- case_excel：测试用例（此处暂时未关联，若后续考虑加入入参的验证，可作为数据驱动入口）
- common：公共方法（业务方法不要放在这里面）
- conf：配置文件（定义各个测试环境配置信息）
- files：测试用例中用到的其他文件（如图片，）
- libs：后续将三方包加入此文件夹做打包
- logs：日志
- report：测试报告
- testcase：实际运行的用例脚本（以页面模块划分，每个页面中定义一个step汇总，添加一些复用较高的一些测试步骤）

主要的思路如下：
* 整体分层设计为：apis（待测接口）->steps（测试步骤）->cases（最终测试用例），其中steps由各个api组成，最终在cases中验证所有步骤的执行

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
* 1.区分单个步骤的用例测试，主要是针对简单场景测试，场景用例测试，对复杂场景测试，单个接口标签：single，场景用例：scenario
* 2.setup以及teardown在传入或调用test中的结果时，使用os环境变量获取，若是类，则直接self传递，已定义俩个fixture：set_global_data，get_global_data，均是存os环境变量中

###### 注：从apis->steps->cases流程中，所有的cases均是验证steps，而非直接验证apis，因此在步骤中的参数要尽可能可配置，参数实体尽量放入cases中