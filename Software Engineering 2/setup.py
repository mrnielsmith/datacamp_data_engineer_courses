from setuptools import setup

setup(name='my_package',
      version='0.0.1',
      description='An example package',
      author='Niel Smith',
      author_email='nsmith7123@gmail.com',
      packages=['my_package'],
      install_requirements=['matplotlib',
                            'numpy=1.15.4',
                            'pycodestyle>=2.4.0'])
