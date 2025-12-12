                                     🏧 ATM Machine Simulator — Python Beginner Project

✨ Overview

🧾 This project is a basic ATM simulator built using simple Python concepts.

💳 Users can log in using their card number + PIN.

🏦 They can check balance, withdraw money, or deposit money.

🎯 The goal is to help beginners understand conditions, variables, and user input.

---------------------------------------------------

🧩 Concepts Used

📌 Variables

📌 if, elif, else conditions

📌 Nested conditions

📌 User input (input())

📌 Arithmetic operations

📌 Basic validation

---------------------------------------------

🛠️ How the Program Works (Step-by-Step)

🔹 1. Create Data for 3 Users

💳 Each user has:

▶️ Card number

▶️ PIN

▶️ Account balance

🧠 This helps the program identify which user is logging in.

🔹 2. Take Card Number Input

⌨️ User enters their card number.

🔍 Program checks if the entered card number matches card_no1, card_no2, or card_no3.

🔹 3. PIN Verification

🔐 If the card is found:

User enters PIN.

Program compares input PIN with stored PIN.

❌ If wrong → “Wrong PIN”.

✔️ If correct → Menu options appear.

🔹 4. Show ATM Menu

📋 User gets 3 options:

1️⃣ Check Balance

2️⃣ Withdraw Money

3️⃣ Deposit Money

🔹 5. Perform Actions Based on Choice

✔️ Check Balance:

Simply prints the current balance.

✔️ Withdraw Money:

User enters amount.

Program checks if balance is enough.

If yes → balance reduces.

If no → “Insufficient Balance”.

✔️ Deposit Money:

User enters amount.

Balance increases.

🔹 6. Invalid Conditions

❗ Wrong card number → “Card not found”.

❗ Wrong menu option → “Invalid Option”.

------------------------------------------------

🧠 Code Explanation 

🔸 User Data Section

🧾 Variables like card_no1, pin1, bal1 store details of User 1.

🌟 Same pattern used for User 2 & User 3.

🔸 Input Section

⌨️ card_no = int(input()) takes card number from user.

🔍 Program starts checking who this card belongs to.

🔸 User Identification

🧠 if card_no == card_no1:

This block runs ONLY for user 1.

🔁 Same logic repeats for user 2 and 3.

🔸 PIN Check

🔐 Program asks for PIN inside each user block.

✔️ PIN matches → access allowed.

❌ Wrong → prints error.

🔸 Menu Choices

🎛️ 1 = check balance, 2 = withdraw, 3 = deposit.

📌 These options are checked using nested if/elif inside the user section.

🔸 Withdraw Logic

🏦 Check if withdrawal amount <= balance.

✔️ If yes → subtract amount.

❌ If no → show error.

🔸 Deposit Logic

➕ Add the entered amount to the balance variable.

--------------------------------------------

▶️ How to Run This Program

🖥️ Install Python

📁 Save file as atm.py

▶️ Run:

python atm.py

Follow on-screen instructions

------------------------------------------

🚀 Future Enhancements

📌 Add unlimited users using lists/dictionaries

📌 Add cash transfer feature

📌 Add loop for multiple actions

📌 Add hidden PIN input (getpass)

📌 Add receipt print option

