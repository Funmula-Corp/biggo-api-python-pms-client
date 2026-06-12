from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='biggo_pms_api_python',
    version='1.1.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    install_requires=['requests'],
    python_requires='>=3.6',
)
