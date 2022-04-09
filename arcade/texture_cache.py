"""
Caching of internal image data in textures
"""
import weakref


class ImageData:
    pass


class BaseTextureCache:

    def __init__(self):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass


class EternalTextureCache(BaseTextureCache):

    def __init__(self):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass


class WeakTextureCache(BaseTextureCache):

    def __init__(self):
        self._data = weakref.WeakValueDictionary()

    def __getitem__(self, key):
        return self._data.get(key, None)

    def __setitem__(self, key: str, value: ImageData):
        self._data[key] = value


class NullTextureCache(BaseTextureCache):

    def __init__(self):
        pass


if __name__  == "__main__":
    cache = WeakTextureCache()
    cache["thing"] = ImageData()
    print(cache)
