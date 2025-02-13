import tkinter as tk
import csv
import os
import openpyxl
import matplotlib.pyplot as plt
import numpy as np

root = tk.Tk()
root.geometry("300x200")
root.configure(background='white')
# 创建 Label、Entry 和 Button 对象
label = tk.Label(root, text="请输入CSV文件名:")
label.pack(pady=10)
entry = tk.Entry(root, width=50,background='red')
entry.pack()
button = tk.Button(root, text="打开CSV文件",background='blue')