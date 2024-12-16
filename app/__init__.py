import os
from flask import Flask
from .routes import bp


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Homepage
    @app.route('/home')
    def home_page():
        return '''
            <html>
                <head>
                    <title>Software Development Processes Project</title>
                </head>
                <body>
                    <h1>Software Development Processes Project - Group 3</h1>
                    <h3>Students: Cecilia Machado Alves and Peter Bader</h3>
                    <p>This project is part of the MIO program from FHTW. The
                    aim of this project is to practice the methods of current
                    software development processes.</p>
                    <p>Click on the links below to check the values for
                    Temperature and Disk Usage</p>
                    <ul>
                        <li><a href="/cpu/temp">CPU Temperature</a></li>
                        <li><a href="/cpu/temp/error">CPU Temperature 
                        Status</a></li>
                        <li><a href="/disk/usage">Disk Usage</a></li>
                    </ul>
                </body>
            </html>
        '''

    app.register_blueprint(bp)

    return app
