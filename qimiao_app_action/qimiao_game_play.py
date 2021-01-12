import uiautomator2 as u2
import xml.etree.ElementTree as ET
import os
import random, time

class PlayGame:
    def __init__(self,d):
        self.d = d
        self.display = self.d.device_info['display']
        self.width = self.display['width']
        self.hight = self.display['height']

        ##  跑的起始位置（轮盘）
        self.pao_width = self.width*0.5
        self.pao_high = self.hight*0.85

        ##  跳跃按钮位置
        self.jump_width = self.width * 0.9
        self.jump_hight = self.hight * 0.77

        ##  配置文件
        self.resT = self.read_config(f'{os.path.abspath("..")}\config\qimiao.xml')


    def read_config(self, path):
        res=[]
        tree = ET.parse(path).getroot()
        i =  tree.find('Doaction')
        click = i.find('click').text
        res.append(click)
        sliding = i.find('sliding').text
        res.append(sliding)

        j = tree.find('ScreenLocation')
        lun_up = j.find('lun_up').text
        res.append(lun_up)

        return res

    ##  随机跑、跳
    def sliding_jump_randge(self):
        resTD = float(self.resT[0]) * 100
        randNum = random.randint(0,100)

        ##  跳跃
        if randNum < resTD:
            print('点击跳跃~~~')
            self.d.click(self.jump_width, self.jump_hight)

        ##  跑
        if resTD <=randNum:
            resJump = float(self.resT[2]) * 100
            randNumJump = random.randint(0, 100)

            ##  滑动功能的步长值
            randNum_i = round(random.uniform(0.5,2), 2)

            if randNumJump > resJump:
                randNum_width = random.randint(1, self.width)
                randNum_hight = random.randint(1, self.pao_high)
            else:
                randNum_width = random.randint(1, self.width)
                randNum_hight = random.randint(self.pao_high, self.hight)

            print('滑动跑~~~')
            try:
                self.d.swipe(self.pao_width, self.pao_high, randNum_width, randNum_hight, randNum_i)
            except Exception as e:
                print('滑动的时候出错了~~~')

    ##  固定几次滑动、跑
    def sliding_jump_guding(self, sliding=1, jump=1, randNum_i=0.5):
        ##  跳跃
        for i in range(jump):
            time.sleep(1)
            print('点击跳跃~~~')
            self.d.click(self.jump_width, self.jump_hight)


        ##  滑动
        for i in range(sliding):
            resJump = float(self.resT[2]) * 100
            randNumJump = random.randint(0, 100)

            ##  滑动功能的步长值
            # randNum_i = round(random.uniform(0.5, 2), 2)

            if randNumJump > resJump:
                randNum_width = random.randint(1, self.width)
                randNum_hight = random.randint(1, self.pao_high)
            else:
                randNum_width = random.randint(1, self.width)
                randNum_hight = random.randint(self.pao_high, self.hight)

            print('滑动跑~~~')
            try:
                self.d.swipe(self.pao_width, self.pao_high, randNum_width, randNum_hight, randNum_i)
                time.sleep(0.5)
            except Exception as e:
                print('滑动的时候出错了~~~')


if __name__ == '__main__':
    d = u2.connect('a302ac9c')
    d.app_start(package_name='com.qmnl.qmpd', activity='com.qmnl.pati.ui.SplashActivity')
    s = d.session(package_name='com.qmnl.qmpd', attach=True)
    pg = PlayGame(s)
    # while True:
    pg.sliding_jump_guding(20,20,1)