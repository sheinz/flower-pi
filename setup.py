
from setuptools import setup
#from distutils.core import setup


setup(
      name = "flower-pi",
      version = "0.1",
      packages = ['flowerpi'],
      scripts = ['flower-pi'],
      
      data_files = [('/etc/init', ['upstart/flower-pi.conf'])],
      
      # Project uses RPIO to communicate with GPIO
      # Also uses 'astral' to determine sunrise and sunset time
      # 'astra' requires 'pytz'
      install_requires = ['RPIO>=0.10', 'pytz>=2013d', 'astral>=0.7.2'],
      
      author = "Yuriy",
      author_email = "",
      description = "Plants growing automation based on Raspberry PI board",
      license = "MIT",
      keywords = "raspberry pi flower plant automation",
      url = "http://github.com/sheinz/flower-pi",
      
      )