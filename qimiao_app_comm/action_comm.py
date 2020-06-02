import qimiao_app_comm.app_start as start
import time

class ActionComm:

    ##  检测元素是否存在
    def detection_element_exist(self, mode, cmd_name):
        d = start.TestStart().connCMD(cmd_name)
        for i in range(5):
            if (d(resourceId= mode)):
                return True
            else:
                time.sleep(2)
        return False
