import logging
from commons.path_config import logs_path


class RunLog:

    def set_log(self, level, msg):
        my_logger = logging.getLogger('testLog')
        my_logger.setLevel(level)

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-%(name)s-日志信息：%(message)s')

        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)
        fh = logging.FileHandler(logs_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.set_log('DEBUG', msg)

    def info(self, msg):
        self.set_log('INFO', msg)

    def warning(self, msg):
        self.set_log('WARNING', msg)

    def error(self, msg):
        self.set_log('ERROR', msg)

    def critical(self, msg):
        self.set_log('CRITICAL', msg)


if __name__ == '__main__':
    RunLog().error('看看收集到什么日志s00d')
    RunLog().info('errorrrrrrr')
    RunLog().warning('waringppppp')
