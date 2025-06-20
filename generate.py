from datetime import datetime
from pytz import timezone

# 读取模板
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# 获取北京时间
now = datetime.now(timezone('Asia/Shanghai'))
time_str = now.strftime("%H:%M")
date_str = now.strftime("%Y年%m月%d日")
weekday_map = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
weekday_str = weekday_map[now.weekday()]

# 替换模板内容
output = template.replace("{{TIME}}", time_str)
output = output.replace("{{DATE}}", date_str)
output = output.replace("{{WEEKDAY}}", weekday_str)

# 写入 index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)
