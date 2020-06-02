import os
import logging
import time

class WriteLog:
    path = lambda p : os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )

    def logging_getLogger(self):
        logging.basicConfig(level=logging.WARNING,
                            format='%(threadName)s - %(thread)d  %(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                            # datefmt='%a %d %b %Y %H:%M:%S',
                            datefmt='%Y-%m-%d%H:%M:%S',
                            filename=r'C:\log\奇妙.txt',
                            filemode='a')
        log = logging.getLogger()
        return log

    def logging_logcat(self):
        path_log = r'C:\log'
        run_time = time.strftime('%Y%m%d%H:%M:%S', time.localtime(time.time()))
        logcat_log = os.path.join(path_log, "奇妙.txt")
        logcat = f'adb logcat -s Unity >> {logcat_log}'
        cmd_res = os.popen(logcat).readlines()
        for i in cmd_res:
            print(i)
        print('logcat命令：', logcat)


if __name__ == '__main__':
    w = WriteLog()
    # w.logging_logcat()
    c = w.logging_getLogger().info('fdsf')
    print(c)
