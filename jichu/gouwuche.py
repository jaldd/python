# -*- coding:utf-8 -*-
# Author:Dan Li

product_list=[
    ('Iphone',5800),
    ('Mac pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('aa',100)
]
shopping_list=[]
salary=input("please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        # for item in product_list:
        #     print(product_list.index(item),item)
        for index,item in enumerate(product_list):
            print(index,item);
        user_choice=input("did you want it:")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(product_list) and user_choice>=0:
                p_item=product_list[user_choice]
                if p_item[1]<=salary:
                    shopping_list.append(p_item);
                    salary-=p_item[1];
                    print("append %s,your banlance is \033[31;1m%s\033[0m" %(p_item,salary));
                else:
                    print("\033[41;1m余额[%s]\033[0m" %salary)
            else:
                print("%s not exists" %(user_choice))
        elif user_choice=='q':
            print('your shopping list')
            for p in shopping_list:
                print(p)
            print("balance:",salary)
            exit()
        else:
            print('invalid option')

