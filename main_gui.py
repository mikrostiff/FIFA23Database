import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import *
import sys
data_path = PLAYER_DATA_PATH

class FIFAAnalyzer:
    def __init__(self, root):
        # create root window
        self.root = root
        self.root.title("FIFA 23 Player Analysis")
        self.root.geometry("1200x800")
        # Configure tab style with larger font
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=('Arial', 12, 'bold'))
        
        # Load data
        self.df = pd.read_csv(data_path)
        
        # Create main container
        self.create_notebook()
        
    def create_notebook(self):
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        
        # Create tabs
        self.dashboard_tab = ttk.Frame(self.notebook)
        self.financial_tab = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.dashboard_tab, text='Analysis')
        self.notebook.add(self.financial_tab, text='Financial Analysis')
        
        self.notebook.pack(expand=True, fill='both')
        
        # Initialize tabs
        self.init_dashboard()
        self.init_financial()
    
    def init_dashboard(self):
        # Create frames for dashboard layout
        control_frame = ttk.Frame(self.dashboard_tab)
        control_frame.pack(side='top', fill='x', padx=5, pady=5)
        
        
        # Add exit button
        exit_button = ttk.Button(control_frame, text="Exit", command=lambda: sys.exit())
        exit_button.pack(side='right', padx=5)

        # Create plots frame
        self.plots_frame = ttk.Frame(self.dashboard_tab)
        self.plots_frame.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Add initial plots
        self.create_dashboard_plots()
    
    def create_dashboard_plots(self):
        # Create figure with 2 rows: top row for original plots, bottom row for abilities
        fig = plt.figure(figsize=(15, 10))
        gs = fig.add_gridspec(2, 5)

        # Top row: Original plots (spanning 2 columns each)
        ax1 = fig.add_subplot(gs[0, :2])
        ax2 = fig.add_subplot(gs[0, 2:4])
    
        # Original plots
        ax1.hist(self.df['overall'], bins=30, color='#2ecc71', alpha=0.7)
        ax1.set_title('Overall Rating Distribution')
        ax1.set_xlabel('Overall Rating')
        ax1.set_ylabel('Number of Players')
        ax1.grid(True, alpha=0.3)
    
        ax2.scatter(self.df['age'], self.df['overall'], alpha=0.5, color='#3498db')
        ax2.set_title('Age vs Overall Rating')
        ax2.set_xlabel('Age')
        ax2.set_ylabel('Overall Rating')
        ax2.grid(True, alpha=0.3)

        # Bottom row: Ability distributions
        abilities = ['pace', 'shooting', 'passing', 'dribbling', 'defending']
        for idx, ability in enumerate(abilities):
            ax = fig.add_subplot(gs[1, idx])
            ax.hist(self.df[ability], bins=20, color='skyblue', edgecolor='black')
            ax.set_title(f'{ability.capitalize()}')
            ax.set_xlabel('Rating')
            ax.tick_params(labelsize=8)
            ax.grid(True, linestyle='--', alpha=0.5)

        # Adjust layout
        plt.tight_layout()
    
        # Create canvas
        self.canvas = FigureCanvasTkAgg(fig, self.plots_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=True, fill='both')
    
    def init_financial(self):
        # Create frame for financial analysis
        self.financial_frame = ttk.Frame(self.financial_tab)
        self.financial_frame.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Create financial plots
        self.create_financial_plots()

    def create_financial_plots(self):
        # Create figure for financial analysis
        fig = plt.figure(figsize=(15, 10))
        gs = fig.add_gridspec(1, 5)

        # Columns to analyze against wage_eur
        abilities = ['pace', 'shooting', 'passing', 'dribbling', 'defending']
        for idx, ability in enumerate(abilities):
            ax = fig.add_subplot(gs[0, idx])
            ax.scatter(self.df['wage_eur'], self.df[ability], alpha=0.5, color='green')
            ax.set_title(f'Wage vs {ability.capitalize()}')
            ax.set_xlabel('Wage (EUR)')
            ax.set_ylabel(ability.capitalize())
            ax.tick_params(labelsize=8)
            ax.grid(True, linestyle='--', alpha=0.5)

        # Adjust layout
        plt.tight_layout()
    
        # Create canvas
        self.canvas = FigureCanvasTkAgg(fig, self.financial_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=True, fill='both')

if __name__ == "__main__":
    root = tk.Tk()
    app = FIFAAnalyzer(root)
    root.mainloop()
