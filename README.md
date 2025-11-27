# ➕ Add Two Numbers as Reversed Linked Lists   
### Interactive Python Demo • Educational • Zero Dependencies

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"You are given two non-empty lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a list."**  


This tiny script brings that classic problem to life **interactively** in your terminal.

### 🎉 Live Example
```
=== Add Two Numbers (digits in reverse order) ===
Example: 342 is entered as: 2 4 3

Enter the first number's digits (space-separated): 2 4 3
Enter the second number's digits (space-separated): 5 6 4

Result: 7 0 8
Which represents the number: 807

Verification: 342 + 465 = 807
```

Yes! (342 + 465 = 807) → reversed digits [2,4,3] + [5,6,4] = [7,0,8]

### Why This Problem Is Legendary
This question perfectly tests:

Understanding of carry-over in addition (just like you learned in elementary school!)
Working with indices and boundaries safely
Handling numbers larger than any built-in integer type (no overflow worries!)
Clean, readable loop logic

It’s the reason many engineers still wake up in cold sweat remembering their Google/Facebook interviews.

## How It Works (Step-by-Step Explanation)
```
while i < len(l1) or i < len(l2) or carry:
    digit1 = l1[i] if i < len(l1) else 0
    digit2 = l2[i] if i < len(l2) else 0
    total  = digit1 + digit2 + carry
    result.append(total % 10)   # current digit
    carry  = total // 10        # carry for next position
    i += 1
```
That’s literally all the magic.
No recursion. No libraries. Pure elementary-school arithmetic recreated in code.

## 🚀 How to Run

```
# 1. Clone the repo
git clone https://github.com/yourusername/add-two-numbers-reversed.git
cd add-two-numbers-reversed

# 2. Run it!
python add_two_numbers.py
```
### Perfect For

Learning how big integers really work under the hood
-- Practicing clean Python one-liners and list comprehensions
Preparing for coding interviews (you’ll see this question… trust me)
Teaching kids addition with a cool twist

