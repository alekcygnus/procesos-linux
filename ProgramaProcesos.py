#Python 3 
import matplotlib.pyplot as plt
import networkx as nx
import sys
import subprocess
import psutil
import numpy as np

def opcion1():
    
    process = subprocess.run(
            ['pstree'], capture_output=True)
    
    print(process.stdout.decode())


def option2():
    G = nx.DiGraph()
    process_count = 0
    max_process_count = 10

    for process in psutil.process_iter(['pid', 'ppid', 'name']):
        if process_count >= max_process_count:
            break

        pid = process.info['pid']
        ppid = process.info['ppid']
        G.add_node(pid, label=f"{process.info['name']} (PID: {pid})")
        if ppid != 0:
            G.add_edge(ppid, pid)
        process_count += 1 

    pos = nx.spring_layout(G)

    label_names = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
    nx.draw_networkx_labels(G, pos, labels=label_names, font_size=10)

    plt.title("Map of processes with their PID")
    plt.show()




def option3():
    G = nx.DiGraph()
    process_count = 0
    max_process_count = 10

    for process in psutil.process_iter(['pid', 'ppid', 'name']):
        if process_count >= max_process_count:
            break

        pid = process.info['pid']
        ppid = process.info['ppid']
        G.add_node(pid, label=f"{process.info['name']} ({pid})")
        if ppid != 0:
            G.add_edge(ppid, pid)
        process_count += 1 

    pos = nx.spring_layout(G)

    label_names = nx.get_node_attributes(G, 'label')

    number_nodes = G.number_of_nodes()
    colors = plt.cm.rainbow(np.linspace(0, 1, number_nodes))

    nx.draw_networkx_nodes(G, pos, node_size=500, node_color=colors)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
    nx.draw_networkx_labels(G, pos, labels=label_names, font_size=10)

    plt.title("Map of processes with their PID and colors")
    plt.show()


def option4():
    process = subprocess.run(
            ['ps', 'eo', 'pid,comm,state,user,etime,%cpu,%mem'], capture_output=True)
    print(process.stdout.decode())

def exit():
    print("exit the program")
    exit()

def menu():
    while True:
        print("Menu de opciones")
        print("1. Opcion 1 ver lista de procesos en forma de arbol")
        print("2. Opcion 2 ver procesos del sistema en un grafico enlazado")
        print("3. Opcion 3 ver grafico con cada nodo de colores diferentes")
        print("4. Opcion 4 ver tabla con informacion detallada de los procesos")
        print("5. Exit")


        selection = input("Select an option: ")

        if selection == "1":
            opcion1()
        elif selection == "2":
            option2()
        elif selection == "3":
            option3()
        elif selection == "4":
            option4()
        elif selection == "5":
            sys.exit(0)
        else: 
            print("Invalid option try again")

menu()
