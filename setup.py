from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='attrdictx',
    version='0.1.0', 
    author='Kyo Takano',
    author_email='kyo.takano@mentalese.co',
    description='An extended AttrDict class',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kyo-takano/attrdictx',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
