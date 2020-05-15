# -*- coding:utf8 -*-
"""
2020-05-15
python日志处理
"""
import logging
import time

class Logger(object):
    def __init__(self):
        # 创建日志器
        self.logger = logging.getLogger("logger")
        # 输出当前设置等级及以上等级所有信息
        # logger.setLevel(logging.ERROR)  # 如果不设置，默认等级为warning
        if not self.logger.handlers:  # 方案2：判断如果logger没有handler，才创建处理器
            # 创建handler处理器 一个logger可有多个handler
            # StreamHandler 控制台输出
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)  # 单独设置控制台输出DEBUG信息

            # FileHandler 文件输出日志 指定日志文件名格式，日志目录要提前创建好，否则提示找不到目录
            fh = logging.FileHandler('../logs/{}_log'.format(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())),
                                     encoding="utf-8")
            fh.setLevel(logging.ERROR)  # 单独设置输出ERROR信息到文件

            # 创建日志输出格式，如果使用了参数fmt，后面就要加上datefmt
            formatter = logging.Formatter(
                fmt="%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s %(message)s", datefmt="%y%m%d %X")

            # 日志器添加处理器
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

            sh.setFormatter(formatter)
            fh.setFormatter(formatter)

            # 日志信息输出
            # logger.debug("debug")
            # logger.info("info")
            # logger.warning("warning")
            # logger.error("error")
        self.logger.critical("critical")

        # # 方案1：移出日志处理器，避免多次调用的重复日志问题
        # logger.removeHandler(sh)
        # logger.removeHandler(fh)

    def log(self):
        return self.logger

# log()  # 1个控制台处理器，打印1条
# log()  # 2个控制台处理器，所以再打印2条
# log()  # 3个控制台处理器，所以再打印3条


if __name__ == '__main__':
    log = Logger()
    log.log()