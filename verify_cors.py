import requests

def test_options(url, origin):
    print(f"Testing OPTIONS {url} with Origin {origin}...")
    try:
        response = requests.options(url, headers={
            "Origin": origin,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "Content-Type"
        })
        print(f"Status: {response.status_code}")
        # print(f"Headers: {response.headers}")
        if response.status_code in [200, 204]:
            print("SUCCESS: Preflight handled correctly.")
        else:
            print("FAILURE: Preflight returned error status.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    urls = ["http://127.0.0.1:8000/auth/signup", "http://127.0.0.1:8000/story/generate-comic"]
    origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:3000",
        "http://127.0.0.1:8080"
    ]
    for url in urls:
        for origin in origins:
            test_options(url, origin)
