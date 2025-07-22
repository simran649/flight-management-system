# PROJECT ON FLIGHT MANAGEMENT SYSTEM
# BY SIMRAN SINGH
# OF CLASS 12th-A
# ROLL NO.: 36
# PROJECT SUBMITTED TO:
#                      MRS. SANGEETA PAL

import mysql.connector as sqltor
obj = sqltor.connect(host='localhost', user='root', password='accio')
# here obj is connection object

# checking if the connection is established
if obj.is_connected()==False:
    print('Error connecting to MySQL')

# creating cursor instance
mycursor=obj.cursor()

# creating database
mycursor.execute("create database if not exists airlines")
mycursor.execute("use airlines")


# creating table for ordering food
mycursor.execute('''create table if not exists food_items(food_id int(4) auto_increment primary key,
                  food_name varchar(40) not null, price int(4) not null )''')
mycursor.execute('''INSERT INTO food_items(food_id, food_name, price)
                 VALUES
                 (1, "pepsi", 150),
                 (2, "coffee", 70),
                 (3, "tea", 50),
                 (4, "water", 60),
                 (5, "milk shake", 80),
                 (6, "chicken burger", 160),
                 (7, "cheeze pizza", 70),
                 (8, "chicken biryani", 300),
                 (9, "plain rice", 80),
                 (10, "aloo paratha", 120),
                 (11, "roti sabji", 100),
                 (12, "omlette", 50)
                 ON DUPLICATE KEY UPDATE 
                 food_name=VALUES(food_name),
                 price=VALUES(price)''')


# creating table for luggage entry
mycursor.execute('''create table if not exists luggage(luggage_id int(4) auto_increment primary key, 
                 luggage_weight int(3) not null, price int(5) not null)''')


# creating table for class details
mycursor.execute('''create table if not exists class_details(class_id int(4) auto_increment primary key,
                 class_type varchar(40) not null, price int(5) not null)''')
mycursor.execute('''INSERT INTO class_details(class_id ,class_type, price)
                 VALUES
                 (1, "economy", 2000),
                 (2, "premium economy", 4000),
                 (3, "business", 6000),
                 (4, "first class", 8000)
                 ON DUPLICATE KEY UPDATE
                 class_type=VALUES(class_type),
                 price=VALUES(price)''')


# creating table for customer details
mycursor.execute('''create table if not exists customer_details(cus_id int(5) auto_increment primary key,
                 cus_name varchar(40) not null, mob_no bigint(10) not null, fl_id int(4) not null,
                 fl_name varchar(40) not null, class varchar(40) not null, dept varchar(40) not null,
                 dest varchar(40) not null, day varchar(40) not null,
                 f_time time not null, price int(6) not null) ''')


# creating table for flight details
mycursor.execute('''create table if not exists flight_details(flight_id int(5) auto_increment primary key,
                 flight_name varchar(40), departure varchar(40), destination varchar(40), day varchar(40),
                 f_time time, economy int(4), premium_economy int(3), business int(3),
                 first_class int(3))''')
mycursor.execute('''INSERT INTO flight_details(flight_id, flight_name, departure, destination, 
                day, f_time, economy, premium_economy, business, first_class)
                VALUES
                (1, 'spice jet', 'Delhi', 'Mumbai', 'Sunday', '04:00', 1010, 1000, 800, 500),
                (2, 'go first', 'haryana', 'goa', 'tuesday', '16:30', 1010, 800, 800, 300),
                (3, 'vistara', 'new delhi', 'paris', 'wednesday', '15:00', 1010, 1000, 800, 500),
                (4, 'indigo', 'chandigarh', 'tokyo', 'thursday', '16:45', 900, 800, 500, 300),
                (5, 'air india', 'guwahati', 'kolkata', 'monday', '06:00', 1010, 900, 800, 300)
                ON DUPLICATE KEY UPDATE
                flight_name=VALUES(flight_name),
                departure=VALUES(departure),
                destination=VALUES(destination),
                day=VALUES(day),
                f_time=VALUES(f_time),
                economy=VALUES(economy),
                premium_economy=VALUES(premium_economy),
                business=VALUES(business),
                first_class=VALUES(first_class)''')

obj.commit()
# commit() saves the changes to the database


#to enter the details of luggage
def luggage():
    while True:
        print(" ")
        print("What do you want to do?")
        print(" ")
        print("1.  Add Luggage")
        print("2.  Delete Luggage")
        print("3.  Exit")
        print(" ")
        x=int(input('Enter your choice: '))
        if x==1:
            print(" ")
            lweight=int(input("Enter weight of your luggage (in kg): "))
            lprice= 350*lweight
            print(" ")
            print(f"the price of {lweight}kg of your luggage would be: Rs {lprice}")
            sql='''INSERT INTO luggage(luggage_weight, price)
                   VALUES(%s, %s)'''
            values=(lweight, lprice)
            mycursor.execute(sql, values)
            obj.commit()
        elif x==2:
            print(" ")
            lid=int(input("Enter your luggage id: "))
            sql='''DELETE FROM luggage 
                   WHERE luggage_id= %s'''
            values=(lid,)
            mycursor.execute(sql, values)
            obj.commit()
        elif x==3:
            break
        else:
            print("*********************PLEASE ENTER A VALID OPTION FROM 1 AND 2********************")
            luggage()
