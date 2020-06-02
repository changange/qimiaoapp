import qimiao_app_main.qimiao_home_test as home_test
import qimiao_app_comm.app_start as start
import  concurrent.futures
import time


class MainTest:

    def test_main(self, cmd_name):
        ##APP日志操作   清空
        start.TestStart().clear_cache_log(cmd_name)
        start.TestStart().delete_mobile_log(cmd_name, 'qimiao_log')     ##  文件夹

        ##  启动APP
        start.TestStart().openQimiao(cmd_name)
        ##  跳过弹框
        start.TestStart().jumpFrame(cmd_name)
        ##  随机进入fangjian
        while True:
            home_test.HomeTest().test_rooms_main(cmd_name)

    def qimiao_threading_excution(self):
        phone_number = start.TestStart().connectMoblie()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as excutor:
            if len(phone_number) >= 1:
                for i in range(len(phone_number)):
                    excutor.submit(self.test_main, phone_number[i])
                    time.sleep(3)
                    excutor.submit(start.TestStart().save_app_log, phone_number[i], 'qimiao_log')
            else:
                print('adb无法连接到手机~~~')




if __name__ == '__main__':
    mainT = MainTest()
    mainT.qimiao_threading_excution()
