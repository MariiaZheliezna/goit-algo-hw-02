from queue import Queue

def generate_request(q:Queue):
    request = ' '
    while request:
        request = input('Input new request for que, or press Enter to stop >>>')
        if request != '':
            q.put(request)
    return q

def process_request(q:Queue):
    if q.empty():
        print('черга пуста')
    while not q.empty():
        print(f'Request "{q.get()}" processed sucessfully! Que size: {len(q.queue)}')
    return q

q = Queue()
exit = True
while exit:
    q = generate_request(q)
    q = process_request(q)
    exit = input('>>> Continue? Press Enter to stop >>>')