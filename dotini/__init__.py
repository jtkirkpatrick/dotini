"""
dotini - dot notation for configuration files.

dotini is built using configparser from the Python standard library.
As with configparser, values are read from configuration files as
strings, as there is no automatic type conversion.

For information regarding the format of configuration files, see the
documentation for configparser.

Setting sections and keys that have valid variable names can be accessed
with dot notation, those that do not have valid variable names can be
accessed using the square bracket notation, just as in configparser.

Example usage:

    import dotini
    settings = dotini.read('my_settings.ini')
    _login(user=settings.user.name,
           pass=settings.user['pass'])  # not a valid name, must use []
    _set_cores(settings.performance.cores)

Example configuration file:

    # Example file
    [user]
    name = 'dotini'
    pass = 'initod'
    [performance]
    cores = 4
    speed = 10
"""
import configparser


__copyright__ = "Copyright (c) 2018 James Thomas Kirkpatrick IV"
__license__ = "MIT"
__version__ = "0.0.1"


class _ConfigSection(object):
    """Hold settings for a section of the configuration file."""

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            raise AttributeError('No "%s" setting in section.' % attr)

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return str(tuple(self.__dict__.keys()))


def read(config_file):
    """Read settings from file and return a dot notation object."""
    config = configparser.ConfigParser()
    config.read(config_file)

    dotini = _ConfigSection()

    for section in config.sections():
        settings = _ConfigSection()
        for key, value in config.items(section):
            setattr(
                settings, key.lower().replace(" ", "_"), value.lower().replace(" ", "_")
            )

        setattr(dotini, section.lower().replace(" ", "_"), settings)

    return dotini
