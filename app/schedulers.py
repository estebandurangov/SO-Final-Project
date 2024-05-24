def RR(process_times, q):
    n = len(process_times)
    remaining_times = list(process_times)
    wait_times = [0] * n
    response_times = [-1] * n
    turnaround_times = [0] * n
    current_time = 0
    queue = list(range(n))  # Lista de índices de procesos

    while queue:
        # Rotar la cola de procesos
        current_process = queue.pop(0)
        if response_times[current_process] == -1:
            response_times[current_process] = current_time

        # Calcular el tiempo de ejecución
        time_slice = min(q, remaining_times[current_process])
        remaining_times[current_process] -= time_slice
        current_time += time_slice

        # Actualizar tiempos de espera
        for j in queue:
            wait_times[j] += time_slice

        # Si el proceso aún necesita más tiempo, vuelve a la cola
        if remaining_times[current_process] > 0:
            queue.append(current_process)
        else:
            turnaround_times[current_process] = current_time

    return prom(response_times), prom(turnaround_times), prom(wait_times)

def SJF(process_times):
    n = len(process_times)
    wait_times = [0] * n
    response_times = [-1] * n
    turnaround_times = [0] * n
    current_time = 0

    # Crear lista de procesos con sus índices y tiempos
    processes = sorted(list(enumerate(process_times)), key=lambda x: x[1])

    for process in processes:
        process_id, process_time = process
        if response_times[process_id] == -1:
            response_times[process_id] = current_time

        # Ejecutar el proceso hasta su finalización
        current_time += process_time
        turnaround_times[process_id] = current_time
        wait_times[process_id] = turnaround_times[process_id] - process_time

    return prom(response_times), prom(turnaround_times), prom(wait_times)

def MLQ(process_times):
    n = len(process_times)
    short_queue = []
    long_queue = []
    threshold = sum(process_times) / len(process_times)  # Media como umbral

    # Clasificar procesos en colas
    for i, time in enumerate(process_times):
        if time <= threshold:
            short_queue.append((i, time))
        else:
            long_queue.append((i, time))

    queues = [short_queue, long_queue]
    response_times = [-1] * n
    wait_times = [0] * n
    turnaround_times = [0] * n
    current_time = 0

    for queue in queues:
        for process in queue:
            process_id, process_time = process
            if response_times[process_id] == -1:
                response_times[process_id] = current_time

            current_time += process_time
            turnaround_times[process_id] = current_time
            wait_times[process_id] = turnaround_times[process_id] - process_time

    return prom(response_times), prom(turnaround_times), prom(wait_times)


def prom(list):
    return round((sum(list) / len(list)),2)