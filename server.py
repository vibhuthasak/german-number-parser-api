from waitress import serve
import logging
from api import app
from paste.translogger import TransLogger

if __name__ == "__main__":
    logger = logging.getLogger("waitress")
    logger.setLevel(logging.DEBUG)
    serve(
        TransLogger(app, setup_console_handler=False),
        host="0.0.0.0",
        port=8080,
        threads=4,
    )
