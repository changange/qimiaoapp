import uiautomator2 as u2
import time

class QimiaoTest:
    def __init__(self):
        self.d = u2.connect('a302ac9c')
        # self.d.app_start(pkg_name='com.android.calculator2')
        self.d.app_start(package_name='com.qmnl.qmpd', activity='com.qmnl.pati.ui.SplashActivity')
        # 创建Session对象，并与计算器绑定。可通过s.info属性来进行确认
        self.s = self.d.session(package_name='com.qmnl.qmpd', attach=True)


    def random(self,one,two,three,four):
        display = self.d.device_info['display']
        self.width = display['width']
        self.hight = display['height']

        self.s.click(self.width*0.9, self.hight*0.77)
        self.s.swipe(self.width * one, self.hight * two, self.width * three, self.hight * four, 1)


