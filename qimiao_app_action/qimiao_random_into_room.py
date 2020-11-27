import qimiao_app_comm.app_start as start
import random
import qimiao_app_comm.qimiao_comm as comm

class RoomAction:

    ##  随机进入一个房间
    def intoRoom(self, cmd_name, room_name):
        d = start.TestStart().connCMD(cmd_name)
        ##  获取总共有几个房间
        roomNum = d(resourceId='com.qmnl.qmpd:id/chat_room_title').count
        if roomNum > 3:     ##  没办法开发LJ  ID都不是唯一的
            roomNum = 3
        num = random.randint(0,roomNum-1)   ##随机进入一个房间
        print("第  --  {}  ---个房间".format(num))
        d(resourceId='com.qmnl.qmpd:id/chat_room_title', instance=num).click()

    ##  进入指定的房间
    def into_room_only(self, cmd_name, room_name):
        d = start.TestStart().connCMD(cmd_name)
        print('开始寻找指定的房间~~~')
        while True:
            cc = d(resourceId='com.qmnl.qmpd:id/chat_room_title').count
            for i in range(cc):
                try:
                    if d(resourceId='com.qmnl.qmpd:id/chat_room_title', instance=i).get_text() == room_name:
                        d(resourceId='com.qmnl.qmpd:id/chat_room_title', instance=i).click()
                        print('已找到指定的房间~~~')
                        return False
                except Exception as e:
                    print(e)

            if cc < 2:
                comm.QimiaoCommnotAction().side(0.712, 0.171, 0.756, 0.829, cmd_name)   ##  下拉刷新
                print('房间数小于2个下拉数显首页')
            else:
                comm.QimiaoCommnotAction().side(0.56, 0.78, 0.5, 0.278, cmd_name)       ##  上拉查找
                print('正在查找指定房间')
        return True


if __name__ == '__main__':
    t = RoomAction()
    # t.intoRoom()
    t.into_room_only('792QBEQN222NB', '嘿嘿嘿')
