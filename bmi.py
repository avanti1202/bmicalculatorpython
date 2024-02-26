#Importing packages, modules
from tkinter import Tk , ttk
import tkinter as tk
from tkinter import *
from requests import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re

root = Tk()
root.geometry("500x520+500+150")
root.title("Body Mass Index Calculator By Avanti")
root.configure(bg = "white")
f = ("Arial",20, "bold")
root.resizable(height = FALSE, width =FALSE)

#Top frame
top = Frame(root, width=500, height=85, bg= "#FF1493")
top.grid(row=0, column=0)

icon = Image.open('C:/internship/mira/Python/task2/p2_bmiapp/images/abm.png')
icon = icon.resize((80, 80))
icon= ImageTk.PhotoImage(icon)

app_name = Label(top, image= icon, compound=LEFT, text=" BMI Calculator",  height = 4, padx =20,pady =35, anchor = CENTER, font = f , bg = "#FF1493", fg = "black" )
app_name.place(x=50, y=8)

#Main frame
root = Frame(root, width=500, height=435, bg= "#fff0db")
root.grid(row=1, column=0)
f1 =("Helvetica", 16, "bold")

#Age input
lab_age = Label(root, text="Enter Age =", font = f1, bg = "#fff0db")
lab_age.place(x=10, y =10)
ent_age = Entry(root, font = f, relief = "solid", width = 8)
ent_age.place(x=150, y =10)

#Gender Selection
def get_gender():
    gender = gender_var.get()
    print(f"Selected gender: {gender}")
gender_var = tk.StringVar(value="Male") 

lab_gen = tk.Label(root, text="Select Gender: ", font = f1, bg = "#fff0db")
lab_gen.place(x=10, y =70)

# Radio buttons for male and female
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", command=get_gender, bg = "#fff0db", font = f1)
male_radio.place(x=190, y =70)

female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", command=get_gender, bg = "#fff0db", font = f1)
female_radio.place(x=300, y =70)

#Height input
lab_height = Label(root, text="Height   =", font = f1, bg = "#fff0db")
lab_height.place(x=10, y =130)
ent_height = Entry(root, font = f, relief = "solid", width = 6)
ent_height.place(x=150, y =130)

def toggle_dropdown(event=None):
    height_ut =height_combo.get()
    if height_ut == "Feet/Inches":
        dropdown.config(state=tk.NORMAL)  # Enable the inches dropdown
    else:
        dropdown.config(state=tk.DISABLED)  # Disable the inches dropdown

unit_options = ["Feet/Inches", "cm"]
height_unit_var = tk.StringVar()
default_value1 = unit_options[1]
height_combo = ttk.Combobox(root, textvariable=height_unit_var, values=unit_options, state="readonly", width = 5, font=f1)
height_combo.bind("<<ComboboxSelected>>", toggle_dropdown)
height_combo.set(default_value1)
height_combo.place(x=350, y =130)

options = list(range(12))

dropdown_var = tk.StringVar(root)
dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.config(width=5)
dropdown_var.set(0)
dropdown.place(x=270, y = 130)
dropdown.config(state=tk.DISABLED)

#Weight input
lab_weight = Label(root, text="Weight  =", font = f1, bg = "#fff0db")
lab_weight.place(x=10, y =190)
ent_weight = Entry(root, font = f, relief = "solid", width = 6)
ent_weight.place(x=150, y =190)

weight_unit = ["kg", "lbs"]
weight_unit_var = tk.StringVar()
weight_combo = ttk.Combobox(root, textvariable=weight_unit_var, values=weight_unit, state="readonly", width = 5, font=f1)
default_value2 = weight_unit[0]
weight_combo.set(default_value2)
weight_combo.place(x=350, y =190)

#Calculate function

