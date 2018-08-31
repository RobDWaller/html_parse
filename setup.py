import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='html_parse',
      version='0.1.0-alpha',
      description='Parse HTML strings in to a value object that can output JSON and offers a number of helper methods.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/RobDWaller/html_parse',
      author='RobDWaller',
      author_email='rdwaller1984@googlemail.com',
      license='MIT',
      packages=setuptools.find_packages(exclude=['tests*']),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ])
