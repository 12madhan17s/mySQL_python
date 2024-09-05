from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    passwd='mad_xpain10',
    user='root',
    database='baka'
    )


def insert(name,passwords,balance):
    res = con.cursor()
    sql = "insert into atm(UserName,passwords,balance) values(%s,%s,%s)"
    nam = (name,passwords,balance)
    res.execute(sql,nam)
    con.commit()
    print('data inserted successfully')


def select():
    res = con.cursor()
    res.execute("SELECT * FROM atm")

    users = res.fetchall()
    print(tabulate(users, headers=['Id','UserName','password','balance']))


def delete(id):
    res = con.cursor()
    sql = "delete from atm where Id= %s"
    nam = (id,)
    res.execute(sql,nam)
    con.commit()
    print('data deleted successfully')


def update(bal,pin):
    res = con.cursor()
    sql = "update atm set balance=%s where  passwords=%s"
    val = (bal,pin)
    res.execute(sql,val)
    con.commit()
    print('Data updated Successfully')

def u_balance(name,pas):
    res=con.cursor()
    sql = "select balance from atm where username=%s and passwords=%s"
    val = (name,pas)
    res.execute(sql,val)
    value = res.fetchall()
    print(tabulate(value,headers=['balance ']))


i = 0

while True:

    print("\n1 -- view all data\n"
          "2 -- insert data\n"
          "3 -- to update data\n"
          "4 -- your Balance\n"
          "5 -- to delete data \n"
          "6 -- to exit\n")
    i = int(input("Enter choice : "))
    if i == 1:
       select()
    elif i == 2:
        name = input('Enter name: ')
        password = int(input('Enter your password: '))
        balance = input('Enter the balance: ')
        insert(name,password,balance)
    elif i == 3:
        balance = input('Enter balance: ')

        password = int(input('Enter your password: '))

        update(balance,password)
    elif i == 4:
        name = input('Enter name: ')
        pas = int(input("Enter your password: "))
        u_balance(name,pas)
    elif i == 5:
        ids = input('Enter id: ')
        delete(ids)
    elif i == 6:
        quit()




