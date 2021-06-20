import socket
import os
import psutil


def dir(code):
  lista = '<------------------------------>\n'
  caminho = os.scandir()
  files = {}
  for diretorio in caminho:
    files[diretorio.name] = diretorio.stat().st_size
    espace = len(str(files[max(files, key=files.get)])) + 5
    lista += 'Size' + ' ' * (espace - 4) + 'Name' + '\n\n'
    for file in files:
        tamanho = len(str(files[file]))
        espace_total = ' ' * (espace - tamanho)
        lista += str(files[file]) + str(espace_total) + str(file) + '\n'
        lista += '\n<------------------------------>'
        if code == True:
            return lista.encode()
        if code == False:
            return lista


def cd(data):
    try:
        repository = data.replace('cd', '').strip()
        os.chdir(repository)
        return 'Diretorio acessado com sucesso'
    except:
        return 'Algum erro ocorreu'


def mkdir(data):
    name = data.replace('mkdir', '').strip()
    os.mkdir(name)
    return 'Pasta criada com sucesso'


def pwd():
    diretory = os.getcwd()
    return '<------------------------------>\n' + diretory + '\n<------------------------------>'


def rmdir(data):
    try:
        name = data.replace('rmdir', '').strip()
        os.rmdir(name)
        return 'Pasta excluida com sucesso'
    except:
        return 'Algum erro ocorreu'


def system(data):
    state = data.replace('system', '').strip()
    memory_disk = psutil.disk_usage('/')
    cpu_percent = psutil.cpu_percent()
    cpu_stat = psutil.cpu_stats()
    cpu_freq = psutil.cpu_freq()
    memory_ram = psutil.virtual_memory()
    users = psutil.users()
    response = ''
    if state == 'computer-info':
        response = f"""

              CPUs              =   {psutil.cpu_count()}
              CPU FREQUENCY MIN =   {cpu_freq.min} GHz
              CPU FREQUENCY MAX =   {cpu_freq.max} GHz
              
              MEMORY DISC TOTAL =   {(memory_disk.total/1000000000):.3f} Gb
              MEMORY DISC USED  =   {(memory_disk.used/1000000000):.3f} Gb
              MEMORY DISC FREE  =   {(memory_disk.free/1000000000):.3f} Gb

              MEMORY RAM TOTAL  =   {(memory_ram.total/1000000000):.3f} Gb
              MEMORY RAM USED   =   {(memory_ram.used/1000000000):.3f} Gb
              MEMORY RAM FREE   =   {(memory_ram.free/1000000000):.3f} Gb

              """
    if state == 'user-info':
        for user in users:
            response += f'\n\n              USER = {user.name}    TERMINAL = {user.terminal}   HOST = {user.host}   PID = {user.pid}\n'
        response += '\n'

    if state == 'cpu-stat':
        response = f"""

            PERCENT             =   {cpu_percent} %
            FREQUENCY           =   {cpu_freq.current} GHz

                CTX SWITCHES    =   {cpu_stat.ctx_switches}
                INTERRUPTS      =   {cpu_stat.interrupts}
                SOFT INTERRUPTS =   {cpu_stat.soft_interrupts}
                SYSCALLS        =   {cpu_stat.syscalls}

        """

    return response


while True:
    HOST = ''
    PORT = 4000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    conn, ender = s.accept()
    print(f'Conectado com {ender[0]}')
    while True:
        resposta = conn.recv(500000)
        resposta_decode = resposta.decode()
        total = 'NENHUM COMANDO ENCONTRADO'
        if resposta_decode.startswith('dir'):
            lista = dir(False)
            total = lista
        if resposta_decode.startswith('cd'):
            total = cd(resposta_decode)
        if resposta_decode.strip() == 'pwd':
            total = pwd()
        if resposta_decode.strip().startswith('mkdir'):
            total = mkdir(resposta_decode)
        if resposta_decode.strip().startswith('rmdir'):
            total = rmdir(resposta_decode)
        if resposta_decode.strip().startswith('system'):
            total = system(resposta_decode)
        if resposta_decode.strip() == 'close':
            conn.close()
            break
        conn.send(total.encode())
