import qimiao_app_comm.app_start as start
import time

class OtherRoom:

    def __init__(self, cmd_name):
        self.d = start.TestStart().connCMD(cmd_name)
        self.display = self.d.device_info["display"]
        self.width = self.display['width']
        self.height = self.display['height']


    ##  语聊房、营地功能点击
    def click_up_wheat(self):
        ##   上下麦
        self.d.click(self.width*0.086, self.height*0.954)
        print('第 一 次点击上下麦按钮')
        # self.d.disable_popups(False)
        ##  再点一次
        time.sleep(3)
        self.d.click(self.width*0.086, self.height*0.954)
        print('第 二 次点击上下麦')

        #   发送文字
        self.d.click(self.width*0.4, self.height*0.95)
        time.sleep(0.5)
        print("输入键盘已弹出")
        #   输入文字
        self.d.click(self.width * 0.072, self.height * 0.7)
        time.sleep(0.2)
        self.d.click(self.width * 0.072, self.height * 0.635)
        time.sleep(0.2)
        #   发送按钮
        self.d.click(self.width * 0.913, self.height * 0.560)
        time.sleep(1)
        self.d.click(self.width * 0.6, self.height * 0.43)
        print('文字已发送完成')


        #   发送表情
        print('开始发送表情-----')
        self.d.click(self.width * 0.660, self.height * 0.954)
        time.sleep(1)
        self.d.click(self.width * 0.38, self.height * 0.43)
        time.sleep(1)
        print('表情发送完成')


        ## =================================暂时先不做====================================
        '''
        #   道具、动作
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
        '''
        ## =====================================================================



        #   发红包、礼物
        print('开始发起红包、送礼物操作-------')
        # 礼物发送
        self.d.click(self.width * 0.923, self.height * 0.954)
        time.sleep(0.5)
        self.d.click(self.width * 0.15, self.height * 0.68)
        time.sleep(0.5)
        self.d.click(self.width * 0.85, self.height * 0.95)
        time.sleep(1)
        #红包
        self.d.click(self.width * 0.923, self.height * 0.954)
        time.sleep(0.5)
        self.d.click(self.width * 0.27, self.height * 0.39)
        time.sleep(0.5)
        self.d.click(self.width * 0.2, self.height * 0.6)
        time.sleep(0.5)
        self.d.click(self.width * 0.85, self.height * 0.95)
        print('礼物、红包发送完了')

    def test_other_room(self):
        self.click_up_wheat()

if __name__ == '__main__':
    o = OtherRoom('792QBEQN222NB')
    o.test_other_room()


