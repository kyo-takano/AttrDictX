class AttrDictX(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDictX, self).__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = AttrDictX(value)

    def __getattr__(self, name):
        if name in self:
            return self[name]
        raise AttributeError(f"'AttrDictX' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        self[name] = value

"""
This package also covers the following potential confusion.
"""
AttrDict = AttrDictX
