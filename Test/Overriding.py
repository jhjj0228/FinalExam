# -*-coding: cp949 -*-
import HouseJang





class HouseHyun(HouseJang.Name):

    lastname="��"



    def travel(self, where, day):
        print(("{} {} {} ����").format(self.fullname, where, day))


if __name__ == "__main__":
    fullname=HouseHyun("�μ�")
    fullname.travel("�̱�", "20��")