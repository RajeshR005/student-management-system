import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkfont


try:
    with open('studentmanagement.json', 'r') as f:
        data1 = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data1 = []


def save_data():
    with open('studentmanagement.json', 'w') as f:
        json.dump(data1, f, indent=3)


def add_student():
    name = simpledialog.askstring("➕ Add Student", "Enter student name:")
    age = simpledialog.askinteger("➕ Add Student", "Enter student age:")
    location = simpledialog.askstring("➕ Add Student", "Enter student location:")

    if name and age and location:
        data1.append({'name': name, 'Age': age, 'location': location})
        save_data()
        messagebox.showinfo("Success", f"🎉 Student '{name}' Added Successfully!")
    else:
        messagebox.showwarning("Incomplete", "Please fill all fields.")


def view_students():
    if data1:
        students = "\n\n".join([f"👤 Name: {i['name']}\n🎂 Age: {i['Age']}\n📍 Location: {i['location']}" for i in data1])
        messagebox.showinfo("📚 Student Records", students)
    else:
        messagebox.showinfo("📚 Student Records", "No student records found.")


def search_student():
    search_name = simpledialog.askstring("🔍 Search Student", "Enter student name:").lower()
    results = [i for i in data1 if search_name in i['name'].lower()]
    if results:
        students = "\n\n".join([f"👤 Name: {i['name']}\n🎂 Age: {i['Age']}\n📍 Location: {i['location']}" for i in results])
        messagebox.showinfo("🔎 Search Results", students)
    else:
        messagebox.showinfo("🔎 Search Results", "No matching student found.")


def update_student():
    search_name = simpledialog.askstring("✏️ Update Student", "Enter student name:").lower()
    for i in data1:
        if i['name'].lower() == search_name:
            field = simpledialog.askinteger("✏️ Update Field", "Select field to update:\n1️⃣ Name\n2️⃣ Age\n3️⃣ Location")
            if field == 1:
                new_name = simpledialog.askstring("Update Name", "Enter new name:")
                i['name'] = new_name
            elif field == 2:
                new_age = simpledialog.askinteger("Update Age", "Enter new age:")
                i['Age'] = new_age
            elif field == 3:
                new_location = simpledialog.askstring("Update Location", "Enter new location:")
                i['location'] = new_location
            else:
                messagebox.showerror("Error", "❗ Invalid field number.")
                return
            save_data()
            messagebox.showinfo("Success", "✅ Student updated successfully!")
            return
    messagebox.showinfo("Update", "❌ No matching student found.")


def delete_student():
    search_name = simpledialog.askstring("❌ Delete Student", "Enter student name to delete:").lower()
    for i in data1:
        if i['name'].lower() == search_name:
            confirm = messagebox.askyesno("⚠️ Confirm Delete", f"Are you sure you want to delete '{i['name']}'?")
            if confirm:
                data1.remove(i)
                save_data()
                messagebox.showinfo("Deleted", "🗑️ Student deleted successfully!")
            return
    messagebox.showinfo("Delete", "❌ No matching student found.")


def confirm_exit():
    if messagebox.askokcancel("Exit", "Do you really want to quit? 🥺"):
        root.destroy()


root = tk.Tk()
root.title("🎓 Student Management System")
root.geometry("500x600")
root.configure(bg="#f0f2f5")

header_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

header = tk.Label(root, text="Student Management System", bg="#f0f2f5", fg="#333", font=header_font)
header.pack(pady=20)

button_style = {
    "width": 25,
    "height": 2,
    "bg": "#4CAF50",
    "fg": "white",
    "font": button_font,
    "bd": 0,
    "activebackground": "#45a049"
}

exit_button_style = button_style.copy()
exit_button_style["bg"] = "#f44336"
exit_button_style["activebackground"] = "#e53935"

tk.Button(root, text="➕ Add Student", command=add_student, **button_style).pack(pady=10)
tk.Button(root, text="👀 View All Students", command=view_students, **button_style).pack(pady=10)
tk.Button(root, text="🔍 Search Student", command=search_student, **button_style).pack(pady=10)
tk.Button(root, text="✏️ Update Student", command=update_student, **button_style).pack(pady=10)
tk.Button(root, text="❌ Delete Student", command=delete_student, **button_style).pack(pady=10)
tk.Button(root, text="🚪 Exit", command=confirm_exit, **exit_button_style).pack(pady=20)

root.mainloop()
