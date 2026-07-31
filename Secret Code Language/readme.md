# 🔐 Secret Code Language Encoder & Decoder

A beginner-friendly Python project that encodes and decodes secret messages using a custom encryption technique based on string manipulation and random characters.

## 📌 Features

- 🔒 Encode plain text into a secret language.
- 🔓 Decode the encoded text back to its original form.
- 🎲 Generates random alphabetic characters for every encoded word.
- 🔄 Automatically reverses words shorter than 3 characters.
- 💻 Menu-driven interface using `match-case`.

---

## 🛠️ Technologies Used

- Python 3
- `random` module
- `string` module

---

## 🚀 How It Works

### Encoding

For words with **3 or more characters**:

1. Move the first character to the end.
2. Add **3 random letters** to the beginning.
3. Add **3 random letters** to the end.

Example:

Original:
```
Hardik
```

Encoded (Example):
```
AbcardikHXYZ
```

> **Note:** The random letters change every time you encode.

---

For words with **less than 3 characters**:

The word is simply reversed.

Example:

```
is
```

↓

```
si
```

---

### Decoding

For encoded words:

1. Remove the first 3 characters.
2. Remove the last 3 characters.
3. Move the last character back to the beginning.

Example:

```
AbcardikHXYZ
```

↓

```
Hardik
```

For short words:

```
si
```

↓

```
is
```

---

## 📸 Example

### Input

```
Hardik is learning Python
```

### Encoded (Example)

```
AbcardikHXYZ si QweearninglDef MnoythonPGhi
```

### Decoded

```
Hardik is learning Python
```

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/Secret-Code-Language.git
```

2. Open the project folder.

3. Run the program.

```bash
python code_lang.py
```

---

## 📂 Project Structure

```
Secret-Code-Language/
│── code_lang.py
│── README.md
```

---

## 📖 Concepts Used

- Variables
- User Input
- `match-case`
- Lists
- `append()`
- `split()` & `join()`
- String Slicing
- Loops
- Conditional Statements
- Random Module
- String Module

---

## ⭐ Future Improvements

- Preserve punctuation (`.`, `,`, `!`, `?`)
- Save encoded messages to a file
- Graphical User Interface (GUI)
- Encrypt complete paragraphs while preserving formatting

---

## 👨‍💻 Author

**Hardik**

Built while learning Python and practicing string manipulation through beginner-friendly projects.

If you found this project useful, consider giving it a ⭐ on GitHub!
