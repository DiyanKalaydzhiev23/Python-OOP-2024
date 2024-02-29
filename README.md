# Theory tests

- [First Steps In OOP](https://forms.gle/jenahYVLxPK8PYhN6)

- [Classes and Objects](https://forms.gle/PeoSqmdHyCJbptxP8)

- [Inheritance](https://forms.gle/jzjTh2sLYGRNQak6A)

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
   - Обектите се състоят от две основни части:
     - Характеристики (State)
     - Поведение (Behavior)
  ```py
    class MyObject:
        def __init__(self, property1):
            self.property1 = property1  # State

        def doSomething():  # Behavior
            ...
  ```

---

### 02. Classes and Objects

1. Атрибути
   - Data Attributes
     - Instance Attributes -
       - Закачени на инстанцията(self)
       - Уникални за всяка инстанция
     - Class Attributes
       - Закачени на класа
       - Споделени между всички инстанции
   - Methods
     - Функции принадлежящи на класа
    
2. Магически методи
   - **__init__** - използваме за инстанциране на класа
   - **__str__** - използваме за стрингова репрезентация на класа (т.е. вместо <object in memory ...>); извиква се, когато се опитаме да кастнем инстанция към стринг
   - **__repr__** - използваме, за да представим класа като стринг дори при дебъгване (машинна репрезентация)
   - **__dict__** - репрезентира стейта на класа като dictionary
   - **__doc__** - връща документацията на обекта 

---

### 03. Inheritance

1. Какво е наследяване?
   - Наследяването е един от четирите основни стълба на обектно ориентираното програмиране
   - Използваме го, за по-добра абстракция и преизползване на код
   - DRY - **Don't Repeat Yourself**

2. super()
   - **super** представлява първия бащин клас
  
3. Видове наследяване
   - Single
     </br>
     <img src="https://simplesnippets.tech/wp-content/uploads/2018/03/single_inheritance_in_cpp.png" width=400 height=200 />
   - Multiple
     </br>
     <img src="https://media.geeksforgeeks.org/wp-content/uploads/20191222084630/multipleinh.png" width=400 height=200 >
   - Multilevel
     </br>
     <img src="https://media.geeksforgeeks.org/wp-content/uploads/multilevel-inheritance.png" width=400 height=200 >
   - Hierarchical
     </br>
     <img src="https://www.simplilearn.com/ice9/free_resources_article_thumb/Hierarchical_Inheritance_In_C_P_P_Chart.png" width=400 height=200>

4. What is MRO (Method Resolution Order)
   - Depth First Resolve
   - Подрежда наследяваните класове в определен ред.

5. Mixins
   - Миксините са класове, които използваме, за да наследим някаква функционалност в множество класове.
   - Пример:
     - Имаме клас кола и клас фурна
     - Колата и фурната имат часовник, които работи както всички други часовници по света
     - Съответно правим миксин клас часовник, който да наследим в другите 2 класа.
