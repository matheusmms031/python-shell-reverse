import os
import psutil



def command_selector(command):
    command = command.strip()
    if command.startswith('system_hardware'):
        return system_hardware(command)

def system_hardware(data):
    state = data.replace('system_hardware', '').strip()
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

command = ''
while command.strip() != 'close':
    command = str(input('[x]>'))
    response = command_selector(command)
    print(response)