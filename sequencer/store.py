class DataStore:
    _instance = None
    _data = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataStore, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def set_data(self, key, data):
        self._data[key] = data

    def get_data(self, key):
        return self._data.get(key, None)
