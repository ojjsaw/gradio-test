import requests

def detect_gradio_app(request):
    headers = request.headers
    if 'gradio-app-id' in headers:
        return True
    payload = request.json
    if 'app_id' in payload:
        return True
    ip_address = request.remote_addr
    if ip_address == '127.0.0.1':
        return True
    return False

if __name__ == '__main__':
    request = requests.get('http://127.0.0.1:7860')
    print(request.headers)
    #is_gradio_app = detect_gradio_app(request)
    #print(is_gradio_app)