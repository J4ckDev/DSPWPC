#!/usr/bin/python3

import nmap

def clean_string(string_value):
    string_value.strip()
    string_value = string_value.replace("\t","-")
    string_value = string_value.replace(" ","")
    return string_value.replace("\n", "|")     

nmap_port_scanner = nmap.PortScanner()

ip_to_scan = '172.17.0.2'

ports_to_scan = '10, 20, 21, 80, 25'

aditional_parameters = "-O -sS"

scan_result = nmap_port_scanner.scan(ip_to_scan, ports_to_scan, aditional_parameters)
os_info = scan_result['scan'][ip_to_scan]['osmatch'][0]
os_class = "Clase(s) de sistema(s)\n"
for osclass in os_info['osclass']:
    os_class += f"CPE: {osclass['cpe'][0]}\n"

filtered_info = (
    f"OS Info - Detectado con {os_info['accuracy']}% de probabilidad\n" 
    f"Nombre: {os_info['name']}\n"
    f"{os_class}\n"
    "Información de los puertos abiertos detectados\n"  
    "----------------------------------------------------------\n"  
)

for port, port_data in scan_result['scan'][ip_to_scan]['tcp'].items():
    if port_data['state'] == 'open':
        result_port_info = nmap_port_scanner.scan(ip_to_scan, f"{port}", "-sCV")
        result_port_info = result_port_info['scan'][ip_to_scan]['tcp'][port]
        filtered_info += (
            "Puerto\tNombre\tProducto\tCPE\n"
            f"{port}\t{result_port_info['name']}\t{clean_string(result_port_info['product'])}\t{clean_string(result_port_info['cpe'])}\n"
        )
        if "script" in result_port_info:
            filtered_info += (
                "----------------------------------------------------------\n"
                "Nombre Script\t\tDescripción\n"
            )
            for script_name, description in result_port_info['script'].items():
                filtered_info += f"{clean_string(script_name)}\t\t{clean_string(description)}\n"
        filtered_info += "----------------------------------------------------------\n"

print(filtered_info)