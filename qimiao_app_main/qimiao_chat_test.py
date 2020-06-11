import qimiao_app_action.qimiao_chat_in_out_group as chat_group
import datetime
import qimiao_app_comm.app_start as start
import time

class ChatTest:
    def __init__(self, cmd_name):
        self.cmd_name = cmd_name
        self.chat = chat_group.ChatGroup(self.cmd_name)
        self.d = start.TestStart().connCMD(cmd_name)

    ##  私信操作
    def test_private_letter(self):
        ##  进入聊天--消息页面
        self.chat.into_chat_list()
        ##  随机选择一个聊天窗口
        self.chat.into_chat_detail()
        ##  发送内容
        text_time =datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print(text_time)
        self.chat.send_text(text_time)

        ##  返回到首页  （返回键）
        self.d.press('back')

    ##  群聊操作
    def test_group_chat(self):
        ##  进入聊天--消息页面
        self.chat.into_chat_list()
        ##  进入推荐小组
        self.chat.find_recommend_group()
        ##  发送消息
        text_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print(text_time)
        self.chat.send_text(text_time)

        ##  返回到首页  （返回键）
        self.d.press('back')
        time.sleep(0.5)
        self.d.press('back')

    def test_chat_main(self):
        ##  私信页面
        print('------------私信-----------')
        self.test_private_letter()
        print('------------群聊------------')
        ##  群聊页面
        self.test_group_chat()

if __name__ == '__main__':
    c = ChatTest('LFLBB19418208291')
    c.test_chat_main()