"""
 * Project name(项目名称)：Python合并字符串和统计字符串出现的次数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 19:51
 * Version(版本): 1.0
 * Description(描述)： 统计字符串出现的次数
 count 方法用于检索指定字符串在另一字符串中出现的次数，如果检索的字符串不存在，则返回 0，否则返回出现的次数。

 str.count(sub[,start[,end]])
str：表示原字符串；
sub：表示要检索的字符串；
start：指定检索的起始位置，也就是从什么位置开始检测。如果不指定，默认从头开始检索；
end：指定检索的终止位置，如果不指定，则表示一直检索到结尾。
 """

if __name__ == '__main__':
    str1 = "出现 count 方法用于检索指定字符串在另一字符串中出现的次数 出现"
    print(str1.count("出现"))
    print(str1.count("出现", 6))
    print(str1.count("出现", 0, 10))

    input()
