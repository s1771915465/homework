def tao_tai(players, y, z):
    """
    Input:
    players:总人数
    y:每几人杀死一个
    z:最后剩余几个人

    Output:
    result:返回剩余人的序号
    """
    list1 = [i for i in range(players + 1)]
    del list1[0]
    # print(list1)  ps:初始人列表
    p, k = 0, 0
    while len(list1) != z:
        p = (len(list1) % y + p) % y
        del list1[y - k - 1:len(list1):y]
        k = p
    # print(list1)  ps:每次杀完人剩下的人
    return list1


if __name__ == "__main__":
    a = int(input("请输入参加游戏的人数:"))
    b = int(input("请输入杀死的数字:"))
    c = int(input("请输入幸存者人数:"))
    print(tao_tai(a, b, c))
