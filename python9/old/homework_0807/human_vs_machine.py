#5  人和机器猜拳游戏写成一个类，有如下几个函数：
#1）函数1：选择角色 1曹操  2张飞  3刘备
#2）函数2：角色猜拳 1剪刀 2石头 3布 玩家输入一个1-3的数字
#3) 函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
#4）函数4：角色和机器出拳对战，对战结束后，
#最后出示本局对战结果...赢...输，然后提示用户是否继续？按y继续，按n退出。
#5）最后结束的时候输出结果 角色赢几局  电脑赢几局，平局几次 游戏结束
import random
class HumanVsMachine:
    fist_dict = {"1": "剪刀", "2": "石头", "3": "布"}
    role_dict = {"1": "曹操", "2": "张飞", "3": "刘备"}
    def ChooseRole(self):


        while True:
            role_num = input("请输入数字选择你的角色： 1曹操  2张飞  3刘备")
            if role_num in ("1","2","3"):
                role_name=self.role_dict[role_num]
                break
            else:
                print("你输入的角色错误，请重新输入？")
                continue
        return role_name#返回我所选择的角色

    def Human(self,role_name):#角色出拳

        fist_num=input("{0}请出拳！".format(role_name))
        try:
            print("{0}出拳为：{1}".format(role_name,self.fist_dict[fist_num]))
        except Exception as e:
            print("出错啦：%s"%e)
        else:
            return int(fist_num)

    def Machine(self):
        fist_num=random.randint(1,3)
        print("电脑出拳为：{0}".format(self.fist_dict[str(fist_num)]))
        return fist_num

    def human_vs_machine(self):
        role_name=self.ChooseRole()#确定的的角色名？

        human_win=0#角色赢
        machine_win=0#机器赢
        draw_num=0#平局

        while True:
            human_fist=self.Human(role_name)#角色出拳
            machine_fist=self.Machine()#电脑出拳
            #1剪刀  2石头  3布
            #1--3  2--1 3--2

            #这个加个异常处理
            try:
                if human_fist-machine_fist==-2 or human_fist-machine_fist==1 or human_fist-machine_fist==-1:
                    human_win+=1#以上情况符合  就是角色赢了
                    print("恭喜{0}赢了本局！".format(role_name))
                elif human_fist-machine_fist==0:#平局
                    draw_num+=1
                    print("本局打平")
                else:
                    machine_win+=1#电脑赢了
                    print("很遗憾{0}输了，电脑赢了！".format(role_name))
            except Exception as e:
                print("出的拳不对！%s"%e)
            finally:
                #判断是否继续进行猜拳？
                yes_or_no=input("是否继续？按y继续，按n退出")
                if yes_or_no=="n":
                    break
        #结束对战之后，出结果！
        print("{0}赢了{1}局，电脑赢了{2}局，双方平了{3}局".format(role_name,human_win,machine_win,draw_num))

if __name__ == '__main__':
    HumanVsMachine().human_vs_machine()