obj.commit()


#to update the information of table food_items
def food():
    while True:
        print(" ")
        print("What do you want to do?")
        print("1.  Add new items")
        print("2.  Update price")
        print("3.  Delete items")
        print("4.  Exit")
        print(" ")
        x=int(input("Enter your choice: "))
        if x==1:
            print(" ")
            fname=input("Enter food name: ")
            fprice=input("Enter food price: ")
            sql= '''INSERT INTO food_items(food_name, price)
                    VALUES(%s, %s)'''
            values=(fname, fprice)
            mycursor.execute(sql, values)
            obj.commit()
        elif x==2:
            print(" ")
            fid=int(input("Enter food id: "))
            fprice=int(input("Enter new price: "))
            sql='''UPDATE food_items
                   SET price=%s
                   WHERE food_id=%s'''
            values=(fprice, fid)
            mycursor.execute(sql, values)
        elif x==3:
            print(" ")
            fid=int(input("Enter the id of food which you want to delete from the menu: "))
            sql='''DELETE FROM food_items
                   WHERE food_id=%s'''
            values=(fid,)                 #since the values must be a tuple
            mycursor.execute(sql, values)
            obj.commit()
        elif x==4:
            break
        else:
            print("******************** PLEASE ENTER A VALID OPTION FROM 1, 2, 3 AND 4 ********************")
            food()
obj.commit()


#to update the information of class type
def classtype():
    while True:
        print(" ")
        print("What do you want to change ?")
        print("1.  Change the class type name")
        print("2.  Change the price of class type")
        print("3.  Exit")
        print(" ")
        x=int(input("Enter your choice: "))
        if x==1:
            print(" ")
            oname=input("Enter old name: ")
            nname=input("Enter new name: ")
            sql= '''UPDATE class_details
                    SET class_name= %s
                    WHERE class_type= %s'''
            values= (nname, oname)
            mycursor.execute(sql, values)
            obj.commit()
        elif x==2:
            print(" ")
            ctype=input("Enter class type: ")
            cprice=int(input("Enter updated price: "))
            sql= '''UPDATE class_details
                    SET price= %s
                    WHERE class_type= %s'''
            values= (cprice, ctype)
            mycursor.execute(sql, values)
            obj.commit()
        elif x==3:
            break
        else:
            print("********************PLEASE ENTER A VALID OPTION FROM 1 AND 2********************")
            classtype()
obj.commit()


#to see the available food items in menu
def fooditems():
    print(" ")
    print(" ")
    print("********************THE AVAILABLE FOOD ITEMS ARE********************")
    print(" ")
    print(" ")
    mycursor.execute("SELECT * FROM food_items")
    x=mycursor.fetchall()
    for i in x:
        print("Food id: ", i[0])
        print("Food name: ", i[1])
        print("Price: ",i[2])
        print(" ")
        

#admin interface after verifying password
def admin1():
    while True:
        print("********************WHAT ARE YOU WORKING ON TODAY ?********************")
        print(" ")
        print("1.  Update details")
        print("2.  Access details")
        print("3.  Exit")
        print(" ")
        x=int(input("Select your choice: "))
        if x==1:
            print(" ")
            print("which table do you want to update?")
            print("1.  Class Type")
            print("2.  Food")
            print("3.  Luggage")
            print(" ")
            x1=int(input("Select your choice: "))
            if x1==1:
                classtype()
            elif x1==2:
                food()
            elif x1==3:
                luggage()
            else:
                print("********************PLEASE ENTER A VALID OPTION********************")
                admin1()
        elif x==2:
            print(" ")
            print("1. class_details")
            print("2. food_items")
            print("3. luggage")
            print("4. customer_details")
            print(" ")
            y=int(input("From which table?: "))
            if y==1:
                print(" ")
                mycursor.execute("SELECT * FROM class_details")
                y1=mycursor.fetchall()
                for i in y1:
                    print("Class id : ", i[0])
                    print("Class type: ", i[1])
                    print("Price: ", i[2])
                    print(" ")
            elif y==2:
                print(" ")
                fooditems()
            elif y==3:
                print(" ")
                mycursor.execute("SELECT * FROM luggage")
                y2=mycursor.fetchall()
                for i in y2:
                    print("Luggage id: ", i[0])
                    print("Lugage weight :", i[1])
                    print("Price: ", i[2])
                    print(" ")
            elif y==4:
                print(" ")
                mycursor.execute("SELECT * FROM customer_details")
                y3= mycursor.fetchall()
                for i in y3:
                    print("Customer id: ", i[0])
                    print("Customer name: ", i[1])
                    print("Mobile no.: ", i[2])
                    print("Flight id: ", i[3])
                    print("Flight name: ", i[4])
                    print("Class: ", i[5])
                    print("Departure place: ", i[6])
                    print("Destination place: ", i[7])
                    print("Day: ", i[8])
                    print("Flight time: ", i[9])
                    print("Price: ", i[10])
                    print(" ")
        elif x==3:
            exit()
        else:
            ("********************PLEASE ENTER A VALID OPTION FROM 1, 2, AND 3********************")
            admin1()
