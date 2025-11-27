# Simple Add Two Numbers (LeetCode style) with user input
# Numbers are given as reversed digit lists: 342 → [2,4,3]

print("=== Add Two Numbers (digits in reverse order) ===")
print("Example: 342 is entered as: 2 4 3")
print()

# Get first number
l1_input = input("Enter the first number's digits (space-separated): ")
l1 = [int(x) for x in l1_input.strip().split()]

# Get second number
l2_input = input("Enter the second number's digits (space-separated): ")
l2 = [int(x) for x in l2_input.strip().split()]

# The actual addition — pure sequential code
result = []
carry = 0
i = 0

while i < len(l1) or i < len(l2) or carry:
    digit1 = l1[i] if i < len(l1) else 0
    digit2 = l2[i] if i < len(l2) else 0
    
    total = digit1 + digit2 + carry
    digit = total % 10
    carry = total // 10
    
    result.append(digit)
    i += 1

# Show the result
print("\nResult:", " ".join(map(str, result)))
print("Which represents the number:", "".join(map(str, result[::-1])))

# Bonus: show what the original numbers were (reversed back)
num1 = "".join(map(str, l1[::-1])) if l1 else "0"
num2 = "".join(map(str, l2[::-1])) if l2 else "0"
total = int(num1) + int(num2)
print(f"\nVerification: {num1} + {num2} = {total}")