from distutils.core import setup

setup(
    name='psnstoreprice',
    packages=['psnstoreprice'],
    package_dir={'psnstoreprice': 'psnstoreprice'},
    version='0.1',
    install_requires=['dryscrape', 'beautifulsoup4'],
    description='Find the price on PlayStation Store from url',
    author='Alessandro Sbarbati',
    author_email='miriodev@gmail.com',
    url='https://github.com/Mirio/psnstoreprice',
    download_url='https://github.com/Mirio/psnstoreprice/tarball/0.1',
    keywords=['playstation', 'psn', 'psn store', "psnstoreprice"],
    license='BSD',
    classifiers=["License :: OSI Approved :: BSD License", "Programming Language :: Python :: 3",
                 "Topic :: Software Development :: Libraries :: Python Modules", "Topic :: Utilities"],
)