obj.commit()


#admin interface
def admin():
    while True:
        sec=input("Enter your password: ")
        if sec=="accio":
            admin1()
            break
        else:
            print("********************YOUR PASSWORD IS INCORRECT********************")
            print("*************************PLEASE TRY AGAIN*************************")
            admin()
        
#to see the record of the customer
def record():
    cid=int(input("Enter your customer id: "))
    sql= '''SELECT * FROM customer_details
            WHERE cus_id= %s'''
    values= (cid,)
    mycursor.execute(sql, values)
    records=mycursor.fetchall()

    #checks if any records were found where cus_id=cid
    if records:                 
        record=records[0]
        print("********************YOUR DETAILS ARE HERE********************")
        print(" ")
        print("customer id: ", record[0])
        print("name: ", record[1])
        print("mobile number: ", record[2])
        print("flight id: ", record[3])
        print("flight name: ", record[4])
        print("classtype: ", record[5])
        print("departure place:", record[6])
        print("destination: ", record[7])
        print("day: ", record[8])
        print("flight time: ", record[9])
        print("price of ticket: ", record[10])
    else:
        print("No records found for the given customer id.")


#to book the tickets
def ticketbooking():
    from datetime import datetime
    cname=input("Enter your name: ")
    cmob=int(input("Enter your mobile number: "))
    if cmob==0000000000:
        print("Mobile number can't be null")
        ticketbooking()
    fid=int(input("Enter flight id: "))
    fname=input("Enter flight name: ")
    fdept=input("Enter departure place: ")
    fdest=input("Enter destination: ")
    #fdate=input("Enter the date (YYYY-MM-DD): ")
    #ffdate=datetime.strptime(fdate, "%Y-%m-%d").date()
    fday=input("enter the day: ")
    ftime=input("enter flight time (HH:MM): ")
    time=datetime.strptime(ftime, "%H:%M").time()
    print(" ")
    print("we have the following class types available:")
    print("1. Economy")
    print("2. Premium Economy")
    print("3. Business")
    print("4. First class")
    print(" ") 
    while True:
        fclass=input("name the classtype you want to travel in: ")
        sql= '''SELECT price FROM class_details
                WHERE class_type= %s'''
        values= (fclass,)
        mycursor.execute(sql, values)
        result=mycursor.fetchone()
        if result:
            fprice=result[0]
            print(f"the price for {fclass} class is: {fprice}")
            break
        else:
            print("********************NO SUCH CLASS EXISTS IN HERE********************")
            ticketbooking()
    
    sql='''INSERT INTO customer_details(cus_name, mob_no, fl_id,
           fl_name, class, dept, dest, day, f_time, price)
           VALUES
           (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    values= (cname, cmob, fid, fname, fclass, fdept, fdest, fday, time, fprice)
    mycursor.execute(sql, values)
    obj.commit()


#to see the available flights
def flightavailable():
    print(" ")
    print(" ")
    print("********************THE AVIALBLE FLIGHTS ARE:********************")
    print(" ")
    print(" ")
    mycursor.execute("SELECT * FROM flight_details")
    x=mycursor.fetchall()
    for i in x:
        print(" ")
        print("flight id: ", i[0])
        print("flight name: ", i[1])
        print("departure: ", i[2])
        print("destination: ", i[3])
        print("take off day: ", i[4])
        print("take off time: ", i[5])
        print("no. of seats in economy: ", i[6])
        print("no. of seats in premium economy: ", i[7])
        print("no. of seats in business class: ", i[8])
        print("no. of seats in first class: ", i[9])
        print(" ")
    print("______________________________________________________________________________________________")


#user interface
def user():
    while True:
        print("******************** HOW MAY I HELP YOU? ********************")
        print(" ")
        print("1.  Flight details")
        print("2.  Food details")
        print("3.  Book tickets")
        print("4.  My details")
        print("5.  Exit")
        print(" ")
        x=int(input("Enter your choice: "))
        if x==1:
            flightavailable()
        elif x==2:
            fooditems()
        elif x==3:
            ticketbooking()
        elif x==4:
            record()
        elif x==5:
            print(" ")
            print(" ")
            print("******************** HAPPY TO SERVE YOU ********************")
            print(" ")
            break
        else:
            print("******************** PLEASE ENTER A VALID OPTION ********************")
            print(" ")
        

#main interface
def identity():
    print("******************** YOUR DESIGNATION? ********************")
    print(" ")
    print("1.  Admin")
    print("2.  User")
    print("3.  Exit")
    x=int(input("Enter your option: "))
    while True:
        if x==1:
            admin()
        elif x==2:
            user()
        elif x==3:
            exit()
        else:
            print("******************** PLEASE ENTER A VALID OPTION ********************")
            identity()

identity()
mycursor.close()
obj.close()
