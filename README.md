# AttrDictX

[![PyPI](https://img.shields.io/pypi/v/attrdictx.svg)](https://pypi.org/project/attrdictx/)
[![License](https://img.shields.io/pypi/l/attrdictx.svg)](https://github.com/kyo-takano/AttrDictX/blob/main/LICENSE)

## Overview

AttrDictX is a lightweight Python package that allows seamless access to dictionary values as if they were class attributes. This package offers an elegant and dependency-free solution, enhancing code legibility and ease of use.

Unlike traditional dictionary access (`random_dict["key"]`), AttrDictX simplifies the process (`random_dict.key`), saving three characters per access. Additionally, it supports nested dictionaries and is free of any dependency-related errors, addressing limitations present in other packages like `attrdict`.

## Installation

To install `attrdictx`, you can use `pip`:

```bash
pip install attrdictx
```

Alternatively, you may just copy & paste the following source code to use this package:

```python
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
```

## Usage

After importing the `AttrDictX` class (when `import AttrDict` also works), you can create an instance from your dictionary and access values like class attributes.

```python
from attrdictx import AttrDictX

# Example: configuration for a random web app
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'username': 'my_user',
        'password': 'my_password'
    },
    'api_keys': {
        'weather_api': 'abc123def456',
        'news_api': 'xyz789'
    },
    'cache_enabled': True
}

# Create an AttrDictX instance from the configuration dictionary
app_config = AttrDictX(config)

# Accessing configuration settings with recursive attributes
print(app_config.cache_enabled)
# => True

print(app_config.api_keys.weather_api)
# => abc123def456
```

In addition to initializing `AttrDictX` with a dictionary, you can also use **variadic arguments** to create an instance. This approach is particularly handy for simpler configurations or when you prefer a cleaner, argument-based syntax.

```python
from attrdictx import AttrDictX

# Example: Simplified configuration using variadic arguments
simple_config = AttrDictX(
    debug_mode=True,
    max_connections=10,
    default_timeout='30s',
    logging_level='INFO'
)

# Accessing the configuration settings as attributes
print(simple_config.debug_mode)
# => True

print(simple_config.max_connections)
# => 10

print(simple_config.default_timeout)
# => '30s'

print(simple_config.logging_level)
# => 'INFO'
```

## Contributions

We welcome contributions from the community to improve and expand AttrDictX. If you encounter any issues, have suggestions, or want to contribute code, feel free to open an issue or submit a pull request on our GitHub repository: [https://github.com/kyo-takano/AttrDictX](https://github.com/kyo-takano/AttrDictX)

## License

AttrDictX is released under the [MIT License](https://github.com/kyo-takano/AttrDictX/blob/main/LICENSE).
