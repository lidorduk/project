import mysql.connector
from cryptography.fernet import Fernet
import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="AmitHalperin12345",
    port='3306',
    database='projectsca'
)
mycursor = db.cursor()


def insert_rec_to_client_user_table(user_name, first_name, last_name, password):
    mycursor.execute('insert into client_user (user_name, first_name, last_name, password) values (%s,%s,%s,%s)', (user_name, first_name, last_name, password))
    db.commit()

def delete_rec_from_client_user_table(user_name_to_delete):
    mycursor.execute(f'''delete from client_user 
                         where user_name = "{user_name_to_delete}"''')
    db.commit()

def showing_password_of_specific_rec_client_user_table(user_name):
    mycursor.execute(f'select password from client_user where user_name like "{user_name}"')
    for x in mycursor:
        # print(x[0])
        # print(type(x[0]))   str
        return x[0]







def insert_rec_to_client_password_key_table(user_name, keyy):
    mycursor.execute('insert into client_password_key (user_name, keyy) values (%s,%s)', (user_name, keyy))
    db.commit()

def delete_rec_from_client_password_key_table(user_name_to_delete):
    mycursor.execute(f'''delete from client_password_key 
                         where user_name = "{user_name_to_delete}"''')
    db.commit()

def showing_key_of_specific_rec_client_password_key_table(user_name):
    mycursor.execute(f'select keyy from client_password_key where user_name like "{user_name}"')
    for x in mycursor:
        return x[0]






def insert_rec_to_client_table(user_name, client_socket):  # online clients
    mycursor.execute('insert into client (user_name, client_socket) values (%s,%s)', (user_name, client_socket))
    db.commit()

def delete_rec_from_client_table(client_socket_to_delete):
    mycursor.execute(f'''delete from client 
                         where client_socket = "{client_socket_to_delete}"''')
    db.commit()





def insert_rec_to_client_seeds_table(client_socket, public_key, modulo_pq, seed, setSeed_pad):  # online clients
    mycursor.execute('insert into client_seeds (client_socket, public_key, modulo_pq, seed, setSeed_pad) values (%s,%s,%s,%s,%s)', (client_socket, public_key, modulo_pq, seed, setSeed_pad))
    db.commit()

def delete_rec_from_client_seeds_table(client_socket_to_delete):
    mycursor.execute(f'''delete from client_seeds 
                         where client_socket = "{client_socket_to_delete}"''')
    db.commit()




def insert_rec_to_sus_msg_talking_room_table(user_name, msg):
    mycursor.execute('insert into sus_msg_talking_room (user_name, msg, date_time) values (%s,%s,%s)', (user_name, msg, str(datetime.datetime.now())[:-7]))
    db.commit()

def insert_rec_to_sus_msg_work_room_table(user_name, msg):
    mycursor.execute('insert into sus_msg_work_room (user_name, msg, date_time) values (%s,%s,%s)', (user_name, msg, str(datetime.datetime.now())[:-7]))
    db.commit()

def insert_rec_to_sus_msg_dating_room_table(user_name, msg):
    mycursor.execute('insert into sus_msg_dating_room (user_name, msg, date_time) values (%s,%s,%s)', (user_name, msg, str(datetime.datetime.now())[:-7]))
    db.commit()

def insert_sus_msg_to_specific_room(user_name, msg, room):
    if room == 'talking':
        insert_rec_to_sus_msg_talking_room_table(user_name, msg)
    elif room == 'work':
        insert_rec_to_sus_msg_work_room_table(user_name, msg)
    else:
        insert_rec_to_sus_msg_dating_room_table(user_name, msg)

def check_how_many_clients_are_online_and_how_many_accounts_in_db():
    message = ''
    mycursor.execute('select count(user_name) from client')
    for rec in mycursor:
        message += f'there is {mycursor[0][0]} clients right now '
    mycursor.execute('select count(user_name) from client_user')
    for rec in mycursor:
        message += f'and there is {mycursor[0][0]} accounts in the system.'
    print(message)


def insert_data_from_db_to_clients_users(clients_users):
    mycursor.execute('select * from client_user')
    for rec in mycursor:
        clients_users[rec[0]] = [rec[1], rec[2], rec[3]]  # (user_name, first_name, last_name, password)

# insert_rec_to_client_user_table('nutik', 'anat', 'lakus', 31002)
# insert_rec_to_client_user_table('niro', 'nir', 'golan', 987)



#mycursor.execute('select * from client_user')
#delete_rec_from_client_user_table('niro')

#for i in mycursor:
    #print(type(i))
    #print(i[0])




'''
key = Fernet.generate_key()
print(key)
print(type(key))
print(key.decode())
print(type(key.decode()))



#insert_rec_to_client_password_key_table('ddd', key.decode())
#delete_rec_from_client_password_key_table('ddd')
#k = showing_key_of_specific_rec_client_password_key_table('ddd').encode()

print(k)

print(type(k))

print(str(k))
'''

