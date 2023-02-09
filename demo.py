import pymongo
import tkinter as tk
from tkinter import messagebox

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["enrollment_system"]
my_col = my_db["students"]

lst = [['ID','Name','Age','Email']]

def callback(event):
    li = []
    li = event.widget._values
    student_id.set(lst[li[1]][0])
    student_name.set(lst[li[1]][1])
    student_age.set(lst[li[1]][2])
    student_email.set(lst[li[1]][3])

def create_grid(n):
    lst.clear()
    lst.append(['ID', 'Name', 'Age', 'Email'])
    cursor = my_col.find({})
    for text_fromDB in cursor:
        student_id = str(text_fromDB["student_id"])
        student_name = str(text_fromDB["student_name"]).encode("utf-8").decode("utf-8")
        student_age = str(text_fromDB["student_age"]).encode("utf-8").decode("utf-8")
        student_email = str(text_fromDB["student_email"]).encode("utf-8").decode("utf-8")
        lst.append([student_id,student_name,student_age,student_email])
    
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            mgr_id = tk.Entry(window, width=10)
            mgr_id.insert(tk.END,lst[i][j])
            mgr_id._values = mgr_id.get() , i
            mgr_id.grid(row=i + 7,column=j + 6)
            mgr_id.bind("<Button-1>",callback)
    
    if n == 1:
        for label in window.grid_slaves():
            if int(label.grid_info()["row"]) > 6:
                label.grid_forget()


def msg_box(msg,title_bar):
    result=messagebox.askokcancel(title=title_bar,message=msg)
    return result

def save():
    # save 
    r = msg_box("save record ?","record")
    if r == True:
        new_id = my_col.count_documents({})
        if new_id != 0:
            new_id = my_col.find_one(sort=[("student_id",-1)])["student_id"]
        id = new_id + 1
        student_id.set(id)
        my_dict = {"student_id":int(student_id_.get()),"student_name":student_name_.get(),"student_age":student_age_.get(),"student_email":student_email_.get()}
        x = my_col.insert_one(my_dict)
        create_grid(1)
        create_grid(0)

def delete():
    # delete
    r = msg_box("Delete record ?", "record")
    if r == True:
        my_query = {"student_id":int(student_id_.get())}
        x = my_col.delete_one(my_query)
        create_grid(1)
        create_grid(0)

def update():
    # update
    # delete
    r = msg_box("Update record ?", "record")
    if r == True:
        my_query = {"student_id": int(student_id_.get())}
        new_values = {"$set" : {"student_name":student_name_.get()}}
        my_col.update_one(my_query, new_values)

        new_values = {"$set": {"student_age": student_age_.get()}}
        my_col.update_one(my_query, new_values)

        new_values = {"$set": {"student_email": student_email_.get()}}
        my_col.update_one(my_query, new_values)

        create_grid(1)
        create_grid(0)


window = tk.Tk()
window.title("Students Form")
window.geometry("1050x400")
window.configure(bg="gray")

label = tk.Label(window, text="CRUD | Student Enlistment Form", width=30 , height=1 ,bg="orange" ,anchor="center")
label.config(font={"courier",10})
label.grid(column=2,row=1)

label = tk.Label(window, text="Student ID:",width=10, height=1, bg="orange")
label.grid(column=1, row=2)
student_id=tk.StringVar()
student_id_=tk.Entry(window,textvariable=student_id)
student_id_.grid(column=2,row=2)
# student_id_.configure(state=tk.DISABLED)

label = tk.Label(window, text="Student Name:", width=10, height=1, bg="orange")
label.grid(column=1, row=3)
student_name = tk.StringVar()
student_name_ = tk.Entry(window, textvariable=student_name)
student_name_.grid(column=2, row=3)

label = tk.Label(window, text="Student Age:", width=10, height=1, bg="orange")
label.grid(column=1, row=5)
student_age = tk.StringVar()
student_age_ = tk.Entry(window, textvariable=student_age)
student_age_.grid(column=2, row=5)

label = tk.Label(window, text="Student Email:",width=10, height=1, bg="orange")
label.grid(column=1, row=4)
student_email = tk.StringVar()
student_email_ = tk.Entry(window, textvariable=student_email)
student_email_.grid(column=2, row=4)

create_grid(0) #create text field grid
save_btn = tk.Button(text="Save",command=save)
save_btn.grid(column=1,row=6)
save_btn = tk.Button(text="Delete",command=delete)
save_btn.grid(column=2,row=6)
save_btn = tk.Button(text="Update", command=update)
save_btn.grid(column=3, row=6)

window.mainloop()