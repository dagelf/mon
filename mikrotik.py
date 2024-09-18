import re
import subprocess

def ssh(host, command):
    ssh_command = ['ssh', host, command]
    result = subprocess.run(ssh_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return result.stdout

def parse(input_data):
    parse_pattern = re.compile(r'(\w[\w-]*)=([\w\./:-]+)')
    parsed_data = []
    for line in input_data.splitlines():
        matches = parse_pattern.findall(line)
        if matches:
            data = {key: value for key, value in matches}
            parsed_data.append(data)
    return parsed_data

def parse_file(file_path):
    return parse(open(file_path, 'r').read())

def parse_ssh(host, command):
    return parse(ssh(host,"/"+command+" print terse"))

host = '192.168.2.1'
health = parse_ssh(host,"sys health")

# you can paste the above in the Ptyhon REPL, just run `python` from the terminal and paste, no need for notebooks

>>> health
[ {'name': 'cpu-temperature', 'value': '55', 'type': 'C'}, 
  {'name': 'fan-state', 'value': 'ok'}, 
  {'name': 'fan1-speed', 'value': '4230', 'type': 'RPM'}, 
  {'name': 'fan2-speed', 'value': '4020', 'type': 'RPM'}, 
  {'name': 'board-temperature1', 'value': '34', 'type': 'C'}, 
  {'name': 'psu1-state', 'value': 'ok'}, 
  {'name': 'psu2-state', 'value': 'fail'} ]

>>> health[0]
{'name': 'cpu-temperature', 'value': '55', 'type': 'C'}

>>> health[0]['name']
'cpu-temperature'

>>> for a in health: print(a)
{'name': 'cpu-temperature', 'value': '55', 'type': 'C'}
{'name': 'fan-state', 'value': 'ok'}
{'name': 'fan1-speed', 'value': '4230', 'type': 'RPM'}
{'name': 'fan2-speed', 'value': '4020', 'type': 'RPM'}
{'name': 'board-temperature1', 'value': '34', 'type': 'C'}
{'name': 'psu1-state', 'value': 'ok'}
{'name': 'psu2-state', 'value': 'fail'}

>>> for a in health: print(a);
{'name': 'cpu-temperature', 'value': '55', 'type': 'C'}
{'name': 'fan-state', 'value': 'ok'}
{'name': 'fan1-speed', 'value': '4230', 'type': 'RPM'}
{'name': 'fan2-speed', 'value': '4020', 'type': 'RPM'}
{'name': 'board-temperature1', 'value': '34', 'type': 'C'}
{'name': 'psu1-state', 'value': 'ok'}
{'name': 'psu2-state', 'value': 'fail'}


>>> for a in health: print(a['name'],a['value'],a.get('type','')); # a.get gives a default value if the element isn't present
cpu-temperature 55 C
fan-state ok 
fan1-speed 4230 RPM
fan2-speed 4020 RPM
board-temperature1 34 C
psu1-state ok 
psu2-state fail 

>>> for a in filter(lambda i: 'type' in i and 'C' in i['type'], health): print(a)
{'name': 'cpu-temperature', 'value': '54', 'type': 'C'}
{'name': 'board-temperature1', 'value': '33', 'type': 'C'}

