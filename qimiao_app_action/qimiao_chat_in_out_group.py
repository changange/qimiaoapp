import qimiao_app_comm.app_start as start
import random

class ChatGroup:
    def __init__(self, cmd_name):
        self.cmd_name = cmd_name
        self.s = start.TestStart().sessionConn(self.cmd_name)
        self.d = start.TestStart().connCMD(self.cmd_name)

    ##   进入聊天--消息 页面
    def into_chat_list(self):
        chat_button = self.s(text='聊天').wait(5)
        if chat_button:
            print('已回到首页~~~找到  聊天  入口')
        else:
            print('没有找到聊天入口~~~')
            return False

        self.s(text='聊天').click()
        if self.s(text='消息').wait(3):
            print('已找到  消息  入口')
        else:
            print('没有消息入口')
            return False
        self.s(text='消息').click()
        print('已进入 消息 列表 页面')
        return True

    ##  进入消息详情页
    def into_chat_detail(self):
        mess_list = self.s(resourceId='com.qmnl.qmpd:id/title').count
        num_list = random.randint(0, mess_list)
        if num_list > 0:
            num_list -=1
        print(f'进入第：{num_list} 个聊天列表')
        self.d(resourceId='com.qmnl.qmpd:id/title', instance=num_list).click()
        if self.s(resourceId='com.qmnl.qmpd:id/report_iv').wait(1):
            print('已经成功进入 消息详情页')
        elif self.s(resourceId='com.qmnl.qmpd:id/chat_group_title').wait(1):
            print('已经成功进入 消息详情页')
        else:
            print('进入详细详情页失败~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            return False

    ##  聊天 发内容
    def send_text(self,text):
        self.d(resourceId='com.qmnl.qmpd:id/input').click()
        self.s(resourceId='com.qmnl.qmpd:id/input').set_text(text)
        self.s(text='发送').click()
        text_list = self.s(resourceId='com.qmnl.qmpd:id/text').count
        print(f'消息详情页共： {text_list} 条消息')

        try:
            if self.s(resourceId='com.qmnl.qmpd:id/text', instance=text_list-1).get_text() == text:
                print('消息发送成功')
            else:
                if self.s(resourceId='com.qmnl.qmpd:id/text', instance=text_list).get_text() == text:
                    print('消息发送成功')
                else:
                    print('消息发送失败~~~~~~~~~~~~~~~~~~~~~')
        except Exception as e :
            if self.s(resourceId='com.qmnl.qmpd:id/text', instance=text_list).get_text() == text:
                print('消息发送成功')
            else:
                print('消息发送失败~~~~~~~~~~~~~~~~~~~~~')

    ##  进入 小组成员信息
    def into_group_information(self):
        display = self.d.device_info["display"]
        width = display['width']
        height = display['height']

        self.s.click(width * 0.932, height * 0.074)
        if self.s(resourceId='com.qmnl.qmpd:id/selected_title').wait(3):
            print('进入 小组信息 页面成功')
        else:
            print('进入 小组信息 页面失败~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            return False

        member_list = self.s(resourceId='com.qmnl.qmpd:id/avatar').count
        member_num = random.randint(0, member_list)
        print(f'进入第：{member_num}个成员的个人主页')
        return member_num

    ##  发现小组--推介小组
    def find_recommend_group(self):
        join_list = 0
        if self.d(text='发现小组').wait(3):
            print('已找到 发现小组')
            self.d(text='发现小组').click()
            if self.d(text='小组').wait(3):
                print('已进入 小组页面')

                self.d(text='推荐的小组').click()
                try:
                    join_list = self.d(text='加入').count
                except Exception:
                    print('推荐小组 里没有可加入的列表 ')

                if join_list > 0:
                    print('推荐的小组 存在可加入的消息')
                    join_num = random.randint(0,join_list)
                    self.d(resourceId='com.qmnl.qmpd:id/chat_group_join_tv', instance=join_num).click()
                    if self.d(resourceId='com.qmnl.qmpd:id/chat_group_title').wait(3):
                        print('进入 推荐小组的聊天页面 成功')
                    else:
                        print('进入 推荐小组的聊天页面 失败~~~~~~~~~~~~~~~~~~~~~~~')
                else:
                    self.d(text='好友的小组').click()
                    if self.d(resourceId='com.qmnl.qmpd:id/chat_group_join_tv').wait(3):
                        in_list = self.d(text='去聊天').count
                        join_num = random.randint(0, in_list)
                        self.d(resourceId='com.qmnl.qmpd:id/chat_group_join_tv', instance=join_num).click()
                        if self.d(resourceId='com.qmnl.qmpd:id/chat_group_title').wait(3):
                            print('进入 好友的聊天页面 成功')
                        else:
                            print('进入 好友的聊天页面失败~~~~~~~~~~~~~~~~~~~~~~~')
            else:
                print('进入 推荐的小组 失败~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        else:
            print('没有找到 发现小组~~~~~~~~~~~~~~~~~~~~~~~~')
            return False

if __name__ == '__main__':
    c = ChatGroup('LFLBB19418208291')
    c.find_recommend_group()