# -*-coding: cp949 -*-

class Name:

    lastname="��"

    def __init__(self,name):
        self.fullname=self.lastname+name
        print("{}����".format(self.fullname))

    def travel(self, where):
        print ("{} {} ������ ����". format(self.fullname, where) )

    def __del__(self):
        print("{} ����".format(self.fullname))


if __name__=="__main__":

    # pey=Name("����")
    # pey.travel("����")

    a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
    print(list(a.keys()))
    print(list(a.items()))
    for k in a.keys():
        print(k)
