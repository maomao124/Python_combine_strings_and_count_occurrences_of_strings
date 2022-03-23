"""
 * Project name(项目名称)：Python合并字符串和统计字符串出现的次数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 19:45
 * Version(版本): 1.0
 * Description(描述)： join()方法用来将列表（或元组）中包含的多个字符串连接成一个字符串。

 join() 方法
new str = str.join(iterable)

此方法中各参数的含义如下：
new str：表示合并后生成的新字符串；
str：用于指定合并时的分隔符；
iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供。
 """

if __name__ == '__main__':
    list1 = ["12", "13", "19", "56", "78"]
    str1 = ".".join(list1)
    print(str1)
    str1 = "---".join(list1)
    print(str1)

    input()
