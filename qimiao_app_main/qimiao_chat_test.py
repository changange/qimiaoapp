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
        isOk = self.chat.into_chat_detail()

        if isOk == True:
            ##  发送内容
            text_time =datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            print(text_time)
            self.chat.send_text(text_time)

            ##  发送奇妙秀
            self.chat.QMX_record_send()

            ##  返回到首页  （返回键）    按两次返回键才可以返回到首页
            self.d.press('back')
            if not self.d(resourceId='com.qmnl.qmpd:id/home_party_iv'):
                self.d.press('back')
            print('已返回到首级页面')

        else:
            print('消息列表没有消息，或者是只有一个开播提醒，退出发消息，进行下一步')

    ##  推介小组
    def test_group_chat(self):
        ##  进入聊天--消息页面
        self.chat.into_chat_list()
        ##  进入推荐小组
        self.chat.find_recommend_group()
        ##  发送消息
        text_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print(text_time)
        self.chat.send_text(text_time)

        ##  发送奇妙秀
        self.chat.QMX_record_send()

        ##  返回到首页  （返回键）
        self.d.press('back')
        time.sleep(0.5)
        if not self.d(resourceId='com.qmnl.qmpd:id/home_party_iv'):
            self.d.press('back')
            self.d.press('back')

    def test_chat_main(self):
        ##  消息聊天页面
        print('------------私信-----------')
        self.test_private_letter()
        print('------------群聊------------')
        ##  推介小组
        self.test_group_chat()

if __name__ == '__main__':
    c = ChatTest('LFLBB19418208291')
    c.test_chat_main()