# Hacker Scripts
黑客脚本 --- 超过90s的任务，不自动化，你好意思说你是黑客？[(资源：伯乐在线)]()

[![Join the chat at https://gitter.im/ehnydeel/hacker-scripts](https://badges.gitter.im/ehnydeel/hacker-scripts.svg)](https://gitter.im/ehnydeel/hacker-scripts?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Based on a _[true
story](https://www.jitbit.com/alexblog/249-now-thats-what-i-call-a-hacker/)_:

这是一个真实的故事：Alex有一位前同事，就是生活在终端里面的大牛。如果某些事情，花费他的时间超过90秒，他就会写一个脚本，实现自动处理那些事情。

> xxx: OK, so, our build engineer has left for another company. The dude was literally living inside the terminal. You know, that type of a guy who loves Vim, creates diagrams in Dot and writes wiki-posts in Markdown... If something - anything - requires more than 90 seconds of his time, he writes a script to automate that.

> 某某某：好吧，我们的构建工程师已经离开了，去了另外一家公司。那哥们是真的生活在终端里面。你知道的，那种类型的家伙，喜欢Vim,在Dot里面创建图形，在Markdown里面写wiki帖子......如果有事情，或者说任意事情，需要超过他90秒的时间，他就会写一个脚本，自动去处理。

> xxx: So we're sitting here, looking through his, uhm, "legacy"

> 某某某：嗯，因此我们坐在这里，浏览他的“遗产”

> xxx: You're gonna love this

> 某某某：你会喜欢这个的

> xxx: [`smack-my-bitch-up.sh`](https://github.com/NARKOZ/hacker-scripts/blob/master/smack-my-bitch-up.sh) - sends a text message "late at work" to his wife (apparently). Automatically picks reasons from an array of strings, randomly. Runs inside a cron-job. The job fires if there are active SSH-sessions on the server after 9pm with his login.

> 某某某：[`smack-my-bitch-up.sh`](https://github.com/NARKOZ/hacker-scripts/blob/master/smack-my-bitch-up.sh) 似乎是，发送一条信息“在加班”给他老婆。自动地从一个字符串数组中随机地选择原因。运行在一个计划任务中。如果晚上9点以后，在服务器上，他的登录状态是激活的SSH会话，这个任务就会触发。

> xxx: [`kumar-asshole.sh`](https://github.com/NARKOZ/hacker-scripts/blob/master/kumar-asshole.sh) - scans the inbox for emails from "Kumar" (a DBA at our clients). Looks for keywords like "help", "trouble", "sorry" etc. If keywords are found - the script SSHes into the clients server and rolls back the staging database to the latest backup. Then sends a reply "no worries mate, be careful next time".

> xxx: [`hangover.sh`](https://github.com/NARKOZ/hacker-scripts/blob/master/hangover.sh) - another cron-job that is set to specific dates. Sends automated emails like "not feeling well/gonna work from home" etc. Adds a random "reason" from another predefined array of strings. Fires if there are no interactive sessions on the server at 8:45am.

> xxx: (and the oscar goes to) [`fucking-coffee.sh`](https://github.com/NARKOZ/hacker-scripts/blob/master/fucking-coffee.sh) - this one waits exactly 17 seconds (!), then opens a telnet session to our coffee-machine (we had no frikin idea the coffee machine is on the network, runs linux and has a TCP socket up and running) and sends something like `sys brew`. Turns out this thing starts brewing a mid-sized half-caf latte and waits another 24 (!) seconds before pouring it into a cup. The timing is exactly how long it takes to walk to the machine from the dudes desk.

> xxx: holy sh*t I'm keeping those

> 某某某：太神奇了，SHIT，我要保留这些东西

Original: http://bash.im/quote/436725 (in Russian)  
Pull requests with other implementations (Python, Perl, Shell, etc) are welcome.

来源： http://bash.im/quote/436725 (俄语)  
欢迎提供其他语言的实现(Python, Perl, Shell, ...)

## Usage 
用法

You need these environment variables:

你需要这些环境变量：

```sh
# used in `smack-my-bitch-up` and `hangover` scripts
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

# used in `kumar_asshole` script
GMAIL_USERNAME=admin@example.org
GMAIL_PASSWORD=password
```

For Ruby scripts you need to install gems:
`gem install dotenv twilio-ruby gmail`

为了运行Ruby脚本，你需要安装gems：

## Cron jobs
计划任务

```sh
# Runs `smack-my-bitch-up.sh` monday to friday at 9:20 pm.
20 21 * * 1-5 /path/to/scripts/smack-my-bitch-up.sh >> /path/to/smack-my-bitch-up.log 2>&1

# Runs `hangover.sh` monday to friday at 8:45 am.
45 8 * * 1-5 /path/to/scripts/hangover.sh >> /path/to/hangover.log 2>&1

# Runs `kumar-asshole.sh` every 10 minutes.
*/10 * * * * /path/to/scripts/kumar-asshole.sh

# Runs `fucking-coffee.sh` hourly from 9am to 6pm on weekdays.
0 9-18 * * 1-5 /path/to/scripts/fucking-coffee.sh
```

---
Code is released under WTFPL.

代码已经在WTFPL下发布了
