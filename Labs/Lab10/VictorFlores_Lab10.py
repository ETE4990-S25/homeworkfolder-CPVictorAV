import docker

client = docker.from_env()

def show_container_ip(container_name):
    container = client.containers.get(container_name)
    networks = container.attrs['NetworkSettings']['Networks']
    
    for net_name, net_data in networks.items():
        print(f"{container_name} in network '{net_name}' has IP: {net_data['IPAddress']}")




def container_scanner (container):
    Container_running = client.containers.get(container)

    if Container_running.status == 'running':
        return True
    else:
        return False

def restart_container (stopped_container):

    container_select = client.containers.get(stopped_container)

    container_select.restart()


show_container_ip("mysql")
show_container_ip("adminer")

if container_scanner("mysql") == True:

    print("Container is still running")

else:
    restart_container("mysql")
    print("The Container has restrted")

if container_scanner("adminer") == True:

    print("Container is still running")

else:
    restart_container("adminer")
    print("The Container has restrted")