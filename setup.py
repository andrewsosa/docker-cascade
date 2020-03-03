from setuptools import find_packages
from setuptools import setup

install_requires = [
    'click',
    'docker',
    'PyYAML',
]

setup(
    name='docker-cascade',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points="""
    [console_scripts]
    docker-cascade=cascade.cli:cli
    """,
)
