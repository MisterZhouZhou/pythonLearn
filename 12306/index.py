#!/usr/bin/env python
# -*- coding: utf-8 -*-

from splinter import Browser
from time import sleep
import sys

class BrushTicket(object):
    """买票类及实现方法"""
    def __init__(self, passengers, from_time, from_station, to_station, number_seat):
        """定义实例属性，初始化"""
        # 乘客姓名
        self.passengers = passengers
        # 起始站和终点站
        self.from_station = from_station
        self.to_station = to_station
        # 乘车日期
        self.from_time = from_time
        # 车次 - 座位 dict
        num_seat_dic = {}
        for num_seat in number_seat:
            use = num_seat.split(':')
            num = use[0]
            seats = use[1]
            seats_use = seats.split(',')
            seat_str = ''
            for seat in seats_use:
                # 座位类型所在td位置
                if seat == '商务座特等座':
                    seat_type_index = 1
                    seat_type_value = 9
                elif seat == '一等座':
                    seat_type_index = 2
                    seat_type_value = 'M'
                elif seat == '二等座':
                    seat_type_index = 3
                    seat_type_value = 0
                elif seat == '高级软卧':
                    seat_type_index = 4
                    seat_type_value = 6
                elif seat == '软卧':
                    seat_type_index = 5
                    seat_type_value = 4
                elif seat == '动卧':
                    seat_type_index = 6
                    seat_type_value = 'F'
                elif seat == '硬卧':
                    seat_type_index = 7
                    seat_type_value = 3
                elif seat == '软座':
                    seat_type_index = 8
                    seat_type_value = 2
                elif seat == '硬座':
                    seat_type_index = 9
                    seat_type_value = 1
                elif seat == '无座':
                    seat_type_index = 10
                    seat_type_value = 1
                elif seat == '其他':
                    seat_type_index = 11
                    seat_type_value = 1
                else:
                    seat_type_index = 7
                    seat_type_value = 3
                seat_str += (str(seat_type_index) + '-' + str(seat_type_value) + ',')
            num_seat_dic[num] = seat_str
        self.num_seat_dic = num_seat_dic
        # 新版12306官网主要页面网址
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.init_my_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        # 浏览器驱动信息，驱动下载页：https://sites.google.com/a/chromium.org/chromedriver/downloads
        self.driver_name = 'chrome'
        self.driver = Browser("chrome")
        # self.driver = ChromeWebDriver("chrome")
    def do_login(self):
        """登录功能实现，手动识别验证码进行登录"""
        self.driver.visit(self.login_url)
        sleep(1)
        # 选择登陆方式登陆
        print('请扫码登陆或者账号登陆……')
        while True:
            if self.driver.url != self.init_my_url:
                sleep(1)
            else:
                break
    def start_brush(self):
        """买票功能实现"""
        # 浏览器窗口最大化
        self.driver.driver.maximize_window()
        # 登陆
        self.do_login()
        # 跳转到抢票页面
        self.driver.visit(self.ticket_url)
        try:
            print('开始刷票……')
            # 加载车票查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.from_station})
            self.driver.cookies.add({"_jc_save_toStation": self.to_station})
            self.driver.cookies.add({"_jc_save_fromDate": self.from_time})
            self.driver.reload()
            count = 0
            while self.driver.url == self.ticket_url:
                self.driver.find_by_text('查询').click()
                sleep(1)
                count += 1
                print('第%d次点击查询……' % count)
                if count % 50 == 0:
                    self.driver.find_by_id('login_user').click()
                    sleep(1)
                    self.driver.visit(self.ticket_url)
                    sleep(1)
                    print('继续刷票......')
                    # 加载车票查询信息
                    self.driver.cookies.add({"_jc_save_fromStation": self.from_station})
                    self.driver.cookies.add({"_jc_save_toStation": self.to_station})
                    self.driver.cookies.add({"_jc_save_fromDate": self.from_time})
                    self.driver.reload()
                    if self.driver.url == self.ticket_url:
                        continue
                try:
                    # 多车次处理
                    for bander in self.num_seat_dic.keys():
                        current_tr = self.driver.find_by_xpath('//tr[@datatran="' + bander + '"]/preceding-sibling::tr[1]')
                        if current_tr:
                            # 多座次处理
                            seat_value = self.num_seat_dic[bander]
                            seat_split = seat_value.split(',')
                            for seat in seat_split:
                                if seat:
                                    seat_type = seat.split('-')
                                    seat_type_index = int(seat_type[0])
                                    seat_type_value = int(seat_type[1])
                                    if current_tr.find_by_tag('td')[seat_type_index].text == '--':
                                        print(bander + ' 还未出售')
                                        sleep(1)
                                    elif current_tr.find_by_tag('td')[seat_type_index].text == '无':
                                        print(bander + ' 无票，继续尝试……')
                                        sleep(1)
                                    else:
                                        # 有票，尝试预订
                                        print(bander + ' 刷到票了（余票数：' + str(
                                            current_tr.find_by_tag('td')[seat_type_index].text) + '），开始尝试预订……')
                                        current_tr.find_by_css('td.no-br>a')[0].click()
                                        print(current_tr)
                                        sleep(1)
                                        key_value = 1

                                        for p in self.passengers:
                                            # 选择用户
                                            print('开始选择用户……')
                                            self.driver.find_by_text(p).last.click()
                                            # 选择座位类型
                                            print('开始选择席别……')
                                            if seat_type_value != 0:
                                                self.driver.find_by_xpath(
                                                    "//select[@id='seatType_" + str(key_value) + "']/option[@value='" + str(
                                                        seat_type_value) + "']").first.click()
                                            key_value += 1
                                            sleep(0.2)
                                            if p[-1] == ')':
                                                self.driver.find_by_id('dialog_xsertcj_ok').click()
                                        print('正在提交订单……')
                                        '''
                                        self.driver.find_by_id('submitOrder_id').click()
                                        sleep(2)
                                        # 查看放回结果是否正常
                                        submit_false_info = self.driver.find_by_id('orderResultInfo_id')[0].text
                                        if submit_false_info != '':
                                            print(submit_false_info)
                                            self.driver.find_by_id('qr_closeTranforDialog_id').click()
                                            sleep(0.2)
                                            self.driver.find_by_id('preStep_id').click()
                                            sleep(0.3)
                                            continue
                                        print('正在确认订单……')
                                        self.driver.find_by_id('qr_submit_id').click()
                                        '''
                                        print('预订成功，请及时前往支付……')
                        else:
                            # print('不存在当前车次【%s】，已结束当前刷票，请重新开启！' % self.number)
                            print('不存在当前车次，已结束当前刷票，请重新开启！')
                            sys.exit(1)
                except Exception as error_info:
                    print(error_info)
        except Exception as error_info:
            print(error_info)
if __name__ == '__main__':
    # nya
    passengers=['周巍'] # 用户名
    from_time='2019-07-13' # 出发日期
    from_station='%u4E0A%u6D77%2CSHH'  # 起始站点 - 来自12306 余票查询 请求 - cookie （此处 - 上海）
    to_station='%u6C11%u6743%2CMQF' # 结束站点 （此处 - 民权）
    number_seat=['K152:硬座,无座','K4916:硬座,无座'] # 车次：座位类型
    # 开始抢票
    ticket = BrushTicket(passengers, from_time, from_station, to_station, number_seat)
    ticket.start_brush()