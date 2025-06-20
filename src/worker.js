export default {
  async fetch() {
    const now = new Date(Date.now() + 8*60*60*1000); // 北京时间
    const hh  = String(now.getHours()).padStart(2,'0');
    const mm  = String(now.getMinutes()).padStart(2,'0');
    const wk  = ['日','一','二','三','四','五','六'][now.getDay()];
    const date = now.toLocaleDateString('zh-CN');

    const html = `<!DOCTYPE html><meta charset=utf-8>
    <meta http-equiv="refresh" content="60">
    <style>body{font-family:Arial;text-align:center;margin-top:30vh}
           .time{font-size:3.2em;font-weight:bold}
           .date{font-size:1.6em}</style>
    <img src="https://shilei850.github.io/kindle-clock/dog.png" width="60"><br>
    <h1 style="font-size:2em">おはよう 宝贝</h1>
    <div class="time">${hh}:${mm}</div>
    <div class="date">${date}（星期${wk}）</div>`;

    return new Response(html, {
      headers: { 'content-type': 'text/html;charset=utf-8' }
    });
  }
};
