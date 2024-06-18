import re 
import datetime
import smtplib
def shopping_mall():
    f=open("mall.txt","r")
    print(f.read())
#regular expression
    f=open("hypermarket_store.txt","r")
    txt=f.read()
    your_store=input("Which store you want to explore: ")
    shop=re.search(your_store,txt)
    print(shop)
    if shop:
        print(f"Yes!! {your_store} is available in LuLu Hypermarket...")  
        if your_store=="Mobile Accessories Shop":
            print(f"Hello!! Welcome to {your_store}")
            print("***Mobile Models***\nApple iPhone\noppo reno\nVivo")
            iphone15_pro=134000
            oppo_reno10=50000
            vivo_x90=58000
        #regular expression
            f=open("mobile.txt","r")
            txt=f.read()
            your_mobile=input("Enter your mobile model: ")
            mobile=re.search(your_mobile,txt)
            print(mobile)
            if mobile:
                print(f"Yes!! {your_mobile} is available in  Mobile Accessories Store..")
            #exception handling
                try:
                    how_many=int(input(f"How many {your_mobile} you want: "))
                    iphone15_netprice=155000
                    oppo_netprice=58000
                    vivo_netprice=64000
                    if your_mobile=="iPhone15 Pro":
                        total=iphone15_pro*how_many
                        if total>=80000:
                            discount=total-20000
                        #gst calculation
                            gst=iphone15_netprice-iphone15_pro
                            gst_percent=((gst*100)/iphone15_pro)
                            print(f"You purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}")
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully...")
                                except:
                                    print("Mail not sent to customer")
                        else:
                            print(f"You purchased {how_many} {your_mobile} So your bill is {total}")
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_mobile} So your bill is {total}")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            print("Bill generated successfully")
                    elif your_mobile=="OPPO Reno 10":
                        total=oppo_reno10*how_many
                        if total>=80000:
                            discount=total-20000
                        #gst calculation
                            gst=oppo_netprice-oppo_reno10
                            gst_percent=((gst*100)/oppo_reno10)
                            print(f"You purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}")
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4b")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully")
                                except:
                                    print("Mail not sent to customer")  
                        else:
                            print(f"You purchased {how_many} {your_mobile} So your bill is {total}")
                        #gst calculation
                            gst=oppo_netprice-oppo_reno10
                            gst_percent=((gst*100)/oppo_reno10)
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_mobile} So your bill is {total}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_mobile} So your bill is {total}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully")
                                except:
                                    print("Mail not sent to customer")
                    elif your_mobile=="Vivo X90":
                        total=vivo_x90*how_many
                        if total>=80000:
                            discount=total-20000
                        #gst calculation
                            gst=vivo_netprice-vivo_x90
                            gst_percent=((gst*100)/vivo_x90)
                            print(f"You purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}")
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_mobile} for more than 80000, so your discount price is {discount}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully")
                                except:
                                    print("Mail not sent to customer")                                                    
                            print("Bill generated successfully")
                        else:
                            print(f"You purchased {how_many} {your_mobile} So your bill is {total}")
                        #gst calculation
                            gst=vivo_netprice-vivo_x90
                            gst_percent=((gst*100)/vivo_x90)
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_mobile} So your bill is {total}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_mobile}, so your bill is {total}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully")
                                except:
                                    print("Mail not sent to customer")
                except:
                    print("Please type numbers only...")
            else:
                print(f"Sorry!! {your_mobile} is not available in Mobile Accessories Store..")
        elif your_store=="Fashion and Lifestyle Shop":
            print(f"Hello!! Welcome to {your_store}")
            print("***Cloths and dress***\nDenim Shirt\nMen's Jacket")
            denim_shirt=1000
            mens_jacket=1600
        #regular expression
            f=open("cloth.txt","r")
            txt=f.read()
            your_dress=input("Enter your cloth name: ")
            cloth=re.search(your_dress,txt)
            print(cloth)
            if cloth:
                print(f"Yes!! {your_dress} is available in Fashion and Lifestyle Shop..")
            #exception handling
                try:
                    how_many=int(input(f"How many {your_dress} you want: "))
                    denim_netprice=1200
                    jacket_netprice=2000
                    if your_dress=="Denim Shirt":
                        total=denim_shirt*how_many
                        if total>=2000:
                            discount=total-200
                        #gst calculation
                            gst=denim_netprice-denim_shirt
                            gst_percent=((gst*100)/denim_shirt)
                            print(f"You purchased {how_many} {your_dress} for more than 2000 Rs, so your discount price is {discount}")
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_dress} for more than 2000 Rs, so your discount price is {discount}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_dress} for more than 2000 Rs, so your discount price is {discount}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully...")
                                except:
                                    print("Mail not sent to customer")                                                      
                        else:
                            print(f"You purchased {how_many} {your_dress}, so your bill is {total}")
                        #gst calculation
                            gst=denim_netprice-denim_shirt
                            gst_percent=((gst*100)/denim_shirt)
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_dress}, so your bill is {total}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_dress}, so your bill is {total}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfull...")
                                except:
                                    print("Mail not sent to customer")
                    elif your_dress=="Men's Jacket":
                        total=mens_jacket*how_many
                        if total>=2000:
                            discount=total-200
                        #gst calculation
                            gst=jacket_netprice-mens_jacket
                            gst_percent=((gst*100)/mens_jacket)
                            print(f"You purchased {how_many} {your_dress} for more than 2000 Rs, so your discount price is {discount}")
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_dress} for more than 2000 Rs, so your discount price is {discount}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4b")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_dress} for more than 2000 Rs, so your discount price is {discount}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully...")
                                except:
                                    print("Mail not sent to customer")                                                      
                        else:
                            print(f"You purchased {how_many} {your_dress}, so your bill is {total}")
                        #gst calculation
                            gst=jacket_netprice-mens_jacket
                            gst_percent=((gst*100)/mens_jacket)
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_dress}, so your bill is {total}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}") 
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4b")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_dress}, so your bill is {total}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully...")
                                except:
                                    print("Mail not sent to customer")
                except:
                    print("Please type number only..")   
            else:
                print(f"Sorry!! {your_dress} is not available in Fashion and Lifestyle Shop..")         
        elif your_store=="Groceries Section":   
            print(f"Hello!! Welcome to {your_store}")
            print("***Groceries Items***\nCoffee Powder\nAlmond Nuts")   
            coffee_powder=200
            almond_nut=800  
        #regular expression
            f=open("grocery.txt","r")
            txt=f.read()
            your_things=input("Enter your Grocery item: ")
            grocery=re.search(your_things,txt)
            print(grocery)  
            if grocery:
                print(f"Yes!! {your_things} is available in Groceries Section...")
            #exception handling
                try:
                    how_many=int(input(f"How many {your_things} you want: "))
                    coffee_netprice=240
                    almond_netprice=900
                    if your_things=="Coffee Powder":
                        total=coffee_powder*how_many
                        if total>=1000:
                            discount=total-150
                        #gst calculation
                            gst=coffee_netprice-coffee_powder
                            gst_percent=((gst*100)/coffee_powder)
                            print(f"You purchased {how_many} {your_things} for more than 1000 Rs, so your discount price is {discount}")
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_things} for more than 1000 Rs, so your discount price is {discount}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze dsfv jhgj fqw4")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_things} for more than 1000 Rs, so your discount price is {discount}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully...")
                                except:
                                    print("Mail not sent to customer")                                                      
                        else:
                            print(f"You purchased {how_many} {your_things}, so your bill is {total}")
                        #gst calculation
                            gst=coffee_netprice-coffee_powder
                            gst_percent=((gst*100)/coffee_powder)
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_things}, so your bill is {total}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtzj kwgf devt rvube")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_things}, so your bill is {total}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully...")
                                except:
                                    print("Mail not sent to customer")
                    elif your_things=="Almonds Nut":
                        total=almond_nut*how_many
                        if total>=1000:
                            discount=total-150
                        #gst calculation
                            gst=almond_netprice-almond_nut
                            gst_percent=((gst*100)/almond_nut)
                            print(f"You purchased {how_many}kg {your_things} for more than 1000 Rs, so your discount price is {discount}")
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many}kg {your_things} for more than 1000 Rs, so your discount price is {discount}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")                                                      
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtzjd kwgf devt rvubh")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_things} for more than 1000 Rs, so your discount price is {discount}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully...")
                                except:
                                    print("Mail not sent to customer")
                        else:
                            print(f"You purchased {how_many} {your_things}, so your bill is {total}")
                        #gst calculation
                            gst=almond_netprice-almond_nut
                            gst_percent=((gst*100)/almond_nut) 
                            print("GST for the product= ",end='')
                            print(round(gst_percent),end='')
                            print("%")
                        #datetime
                            x=datetime.datetime.now()
                            print(f"Bill generated at : {x}")
                            f=open("bill.txt","w")
                            f.write(f"You purchased {how_many} {your_things}, so your bill is {total}")
                            f=open("bill.txt","a")
                            f.write(f"\nGST for the product= {round(gst_percent)}%")
                            f=open("bill.txt","a")  
                            x=datetime.datetime.now()
                            f.write(f"\n\nBill generated at : {x}")
                            f.write("\n\n********Thanks for visiting LuLu Hypermarket********")
                        #mail sending
                            user=input("Enter your mail-id: ")
                            if user=="shaik112abdullah@gmail.com":
                                try: 
                                    receiver_mail=["shaik112abdullah@gmail.com"]
                                    for i in receiver_mail:
                                        s=smtplib.SMTP('smtp.gmail.com',587) 
                                        s.starttls()
                                        s.login("shaikh113abdullah@gmail.com","dtze kwgf decj jhub")
                                        message=f"----Your Bill Receipt----\n\n\nYou purchased {how_many} {your_things}, so your bill is {total}\nGST for the product= {round(gst_percent)}%\n\nBill generated at : {x}\n\n\n********Thanks for visiting LuLu Hypermarket********"
                                        s.sendmail("shaikh113abdullah@gmail.com",i,message) 
                                        s.quit()                                                  
                                        print("Bill generated to customer mail Successfully...")
                                except:
                                    print("Mail not sent to customer")
                except:
                    print("Please type number only..")
            else:
                print(f"Sorry!! {your_things} is not available in Groceries Section..")
    else:
        print(f"Sorry!! {your_store} is not available in LuLu Hypermarket...") 
#function calling
shopping_mall()


        