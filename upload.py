from app import app
wsgi_app = app.wsgi_app
if __name__ == '__main__':
    app.run(port = 5000, debug = True)