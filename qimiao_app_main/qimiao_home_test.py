import qimiao_app_action.qimiao_random_into_room as into_room
import qimiao_app_comm.app_start as start
import qimiao_app_comm.qimiao_comm as comm
import qimiao_app_comm.action_comm as ac_comm
import qimiao_app_main.qimiao_room_test as other_room
import time

class HomeTest:

    def test_into_rooms(self,cmd_name, room_name):
        s = start.TestStart().sessionConn(cmd_name)
        d = start.TestStart().connCMD(cmd_name)

        display = d.device_info["display"]
        width = display['width']
        height = display['height']

        if s(resourceId='com.qmnl.qmpd:id/home_party_iv').wait(1):
            s(resourceId='com.qmnl.qmpd:id/home_party_iv').click()
        else:
            print("退出到首页失败了~~~~~~~~~~")

        if s(resourceId='com.qmnl.qmpd:id/game_iv').wait(5):
            print('首页--派对页面打开成功')
        elif s(resourceId='com.qmnl.qmpd:id/chat_room_title').wait(5):
            print('首页--派对页面打开成功')
        else:
            print('首页--派对打开失败~~~~~~~~~~~~~~~~')
            return False

        for i in range(10):
            ##  进入前先刷新下     传参（百分比）
            print('开始刷新首页~~')
            comm.QimiaoCommnotAction().side(0.712, 0.171, 0.756, 0.829, cmd_name)
            # time.sleep(0.5)
            comm.QimiaoCommnotAction().side(0.712, 0.171, 0.756, 0.829, cmd_name)
            print('刷新首页完成~~')

            ##  上拉模拟用户滑动
            print('开始上拉列表~~')
            comm.QimiaoCommnotAction().side(0.49, 0.49, 0.482, 0.224, cmd_name)
            print('上拉列表页完成~~~')
            if not ac_comm.ActionComm().detection_element_exist('com.qmnl.qmpd:id/chat_room_title', cmd_name):
                print('首页列表元素没有发现----列表为空')

            ##  随机进入一个房间
            into_room.RoomAction().intoRoom(cmd_name, room_name)      ##  随机进入
            # into_room.RoomAction().into_room_only(cmd_name, room_name)          #指定进入某一房间
            time.sleep(1)
            ##  是否存在“知道了”弹框
            is_ok = comm.QimiaoCommnotAction().into_room_exic(cmd_name)
            if is_ok == False:
                continue
            else:
                break
        time.sleep(10)

        ##  语聊房内
        other_room.OtherRoom(cmd_name).click_up_wheat()


        ##  推介房间
        s.click(width*0.875, height*0.268)
        ##  房主解散房间
        time.sleep(0.5)
        s.click(width*0.488, height*0.614)

        time.sleep(10)
        if d(resourceId='com.qmnl.qmpd:id/chat_room_title'):
            print('房主已解散房间~~~')
        else:
            ##  离开房间
            print('准备离开房间')
            comm.QimiaoCommnotAction().leave_room(cmd_name)
            time.sleep(10)



    def test_rooms_main(self,cmd_name, room_name):
        print('---------------进入首页房间---------------')
        self.test_into_rooms(cmd_name, room_name)
