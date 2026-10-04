from loguru import logger


logger.remove()
logger.enable(__name__)
logger.add(".LOGS/log_{time:DD}.{time:MM}.{time:YYYY}.log",
           level="INFO",
           encoding="utf-8",
           format="{time:DD.MM.YYYY at HH:mm:ss} | {level} | file {file}:{line} | {message}"
           )
logger.opt(raw=True).info("\n""\n\n")