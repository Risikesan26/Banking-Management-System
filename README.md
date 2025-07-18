# Banking-Management-System
# 🏦 Python Banking System

A simple yet powerful console-based banking system built in Python that simulates real-world banking operations. This project supports account management, transaction history, balance inquiries, binary search, and even hierarchical access control via tree structures.

## ✨ Features

- 🔐 **Create Account** with unique 10-digit number and initial deposit
- 💰 **Deposit / Withdraw / Transfer** money between accounts
- 📄 **Transaction History** with last 20 records using a queue
- 📊 **Balance Inquiry** for a single account
- 🔎 **Binary Search** for account number
- 🧑‍💼 **Update Account Owner Name**
- ❌ **Delete Account** with confirmation
- 📈 **Generate Report** sorted by account balance
- 🌳 **Access Control View** using a tree to model users (Manager → Teller → Customer)
- 💾 **Data Persistence** using JSON for saving/loading account data

---

## 🛠️ Technologies Used

- **Python 3**
- Data Structures:
  - `Dictionary` for account storage
  - `Deque` for transaction history
  - `List` & custom `Binary Search`
  - `Tree (UserNode class)` for access control
- `JSON` for data persistence

---

## 📁 File Structure
banking_system/
├── bank_system.py # Main Python script
├── bank_data.json # Auto-generated file for saved accounts
└── README.md # This file
---

## 🧪 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/banking-system.git
   cd banking-system
2.Run the Python script:
   python bank_system.py

📸 Sample Output
==== Welcome to Python Bank ====
1. Create account
2. Deposit
3. Withdraw
4. Transfer
5. View balance
...
12. Exit

✅ Learning Outcomes
This project was developed as part of an academic assignment and includes:

Strong use of object-oriented programming

Integration of multiple data structures in a single system

Simulation of real-world banking workflows

👥 Author
Risikesan Yogeswaran

💼 AI Student

🇲🇾 Malaysia

📫 LinkedIn:www.linkedin.com/in/risikesan-yogeswaran-a25ba9281
