class FridgeForFruits(Exception):
    """
    Возбуждается, когда в холодильник пытаются положить выпечку.
    """
    pass

class StoreroomForBake(Exception):
    """
    Возбуждается, когда в склад пытаются положить фрукт.
    """
    pass