# 🎮 Player Health System — Python

A simple Python project created to practice **getters, setters, `@property`, and data validation** using a game-player health system.

## 📌 What I Learned

* Python `@property`
* Getters
* Setters using `@health.setter`
* Why `_health` is used as an internal variable
* Property validation
* How getters and setters are triggered automatically
* Using properties inside other methods
* Basic Object-Oriented Programming (OOP)

## ⚙️ Features

* Create a player with a name and health
* Get the player's current health
* Set health with validation
* Take damage
* Heal the player
* Prevent health from going below `0` or above `100`

## 💻 Example

```python
p1 = Player("Hardik", 100)

print(f"Player Health is {p1.health}\n")

p1.health = 90
p1.health = 600

p1.take_damage(30)
p1.heal(20)
```

## 🧠 How `@property` Works

The `health` property provides controlled access to the internal `_health` variable.

```python
@property
def health(self):
    return self._health
```

When we write:

```python
p1.health
```

the getter is automatically called.

When we write:

```python
p1.health = 90
```

the setter is automatically called:

```python
@health.setter
def health(self, new_health):
```

### Why `_health`?

`_health` stores the actual value.

```text
health  → Property / controlled access
_health → Actual stored value
```

Using a separate variable prevents the getter and setter from recursively calling themselves.

## 📂 Project Structure

```text
player-health-system/
│
├── player.py
└── README.md
```

## 🚀 Future Improvements

* Add a maximum healing limit
* Prevent damage greater than the player's current health
* Add attack functionality
* Add player levels
* Add experience points
* Create a complete text-based battle system

---

### 📚 Status

**Learning Project**

Built while learning Python OOP and `@property` / setters.
