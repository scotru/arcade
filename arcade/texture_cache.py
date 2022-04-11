"""
Caching of internal image data in textures
"""
import weakref


class ImageData:
    pass


class BaseTextureCache:

    def __init__(self):
        pass

    def clear(self):
        pass

    def delete(self, key: str):
        pass

    def __getitem__(self, key):
        return None

    def __setitem__(self, key, value):
        pass


class EternalTextureCache(BaseTextureCache):

    def __init__(self):
        self._data = dict()

    def clear(self):
        self._data = dict()

    def delete(self, key: str):
        del self._data[key]

    def __getitem__(self, key):
        return self._data.get(key, None)

    def __setitem__(self, key, value):
        self._data[key] = value


class WeakTextureCache(BaseTextureCache):

    def __init__(self):
        self._data = weakref.WeakValueDictionary()

    def clear(self):
        self._data = weakref.WeakValueDictionary()

    def delete(self, key: str):
        del self._data[key]

    def __getitem__(self, key):
        return self._data.get(key, None)

    def __setitem__(self, key: str, value: ImageData):
        self._data[key] = value


class NullTextureCache(BaseTextureCache):
    pass


cache = WeakTextureCache()


if __name__  == "__main__":
    cache = WeakTextureCache()
    data = ImageData()
    cache["thing"] = data
    print(list(cache._data.items()))
    data = None
    print(list(cache._data.items()))
