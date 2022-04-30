import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-QBR6RNK;"
    "Database=Caique;"
)

conn = pyodbc.connect(dados_conexao)
cursor = conn.cursor()

def register(user, email, address):
    cursor.execute(f"insert into Alunos values ('{user}', '{email}', '{address}')" ), 
    conn.commit()

def getRegisters():
    search = cursor.execute("select * from Alunos")  
    dados = search.fetchall()
    data = []
    
    for i in dados:
        data.append(i)
        
    return str(data)