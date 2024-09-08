import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ups_api import UPSApi
from pdf_generator import PDFGenerator

class Application(tk.Frame):
    def __init__(self, master=None, logger=None):
        super().__init__(master)
        self.master = master
        self.logger = logger
        self.ups_api = UPSApi(logger)
        self.pdf_generator = PDFGenerator(logger)
        
        self.master.title("UPS Proof of Delivery Retriever")
        self.master.geometry("500x300")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Tracking Numbers Input
        self.tracking_label = ttk.Label(self, text="Tracking Numbers (one per line):")
        self.tracking_label.pack(pady=(20, 5))
        self.tracking_text = tk.Text(self, width=40, height=5)
        self.tracking_text.pack()

        # Retrieve Button
        self.retrieve_button = ttk.Button(self, text="Retrieve PODs", command=self.retrieve_pods)
        self.retrieve_button.pack(pady=20)

        # Status Label
        self.status_label = ttk.Label(self, text="")
        self.status_label.pack()

    def retrieve_pods(self):
        tracking_numbers = self.tracking_text.get("1.0", tk.END).strip().split("\n")
        tracking_numbers = [tn.strip() for tn in tracking_numbers if tn.strip()]
        
        if not tracking_numbers:
            messagebox.showerror("Error", "Please enter at least one tracking number.")
            return

        self.status_label.config(text="Retrieving POD data...")
        self.update_idletasks()

        output_dir = filedialog.askdirectory(title="Select output directory for PDFs")
        if not output_dir:
            self.status_label.config(text="PDF generation cancelled.")
            return

        success_count = 0
        for tracking_number in tracking_numbers:
            try:
                # Retrieve POD data
                pod_data = self.ups_api.get_proof_of_delivery(tracking_number)

                # Generate PDF
                output_path = f"{output_dir}/{tracking_number}.pdf"
                self.pdf_generator.generate_pdf(pod_data, output_path)
                success_count += 1
            except Exception as e:
                self.logger.error(f"Error retrieving POD for {tracking_number}: {str(e)}")

        self.status_label.config(text=f"Generated {success_count} out of {len(tracking_numbers)} POD PDFs.")
        messagebox.showinfo("Success", f"Generated {success_count} out of {len(tracking_numbers)} POD PDFs.\nSaved to: {output_dir}")

        self.tracking_text.delete("1.0", tk.END)
