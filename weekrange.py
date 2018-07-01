import time

# week_time = time.strftime('%w')
# print('周日', week_time)
# start_week = 3
# end_week = 0
# if week_time in range(start_week,end_week+1):
#     print('yes')



def in_time_range(s):
    """
    输入每周几到周几的时间段区间，判断当前日期是否在区间内，是的返回true，否的返回false
    :param 'week1 00:13*1 00:14': 
    :return: 
    """
    now = time.localtime(time.time())
    # 当前星期几
    now_w = str(time.strftime('%w',now))

    now_h = str(time.strftime('%H',now))
    now_m = str(time.strftime('%M',now))
    print('now',now_w, now_h, now_m)

    s1 = s.replace('week', '')
    print(s1)
    s_list = s1.split('*')
    print(s_list)

    s_time = s_list[0]
    s_time = s_time.replace(':', ' ')
    s_w = s_time[0]
    s_h = s_time[2:4]
    s_m = s_time[5:7]
    print('s',s_w,s_h,s_m)
    e_time = s_list[1]
    e_time = e_time.replace(':', ' ')
    e_w = e_time[0]
    e_h = e_time[2:4]
    e_m = e_time[5:7]
    print('e',e_w,e_h,e_m)
    if s_w < now_w <= e_w:
        return True
    elif s_w == now_w:
        if s_h < now_h:
            return True
        elif s_h == now_h:
            if s_m <= now_m<=e_m :
                return True
            else:
                return False
        else:
            return False
    else:
        return False
if __name__ == '__main__':

    ss = 'week1 00:13*1 00:14'
    print(in_time_range(ss))
