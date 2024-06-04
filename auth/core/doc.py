from flask_swagger_ui import get_swaggerui_blueprint

def documentation(server):
    API_URL = '/v1/doc'
    STATIC_FILE_URL = '/static/swagger.json'
    SWAGGER_BLUERPRINT = get_swaggerui_blueprint(API_URL, STATIC_FILE_URL)
    server.register_blueprint(SWAGGER_BLUERPRINT, url_prefix=API_URL)