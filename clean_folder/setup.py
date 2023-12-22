from setuptools import setup, find_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Program to sort files in a folder',
      author='Yelyzaveta Melikhova',
      license='MIT',
      packages=find_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )
