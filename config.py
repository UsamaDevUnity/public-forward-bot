import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "21997406"))
    API_HASH = os.environ.get("API_HASH", "ce2e4cd3c0f25b82a25124912064cd3a")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6690223775:AAF19ZIvXRsLlMtKiZfdw6MFw3rw1yYrO3U")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "USCryptoking_admin")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "cryptokings212"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "USCryptoKing_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
