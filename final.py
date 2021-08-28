import re
import requests
import json
import time

from requests.api import request


TOKEN ="143401712:AAF-qnpfD2MxmZYFPQ819wCsypwVKvFJrSI"
# url="https://api.telegram.org/bot"+TOKEN

# reap=requests.get(url+"/getUpdates?offset=108730022")
bone_takhfif=["54CMLD","AB2323","24MN01","38L231","1q23A7"]
product = ["Xiaomi Redmi note 10 pro","Lg v60","HUAWEI Mate X2","Iphone 12 pro max","Samsung s20 ultra"]
product_validation = {
    "Xiaomi Redmi note 10 pro": 20000,
    "Lg v60":10000,
    "HUAWEI Mate x2":50000,
    "Iphone 12 pro max":120000,
    "Samsung s20 ultra":140000
}
back_keyboard='{"keyboard" : [["بازگشت"]], "resize_keyboard" : true}'
sabad_button='{"keyboard" : [["اعمال کد تخفیف","ثبت خرید"], ["بازگشت"]], "resize_keyboard" : true}'

def directory(chat_id, data=None):

    if data:
        f = open(str(chat_id) + '.txt', 'w+')
        f.write(data)
    else:
        f = open(str(chat_id) + '.txt', 'r+')
        return f.read()
    

validation = 0
select_product = None

