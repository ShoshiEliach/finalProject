

lock = False
num1=0
id1=""
def set_num_id(num, id):
    global num1, id1, lock

    if not lock:
        lock = True
        num1 = num
        id1 = id
        lock = False
def print_num_id():
    global num1, id1, lock
    if not lock:

        lock = True
        if(num1!=0):
            print(num1, ',', id1)
        lock = False

def print_num_id():
    print_num_id()