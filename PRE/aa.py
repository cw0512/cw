money = 3500
bus = 1000
taxi = 5000
pocket = [money ,'nocard']


def prmsg(message):
    print("{1}, 잔액:{0}".format(money, message))

if 'card' in pocket:
    print("택시를 타라")
elif money >= 5000:
    money -= taxi
    prmsg("택시를 타라")
    """print("택시를 타라, 잔액:{0}".format(money))"""
elif money >= 1000:
    money -= bus
    prmsg("버스를 타라")
    """print("버스를 타라, 잔액:{0}".format(money))"""
else:
    prmsg("걸어가라")
    """print("걸어가라, 잔액:{0}".format(money))"""
