from collections import deque



class Account:
    def __init__(self, account_id, name, balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.account_id}: {self.name} - Balance: ${self.balance}"

accounts = []
transactions = deque()



def create_account(account_id, name, balance=0):
    if find_account(account_id) is not None:
        print("Error: Account ID already exists.")
        return
    accounts.append(Account(account_id, name, balance))
    print("Account created.")

def update_account(account_id, name=None, balance=None):
    acc = find_account(account_id)
    if acc is None:
        print("Error: Account not found.")
        return
    if name:
        acc.name = name
    if balance is not None:
        acc.balance = balance
    print("Account updated.")

def delete_account(account_id):
    global accounts
    accounts = [acc for acc in accounts if acc.account_id != account_id]
    print("Account deleted if existed.")



def binary_search(account_id):
    sorted_accounts = sorted(accounts, key=lambda a: a.account_id)
    low, high = 0, len(sorted_accounts) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_accounts[mid].account_id == account_id:
            return sorted_accounts[mid]
        elif sorted_accounts[mid].account_id < account_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

def find_account(account_id):
    for acc in accounts:
        if acc.account_id == account_id:
            return acc
    return None


def deposit(account_id, amount):
    acc = find_account(account_id)
    if acc:
        acc.balance += amount
        transactions.append(f"Deposited ${amount} to {account_id}")
        print("Deposit successful.")
    else:
        print("Account not found.")

def withdraw(account_id, amount):
    acc = find_account(account_id)
    if acc and acc.balance >= amount:
        acc.balance -= amount
        transactions.append(f"Withdrew ${amount} from {account_id}")
        print("Withdrawal successful.")
    else:
        print("Error: Account not found or insufficient balance.")

def transfer(from_id, to_id, amount):
    acc_from = find_account(from_id)
    acc_to = find_account(to_id)
    if acc_from and acc_to and acc_from.balance >= amount:
        acc_from.balance -= amount
        acc_to.balance += amount
        transactions.append(f"Transferred ${amount} from {from_id} to {to_id}")
        print("Transfer successful.")
    else:
        print("Error: Transfer failed due to missing accounts or insufficient funds.")

def merge_sort(accounts_list):
    if len(accounts_list) <= 1:
        return accounts_list
    mid = len(accounts_list) // 2
    left = merge_sort(accounts_list[:mid])
    right = merge_sort(accounts_list[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0].balance < right[0].balance:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

def generate_report():
    sorted_accs = merge_sort(accounts.copy())
    print("\n--- Account Report (Sorted by Balance) ---")
    for acc in sorted_accs:
        print(acc)


class OrgNode:
    def __init__(self, title):
        self.title = title
        self.children = []

    def add_subordinate(self, node):
        self.children.append(node)

    def print_hierarchy(self, level=0):
        print("  " * level + self.title)
        for child in self.children:
            child.print_hierarchy(level + 1)


if __name__ == "__main__":
    # Create accounts
    create_account(101, "Alice", 1000)
    create_account(102, "Bob", 500)
    create_account(103, "Charlie", 1200)

    
    deposit(101, 200)
    withdraw(102, 100)
    transfer(103, 102, 300)


    update_account(102, name="Bob Jr.")
    delete_account(999)  # Does not exist


    acc = binary_search(102)
    print("\nSearch Result:", acc)


    generate_report()


    print("\n--- Transactions ---")
    for t in transactions:
        print(t)


    print("\n--- Organizational Hierarchy ---")
    ceo = OrgNode("CEO")
    cto = OrgNode("CTO")
    cfo = OrgNode("CFO")
    dev_mgr = OrgNode("Dev Manager")
    acc_mgr = OrgNode("Accounting Manager")

    ceo.add_subordinate(cto)
    ceo.add_subordinate(cfo)
    cto.add_subordinate(dev_mgr)
    cfo.add_subordinate(acc_mgr)

    ceo.print_hierarchy()
