from setuptools import setup


def readme():
    with open('README.txt') as f:
        return f.read()


setup(name='dotini',
      version='0.0.1',
      description='Dot notation for configuration files.',
      long_description=readme(),
      long_description_content_type='text/plain',
      keywords='configuration settings ini cfg config',
      url='https://github.com/cloudsickle/dotini',
      author='James Thomas Kirkpatrick IV',
      license='MIT',
      packages=['dotini'],
      include_package_data=True,
      zip_safe=False)
