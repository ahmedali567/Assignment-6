class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

print("Original Bank Name:", Bank.bank_name)

Bank.change_bank_name("XYZ Bank")
print("Updated Bank Name:", Bank.bank_name)
