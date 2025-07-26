import tkinter as tk
from tkinter import ttk, messagebox

class SaninSavaraAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sanin-Savara Tooth Size Analysis")
        self.root.geometry("1000x800")
        
        # Set style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('Result.TLabel', font=('Arial', 10, 'bold'), foreground='blue')
        self.style.configure('TNotebook', background='#f0f0f0')
        self.style.configure('TNotebook.Tab', font=('Arial', 10))
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_input_tab()
        self.create_info_tab()
        
    def create_input_tab(self):
        # Input tab
        input_tab = ttk.Frame(self.notebook)
        self.notebook.add(input_tab, text="Analysis Calculator")
        
        # Header
        header_frame = ttk.Frame(input_tab)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, text="Sanin-Savara Tooth Size Analysis", style='Header.TLabel').pack()
        ttk.Label(header_frame, text="Calculate tooth size characteristics based on mesiodistal widths").pack()
        
        # Input frame with scrollbar
        canvas = tk.Canvas(input_tab)
        scrollbar = ttk.Scrollbar(input_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Input fields with default ideal values
        input_frame = ttk.LabelFrame(scrollable_frame, text="Tooth Measurements (in mm)", padding="15")
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Maxillary teeth (ideal values from literature)
        ttk.Label(input_frame, text="Maxillary Teeth", font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)
        
        # Central Incisor (ideal: 8.5 mm)
        ttk.Label(input_frame, text="Central Incisor (11, 21):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_central = tk.DoubleVar(value=8.5)
        ttk.Entry(input_frame, textvariable=self.max_central, width=8).grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Lateral Incisor (ideal: 6.5 mm)
        ttk.Label(input_frame, text="Lateral Incisor (12, 22):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_lateral = tk.DoubleVar(value=6.5)
        ttk.Entry(input_frame, textvariable=self.max_lateral, width=8).grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Canine (ideal: 7.6 mm)
        ttk.Label(input_frame, text="Canine (13, 23):").grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_canine = tk.DoubleVar(value=7.6)
        ttk.Entry(input_frame, textvariable=self.max_canine, width=8).grid(row=3, column=1, sticky=tk.W, padx=5, pady=2)
        
        # First Premolar (ideal: 7.0 mm)
        ttk.Label(input_frame, text="First Premolar (14, 24):").grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_first_premolar = tk.DoubleVar(value=7.0)
        ttk.Entry(input_frame, textvariable=self.max_first_premolar, width=8).grid(row=4, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Second Premolar (ideal: 6.8 mm)
        ttk.Label(input_frame, text="Second Premolar (15, 25):").grid(row=5, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_second_premolar = tk.DoubleVar(value=6.8)
        ttk.Entry(input_frame, textvariable=self.max_second_premolar, width=8).grid(row=5, column=1, sticky=tk.W, padx=5, pady=2)
        
        # First Molar (ideal: 10.0 mm)
        ttk.Label(input_frame, text="First Molar (16, 26):").grid(row=6, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_first_molar = tk.DoubleVar(value=10.0)
        ttk.Entry(input_frame, textvariable=self.max_first_molar, width=8).grid(row=6, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Second Molar (ideal: 9.5 mm)
        ttk.Label(input_frame, text="Second Molar (17, 27):").grid(row=7, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_second_molar = tk.DoubleVar(value=9.5)
        ttk.Entry(input_frame, textvariable=self.max_second_molar, width=8).grid(row=7, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Mandibular teeth (ideal values from literature)
        ttk.Label(input_frame, text="\nMandibular Teeth", font=('Arial', 10, 'bold')).grid(row=8, column=0, columnspan=2, pady=(10, 5), sticky=tk.W)
        
        # Central Incisor (ideal: 5.0 mm)
        ttk.Label(input_frame, text="Central Incisor (31, 41):").grid(row=9, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_central = tk.DoubleVar(value=5.0)
        ttk.Entry(input_frame, textvariable=self.mand_central, width=8).grid(row=9, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Lateral Incisor (ideal: 5.5 mm)
        ttk.Label(input_frame, text="Lateral Incisor (32, 42):").grid(row=10, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_lateral = tk.DoubleVar(value=5.5)
        ttk.Entry(input_frame, textvariable=self.mand_lateral, width=8).grid(row=10, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Canine (ideal: 6.5 mm)
        ttk.Label(input_frame, text="Canine (33, 43):").grid(row=11, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_canine = tk.DoubleVar(value=6.5)
        ttk.Entry(input_frame, textvariable=self.mand_canine, width=8).grid(row=11, column=1, sticky=tk.W, padx=5, pady=2)
        
        # First Premolar (ideal: 7.0 mm)
        ttk.Label(input_frame, text="First Premolar (34, 44):").grid(row=12, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_first_premolar = tk.DoubleVar(value=7.0)
        ttk.Entry(input_frame, textvariable=self.mand_first_premolar, width=8).grid(row=12, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Second Premolar (ideal: 7.0 mm)
        ttk.Label(input_frame, text="Second Premolar (35, 45):").grid(row=13, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_second_premolar = tk.DoubleVar(value=7.0)
        ttk.Entry(input_frame, textvariable=self.mand_second_premolar, width=8).grid(row=13, column=1, sticky=tk.W, padx=5, pady=2)
        
        # First Molar (ideal: 11.0 mm)
        ttk.Label(input_frame, text="First Molar (36, 46):").grid(row=14, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_first_molar = tk.DoubleVar(value=11.0)
        ttk.Entry(input_frame, textvariable=self.mand_first_molar, width=8).grid(row=14, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Second Molar (ideal: 10.5 mm)
        ttk.Label(input_frame, text="Second Molar (37, 47):").grid(row=15, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_second_molar = tk.DoubleVar(value=10.5)
        ttk.Entry(input_frame, textvariable=self.mand_second_molar, width=8).grid(row=15, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(scrollable_frame, text="Analysis Results", padding="15")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        self.results_text = tk.Text(results_frame, height=8, wrap=tk.WORD, font=('Arial', 10))
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
    def create_info_tab(self):
        # Information tab
        info_tab = ttk.Frame(self.notebook)
        self.notebook.add(info_tab, text="Information")
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(info_tab)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_scroll = ttk.Scrollbar(text_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        info_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=text_scroll.set, 
                          font=('Arial', 10), padx=10, pady=10)
        info_text.pack(fill=tk.BOTH, expand=True)
        
        text_scroll.config(command=info_text.yview)
        
        # Add information content
        info_content = """SANIN-SAVARA TOOTH SIZE ANALYSIS INFORMATION

Measurement Instructions:
1. Measure the mesiodistal width of each tooth at its greatest contour
2. Use a digital caliper or Boley gauge for accurate measurements
3. Record to the nearest 0.1 mm
4. Measure both left and right teeth and use the average if symmetrical

Parameters:
- Maxillary Teeth: Central incisors (11,21) to second molars (17,27)
- Mandibular Teeth: Central incisors (31,41) to second molars (37,47)
- Measurements should be made on study casts or directly in mouth

Ideal Values (based on Sanin-Savara studies):
Maxillary Teeth (average mesiodistal widths in mm):
- Central Incisor: 8.5 mm
- Lateral Incisor: 6.5 mm
- Canine: 7.6 mm
- First Premolar: 7.0 mm
- Second Premolar: 6.8 mm
- First Molar: 10.0 mm
- Second Molar: 9.5 mm

Mandibular Teeth (average mesiodistal widths in mm):
- Central Incisor: 5.0 mm
- Lateral Incisor: 5.5 mm
- Canine: 6.5 mm
- First Premolar: 7.0 mm
- Second Premolar: 7.0 mm
- First Molar: 11.0 mm
- Second Molar: 10.5 mm

Classification Criteria:
Tooth Size Categories (sum of all teeth in arch):
- Small: <30 mm (extremely rare)
- Average: 30-70 mm (normal range)
- Large: >70 mm (requires evaluation)

Arch Comparison:
- Maxillary > Mandibular: May indicate maxillary excess
- Mandibular > Maxillary: May indicate mandibular excess
- Proportional: Within 2-3% of each other

Clinical Significance:
- Helps identify tooth-size discrepancies affecting occlusion
- Guides treatment planning (interproximal reduction, build-ups)
- Useful for diagnosing cases with:
  - Crowding or spacing issues
  - Class II or Class III malocclusions
  - Anterior open bites or deep bites

Common Causes of Discrepancies:
- Genetic variations in tooth size
- Peg-shaped or malformed teeth
- Missing or supernumerary teeth
- Enamel hypoplasia or other developmental anomalies
"""
        info_text.insert(tk.END, info_content)
        info_text.config(state=tk.DISABLED)
    
    def calculate(self):
        try:
            # Calculate maxillary sum
            max_sum = (self.max_central.get() + self.max_lateral.get() + 
                       self.max_canine.get() + self.max_first_premolar.get() + 
                       self.max_second_premolar.get() + self.max_first_molar.get() + 
                       self.max_second_molar.get()) * 2  # Multiply by 2 for both sides
            
            # Calculate mandibular sum
            mand_sum = (self.mand_central.get() + self.mand_lateral.get() + 
                        self.mand_canine.get() + self.mand_first_premolar.get() + 
                        self.mand_second_premolar.get() + self.mand_first_molar.get() + 
                        self.mand_second_molar.get()) * 2  # Multiply by 2 for both sides
            
            # Maxillary interpretation
            maxillary_interpretation = []
            if max_sum < 60:
                maxillary_interpretation.append("Maxillary teeth are very small (sum <60mm)")
            elif max_sum < 90:
                maxillary_interpretation.append("Maxillary teeth are small (sum 60-90mm)")
            elif max_sum <= 140:
                maxillary_interpretation.append("Maxillary teeth are average-sized (sum 90-140mm)")
            elif max_sum <= 170:
                maxillary_interpretation.append("Maxillary teeth are large (sum 140-170mm)")
            else:
                maxillary_interpretation.append("Maxillary teeth are very large (sum >170mm)")
            
            # Mandibular interpretation
            mandibular_interpretation = []
            if mand_sum < 60:
                mandibular_interpretation.append("Mandibular teeth are very small (sum <60mm)")
            elif mand_sum < 90:
                mandibular_interpretation.append("Mandibular teeth are small (sum 60-90mm)")
            elif mand_sum <= 140:
                mandibular_interpretation.append("Mandibular teeth are average-sized (sum 90-140mm)")
            elif mand_sum <= 170:
                mandibular_interpretation.append("Mandibular teeth are large (sum 140-170mm)")
            else:
                mandibular_interpretation.append("Mandibular teeth are very large (sum >170mm)")
            
            # Arch comparison
            comparison = []
            difference = abs(max_sum - mand_sum)
            percentage_diff = (difference / ((max_sum + mand_sum)/2)) * 100
            
            if percentage_diff < 2:
                comparison.append("Maxillary and mandibular teeth are well proportioned (<2% difference)")
            elif max_sum > mand_sum:
                comparison.append(f"Maxillary teeth are larger than mandibular by {difference:.1f}mm ({percentage_diff:.1f}%)")
            else:
                comparison.append(f"Mandibular teeth are larger than maxillary by {difference:.1f}mm ({percentage_diff:.1f}%)")
            
            # Display results
            result_text = f"""MAXILLARY TEETH TOTAL WIDTH: {max_sum:.1f} mm
MANDIBULAR TEETH TOTAL WIDTH: {mand_sum:.1f} mm
ARCH SIZE DIFFERENCE: {difference:.1f} mm ({percentage_diff:.1f}%)

INTERPRETATION:
• {maxillary_interpretation[0]}
• {mandibular_interpretation[0]}
• {comparison[0]}

CLINICAL NOTES:
- Differences >5% may indicate significant tooth-size discrepancy
- Consider individual tooth sizes and positions in treatment planning
"""
            
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, result_text)
            
        except tk.TclError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def reset(self):
        # Reset maxillary teeth to ideal values
        self.max_central.set(8.5)
        self.max_lateral.set(6.5)
        self.max_canine.set(7.6)
        self.max_first_premolar.set(7.0)
        self.max_second_premolar.set(6.8)
        self.max_first_molar.set(10.0)
        self.max_second_molar.set(9.5)
        
        # Reset mandibular teeth to ideal values
        self.mand_central.set(5.0)
        self.mand_lateral.set(5.5)
        self.mand_canine.set(6.5)
        self.mand_first_premolar.set(7.0)
        self.mand_second_premolar.set(7.0)
        self.mand_first_molar.set(11.0)
        self.mand_second_molar.set(10.5)
        
        self.results_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SaninSavaraAnalysisApp(root)
    root.mainloop()