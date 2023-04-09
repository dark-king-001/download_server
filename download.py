# import Worker as wk
import os
download_server_connections = 8
print(f'server conncetions opened : {download_server_connections}')
chunk_size = 100 #mbs
print(f'chunk_size : {chunk_size}')
# wk.Worker('/home/piyush/Desktop/SystemControl/download_server/download/aria2c.exe' + f'-x{download_server_connections} ' + f' -k{chunk_size}M ' + ' ' + input('Enter Download Link : '))
os.system('aria2c' + f' -x{download_server_connections} ' + f' -k{chunk_size}M ' + ' ' + input('Enter Download Link : '))
