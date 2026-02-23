# i wanna login as admin
from admin_features import create_trainer,create_batch,add_student,fetch_all_trainer,fetch_all_batche,fetch_all_student,fetch_t_b_data,fetch_t_s_data
from admin_login import admin_login
admin_login_status=admin_login()
print(admin_login_status,"8 main.py")

if admin_login_status:
    print("super admin login successfulyyyyyyyyyyyy.............")
    while True:
        print("""
           1. create trainer
           2. create batche
           3. create student
           4. fetch all trainer
           5. fetch all batche
           6. fetch all student
           7. fetch trainer + their batche data only
           8. fetch trainer + their student data only
        """)
        i=int(input("enetr yr choice here :--  "))
        if i== 1:
            t_n=input("enter t_name here :--- ")
            t_e=input("enter t_email here :--- ")
            t_ph=input("enter t_phnum  here :--- ")
            ad_id=int(input("enter ad_id  here :--- "))
            create_trainer(t_n,t_e,t_ph,ad_id)
        elif i== 2:
            b_n=input("enter b_name here :--- ")
            t_id=int(input("enter t_id here :--- "))
            ad_id=int(input("enter ad_id  here :--- "))
            create_batch(b_n,ad_id,t_id)  
        elif i == 3:
            s_n=input("enter s_name here :--- ")
            s_e=input("enter s_email here :--- ")
            s_ph=input("enter s_phNum  here :--- ")
            s_t_id=int(input("enter s_trainer_id  here :--- "))
            s_b_id=int(input("enter s_batch_id  here :--- "))
            s_a_id=int(input("enter s_admin_id  here :--- "))
            add_student(s_n,s_e,s_ph,s_t_id,s_b_id,s_a_id)
        elif i == 4:
            fetch_all_trainer()
        elif i == 5:
            fetch_all_batche()    
        elif i ==6:
            fetch_all_student()
        elif i ==7 :
            t_id=int(input("enter trainer id to get all his data with his batche data"))    
            fetch_t_b_data(t_id)
        elif i == 8:
            t_id=int(input("enter trainer id to get all his data with his batche data"))    
            fetch_t_s_data(t_id)

else:
    print("not valid admin")