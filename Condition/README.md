# **Python Conditional Input Lab**

This repository contains a Python script that demonstrates how to use **conditionals** (`if`, `elif`, `else`) to respond to user input. The script is interactive and allows the user to make choices about shipping a package and purchasing stationery items.

---

## **Description**

The script performs the following tasks:

1. Asks the user if they need to **ship a package**.
   - If the user enters `yes`, it confirms assistance.
   - If the user enters `no`, it politely ends the interaction.

2. Asks the user which **stationery item** they want to buy: `stamps`, `envelope`, or `copy`.
   - Responds according to the user's choice.
   - Handles invalid input gracefully by prompting the user to enter a valid option.

---

## **Python Concepts Covered**

- **Input from the user** using `input()`.
- **Conditional statements** with `if`, `elif`, and `else`.
- **String manipulation** using `.lower()` to handle case-insensitive input.
- **Basic program flow control**.

---

## **Example Output Table**

| User Input (Shipping) | Response (Shipping)                        | User Input (Stationery) | Response (Stationery)                           |
|----------------------|-------------------------------------------|------------------------|-----------------------------------------------|
| yes                  | We can help you ship that package!        | stamps                 | You chose to buy stamps.                       |
| yes                  | We can help you ship that package!        | envelope               | You chose to buy an envelope.                  |
| yes                  | We can help you ship that package!        | copy                   | You chose to make a copy.                      |
| yes                  | We can help you ship that package!        | pencil                 | Invalid choice. Please enter stamps, envelope, or copy. |
| no                   | Please come back when you need to ship a package. Thank you. | N/A                    | N/A                                           |

---

### **Notes**

- The **Shipping column** shows the response to whether the user wants to ship a package.  
- The **Stationery columns** show the response based on the user’s stationery choice.  
- Invalid inputs are handled gracefully with a prompt message.  
- `N/A` indicates that the stationery question was not asked because shipping was declined.  

---

## **File Reference**

- [Conditionals.py](aws-python) → Main Python script
