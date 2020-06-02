import qimiao_app_action.qimiao_random_into_room as into_room
import qimiao_app_comm.app_start as start
import qimiao_app_comm.qimiao_comm as comm
import qimiao_app_comm.action_comm as ac_comm
import qimiao_app_main.qimiao_room_test as other_room
import time

class HomeTest:

    def test_into_rooms(self,cmd_name):
        s = start.TestStart().sessionConn(cmd_name)
        d = start.TestStart().connCMD(cmd_name)

        display = d.device_info["display"]
        width = display['width']
        height = display['height']

        ##  进入前先刷新下     传参（百分比）
        comm.QimiaoCommnotAction().side(0.712, 0.171, 0.756, 0.829, cmd_name)
        time.sleep(0.5)
        comm.QimiaoCommnotAction().side(0.712, 0.171, 0.756, 0.829, cmd_name)

        ##  上拉模拟用户滑动
        comm.QimiaoCommnotAction().side(0.754, 0.8, 0.758, 0.37, cmd_name)
        if not ac_comm.ActionComm().detection_element_exist('com.qmnl.qmpd:id/chat_room_owner_head', cmd_name):
            print('首页列表元素没有发现----列表为空')

        ##  随机进入一个房间
        into_room.RoomAction().intoRoom(cmd_name)
        time.sleep(1)
        ##  是否存在“知道了”弹框
        comm.QimiaoCommnotAction().into_room_exic()
        time.sleep(30)

        ##  语聊房内
        other_room.OtherRoom(cmd_name).click_up_wheat()

        ##  怕有推介房间
        s.click(width*0.875, height*0.268)

        ##  离开房间
        print('准备离开房间')
        comm.QimiaoCommnotAction().leave_room(cmd_name)
        time.sleep(10)



    def test_rooms_main(self,cmd_name):
        self.test_into_rooms(cmd_name)
