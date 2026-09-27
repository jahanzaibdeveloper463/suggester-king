import tkinter as tk
from tkinter import messagebox

# --- FUNCTION FOR LOGIC ---
def calculate_recommendation():
    try:
        salary = float(entry_salary.get())
        expenses = float(entry_expenses.get())
        years = int(entry_years.get())
        
        # Savings calculation logic
        actual_saving = salary - expenses
        max_allowed_emi = salary * 0.30
        
        final_monthly_saving = min(actual_saving, max_allowed_emi)
        total_budget = final_monthly_saving * (years * 12)
        
        # Results text formatting
        result_text = f"Monthly Saving: PKR {final_monthly_saving:,.0f}\n"
        result_text += f"Total Car Budget: PKR {total_budget:,.0f}\n\n"
        result_text += "🚘 RECOMMENDED CARS:\n"
        
        if total_budget <= 1000000:
            result_text += "- Suzuki Mehran\n- Suzuki Alto (Old)\n- Hyundai Santro"
        elif total_budget <= 2500000:
            result_text += "- Suzuki Wagon R\n- Suzuki Cultus (Used)\n- Toyota Vitz"
        elif total_budget <= 5000000:
            result_text += "- New Suzuki Alto\n- New Changan Alsvin\n- Toyota Yaris"
        else:
            result_text += "- Toyota Corolla Grande\n- Honda Civic\n- Kia Sportage"
            
        # Show result in a popup box
        messagebox.showinfo("Your Recommendation", result_text)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# --- UI WINDOW SETUP ---
root = tk.Tk()
root.title("Car Recommendation Tool")
root.geometry("400x300")

# Input 1: Salary
tk.Label(root, text="Monthly Salary (PKR):").pack(pady=5)
entry_salary = tk.Entry(root)
entry_salary.pack()

# Input 2: Expenses
tk.Label(root, text="Monthly Expenses (PKR):").pack(pady=5)
entry_expenses = tk.Entry(root)
entry_expenses.pack()

# Input 3: Years
tk.Label(root, text="Target Years (e.g., 3):").pack(pady=5)
entry_years = tk.Entry(root)
entry_years.pack()

# Calculate Button
tk.Button(root, text="Suggest My Car", command=calculate_recommendation, bg="green", fg="white").pack(pady=20)

root.mainloop()
