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
        # time.sleep(5)
        ##  怕有推介房间
        # self.d.click(self.width*0.875, self.height*0.268)
        ##  上下麦
        self.d.click(self.width*0.086, self.height*0.954)
        print('上麦、下麦、参加点击完成')
        # self.d.disable_popups(False)

        ##  再点一次
        time.sleep(3)
        ##  怕有推介房间
        # self.d.click(self.width*0.875, self.height*0.268)
        self.d.click(self.width*0.086, self.height*0.954)
        print('第二次点击---上麦、下麦、参加点击完成')

        #   发送文字
        self.d.click(self.width*0.21, self.height*0.95)
        time.sleep(0.5)
        print("输入键盘已弹出")
        #   输入文字
        self.d.click(self.width * 0.072, self.height * 0.672)
        time.sleep(0.5)
        #   发送按钮
        self.d.click(self.width * 0.913, self.height * 0.524)
        time.sleep(0.5)
        self.d.click(self.width * 0.47, self.height * 0.3)
        print('文字已发送完成')


        #   发送表情
        print('开始发送表情-----')
        self.d.click(self.width * 0.534, self.height * 0.954)
        time.sleep(1)
        self.d.click(self.width * 0.127, self.height * 0.375)
        time.sleep(1)
        print('表情发送完成')


        #   道具动作
        print('开始道具、表情--')
        self.d.click(self.width * 0.661, self.height * 0.954)
        time.sleep(0.5)
        #   发送道具
        print('开始道具')
        self.d.click(self.width * 0.614, self.height * 0.918)
        time.sleep(1)
        self.d.click(self.width * 0.896, self.height * 0.468)
        time.sleep(0.5)
        #   做动作
        print('开始动作')
        self.d.click(self.width * 0.323, self.height * 0.794)
        time.sleep(1)
        self.d.click(self.width * 0.381, self.height * 0.906)
        time.sleep(0.5)
        #   点动作的时候怕点的是表情
        self.d.click(self.width * 0.472, self.height * 0.024)

            #收起控制台
        self.d.click(self.width * 0.917, self.height * 0.797)
        time.sleep(0.2)
        self.d.click(self.width * 0.5, self.height * 0.256)
        time.sleep(0.5)
        print('开始道具、表情已完成')



        #   发红包、礼物
            #   打开控制台
        print('开始发起红包、送礼物操作-------')
        self.d.click(self.width * 0.787, self.height * 0.954)
        time.sleep(1)
            #礼物发送
        self.d.click(self.width * 0.849, self.height * 0.944)
        time.sleep(2)

            #红包
        self.d.click(self.width * 0.787, self.height * 0.954)
        time.sleep(0.5)
        self.d.click(self.width * 0.27, self.height * 0.39)
        time.sleep(1)
        self.d.click(self.width * 0.849, self.height * 0.944)
        time.sleep(0.5)
        print('礼物、红包发送完了')

            #最后
        self.d.click(self.width * 0.614, self.height *  0.908)
        time.sleep(0.1)
        self.d.click(self.width * 0.9, self.height * 0.465)
        time.sleep(0.1)
        self.d.click(self.width * 0.919, self.height * 0.797)
        print('发红包的流程，最后的操作已经执行完了')
        time.sleep(1)

        #   营地，也执行红包的那一套东西
        print('开始执行营地物品的一套操作')
        self.d.click(self.width * 0.92, self.height * 0.96)
        time.sleep(0.1)
        time.sleep(5)
        print('111111111111111')
            #发送
        self.d.click(self.width * 0.849, self.height * 0.944)
        time.sleep(0.2)
        time.sleep(5)
        print('222222222222222222222')
        self.d.click(self.width * 0.942, self.height * 0.789)



    def test_other_room(self):
        self.click_up_wheat()

if __name__ == '__main__':
    o = OtherRoom('UKPFSCEQ99999999')
    o.test_other_room()


