echo "Hello, world!"
Xvfb :0 -screen 0 1280x768x24&
uvicorn api:app --proxy-headers --host 0.0.0.0 --port 80