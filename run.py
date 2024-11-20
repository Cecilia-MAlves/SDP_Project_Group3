from app import create_app


#Hello trying to push and then pull to main

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0")               # Host for docker
    for rule in app.url_map.iter_rules():
        print(rule)
