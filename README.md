# Theory tests

- [First Steps In OOP](https://forms.gle/jenahYVLxPK8PYhN6)

---

# Plans

### 01. First Steps In OOP

1. Какво е **namespace**?
   - Пространство, в което са дефинирани обекти
   - Видове:
     - Built-In
     - Global
     - Local

2. Какво е **scope**?
   - Поле на действие, в което един обект е достъпен
   - Видове:
     - Built-In
     - Global
     - Enclosing
     - Local

3. Обекти
   - **Всичко в Python е обект**
   - Обектите се състоят от две оновни части:
     - Характеристики (State)
     - Поведение (Behavior)
  ```py
    class MyObject:
        def __init__(self, property1):
            self.property1 = property1  # State

        def doSomething():  # Behavior
            ...
  ```