def process_messages(update):

    global validation
    global select_product

    print("enter the first")
    chatID = update['chat']['id'] 
    dir = directory(chatID)
    print("this is the dir validation :",dir)


    # if update:
    #     print(update)
    #     return None
    if update['text'] == "/start" or update['text'] == "بازگشت":
        
        i=0
                
        print(chatID)
        keyboard = '{"keyboard":[["مشاهده محصولات","درباره ما"],["سبد خرید","شارژ کیف پول"]], "resize_keyboard" : true}'
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}&reply_markup={}".format(chatID,"welcome to this bot this is the online store bot test !\nto continue press one of the buttons :",keyboard))
        directory(chatID, 'None')
        return resp
        

    if update['text'] == "شارژ کیف پول":
        
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,"موجودی کیف پول شما : "+str(validation)+" می باشد"))                        
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}&reply_markup={}".format(chatID,"مبلغ مورد نظر را وارد کنید",back_keyboard))
        print("the validation is : ",validation)
        directory(chatID, 'sharj')
        return resp
        
    if dir == "sharj" :
        print("YES integer")
        validation = int(update['text'])
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,"کیف پول شما به مبلغ " + str(validation)+ "شارژ شد."))
        directory(chatID, 'None')
        return resp

    if update['text'] == "مشاهده محصولات":
        p_keyboard='{"keyboard":[["lg v60"],["Iphone 12 pro max"],["samsuns s20 ultra"],["Redmi note 10 pro","HUAWEI Mate X2"]], "resize_keyboard" : "true"}'
        # first product info :                   
        chatID = update['chat']['id'] 
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}&reply_markup={}".format(chatID,"Xiaomi Redmi note 10 pro",p_keyboard))
        photo = "https://www.hebergementwebs.com/image/c6/c623be63e3c5e6d38e53a9bee81f9895.jpg/[mayeso]-redmi-note-10-pro,-foni-yam'manja-yomwe-aliyense-adzagwere-29.jpg"
        resp = requests.get(url+"/sendPhoto?chat_id={}&photo={}".format(chatID,photo)) 
        with open('p1.txt',encoding="utf-8") as data:
            info = data.read()
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,info))    
        # print(info)    
                        
        # seccound product info :                   
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,"Samsung s20 ultra"))
        photo = "https://www.cnet.com/a/img/gLBzHrcclq8m-FJsfN1Pr4t89fw=/2020/02/08/9b0d9709-c758-42ac-8cfb-339a3f7174e0/samsung-galaxy-s20-ultra-apple-iphone-11-pro-max-camera-8351.jpg"
        resp = requests.get(url+"/sendPhoto?chat_id={}&photo={}".format(chatID,photo)) 
        with open('p2.txt',encoding="utf-8") as data:
            info = data.read()
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,info))    
        # print(info)    
                        
        # third product info :                   
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,"Iphone 12 pro max"))
        photo = "https://fdn.gsmarena.com/imgroot/reviews/20/apple-iphone-12-pro-max/lifestyle/-1200w5/gsmarena_008.jpg"
        resp = requests.get(url+"/sendPhoto?chat_id={}&photo={}".format(chatID,photo)) 
        with open('p3.txt',encoding="utf-8") as data:
            info=data.read()
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,info))    
        # print(info)    
                        
        # fourth product info :                   
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,"HUAWEI Mate X2"))
        photo = "https://www.teknoblog.com/wp-content/uploads/2021/02/huawei-nin-yeni-katlanabilir-telefonu-mate-x2-tanitildi-iste-tum-ozellikleri-7.jpg"
        resp = requests.get(url+"/sendPhoto?chat_id={}&photo={}".format(chatID,photo)) 
        with open('p4.txt',encoding="utf-8") as data:
            info = data.read()
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,info))    
        # print(info)    
                        
        # fiveth product info :                   
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,"Lg v60",))
        photo = "https://cdn.vox-cdn.com/thumbor/SkxgDSb_DbKJq8bhjPmPEUXobHM=/0x0:2040x1360/1200x675/filters:focal(918x520:1244x846)/cdn.vox-cdn.com/uploads/chorus_image/image/66377135/cwelch_200218_3910_0011.0.jpg"
        resp = requests.get(url+"/sendPhoto?chat_id={}&photo={}".format(chatID,photo)) 
        with open('p5.txt',encoding="utf-8") as data:
            info = data.read()
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,info))    
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}&reply_markup={}".format(chatID,"محصول مورد نظر را انتخاب کنید :",back_keyboard))   
        # finish the info of the products
        return resp
        
    if update['text'] == "درباره ما" :
        with open('text_about.txt',encoding="utf-8") as data:
            text_about = data.read()
        resp=requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,text_about))           
        return  resp


    if update['text'] == "سبد خرید":

        if select_product:
            text_shop = select_product + "محصول انتخابی شما :\n" + "قیمت :" + str(product_validation[select_product])
            resp=requests.get(url+"/sendMessage?chat_id={}&text={}&reply_markup={}".format(chatID,text_shop,sabad_button))
            return resp
        else:
            text_shop = "سبد خرید شما خالی است."
            resp=requests.get(url+"/sendMessage?chat_id={}&text={}&reply_markup={}".format(chatID,text_shop,sabad_button))
            return resp
    if update['text'] == "ثبت خرید":

        if validation >= int(product_validation[select_product]):
            validation=validation-product_validation[select_product]
            resp=requests.get(url +"/sendMessage?chat_id={}&text={}".format(chatID,".محصول با موفقیت ثبت گردید"))
            first_name=update['chat']['first_name']
            #last_name=update['chat']['last_name'] if update['chat']['last_name'] else ''
            ful_name=first_name#+last_name
            g = open(str(ful_name) + '.txt' ,'w+')
            text= " نام و نام خانوادگی : " +  ful_name +"\n نام محصول خریداری شده :" + select_product + "\n مبلغ پرداخت شده :" + str(product_validation[select_product]) + "\n با تشکر از خرید شما"
            g.write(text)
            with open(str(ful_name)+'.txt',encoding="utf-8") as d:
                i = d.read()
            resp = requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,i)) 
            return resp
        else:
            resp=requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,"موجودی کافی نمی باشد"))
            return resp

    if update['text'] == "اعمال کد تخفیف" :
        resp=requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID," :کد تخفیف خود را وارد کنید"))
        directory(chatID, 'takhfif')
        return resp

    if update['text'] and dir == 'takhfif':
        if update['text'] in bone_takhfif:
            product_validation[select_product]=product_validation[select_product]*70/100
            takhfif_text="کد تخفیف شما با موفقیت ثبت شد "
            resp=requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,takhfif_text))
            return directory(chatID, 'None')
        else:
            resp=requests.get(url+"/sendMessage?chat_id={}&text={}".format(chatID,".کد نامعتبر است"))
            return resp
                
    if update['text'] == product[0] or update['text'] == product[1] or update['text'] == product[2] or update['text'] == product[3] or update['text'] == product[4] :
        select_product = update['text']
        resp = requests.get(url+"/sendMessage?chat_id={}&text={}&reply_markup={}".format(chatID,select_product+"با موفقیت به سبد خرید اضافه شد ",back_keyboard))
        return resp
                    



last_id = 0

while True:
  
    print("IN THE NAME OF GOD")
    url = "https://api.telegram.org/bot"+TOKEN
    resp = requests.get(url+"/getUpdates?offset={}" + str(last_id + 1))
    resp = requests.get(url+"/getUpdates").json()
    resp = resp['result']

    if resp:
        print(last_id)
        for update in resp:
            if update['update_id'] > last_id:
                last_id = update['update_id']
                if 'message' in update:
                    process_messages(update['message'])
                else:
                    print(update)

                    
        
                    