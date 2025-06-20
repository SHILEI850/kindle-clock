# generate.py  — 每分钟生成 index.html + viewer.html
from datetime import datetime, timedelta
from pytz import timezone

# ── 1. 读取模板 ────────────────────────────────
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# ── 2. 取北京时间并“向上取整”到下一个整分钟 ─
now = datetime.now(timezone("Asia/Shanghai"))
now += timedelta(minutes=1)                # 提前 1 分钟
now = now.replace(second=0, microsecond=0) # 把秒数清零

time_str   = now.strftime("%H:%M")
date_str   = now.strftime("%Y年%m月%d日")
weekday_cn = ["星期一","星期二","星期三","星期四",
              "星期五","星期六","星期日"][now.weekday()]

# ── 3. 生成新的 index.html ─────────────────────
page = (template
        .replace("{{TIME}}", time_str)
        .replace("{{DATE}}", date_str)
        .replace("{{WEEKDAY}}", weekday_cn))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(page)

# ── 4. 生成 viewer.html（0 秒跳转，30 秒后由 meta 刷新） ─
ts = int(now.timestamp())
viewer_html = (
    '<!DOCTYPE html><meta charset="utf-8">'
    f'<meta http-equiv="refresh" content="0;URL=index.html?ts={ts}">'
    '<style>body{font-family:Arial;text-align:center;'
    'padding-top:40vh;}</style>正在加载北京时间页面…'
)

with open("viewer.html", "w", encoding="utf-8") as f:
    f.write(viewer_html)
