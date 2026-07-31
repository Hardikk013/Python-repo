# 🧾 GST Calculator

A simple Python command-line application that calculates the Goods and Services Tax (GST) for different product categories. This project demonstrates the use of functions, `match-case`, user input, and basic arithmetic operations.

---

## 📌 Features

- 🛒 Calculate GST for different product categories.
- 📊 Displays:
  - Product Category
  - Product Price
  - GST Rate
  - GST Amount
  - Total Price
- 🧮 Uses a reusable function for GST calculation.
- 💻 Menu-driven interface using `match-case`.
- ❌ Handles invalid menu choices gracefully.

---

## 🛠️ Technologies Used

- Python 3

---

## 🚀 Supported Categories

| Category | GST Rate |
|----------|:--------:|
| Food | 5% |
| Clothes | 12% |
| Electronics | 18% |
| Luxury Items | 28% |

---

## ▶️ How It Works

1. Select a product category.
2. Enter the product price.
3. The program calculates:
   - GST Amount
   - Total Price (Price + GST)
4. Displays a formatted bill.

---

## 📸 Example

### Input

```text
==========GST CALCULATOR MENU==========

1. Food (5%)
2. Clothes (12%)
3. Electronics (18%)
4. Luxury Items (28%)
5. Exit

Enter Choice: 3

Enter Product Price: 50000
```

### Output

```text
==========FINAL GST CALCULATOR==========

Category     : Electronics
Price        : ₹50000
GST Rate     : 18%
GST Amount   : ₹9000

----------------------------------------

Total Price  : ₹59000
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/GST-Calculator.git
```

2. Open the project folder.

3. Run the program.

```bash
python bill2.py
```

---

## 📂 Project Structure

```
GST-Calculator/
│── bill2.py
│── README.md
```

---

## 📖 Concepts Used

- Variables
- User Input
- Functions
- Parameters & Return Values
- `match-case`
- Conditional Statements
- Arithmetic Operations
- Formatted Output

---

## 🎯 Learning Objectives

This project was built to practice:

- Creating reusable functions
- Using Python's `match-case`
- Building menu-driven applications
- Writing clean and readable code

---

## ⭐ Future Improvements

- Add CGST & SGST calculation separately.
- Generate an invoice receipt.
- Save bills to a text file.
- Add multiple product support.
- Create a graphical user interface (GUI).

---

## 👨‍💻 Author

**Hardik**

Built while learning Python and practicing beginner-friendly programming projects.

If you found this project useful, consider giving it a ⭐ on GitHub!
