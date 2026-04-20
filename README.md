# 🔧 Mechanic Service Program

A Python program to manage car service records for a mechanic garage.
Built as a student project using file handling, functions, and lists.

---

## 📋 Features

- **Add** new customers with their kilometres
- **Update** a customer's kilometre value
- **Delete** a customer and archive their record
- **Display** all customers in a formatted table with service urgency
- **Auto-saves** all changes to a text file

---

## 🚗 Service Urgency Levels

| Kilometres | Status |
|------------|--------|
| Under 5,000 km | No Service Needed |
| 5,000 - 9,999 km | Service Due Soon |
| 10,000 km and over | Service Overdue |

---

## 📁 Files

| File | Description |
|------|-------------|
| `mechanic.py` | Main program |
| `services.txt` | Stores all active customer records |
| `deleted.txt` | Archive of deleted customer records |

---

## ▶️ How to Run

1. Make sure `services.txt` is in the same folder as `mechanic.py`
2. Run the program in PyCharm or any Python editor
3. Use the menu to navigate

```
===== MECHANIC SERVICE PROGRAM =====
1. Show all customers
2. Add new customer
3. Update kilometres
4. Delete customer
5. Exit
=====================================
```

---

## 💻 Technologies Used

- Python 3
- File handling (read, write, append)
- Functions
- Lists

---

## 👨‍🎓 About

This project was built as part of a Python programming course.
It demonstrates core Python concepts including functions, file handling, and list manipulation.
