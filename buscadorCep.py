from tkinter import *
from tkinter import messagebox
import requests

def get_endereço():
    cep = entry_cep.get()
    cep = cep.replace("-","").replace(" ","").replace(".","")
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        response = requests.get(url)
        data = response.json()
        if 'erro' not in data:
            lbl_logradouro.config(text=data['logradouro'])
            lbl_bairro.config(text=data['bairro'])
            lbl_cidade.config(text=data['localidade'])
            lbl_estado.config(text=data['uf'])
        else:
            messagebox.showerror("Erro", "CEP não encontrado")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("ERRO","Formato de CEP Invalido")

# Criando a janela
tabela = Tk()
tabela.title("Consulta de CEP")
tabela.geometry("400x200")
tabela.iconbitmap("assets/placeholder.ico")

# Definindo cores
cor_verde = "#ADF0CD"  # Verde claro
cor_amarelo = "#FFD700"  # Amarelo

# Estilizando
tabela.configure(bg=cor_verde)

# Criando os widgets
lbl_cep = Label(tabela, text="Digite o CEP:", bg=cor_verde)
lbl_cep.grid(row=0, column=0, padx=10, pady=10)

entry_cep = Entry(tabela)
entry_cep.grid(row=0, column=1, padx=10, pady=10)

btn_buscar = Button(tabela, text="Buscar", command=get_endereço, bg=cor_amarelo)
btn_buscar.grid(row=0, column=2, padx=10, pady=10)

txt_logradouro = Label(tabela, text="Logradouro:", bg=cor_verde)
txt_logradouro.grid(row=1, column=0, padx=10, pady=5)
lbl_logradouro = Label(tabela, text="", bg=cor_verde)
lbl_logradouro.grid(row=1, column=1, padx=10, pady=5)

txt_bairro = Label(tabela, text="Bairro:", bg=cor_verde)
txt_bairro.grid(row=2, column=0, padx=10, pady=5)
lbl_bairro = Label(tabela, text="", bg=cor_verde)
lbl_bairro.grid(row=2, column=1, padx=10, pady=5)

txt_cidade = Label(tabela, text="Cidade:", bg=cor_verde)
txt_cidade.grid(row=3, column=0, padx=10, pady=5)
lbl_cidade = Label(tabela, text="", bg=cor_verde)
lbl_cidade.grid(row=3, column=1, padx=10, pady=5)

txt_estado = Label(tabela, text="Estado:", bg=cor_verde)
txt_estado.grid(row=4, column=0, padx=10, pady=5)
lbl_estado = Label(tabela, text="", bg=cor_verde )
lbl_estado.grid(row=4, column=1, padx=10, pady=5)

# Executando a janela
tabela.mainloop()
