import qimiao_app_comm.app_start as start
import time

class OtherRoom:

    def __init__(self, cmd_name):
        self.d = start.TestStart().connCMD(cmd_name)
        self.display = self.d.device_info["display"]
        self.width = self.display['width']
        self.height = self.display['height']

    ##  点击上麦或者参加(坐标)

    def click_up_wheat(self):
        time.sleep(5)
        ##  怕有推介房间
        self.d.click(self.width*0.875, self.height*0.268)
        ##  上下麦
        self.d.click(self.width*0.086, self.height*0.954)
        print('上麦、下麦、参加点击完成')

        # self.d.disable_popups(False)

        ##  再点一次
        time.sleep(2)
        ##  怕有推介房间
        self.d.click(self.width*0.875, self.height*0.268)
        self.d.click(self.width*0.086, self.height*0.954)
        print('第二次点击---上麦、下麦、参加点击完成')

    def test_other_room(self):
        self.click_up_wheat()

if __name__ == '__main__':
    o = OtherRoom('LFLBB19418208291')
    o.test_other_room()


