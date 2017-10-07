import nmap

nm = nmap.PortScanner()
print (nm.nmap_version())

nm.scan('x.x.xx.xxx', '1-1024', '-v')
print(nm.scaninfo())
print(nm.csv())
