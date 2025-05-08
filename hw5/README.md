# ✏️ Backpropagation by Hand – Chain Rule Exercises

This project walks through two exercises for manually computing gradients using the **chain rule** of calculus, to understand **backpropagation** step-by-step.

---

## 📌 Problems

### Question 1
**Function:**  
`f(x, y, z) = (x * y) + z`  
**Given:**  
`x=1, y=2, z=3`

### Question 2
**Function:**  
`f(x, y, z, t) = ((x * y) + z) * t`  
**Given:**  
`x=1, y=2, z=3, t=4`

---

## ✅ Final Answers

### Question 1:
- ∂f/∂x = 2  
- ∂f/∂y = 1  
- ∂f/∂z = 1  

### Question 2:
- ∂f/∂x = 8  
- ∂f/∂y = 4  
- ∂f/∂z = 4  
- ∂f/∂t = 5  

---

## 🧠 Learning Goal

These exercises teach how **gradients** flow through a computation graph, and how to use the **chain rule** to compute derivatives manually — a fundamental idea behind **backpropagation** in neural networks.
