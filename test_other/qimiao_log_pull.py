import os

class LogPull:

    def log_pull(self, cmd_name):
        cmd_c_exist = "dir C:\\"
        res_c_exist = os.popen(cmd_c_exist)

        ##  结果的过滤      暂时无用
        # res_c_map_exist = list(map(lambda x:x.strip(), res_c_exist.readlines()))
        # res_c_k_exist = list(filter(lambda x:x != '', res_c_map_exist))

        if os.path.exists(r'C:\qimiao_log'):
            cc = os.remove(r'C:\log')
            print(cc)

        # cmd_pull = f'adb -s {cmd_name} pull /data/local/tmp/qimiao_log C:\qimiao_log'
        # res_pull = os.popen(cmd_pull)

if __name__ == '__main__':
    l = LogPull()
    l.log_pull('UKPFSCEQ99999999')
