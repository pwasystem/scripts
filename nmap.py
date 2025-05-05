import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import threading

class NmapScannerApp:
    def __init__(self, root):
        self.root = root
        root.title("Nmap Scanner")
        
        self.criar_componentes()
        self.scan_types = {
            'Quick Scan': '-T4 -F',
            'Full Scan': '-p- -sV -sC -A',
            'Service Detection': '-sV',
            'OS Detection': '-O'
        }
    
    def criar_componentes(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Entrada do alvo
        ttk.Label(main_frame, text="Domínio/IP:").grid(row=0, column=0, sticky=tk.W)
        self.target_entry = ttk.Entry(main_frame, width=30)
        self.target_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        
        # Tipos de varredura
        ttk.Label(main_frame, text="Tipo de Varredura:").grid(row=1, column=0, sticky=tk.W)
        self.scan_type = tk.StringVar()
        
        row = 2
        for scan in ['Quick Scan', 'Full Scan', 'Service Detection', 'OS Detection']:
            rb = ttk.Radiobutton(main_frame, text=scan, variable=self.scan_type, value=scan)
            rb.grid(row=row, column=0, columnspan=3, sticky=tk.W)
            row += 1
        
        # Botões
        self.btn_scan = ttk.Button(main_frame, text="Iniciar Varredura", command=self.iniciar_varredura)
        self.btn_scan.grid(row=row, column=0, pady=10)
        
        self.btn_save = ttk.Button(main_frame, text="Salvar Resultados", command=self.salvar_resultados)
        self.btn_save.grid(row=row, column=1, pady=10)
        
        # Área de resultados
        self.result_text = tk.Text(main_frame, wrap=tk.WORD, width=60, height=20)
        self.result_text.grid(row=row+1, column=0, columnspan=3, pady=10)
        
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=row+1, column=3, sticky=(tk.N, tk.S))
        self.result_text['yscrollcommand'] = scrollbar.set
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def executar_comando_nmap(self, target, options):
        try:
            comando = ['nmap', *options.split(), target]
            resultado = subprocess.run(
                comando,
                capture_output=True,
                text=True,
                check=True
            )
            return resultado.stdout
        except subprocess.CalledProcessError as e:
            return f"Erro: {e.stderr}"
        except Exception as e:
            return f"Erro inesperado: {str(e)}"
    
    def iniciar_varredura(self):
        target = self.target_entry.get()
        scan_type = self.scan_type.get()
        
        if not target:
            messagebox.showwarning("Aviso", "Digite um domínio ou IP!")
            return
        if not scan_type:
            messagebox.showwarning("Aviso", "Selecione um tipo de varredura!")
            return
        
        options = self.scan_types[scan_type]
        
        self.btn_scan.config(state=tk.DISABLED)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Iniciando varredura {scan_type}...\n")
        
        def thread_varredura():
            resultado = self.executar_comando_nmap(target, options)
            self.root.after(0, self.atualizar_resultados, resultado)
            self.btn_scan.config(state=tk.NORMAL)
        
        threading.Thread(target=thread_varredura, daemon=True).start()
    
    def atualizar_resultados(self, resultado):
        self.result_text.insert(tk.END, "\nResultado da varredura:\n")
        self.result_text.insert(tk.END, resultado)
        self.result_text.see(tk.END)
    
    def salvar_resultados(self):
        conteudo = self.result_text.get(1.0, tk.END)
        if not conteudo.strip():
            messagebox.showwarning("Aviso", "Nenhum resultado para salvar!")
            return
        
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de Texto", "*.txt")]
        )
        
        if arquivo:
            try:
                with open(arquivo, 'w') as f:
                    f.write(conteudo)
                messagebox.showinfo("Sucesso", "Resultados salvos com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NmapScannerApp(root)
    root.mainloop()