import tkinter as tk
from tkinter import messagebox

# === GUI Window ===
root = tk.Tk()
root.title("🛒 Cyber Courses - Shopping Cart")
root.geometry("1200x550")
root.configure(bg="#f5fafa")

# === Colors ===
cart_bg_color = "#e0f7fa"
button_color = "#ff6666"
text_color = "#003c50"

# === Products ===
products = {
    "🛡️ Cybersecurity - Weekly": 90,
    "🔐 Cybersecurity - Self-study": 80,
    "🐍 Python from Scratch (30% OFF)": 70,
    "🤖 Build a Bot with Python": 95,
    "📊 Data Analysis with Python": 90,
    "🧠 Intro to Machine Learning": 110,
    "🌐 Web Security Basics": 85,
    "🧱 Firewall & Network Security": 100,
    "🔍 Pentesting Mini-Course (30% OFF)": 66.5,
    "📚 All-in-One Access (Monthly)": 150
}

selected = {}
quantities = {}

# === Title ===
tk.Label(root, text="📘 Course List", font=("Arial", 16, "bold"),
         fg=text_color, bg="#f5fafa").place(x=300, y=20)

# === Course List ===
y_offset = 70
for name, price in products.items():
    var = tk.IntVar()
    qty = tk.IntVar(value=1)

    cb = tk.Checkbutton(root, text=f"{name} - ${price:.2f}", variable=var,
                        command=lambda: update_cart(),
                        bg="#f5fafa", fg=text_color, font=("Arial", 11))
    cb.place(x=300, y=y_offset)

    def decrease(q=qty): q.set(max(1, q.get() - 1)); update_cart()
    def increase(q=qty): q.set(q.get() + 1); update_cart()

    tk.Button(root, text="-", width=3, height=1, font=("Arial", 10), command=decrease).place(x=670, y=y_offset)
    tk.Label(root, textvariable=qty, width=3, font=("Arial", 11)).place(x=710, y=y_offset)
    tk.Button(root, text="+", width=3, height=1, font=("Arial", 10), command=increase).place(x=750, y=y_offset)

    selected[name] = var
    quantities[name] = qty
    y_offset += 35

# === Cart Area ===
tk.Label(root, text="🧺 Cart", font=("Arial", 14, "bold"),
         bg=cart_bg_color, fg=text_color).place(x=920, y=30)

cart_box = tk.Text(root, width=30, height=20, state="disabled",
                   bg=cart_bg_color, fg=text_color, font=("Arial", 10))
cart_box.place(x=880, y=60)

# === Update Cart ===
def update_cart():
    cart_box.config(state="normal")
    cart_box.delete(1.0, tk.END)
    total = 0

    for name in selected:
        if selected[name].get() == 1:
            qty = quantities[name].get()
            price = products[name]
            line_total = qty * price
            total += line_total
            cart_box.insert(tk.END, f"{name}\n  x{qty} = ${line_total:.2f}\n\n")

    cart_box.insert(tk.END, f"🔢 Total: ${total:.2f}")
    cart_box.config(state="disabled")

# === Show Total ===
def show_total():
    total = 0
    for name in selected:
        if selected[name].get() == 1:
            qty = quantities[name].get()
            total += products[name] * qty
    messagebox.showinfo("Total Price", f"Total amount: ${total:.2f}\n\nThanks for shopping with us! 🛒\nSee you soon 👋")

# === Enter Button ===
tk.Button(root, text="💰 Enter", font=("Arial", 12, "bold"),
          bg=button_color, fg="white", width=15, height=2, command=show_total).place(x=950, y=470)

# === Start GUI ===
root.mainloop()
