## 表情对比
- 发送"doubi"开始这一活动
- 服务器会返回一张热门的表情图
- 用户自拍一张模仿图，发送给机器人
- 服务器会根据我们自己的算法计算出表情的相似度
- [表情相似度算法文档](http://note.youdao.com/share/?token=3EBCFF2F67274562BA9E086379A43A53&gid=31461422)

## 微笑评分
- 方式一 用户主动请求
    - 用户发送 “smile” 给机器人。
    - 机器人回复一条微笑相关名言，并提示用户晒出自己的照片。
    - 用户拍照或选择自己的一张自拍发给机器人。
    - 机器人为用户的微笑进行评分，将分数发送给用户，并给出评价。

- 方式二 机器人定时提醒用户微笑

## 新闻
- 用户发送 “news list”，机器人发送给用户可以订阅的新闻类型列表。
- 用户发送 “newd (index)” 或者 “news (class)”，机器人发送给用户订阅的该新闻类型的新闻。
- 用户发送 “news”，机器人发送给默认的搜狐新闻。
- 定时发送新闻
- 数据源来自Matrix news feed

## 备忘录
- 用户发送 "addmemo content" 增加备忘录
- 用户发送 "getmemo" 查看该用户已有的备忘录

## 预发微信消息
- todo help
- todo add Bluemit 2016-08-21 00:00:00 Happy Birthday!
- todo show
- todo del 1

## routine
- build_routine()
- update_routine()
- process_routine()
- add_new_routine()
