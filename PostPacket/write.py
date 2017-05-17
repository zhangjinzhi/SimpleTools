# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
import requests
import postpacketpayload as GetPostPacket

#功能:将BeautifulSoup解析得到的标题对象转换为一个列表
def get_plain_text(ResultSet):
    text = []
    for i in ResultSet:
        text.append(i.get_text().split()[0])
    return text

#读取数据，提取并清洗数据，最后装入user_information中
def select_data(page_source,Date,GroupType):
    user_information = []
    bsObj = BeautifulSoup(page_source,'html.parser')
    try:
        user_information_obj = bsObj.findAll('tr',style="background: #fff;")
    except Exception as e:
        print("No datas")
    else:
        for i,user_i in enumerate(user_information_obj):
            temp = []
            for td_i in user_i.findAll("td"):
                temp_data = td_i.get_text().split()
                if not temp_data:     #无数据
                    temp.append("-")
                else:
                    temp.append(temp_data[0])
            user_information.append(temp)

        columns = bsObj.findAll(style="padding-top: 1px;")
        columns_text = get_plain_text(columns)
        columns_text.insert(0,u'排名')

        page_now = int(bsObj.find('select',id="AspNetPager1_input").find('option',selected="true").get_text())

        df = pd.DataFrame(user_information,columns = columns_text) #使用pandas储存数据
        df.to_csv('file/'+GroupType+'/'+GroupType+'-'+Date+'-'+str(page_now)+'.csv',index=False) #每采集完一日的一组后，存储一次
        #df.to_csv('file/'+GroupType+'-'+Date+'-'+str(page_now)+'.csv',index=False) #每采集完一日的一组后，存储一次
    return "存储成功"

if __name__ == "__main__":
    Date = '2016-04-20'
    # GroupType = "QingLiangZu"
    GroupType = "ZhongLiangZu"
    url = "http://spds.qhrb.com.cn/SP10/SPOverSee1.aspx"
    WantedPage = 3
    payload = GetPostPacket.getGroupPayload(WantedPage,Date,GroupType)
    headers = GetPostPacket.getGroupHeaders(GroupType)
    response = requests.request("POST", url, data=payload, headers=headers)
    page_source = response.text
    result = select_data(page_source,Date,GroupType)
    print page_source
    print result