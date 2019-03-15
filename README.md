## 简介
从所有可能的房源信息网抓取数据，进行简单的数据清洗后本地保存，对外提供查询、图表展示、价格趋势、价格对比等功能。

## 数据来源
- 链家
- 我爱我家
- 安居客
- 贝壳
- 58 同城
- 赶集
- 吉屋

## 使用说明
项目本身不依赖代理池，但是如果开启代理池能够更好地防止 IP 被 ban。代理池的部署可以参考项目 [async-proxy-pool](https://github.com/chenjiandongx/async-proxy-pool)。启动代理池服务后，在配置文件 `config_default.py` 文件中添加获取代理池的请求地址即可。

```python
py main.py
```

## 感谢
- [proxy_pool](https://github.com/jhao104/proxy_pool)
- [async-proxy-pool](https://github.com/chenjiandongx/async-proxy-pool)

## 声明
请勿将抓取到的数据用作商业用途。