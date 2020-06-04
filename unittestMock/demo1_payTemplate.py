# -*- coding:utf8 -*-
def zhifu():
    """
    2020-06-04 10:47:06
    测试unittest mock模块
    假设这里是一个支付的功能,未开发完
    支付成功返回：{"result": "success", "reason":"null"}
    支付失败返回：{"result": "fail", "reason":"余额不足"}
    reason返回失败原因
    """
    pass


def zhifu_status():
    """
    根据支付的结果success or fail，判断跳转到对应页面
    """
    result = zhifu()
    print(result)
    try:
        if result["result"] == "success":
            return "支付成功"
        elif result["result"] == "fail":
            print("失败原因：", result["reason"])
            return "支付失败"
        else:
            return "未知错误异常"
    except:
        return "Error, 服务端返回异常！"
