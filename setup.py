from distutils.core import setup

def readme():
    with open("README.rst") as f:
        return f.read()

setup(
    name='perlinnoise',
    version='0.1.0',
    packages=['perlinnoise'],
    url='https://github.com/overdev/perlinnoise-0.1.0',
    license='MIT',
    author='Jorge A. G.',
    author_email='jorgegomes83 at hotmail dot com',
    description='A Python3.6 implementation of the improved Perlin Noise function.',
    long_description=readme(),
    keywords='perlin noise procedural generation heightmap terrain',
    classifiers=[
        'Development Status :: 5 - Production Stable',
        'License :: OSI :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
    ],
)
