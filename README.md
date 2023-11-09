## 前言

在实战中 往往不方便直接用自己的主机进行测试

这个时候就需要去抓一些🐔 便于我们一些操作的进行

首先不得不说向日葵的用户量还是非常大的，国内外的主机不计其数，rce的漏洞已经爆出快一年多了，但依旧有大量的主机服务器存在该rce 且存在漏洞的主机甚至都没有装杀软 运维人员简直懒到了极点

抓🐔的第一步肯定是先确定🐔的属性

这里推荐fofa

fofa的语法 

```
body="Verification failure" && country="CN"
```

互联网暴露资产29469台

![](https://cdn-zhiji-icu.oss-cn-hangzhou.aliyuncs.com/2021/image-20230402132817799.png)

python对接fofa api 进行信息收集自动化

![](https://cdn-zhiji-icu.oss-cn-hangzhou.aliyuncs.com/2021/image-20230402140350316.png)

然后是漏洞指纹  进一步确定资产

```
/cgi-bin/rpc?action=verify-haras
```

python实现

![](https://cdn-zhiji-icu.oss-cn-hangzhou.aliyuncs.com/2021/image-20230402151020718.png)

通过上面的手法 就已经能够去找到一些存在漏洞的主机了，这也是平时批量刷src的技巧，但我们的目标是上线、远控、肉

因为大多数的向日葵都是win主机所以我们这里这上渗透神器cobaltstrike

生成powershell远控脚本 

![](https://cdn-zhiji-icu.oss-cn-hangzhou.aliyuncs.com/2021/image-20230402150903308.png)

python实现

![](https://cdn-zhiji-icu.oss-cn-hangzhou.aliyuncs.com/2021/image-20230402151243783.png)

然后就到了最关键的一步  依据以上姿势编写整体脚本  在服务器上运行 或者肉鸡上运行 实现键指一动 敌方主机已上线

![](https://cdn-zhiji-icu.oss-cn-hangzhou.aliyuncs.com/2021/image-20230402151733538.png)

cs自动上线 睡醒起来看🐔就好啦

![](https://cdn-zhiji-icu.oss-cn-hangzhou.aliyuncs.com/2021/image-20230402151930603.png)
