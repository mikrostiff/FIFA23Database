import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    # select the csv to analyze
    def select_file(): 
        file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            entry_file_path.delete(0, tk.END)
            entry_file_path.insert(0, file_path)
    # processing the data, output charts.
    def process_data():
        data_path = entry_file_path.get()
        if not data_path:
            messagebox.showerror("Error", "Please select a CSV file!")
            return
        try:
            data = pd.read_csv(data_path)
            filtered_data = data[data['fifa_version'] == 23]
            columns_to_keep = ['short_name', 'long_name', 'value_eur', 'wage_eur', 'pace', 'shooting', 'passing',
                               'dribbling', 'defending']
            filtered_data = filtered_data[columns_to_keep]
            output_path = filedialog.asksaveasfilename(title="Save Filtered CSV File", defaultextension=".csv",
                                                       filetypes=[("CSV Files", "*.csv")])
            if not output_path:
                return
            filtered_data.to_csv(output_path, index=False)
            messagebox.showinfo("Success", f"Filtered data has been saved to: {output_path}")
            cleaned_data = filtered_data.dropna()
            desc_stats = cleaned_data.describe()
            print("\nDescriptive Statistics:")
            print(desc_stats)
            correlation_wage = cleaned_data['wage_eur'].corr(cleaned_data['value_eur'])
            print(f"\nCorrelation between wage and player value: {correlation_wage:.2f}")
            def plot_wage_vs_value(data):
                plt.figure(figsize=(10, 6))
                plt.scatter(data['wage_eur'], data['value_eur'], alpha=0.5, c='blue', edgecolors='k')
                plt.title('Relationship Between Player Wage and Value (FIFA 23)', fontsize=14)
                plt.xlabel('Wage (in Euros)', fontsize=12)
                plt.ylabel('Value (in Euros)', fontsize=12)
                plt.grid(True, linestyle='--', alpha=0.5)
                plt.show()
            plot_wage_vs_value(cleaned_data)
            def plot_ability_histograms(data):
                abilities = ['pace', 'shooting', 'passing', 'dribbling', 'defending']
                for ability in abilities:
                    plt.figure(figsize=(10, 6))
                    plt.hist(data[ability], bins=20, color='skyblue', edgecolor='black')
                    plt.title(f'Distribution of {ability.capitalize()} (FIFA 23)', fontsize=14)
                    plt.xlabel(f'{ability.capitalize()} Rating', fontsize=12)
                    plt.ylabel('Number of Players', fontsize=12)
                    plt.grid(True, linestyle='--', alpha=0.5)
                    plt.show()
            plot_ability_histograms(cleaned_data)
            def plot_wage_vs_ability(data):
                abilities = ['pace', 'shooting', 'passing', 'dribbling', 'defending']
                for ability in abilities:
                    plt.figure(figsize=(10, 6))
                    plt.scatter(data['wage_eur'], data[ability], alpha=0.5, c='green', edgecolors='k')
                    plt.title(f'Relationship Between Wage and {ability.capitalize()} (FIFA 23)', fontsize=14)
                    plt.xlabel('Wage (in Euros)', fontsize=12)
                    plt.ylabel(f'{ability.capitalize()} Rating', fontsize=12)
                    plt.grid(True, linestyle='--', alpha=0.5)
                    plt.show()
            plot_wage_vs_ability(cleaned_data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while processing the data: {e}")
    root = tk.Tk()
    root.title("FIFA Data Analysis")
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)
    tk.Label(frame, text="Select CSV File:").grid(row=0, column=0, sticky="w")
    entry_file_path = tk.Entry(frame, width=40)
    entry_file_path.grid(row=0, column=1, padx=5)
    tk.Button(frame, text="Browse", command=select_file).grid(row=0, column=2, padx=5)
    tk.Button(frame, text="Start Analysis", command=process_data).grid(row=1, column=1, pady=10)
    root.mainloop()


if __name__ == "__main__":
    main()