def calculate_bmi():
    try:
        age = ent_age.get()
        height = ent_height.get()
        weight = ent_weight.get()
        height_ut =height_unit_var.get()
        weight_ut =weight_unit_var.get()
        bmi_status = ""
    
        pattern = r'^[!@#$%^&*()_+{}\[\]:;<>,.?/\\|]+$'
        regex = r'^[a-zA-Z]+$'
        pattern1 =   r'^[+-]?\d*\.?\d+$'
    
        if (age == "") and (height == "") and (weight ==""):
            messagebox.showerror("Error" , "Please enter all fields")   
        elif(age == ""):
            messagebox.showerror("Error" , "Age is empty\nPlease enter valid age")
        elif (age.isspace()):
            messagebox.showerror("Error" , "Age should not contain spaces\nPlease enter valid age")
            ent_age.delete(0, tk.END)
            ent_age.focus_set()
        elif re.search (pattern, age):
            messagebox.showerror("Error" , "Age should not contain special characters")
            ent_age.delete(0, tk.END)
            ent_age.focus_set()
        elif re.search (regex, age):
            messagebox.showerror("Error" , "Age should not contain alphabets")
            ent_age.delete(0, tk.END)
            ent_age.focus_set()
        elif not re.search (pattern1, age):
            messagebox.showerror("Error" , "Age should not contain combination of digits, alphabets or special characters")
            ent_age.delete(0, tk.END)
            ent_age.focus_set()
        elif (height == ""):
             messagebox.showerror("Error" , "Height is empty\n Please enter appropriate height")
        elif (height.isspace()):
                messagebox.showerror("Error" , "Height should not contain blank spaces")
                ent_height.delete(0, tk.END)
                ent_height.focus_set()
        elif re.search (regex, height):
                messagebox.showerror("Error" , "Height should not contain alphabets")
                ent_height.delete(0, tk.END)
                ent_height.focus_set()
        elif re.search (pattern, height):
                messagebox.showerror("Error" , "Height should not contain special characters")
                ent_height.delete(0, tk.END)
                ent_height.focus_set()
        elif not re.search (pattern1, height):
                messagebox.showerror("Error" , "Height should not contain combination of digits, alphabets or special characters")
                ent_height.delete(0, tk.END)
                ent_height.focus_set()
        elif (weight == ""):
                messagebox.showerror("Error" , "Weight is empty\n Please enter appropriate weight")
        elif (weight.isspace()):
                messagebox.showerror("Error" , "Weight should not contain blank spaces")
                ent_weight.delete(0, tk.END)
                ent_weight.focus_set()
        elif re.search (pattern, weight):
                messagebox.showerror("Error" , "Weight should not contain special characters")
                ent_weight.delete(0, tk.END)
                ent_weight.focus_set()
        elif re.search (regex, weight):
                messagebox.showerror("Error" , "Weight should not contain alphabets")
                ent_weight.delete(0, tk.END)
                ent_weight.focus_set()
        elif not re.search (pattern1, weight):
                messagebox.showerror("Error" , "Weight should not contain combination of digits, alphabets or special characters")
                ent_weight.delete(0, tk.END)
                ent_weight.focus_set()
        else:
            age = float(age)
            height = float(height)
            weight = float(weight)
            if(age <= 0):
                messagebox.showerror("Error" , "Age cannot be negative or zero")
                ent_age.delete(0, tk.END)
                ent_age.focus_set()
            elif (age < 2) or (age > 120):
                messagebox.showerror("Error" , "Age should be between 2 and 120")
                ent_age.delete(0, tk.END)
                ent_age.focus_set()    
            elif (height <= 0):
                messagebox.showerror("Error" , "Height should be greater than 0")
                ent_height.delete(0, tk.END)
                ent_height.focus_set()
            elif (weight <=0):
                messagebox.showerror("Error" , "Weight should be greater than 0")
                ent_weight.delete(0, tk.END)
                ent_weight.focus_set()
             
            else:
                if height_ut == "cm":
                    if (float(height < 50) or float(height > 300) ):
                        messagebox.showerror("Error", "Height in CM units should be between 50CM to 300CM")
                        ent_height.delete(0, tk.END) 
                        return
                    else:
                        height = float(height) / 100 # Convert height from cm to meters
                        print(height)
                else:   
                    feet = float(ent_height.get())  
                    if feet.is_integer():
                        feet = float(feet)
                        inches = float(dropdown_var.get())
                        height = (feet * 12 + inches) * 0.0254 
                        print(height)   
                    else: 
                        messagebox.showerror("Error","Value of feet should be integers")
                        ent_height.delete(0, tk.END)
                        return
                    
                if  weight_ut  == "kg":
                        if (float(weight < 8) or float(weight > 500) ):
                            messagebox.showerror("Error", "Weight in KG units should be between 8kg to 500kg")
                            ent_weight.delete(0, tk.END)
                            return
                        else:
                            weight1 = float(weight)
                else:
                    weight1 = float(weight) * 0.453592   # Calculate BMI
                    print(age)
                    print(weight1)
                
                            
                bmi = weight1 / (height ** 2)
                if bmi < 18.5:
                    bmi_status = "Underweight"
                elif 18.5 <= bmi < 25:
                    bmi_status = "Normal"
                elif 25 <= bmi < 30:    
                    bmi_status = "Overweight"
                else:
                    bmi_status = "Obesity"  

                lab_bmi.config(text=f"Your BMI is: {bmi:.2f} ({bmi_status})")
               
    except Exception as e:
        messagebox.showerror("Error", e)

#Calculate Button
bmi_btn = Button(root, text = "Calculate", font = f1, bg = "lightblue",relief = "solid", command = calculate_bmi)
bmi_btn.place(x = 140, y = 250)

#Clear Button
def clear():
    ent_age.delete(0, tk.END)
    ent_age.focus()
    height_combo.set(default_value1)
    ent_height.delete(0, tk.END)
    ent_height.focus()
    weight_combo.set(default_value2)
    ent_weight.delete(0,tk.END)
    ent_weight.focus()
    lab_bmi.config(text = "")

clear_btn = Button(root, text = "Clear", font = f1, bg = "lightgreen",relief = "solid", command = clear)
clear_btn.place(x = 330, y = 250)

#Label for displaying bmi
lab_bmi = Label(root, text="", font = f1, bg = "#FFFFF0", relief="solid", width = 25, height = 2)
lab_bmi.place(x=90, y =320)

text_lab= Label(root,text="Healthy BMI range: 18.5 kg/m2 - 25 kg/m2", font = f1, bg ="#fff0db")
text_lab.place(x=40, y =380)

root.mainloop()