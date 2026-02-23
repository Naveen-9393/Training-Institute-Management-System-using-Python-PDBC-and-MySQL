
from db_c import curObj,conn
def create_trainer(n,e,ph,a_id):
    q="insert into trainer (t_name,t_email,t_ph,admin_id) values (%s,%s,%s,%s)"
    curObj.execute(q,(n,e,ph,a_id))
    conn.commit()
    print("trainer add successfullyyy.....")

def create_batch(a,b,c):
    q="insert into batche (b_name,admin_id,trainer_id) values (%s,%s,%s)"
    curObj.execute(q,(a,b,c))
    conn.commit()
    print("batch added successfullyyy.....")

def add_student(a,b,c,d,e,f):
    q="insert into student (s_name,s_email,s_phnum,s_t_id,s_b_id,s_a_id) values (%s,%s,%s,%s,%s,%s)"
    curObj.execute(q,(a,b,c,d,e,f))
    conn.commit()
    print("student added successfullyyy.....")

def fetch_all_trainer():
    query="select * from trainer"
    curObj.execute(query)
    data=curObj.fetchall()
    print(data)
    print("fethed all tranier data")

def fetch_all_batche():
    query="select * from batche"
    curObj.execute(query)
    data=curObj.fetchall()
    print(data)
    print("fethed all batche data")
    
def fetch_all_student():
    query="select * from student"
    curObj.execute(query)
    data=curObj.fetchall()
    print(data)
    print("fethed all student data")    
        
def fetch_t_b_data(id):
    query="""
             select t_id,t_name,t_email,b_id,b_name
             from trainer 
             inner join batche
             on trainer.t_id = batche.trainer_id
             where trainer.t_id =%s
    """
    curObj.execute(query,(id,))
    data=curObj.fetchall()
    print(data)
    print("trainer+batch data fetched successfully........")


def fetch_t_s_data(id):
    query="""
             select t_id,t_name,t_email,s_name,s_email,s_b_id
             from trainer 
             right join student
             on trainer.t_id = student.s_t_id
             where trainer.t_id =%s
    """
    curObj.execute(query,(id,))
    data=curObj.fetchall()
    print(data)
    print("trainer+student data fetched successfully........")
