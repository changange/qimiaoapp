import qimiao_app_comm.app_start as start
import random
import time
from skimage import io,data

class ChatGroup:
    def __init__(self, cmd_name):
        self.cmd_name = cmd_name
        self.s = start.TestStart().sessionConn(self.cmd_name)
        self.d = start.TestStart().connCMD(self.cmd_name)

    ##   进入聊天--消息 页面
    def into_chat_list(self):
        chat_button = self.s(resourceId='com.qmnl.qmpd:id/home_chat_iv').wait(5)
        if chat_button:
            print('已回到首页~~~找到  聊天  入口')
        else:
            print('没有找到聊天入口~~~')
            return False

        self.s(resourceId='com.qmnl.qmpd:id/home_chat_iv').click()
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
        print('准备进入消息详情页发送消息  ')
        mess_list = self.s(resourceId='com.qmnl.qmpd:id/title').count

        if mess_list == 0:
            print('消息列表没有可用的群聊消息~~~')
            return False

        print(f'消息页面共：{mess_list}个群聊消息')

        for i in range(5):
            print('循环循环查找 消息列表是不是 开播提醒')
            num_list = random.randint(0, mess_list-1)       ##  这几把也是个坑，我就真是日了狗了，   python这狗日的，报错不给抛异常

            #   消息页面只有一个消息列表的时候，且是开播提醒的时候，就跳过
            if self.d(resourceId='com.qmnl.qmpd:id/title', instance=num_list).get_text() != '开播提醒' and \
                    self.d(resourceId='com.qmnl.qmpd:id/title', instance=num_list).get_text() != '营地招财猫' and \
                    self.d(resourceId='com.qmnl.qmpd:id/title', instance=num_list).get_text() != '奇妙秀通知':
                print(f'进入第：{num_list} 个聊天列表')
                self.d(resourceId='com.qmnl.qmpd:id/title', instance=num_list).click()     ##  num_list
                if self.s(resourceId='com.qmnl.qmpd:id/input').wait(10):
                    print('已经成功进入 消息详情页')
                    return True
                else:
                    print('进入详细详情页失败~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    return False
        print('系统异常，或者没有消息页面')
        return False


    ##  聊天 发内容
    def send_text(self,res_text):
        self.d(resourceId='com.qmnl.qmpd:id/input').click()
        self.s(resourceId='com.qmnl.qmpd:id/input').set_text(res_text)
        self.s(text='发送').click()
        time.sleep(1)
        text_list = self.s(resourceId='com.qmnl.qmpd:id/text').count
        print(f'消息详情页共： {text_list} 条消息')

        try:
            text = self.s(resourceId='com.qmnl.qmpd:id/text')
            for i in range(text_list):
                if text[i].get_text() == res_text:
                    print('消息发送成功')
                    return True
            print(f'消息发送失败~~~~~~~~~~~{res_text}')
        except Exception as e:
            print('发送消息之后异常了~~~~~~~~~~~~')
            print(e)

        # try:
        #     print('检查消息是否发送成功')
        #     if self.s(resourceId='com.qmnl.qmpd:id/text', instance=text_list-1).get_text() == text:
        #         print('消息发送成功')
        #     else:
        #         if self.s(resourceId='com.qmnl.qmpd:id/text', instance=text_list).get_text() == text:
        #             print('消息发送成功')
        #         else:
        #             print('消息发送失败~~~~~~~~~~~~~~~~~~~~~')
        # except Exception as e:
        #     if self.s(resourceId='com.qmnl.qmpd:id/text', instance=text_list).get_text() == text:
        #         print('消息发送成功')
        #     else:
        #         print('消息发送失败~~~~~~~~~~~~~~~~~~~~~')

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

    ##  推介小组
    def find_recommend_group(self):
        join_list = 0
        go_to_chat = 0
        if self.d(text='推荐小组').wait(3):
            print('已找到 推荐小组')
            self.d(text='推荐小组').click()
            if self.d(text='加入').wait(3):
                print('已进入 推介小组 页面')

                try:
                    join_list = self.d(resourceId='com.qmnl.qmpd:id/chat_group_join_tv').count

                    ##  第四个加入或者去聊天是没办法点击到的，所以要减1
                    if join_list >= 4:
                        join_list = 3

                    print(f'XXXXXXXXXXXX共：{join_list} 个加入和去聊天')
                except Exception:
                    print('推荐小组 里没有可加入或者 去聊天的列表 ')

                if join_list > 0:
                    print('推荐的小组 存在可加入或者 去聊天的消息')
                    try:
                        join_num = random.randint(0,join_list-1)        ##  必须要减1
                        print(f'小组--推介的小组--加入第：{join_num}个群聊--{self.d(text="加入",instance=join_num).get_text()}')
                    except Exception as e:
                        print(e)
                    self.d(resourceId='com.qmnl.qmpd:id/chat_group_join_tv', instance=join_num).click()        ###################这是个坑，大几吧坑，日了狗了，花了一天时间就在join_num减了1
                    if self.d(resourceId='com.qmnl.qmpd:id/chat_group_title').wait(3):
                        print('进入 推荐小组的聊天页面 成功')
                    else:
                        print('进入 推荐小组的聊天页面 失败~~~~~~~~~~~~~~~~~~~~~~~')
                else:
                    print('没有群聊或者加入的聊天')

                    # 旧代码
                    # self.d(text='好友的小组').click()
                    # if self.d(resourceId='com.qmnl.qmpd:id/chat_group_join_tv').wait(3):
                    #     in_list = self.d(text='去聊天').count
                    #
                    #     if in_list > 0:
                    #         join_num = random.randint(0, in_list-1)
                    #         self.d(resourceId='com.qmnl.qmpd:id/chat_group_join_tv', instance=join_num).click()
                    #         if self.d(resourceId='com.qmnl.qmpd:id/chat_group_title').wait(3):
                    #             print('进入 好友的聊天页面 成功')
                    #         else:
                    #             print('进入 好友的聊天页面失败~~~~~~~~~~~~~~~~~~~~~~~')
                    #     else:
                    #         print('好友小组的列表为0~~~')
            else:
                print('进入 推荐的小组 失败~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        else:
            print('没有找到 推介小组~~~~~~~~~~~~~~~~~~~~~~~~')
            return False

    ##  聊天页面的奇妙秀录制功能
    def QMX_record_send(self):
        display = self.d.device_info["display"]
        width = display['width']
        height = display['height']

        if self.d(resourceId='com.qmnl.qmpd:id/recordBtn').wait(3):
            print('进入奇妙秀录制功能......')
            self.d(resourceId='com.qmnl.qmpd:id/recordBtn').click()
            num = random.randint(5,15)
            time.sleep(15)
            print("开始惦记奇妙秀录制按钮~~~")
            self.s.long_click(width*0.5, height*0.888, num)

        time.sleep(7)

        ##  滑动，奇妙秀发送完了之后，没有回到最新的消息处(保险起见要滑动两次)
        self.s.swipe(width * 0.5, height *0.8, width*0.5, height*0.2)
        self.s.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2)

        if self.d(resourceId='com.qmnl.qmpd:id/chat_group_video_volume_iv').wait(3):
            print('奇妙秀发送成功了......')
        else:
            print('奇妙秀发送失败了~~~')

if __name__ == '__main__':
    c = ChatGroup('UKPFSCEQ99999999')
    # c.send_text('20200630191019')
    c.QMX_record_send()

