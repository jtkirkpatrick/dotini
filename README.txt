dotini
======

Summary
-------
This package is a simple layer on top of the built-in configparser module.
The advantage of dotini is the option of using dot notation to access
settings in a configuration file, provided the settings and section names are
valid variable names. This is aesthetically pleasing.

Usage
-----
With the dotini module imported, use the read() function to parse a config-
uration file. This is done using configparser, for more details regarding
file format and rules, see the official documentation for configparser.

Once the configuration file has been read, it’s settings can be accessed with
dot notation for settings with valid variable names. Settings without valid
variable names can still be accessed with square brackets.

    import dotini
    settings = dotini.read(‘settings.ini’)
    _login(user=settings.user.name,
           pass=settings.user[‘pass’])

Notes
-----
As mentioned previously, to be able to use the dot notation access, settings
should be made with variable safe names.

Setting values are read in as strings, and there is no automatic type conversion
when they are stored or accessed. Type conversion is up to you!

Example Configuration File
—-------------------------
[user]
name = ‘thomas’
pass = ‘samoht’

[performance]
speed = 10
cores = 4