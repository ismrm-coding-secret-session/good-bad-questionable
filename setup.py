from setuptools import setup, find_packages

setup(name='good_bad_questionable',
      version='0.1',
      description='Demo repo for good, bad and questionable coding practices',
#      url='https://github.com/ismrm-coding-secret-session/good-bad-questionable',
      author='Renat Sibgatulin',
      author_email='renat.sibgatulin@gmail.com',
      license='MIT',
      install_requires=[
          'numpy', 'scipy', 'pandas', 'xarray', 'matplotlib', 'nibabel'
      ],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
