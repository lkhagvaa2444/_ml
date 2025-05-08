## ✍️ **Exercise 5: Backpropagation by Hand**

---

### 🧮 Question 1

Function:

> $f(x, y, z) = (x \cdot y) + z$
> Given:
> $x = 1, y = 2, z = 3$

---

#### 🔁 Forward Pass

Let:

* $q = x \cdot y = 1 \cdot 2 = 2$
* $f = q + z = 2 + 3 = 5$

---

#### 🔄 Backward Pass (Gradients using Chain Rule)

We want:

* $\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}$

From:

* $f = q + z \Rightarrow \frac{\partial f}{\partial q} = 1, \frac{\partial f}{\partial z} = 1$
* $q = x \cdot y \Rightarrow \frac{\partial q}{\partial x} = y = 2, \frac{\partial q}{\partial y} = x = 1$

Now:

* $\frac{\partial f}{\partial x} = \frac{\partial f}{\partial q} \cdot \frac{\partial q}{\partial x} = 1 \cdot 2 = 2$
* $\frac{\partial f}{\partial y} = 1 \cdot 1 = 1$
* $\frac{\partial f}{\partial z} = 1$

---

### ✅ Answer 1:

* $\frac{\partial f}{\partial x} = 2$
* $\frac{\partial f}{\partial y} = 1$
* $\frac{\partial f}{\partial z} = 1$

---

### 🧮 Question 2

Function:

> $f(x, y, z, t) = ((x \cdot y) + z) \cdot t$
> Given:
> $x = 1, y = 2, z = 3, t = 4$

---

#### 🔁 Forward Pass

Let:

* $q = x \cdot y = 1 \cdot 2 = 2$
* $r = q + z = 2 + 3 = 5$
* $f = r \cdot t = 5 \cdot 4 = 20$

---

#### 🔄 Backward Pass

We want:

* $\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}, \frac{\partial f}{\partial t}$

From:

* $f = r \cdot t \Rightarrow \frac{\partial f}{\partial r} = t = 4, \frac{\partial f}{\partial t} = r = 5$
* $r = q + z \Rightarrow \frac{\partial r}{\partial q} = 1, \frac{\partial r}{\partial z} = 1$
* $q = x \cdot y \Rightarrow \frac{\partial q}{\partial x} = y = 2, \frac{\partial q}{\partial y} = x = 1$

Now compute:

* $\frac{\partial f}{\partial q} = \frac{\partial f}{\partial r} \cdot \frac{\partial r}{\partial q} = 4 \cdot 1 = 4$
* $\frac{\partial f}{\partial x} = \frac{\partial f}{\partial q} \cdot \frac{\partial q}{\partial x} = 4 \cdot 2 = 8$
* $\frac{\partial f}{\partial y} = 4 \cdot 1 = 4$
* $\frac{\partial f}{\partial z} = \frac{\partial f}{\partial r} \cdot \frac{\partial r}{\partial z} = 4 \cdot 1 = 4$
* $\frac{\partial f}{\partial t} = 5$

---

### ✅ Answer 2:

* $\frac{\partial f}{\partial x} = 8$
* $\frac{\partial f}{\partial y} = 4$
* $\frac{\partial f}{\partial z} = 4$
* $\frac{\partial f}{\partial t} = 5$