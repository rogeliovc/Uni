import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class CodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Código")
        self.root.geometry("800x600")
        self.current_file = None
        
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')
        
        self.editor_frame = ttk.Frame(self.main_frame)
        self.editor_frame.pack(expand=True, fill='both', padx=5, pady=5)
        
        self.line_numbers = tk.Text(self.editor_frame, width=4, padx=3, pady=5,
                                   background='#e0e0e0', foreground='#666666',
                                   font=('Consolas', 11), state='disabled',
                                   wrap=tk.NONE, cursor='arrow')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        
        self.text_area = tk.Text(self.editor_frame, wrap=tk.WORD, font=('Consolas', 11), 
                               background='#f0f0f0', foreground='#000000',
                               insertbackground='black', selectbackground='#a6d2ff',
                               padx=10, pady=10, yscrollcommand=self.on_textscroll)
        self.text_area.pack(side=tk.LEFT, expand=True, fill='both')
        
        self.scrollbar = ttk.Scrollbar(self.editor_frame, orient='vertical',
                                command=self.on_scrollbar)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_area.config(yscrollcommand=self.on_textscroll)
        
        self.status_bar = ttk.Frame(self.root)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.status_label = ttk.Label(self.status_bar, text="Listo", relief=tk.SUNKEN)
        self.status_label.pack(side=tk.LEFT, padx=2)
        
        self.file_info_label = ttk.Label(self.status_bar, text="", relief=tk.SUNKEN)
        self.file_info_label.pack(side=tk.RIGHT, padx=2)
        
        self.text_area.bind('<KeyRelease>', self.on_key_release)
        self.text_area.bind('<MouseWheel>', self.on_mousewheel)
        
        self.update_line_numbers()
        self.setup_menu()
    
    def update_line_numbers(self):
        self.line_numbers.config(state='normal')
        self.line_numbers.delete(1.0, tk.END)
        line_count = int(self.text_area.index('end-1c').split('.')[0])
        line_numbers_text = '\n'.join(str(i) for i in range(1, line_count + 1))
        self.line_numbers.insert(1.0, line_numbers_text)
        self.line_numbers.config(state='disabled')
    
    def on_textscroll(self, *args):
        self.scrollbar.set(*args)
        self.line_numbers.yview_moveto(args[0])
    
    def on_scrollbar(self, *args):
        self.text_area.yview(*args)
        self.line_numbers.yview_moveto(args[0])
    
    def on_key_release(self, event=None):
        self.update_line_numbers()
        self.update_status()
    
    def on_mousewheel(self, event=None):
        self.update_line_numbers()
    
    def update_status(self):
        try:
            content = self.text_area.get(1.0, tk.END)
            char_count = len(content) - 1
            line_count = content.count('\n')
            status_text = f"Caracteres: {char_count} | Líneas: {line_count}"
            self.status_label.config(text=status_text)
        except:
            self.status_label.config(text="Listo")
    
    def update_file_info(self):
        if self.current_file:
            filename = os.path.basename(self.current_file)
            file_size = os.path.getsize(self.current_file) if os.path.exists(self.current_file) else 0
            file_info = f"{filename} | {file_size} bytes"
        else:
            file_info = "Sin guardar"
        self.file_info_label.config(text=file_info)
    
    def setup_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Nuevo", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Abrir...", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Guardar", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Guardar como...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)
        
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Deshacer", accelerator="Ctrl+Z", command=lambda: self.text_area.event_generate("<<Undo>>"))
        edit_menu.add_command(label="Rehacer", accelerator="Ctrl+Y", command=lambda: self.text_area.event_generate("<<Redo>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Cortar", accelerator="Ctrl+X", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copiar", accelerator="Ctrl+C", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Pegar", accelerator="Ctrl+V", command=lambda: self.text_area.event_generate("<<Paste>>"))
        
        run_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ejecutar", menu=run_menu)
        run_menu.add_command(label="Ejecutar", accelerator="F5")
        run_menu.add_command(label="Depurar", accelerator="F6")
        run_menu.add_command(label="Compilar", accelerator="F9")
        
        compiler_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Compiladores", menu=compiler_menu)
        compiler_menu.add_command(label="Seleccionar compilador...")
        compiler_menu.add_separator()
        
        variables_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Variables", menu=variables_menu)
        variables_menu.add_command(label="Ver variables")
        variables_menu.add_command(label="Administrar variables")
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Ayuda", command=self.show_help)
        help_menu.add_command(label="Acerca de...", command=self.show_about)
        
        self.setup_shortcuts()
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("Nuevo archivo - Editor de Código")
        self.update_line_numbers()
        self.update_file_info()
        self.update_status()
    
    def open_file(self):
        file_types = [("Archivos Python", "*.py"), ("Archivos Java", "*.java"), ("Archivos C++", "*.cpp"), ("Archivos C", "*.c"), ("Archivos HTML", "*.html"), ("Archivos CSS", "*.css"), ("Archivos JavaScript", "*.js"), ("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        
        file_path = filedialog.askopenfilename(filetypes=file_types)
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, file.read())
                self.current_file = file_path
                self.root.title(f"{file_path} - Editor de Código")
                self.update_line_numbers()
                self.update_file_info()
                self.update_status()
                self.status_label.config(text=f"Archivo abierto: {os.path.basename(file_path)}")
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        self.text_area.delete(1.0, tk.END)
                        self.text_area.insert(1.0, file.read())
                    self.current_file = file_path
                    self.root.title(f"{file_path} - Editor de Código")
                    self.update_line_numbers()
                    self.update_file_info()
                    self.update_status()
                    self.status_label.config(text=f"Archivo abierto: {os.path.basename(file_path)}")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")
    
    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Guardado", f"Archivo guardado: {self.current_file}")
                self.update_file_info()
                self.status_label.config(text=f"Archivo guardado: {os.path.basename(self.current_file)}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        else:
            self.save_file_as()
    
    def save_file_as(self):
        file_types = [("Archivos Python", "*.py"), ("Archivos Java", "*.java"), ("Archivos C++", "*.cpp"), ("Archivos C", "*.c"), ("Archivos HTML", "*.html"), ("Archivos CSS", "*.css"), ("Archivos JavaScript", "*.js"), ("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        
        file_path = filedialog.asksaveasfilename(filetypes=file_types)
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path
                self.root.title(f"{file_path} - Editor de Código")
                messagebox.showinfo("Guardado", f"Archivo guardado: {file_path}")
                self.update_file_info()
                self.status_label.config(text=f"Archivo guardado: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    
    def show_help(self):
        messagebox.showinfo("Ayuda", "Editor de código básico\n\n"
                                  "Archivo: Nuevo, Abrir, Guardar archivos\n"
                                  "Editar: Funciones básicas de edición\n"
                                  "Atajos:\n"
                                  "Ctrl+N: Nuevo | Ctrl+O: Abrir | Ctrl+S: Guardar")
    
    def setup_shortcuts(self):
        self.root.bind_all('<Control-n>', lambda e: self.new_file())
        self.root.bind_all('<Control-o>', lambda e: self.open_file())
        self.root.bind_all('<Control-s>', lambda e: self.save_file())
        self.root.bind_all('<Control-z>', lambda e: self.text_area.event_generate("<<Undo>>"))
        self.root.bind_all('<Control-y>', lambda e: self.text_area.event_generate("<<Redo>>"))
        self.root.bind_all('<Control-x>', lambda e: self.text_area.event_generate("<<Cut>>"))
        self.root.bind_all('<Control-c>', lambda e: self.text_area.event_generate("<<Copy>>"))
        self.root.bind_all('<Control-v>', lambda e: self.text_area.event_generate("<<Paste>>"))
    
    def show_about(self):
        messagebox.showinfo("Acerca de", "Editor de Código v1.0\n\n"
                                      "Editor simple con Tkinter")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeEditor(root)
    root.mainloop()