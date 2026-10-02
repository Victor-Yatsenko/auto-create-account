from fastapi_babel import Babel, BabelConfigs, _
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOCALES_DIR = BASE_DIR / "locales"  # Папка переводов: locales


# Конфигурация Babel
# Передаем абсолютный путь (str(LOCALES_DIR)) прямо в BABEL_TRANSLATION_DIRECTORY.
# Это на 100% блокирует любые внутренние баги библиотеки со сдвигом путей.
babel_configs = BabelConfigs(
    ROOT_DIR=str(BASE_DIR),
    BABEL_DEFAULT_LOCALE="uk",
    BABEL_TRANSLATION_DIRECTORY=str(LOCALES_DIR),
)

babel = Babel(configs=babel_configs)
