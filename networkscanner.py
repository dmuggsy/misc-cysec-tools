from socket import *
import time

start_time = time.time()

if __name__ == "__main__":
    target = input('please enter a host name to scan: ')
    protocol = input('Do you want to scan UDP ports too?')
    t_ip = gethostbyname(target)
    print("starting scan on ", target)

#Set port range before use, refer to doc "common_ports" for a good starting point
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        us = socket(AF_INET, SOCK_DGRAM)

        con = s.connect_ex((t_ip, i))
        scon = us.connect_ex((t_ip, i))
        
        
        if(con == 0):
            try:
                service_name = getservbyport(i, 'tcp')
                print(f'Port {i}: OPEN (TCP), Service: {service_name}')
            except OSError:
                print(f'Port {i}: OPEN (TCP), Service: Unknown')
        s.close()

        if(scon == 0) and (protocol == 'yes' ):
            try:
                service_name = getservbyport(i, 'udp')
                print(f'Port {i}: OPEN (UDP), Service: {service_name}')
            except OSError:
                pass
        us.close()
        
print("time taken: ", time.time() - start_time)