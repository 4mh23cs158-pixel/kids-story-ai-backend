import socket

hosts = [
    'aws-1-us-east-1.pooler.supabase.com',
    'aws-0-us-east-1.pooler.supabase.com',
    'db.aszieyjucvzehepfdnaw.supabase.co',
    'google.com'
]

for host in hosts:
    try:
        ip = socket.gethostbyname(host)
        print(f"{host}: {ip}")
    except socket.gaierror as e:
        print(f"{host}: Failed ({e})")
