import qimiao_app_comm.app_start as start

class TestEnd:
    def __init__(self, cmd_name):
        self.cmd_name = cmd_name

    ##  返回上一级
    def back_up_level(self):
        s = start.TestStart().sessionConn(self.cmd_name)
        s.press("back")

if __name__ == '__main__':
    t = TestEnd()
    t.back_up_level()