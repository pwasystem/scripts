import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import socket
import ipaddress
import threading

class IPScannerApp:
    def __init__(self, root):
        self.root = root
        root.title("IP Scanner")
        
        # Cria elementos da interface
        self.criar_componentes()
    
    def criar_componentes(self):
        # Frame para entrada de dados
        frame_entrada = ttk.Frame(self.root, padding="10")
        frame_entrada.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Campos para IP inicial e final
        ttk.Label(frame_entrada, text="IP Inicial:").grid(row=0, column=0, sticky=tk.W)
        self.entrada_ip_inicial = ttk.Entry(frame_entrada, width=15)
        self.entrada_ip_inicial.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        ttk.Label(frame_entrada, text="IP Final:").grid(row=1, column=0, sticky=tk.W)
        self.entrada_ip_final = ttk.Entry(frame_entrada, width=15)
        self.entrada_ip_final.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        # Botão de iniciar varredura
        self.botao_varredura = ttk.Button(frame_entrada, text="Iniciar Varredura", command=self.iniciar_varredura)
        self.botao_varredura.grid(row=0, column=2, rowspan=2, padx=10)
        
        # Área de texto para resultados
        self.texto_resultados = tk.Text(self.root, wrap=tk.WORD, width=50, height=20)
        self.texto_resultados.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para a área de texto
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.texto_resultados.yview)
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.texto_resultados['yscrollcommand'] = scrollbar.set
        
        # Botão para salvar resultados
        self.botao_salvar = ttk.Button(self.root, text="Salvar Resultados", command=self.salvar_resultados)
        self.botao_salvar.grid(row=2, column=0, pady=10)
        
        # Configuração de dimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
    
    def validar_ip(self, ip):
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False
    
    def iniciar_varredura(self):
        ip_inicial = self.entrada_ip_inicial.get()
        ip_final = self.entrada_ip_final.get()
        
        if not self.validar_ip(ip_inicial) or not self.validar_ip(ip_final):
            messagebox.showerror("Erro", "Endereço IP inválido.")
            return
        
        try:
            inicio = ipaddress.IPv4Address(ip_inicial)
            fim = ipaddress.IPv4Address(ip_final)
        except:
            messagebox.showerror("Erro", "Endereço IP inválido.")
            return
        
        if inicio > fim:
            messagebox.showerror("Erro", "O IP inicial deve ser menor ou igual ao IP final.")
            return
        
        self.botao_varredura.config(state=tk.DISABLED)
        self.texto_resultados.delete(1.0, tk.END)
        
        def executar_varredura():
            resultados = []
            ip_atual = inicio
            while ip_atual <= fim:
                ip_str = str(ip_atual)
                try:
                    socket.setdefaulttimeout(2)
                    hostname, _, _ = socket.gethostbyaddr(ip_str)
                    resultados.append(f"{ip_str} - {hostname}")
                except (socket.herror, socket.timeout, socket.gaierror):
                    pass
                except Exception as e:
                    print(f"Erro em {ip_str}: {e}")
                ip_atual += 1
            
            self.root.after(0, self.atualizar_interface, resultados)
        
        threading.Thread(target=executar_varredura, daemon=True).start()
    
    def atualizar_interface(self, resultados):
        if resultados:
            self.texto_resultados.insert(tk.END, "\n".join(resultados) + "\n")
        else:
            self.texto_resultados.insert(tk.END, "Nenhum IP ativo com domínio encontrado.\n")
        self.botao_varredura.config(state=tk.NORMAL)
    
    def salvar_resultados(self):
        conteudo = self.texto_resultados.get(1.0, tk.END)
        if not conteudo.strip():
            messagebox.showwarning("Aviso", "Nenhum dado para salvar.")
            return
        
        caminho = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de Texto", "*.txt")]
        )
        if caminho:
            try:
                with open(caminho, "w") as arquivo:
                    arquivo.write(conteudo)
                messagebox.showinfo("Sucesso", "Resultados salvos com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar: {e}")

if __name__ == "__main__":
    janela = tk.Tk()
    app = IPScannerApp(janela)
    janela.mainloop()