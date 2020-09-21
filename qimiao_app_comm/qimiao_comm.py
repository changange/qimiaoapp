import qimiao_app_comm.app_finally as end
import qimiao_app_comm.app_start as start
import time

class QimiaoCommnotAction:

    ##  离开房间
    def leave_room(self, cmd_name):
        #   调用两次   防止退出之前进入了私聊页面
        end.TestEnd(cmd_name).back_up_level()
        time.sleep(0.5)
        end.TestEnd(cmd_name).back_up_level()

        d = start.TestStart().connCMD(cmd_name)
        s = start.TestStart().sessionConn(cmd_name)
        display = d.device_info['display']
        width = display['width']
        hight = display['height']
        s.click(width*0.686, hight*0.61)

    ##  进入房间先判断房间在不在，不在的话刷新
    def into_room_exic(self, cmd_name):
        try:
            text = start.TestStart().sessionConn(cmd_name)(resourceId='com.qmnl.qmpd:id/okBtn').get_text()
            print(text)
            if "知" in text:
                start.TestStart().sessionConn(cmd_name)(resourceId='com.qmnl.qmpd:id/okBtn').click()
                print('存在 知道了 弹框---房间已被解散')
                return False
        except Exception as e:
            print('不存在 知道了 弹框')
            return True

    ##  滑动的起始位置和终止位置（百分比）
    def side(self, start_width, start_hight, end_width, end_hight, cmd_name):
        d = start.TestStart().connCMD(cmd_name)
        s = start.TestStart().sessionConn(cmd_name)
        display = d.device_info['display']
        width = display['width']
        hight = display['height']
        s.swipe(width*start_width, hight*start_hight, width*end_width, hight*end_hight)




if __name__ == '__main__':
    q = QimiaoCommnotAction()
    # q.side(0.498, 0.283, 0.485, 0.714)
    q.into_room_exic('UKPFSCEQ99999999')
