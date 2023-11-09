# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import datetime
import pyperclip
def countdays(year,month,date):
    expectdate=datetime.datetime(year,month,date)
    today=datetime.datetime.today()
    print("预期时间：%s，当前时间：%s"%(expectdate,today))
    remaindays=(expectdate-today).days
    print("剩余时间"+str(remaindays)+"天")
    return remaindays
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    t1=countdays(2023, 12, 3)
    t2=countdays(2024,2,9)
    pyperclip.copy("距离N2考试还有：%d天\n距离过年还有：%d天"%(t1,t2))
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
