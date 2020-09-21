import qimiao_app_comm.app_start as start
import qimiao_app_action.qimiao_random_into_room as into_room
import qimiao_app_comm.qimiao_comm as comm
import qimiao_app_comm.action_comm as ac_comm
import qimiao_app_main.qimiao_room_test as other_room
import time
import random

class UnityPage:
    def __init__(self,cmd_name):
        self.cmd_name = cmd_name
        self.s = start.TestStart().sessionConn(cmd_name)
        self.d = start.TestStart().connCMD(cmd_name)
        self.display = self.d.device_info["display"]
        self.width = self.display['width']
        self.height = self.display['height']

    ##  个人主页
    def unity_oneself_page(self):
        if self.s(resourceId='com.qmnl.qmpd:id/personalImageClick').wait(10):
            self.s(resourceId='com.qmnl.qmpd:id/personalImageClick').click()
            print('进入主页')
            time.sleep(10)

            ##  进入装扮
            print('进入个人主页--装扮页面')
            self.s.click(self.width * 0.88, self.height * 0.51)
            time.sleep(5)

            y_list = [(0.14*self.width ,0.67*self.height), (0.38*self.width, 0.68*self.height), (0.6*self.width, 0.83*self.height)]
            h_num = random.sample(y_list, 1)[0]
            print(h_num)
            self.s.click(h_num[0], h_num[1])
            time.sleep(0.5)
            self.s.click(self.width * 0.87, self.height * 0.077)
            time.sleep(8)

            ##  进入背景
            print('进入个人主页--背景页面')
            self.s.click(self.width * 0.88, self.height * 0.63)
            time.sleep(5)

            b_list = [(0.38 * self.width, 0.78 * self.height), (0.86 * self.width, 0.78 * self.height),
                      (0.38 * self.width, 0.9 * self.height)]
            b_num = random.sample(b_list, 1)[0]
            print(b_num)
            self.s.click(b_num[0], b_num[1])
            time.sleep(0.5)
            self.s.click(self.width * 0.82, self.height * 0.09)
            time.sleep(5)

            ##  进入奇妙秀列表页
            print('进入个人主页---奇妙秀列表页')
            self.s.click(self.width * 0.88, self.height * 0.75)
            if self.s(resourceId='com.qmnl.qmpd:id/title_tv').wait(10):
                comm.QimiaoCommnotAction().side(0.756, 0.829, 0.712, 0.171, self.cmd_name)

            self.d.press('back')
            time.sleep(5)
            self.d.press('back')
            if self.s(resourceId='com.qmnl.qmpd:id/home_party_parent_bg').wait(10):
                print('从个人业主成功回退到首页')
            else:
                print('从个人主页回退到首页失败了~~~~~~~')

        else:
            print('个人主页的入口没有找到~~~~~~')

    ##  盲盒
    def unity_prize_box(self):
        if self.s(resourceId='com.qmnl.qmpd:id/home_fragment_surprise_box_image').wait(10):
            self.s(resourceId='com.qmnl.qmpd:id/home_fragment_surprise_box_image').click()
            print('进入盲盒')
            time.sleep(5)
            self.s.click(self.width * 0.5, self.height * 0.7)
            print('正在抽奖')
            time.sleep(5)

            self.d.press('back')
            time.sleep(0.1)
            self.d.press('back')

            if self.s(resourceId='com.qmnl.qmpd:id/home_party_parent_bg').wait(2):
                print('盲盒已抽完奖，回到首页成功')
            else:
                print('盲盒已抽完奖，回到首页失败~~~~~~')

        else:
            print('盲盒的入口没有找到~~~~~~')

    ##  奇妙秀
    def unity_qimiaoxiu(self):
        if self.s(resourceId='com.qmnl.qmpd:id/home_live_video_iv').wait(10):
            self.s(resourceId='com.qmnl.qmpd:id/home_live_video_iv').click()
            print('进入奇妙秀')

            if self.s(resourceId='com.qmnl.qmpd:id/home_fragment_btn_create_live_video').wait(10):
                self.s(resourceId='com.qmnl.qmpd:id/home_fragment_btn_create_live_video').click()
                print('进入录制页面')
            else:
                print('没有找到录制按钮~~~~~~')

            time.sleep(8)

            ##  录制
            self.s.click(self.width * 0.5, self.height * 0.85)
            lu_time = random.randint(5, 20)
            time.sleep(lu_time)
            self.s.click(self.width * 0.5, self.height * 0.85)

            if self.s(resourceId='com.qmnl.qmpd:id/publish_tv').wait(10):
                self.s(resourceId='com.qmnl.qmpd:id/publish_tv').click()
                print('正在发布奇妙秀视屏')
            else:
                print('奇妙秀发布页面进入失败了~~~~~~')

            if self.s(text='发布成功').wait(40):
                print('奇妙秀发布成功')
            else:
                print('奇妙秀发布失败~~~~~~')

        else:
            print('奇妙秀入口没有找到~~~~~~~~')


    ##  营地
    def unity_into_room(self, room_name):
        display = self.d.device_info["display"]
        width = display['width']
        height = display['height']

        self.s(resourceId='com.qmnl.qmpd:id/home_party_iv').click()

        if self.s(resourceId='com.qmnl.qmpd:id/game_iv').wait(5):
            print('首页--派对页面打开成功')
        elif self.s(resourceId='com.qmnl.qmpd:id/chat_room_title').wait(5):
            print('首页--派对页面打开成功')
        else:
            print('首页--派对打开失败~~~~~~~~~~~~~~~~')
            return False

        for i in range(10):
            ##  进入前先刷新下     传参（百分比）
            print('开始刷新首页~~')
            comm.QimiaoCommnotAction().side(0.712, 0.171, 0.756, 0.829, self.cmd_name)
            time.sleep(0.5)
            comm.QimiaoCommnotAction().side(0.712, 0.171, 0.756, 0.829, self.cmd_name)
            print('刷新首页完成~~')

            ##  上拉模拟用户滑动
            print('开始上拉列表~~')
            comm.QimiaoCommnotAction().side(0.49, 0.49, 0.482, 0.224, self.cmd_name)
            print('上拉列表页完成~~~')
            if not ac_comm.ActionComm().detection_element_exist('com.qmnl.qmpd:id/chat_room_title', self.cmd_name):
                print('首页列表元素没有发现----列表为空')

            ##  随机进入一个房间
            into_room.RoomAction().intoRoom(self.cmd_name, room_name)  ##  随机进入
            # into_room.RoomAction().into_room_only(cmd_name, room_name)          #指定进入某一房间
            time.sleep(1)
            ##  是否存在“知道了”弹框
            is_ok = comm.QimiaoCommnotAction().into_room_exic(self.cmd_name)
            if is_ok == False:
                continue
            else:
                break
        time.sleep(10)

        ##  语聊房内
        other_room.OtherRoom(self.cmd_name).click_up_wheat()

        ##  推介房间
        self.s.click(width * 0.875, height * 0.268)
        ##  房主解散房间
        time.sleep(0.5)
        self.s.click(width * 0.488, height * 0.614)

        time.sleep(5)
        if self.d(resourceId='com.qmnl.qmpd:id/chat_room_title'):
            print('房主已解散房间~~~')
        else:
            ##  离开房间
            print('准备离开房间')
            comm.QimiaoCommnotAction().leave_room(self.cmd_name)

        if self.s(resourceId='com.qmnl.qmpd:id/home_party_parent_bg').wait(15):
            print('从营地回到首页成功')
        else:
            print('从营地回到首页失败~~~~~~~~~~~~~')


    def unity_main(self, room_name):
        unity_list = [1,2,3,4]
        # unity_list = [1]
        unity_num = random.sample(unity_list,1)

        print(f'生成的ID：{unity_num[0]}')
        if unity_num[0] == 1:
            print('1111111111111')
            self.unity_oneself_page()
        elif unity_num[0] == 2:
            self.unity_prize_box()
        elif unity_num[0] == 3:
            print('999999999999')
            self.unity_qimiaoxiu()
        elif unity_num[0] == 4:
            self.unity_into_room(room_name)

if __name__ == '__main__':
    u = UnityPage('UKPFSCEQ99999999')
    # u.unity_oneself_page()
    u.unity_main('11')