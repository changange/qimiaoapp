import qimiao_app_comm.app_start as start
import random

class RoomAction:

    def intoRoom(self, cmd_name):
        d = start.TestStart().connCMD(cmd_name)
        ##  获取总共有几个房间
        roomNum = d(resourceId='com.qmnl.qmpd:id/content_cl').count
        if roomNum > 3:     ##  没办法开发LJ  ID都不是唯一的
            roomNum = 3
        num = random.randint(0,roomNum-1)   ##随机进入一个房间
        print("第  --  {}  ---个房间".format(num))
        d(resourceId='com.qmnl.qmpd:id/content_cl', instance=num).click()

if __name__ == '__main__':
    t = RoomAction()
    t.intoRoom()
