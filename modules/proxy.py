import requests
def proxy(ip, port, protocol, user=None, passw=None):
    if protocol == 'http':
        if user == None and passw == None:
            proxy = {'http': f'http://{ip}:{port}'}
        else:
            proxy = {'http': f'http://{user}:{passw}@{ip}:{port}'}
    elif protocol == 'https':
        if user == None and passw == None:
            proxy = {'https': f'https://{ip}:{port}'}
        else:
            proxy = {'https': f'https://{user}:{passw}@{ip}:{port}'}
    elif protocol == 'socks4':
        if user == None and passw == None:
            proxy = {'socks4': f'socks4://{ip}:{port}'}
        else:
            proxy = {'socks4': f'socks4://{user}:{passw}@{ip}:{port}'}
    elif protocol == 'socks5':
        if user == None and passw == None:
            proxy = {'socks5': f'socks5://{ip}:{port}'}
        else:
            proxy = {'socks5': f'socks5://{user}:{passw}@{ip}:{port}'}
    return proxy