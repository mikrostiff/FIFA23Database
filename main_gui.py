import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import *
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
        self.player_comparison_tab = ttk.Frame(self.notebook)
        self.performance_tab = ttk.Frame(self.notebook)
        self.financial_tab = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.dashboard_tab, text='Dashboard')
        self.notebook.add(self.player_comparison_tab, text='Player Comparison')
        self.notebook.add(self.performance_tab, text='Performance Analysis')
        self.notebook.add(self.financial_tab, text='Financial Analysis')
        
        self.notebook.pack(expand=True, fill='both')
        
        # Initialize tabs
        self.init_dashboard()
        self.init_player_comparison()
        self.init_performance()
        self.init_financial()
    
    def init_dashboard(self):
        # Create frames for dashboard layout
        control_frame = ttk.Frame(self.dashboard_tab)
        control_frame.pack(side='top', fill='x', padx=5, pady=5)
        
        # Add dropdown for league selection
        ttk.Label(control_frame, text="Select League:").pack(side='left')
        leagues = ['All'] + self.df['league_name'].unique().tolist()
        self.league_var = tk.StringVar()
        league_dropdown = ttk.Combobox(control_frame, textvariable=self.league_var, values=leagues)
        league_dropdown.pack(side='left', padx=5)
        league_dropdown.set('All')
        
        # Create plots frame
        plots_frame = ttk.Frame(self.dashboard_tab)
        plots_frame.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Add initial plots
        self.create_dashboard_plots(plots_frame)
    
    def create_dashboard_plots(self, frame):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        # Overall rating distribution
        ax1.hist(self.df['overall'], bins=30, color='#2ecc71')
        ax1.set_title('Overall Rating Distribution')
        ax1.set_xlabel('Overall Rating')
        ax1.set_ylabel('Count')

        # Age vs Overall scatter
        ax2.scatter(self.df['age'], self.df['overall'], alpha=0.5, color='#3498db')
        ax2.set_title('Age vs Overall Rating')
        ax2.set_xlabel('Age')
        ax2.set_ylabel('Overall Rating')
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill='both')

    def init_player_comparison(self):
        # Player comparison functionality
        control_frame = ttk.Frame(self.player_comparison_tab)
        control_frame.pack(side='top', fill='x', padx=5, pady=5)
        
        # Add player selection dropdowns
        players = self.df['short_name'].tolist()
        self.player1_var = tk.StringVar()
        self.player2_var = tk.StringVar()
        
        ttk.Label(control_frame, text="Player 1:").pack(side='left')
        player1_dropdown = ttk.Combobox(control_frame, textvariable=self.player1_var, values=players)
        player1_dropdown.pack(side='left', padx=5)
        
        ttk.Label(control_frame, text="Player 2:").pack(side='left')
        player2_dropdown = ttk.Combobox(control_frame, textvariable=self.player2_var, values=players)
        player2_dropdown.pack(side='left', padx=5)

    def init_performance(self):
        # Performance analysis functionality
        pass

    def init_financial(self):
        # Financial analysis functionality
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = FIFAAnalyzer(root)
    root.mainloop()
