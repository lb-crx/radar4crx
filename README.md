# 针对扩展综合评分的雷达图生成

参考: [爱猎豹爱扩展~猎豹兼容扩展推荐活动开始啦！[v12.6.13]](http://bbs.liebao.cn/thread-16619-1-1.html)

## 使用

- 对 易用,功能,活跃,美观 四个象限选择对应的评分
- 点击 `就酱`
- 就可以在结果页面看到雷达图了!


## 开发

雷达图表:
- 基于 [ChartDirector](http://www.advsofteng.com/gallery.html) 生成雷达图
- 通过 Python 脚本( `simpleradar.py` ) 控制生成
- 使用 Py脚本 ( `gen4radar.py` ) 生成批量生成命令
- 发布在 ![又拍云存储](http://www.upyun.com/images/logo.gif)

网站 http://radar4crx.sinaapp.com/ :
- 基于 [Bottle](http://bottlepy.org/docs/dev/) 完成在线服务
- 发布在 [Sina App Engine](http://sae.sina.com.cn/)


## 协议

使用 [BSD licenses](http://en.wikipedia.org/wiki/BSD_licenses)
