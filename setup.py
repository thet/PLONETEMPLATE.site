from setuptools import setup
from setuptools import find_packages

version = '1.0'

name = "PLONETEMPLATE.site"
namespace = ['PLONETEMPLATE', ]
baseurl = "http://github.com/thet/PLONETEMPLATE.site"

setup(
    name=name,
    version=version,
    description="plone integration package for {}".format(name),
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone',
    author='Johannes Raggam',
    author_email='johannes@raggam.co.at',
    url='%s/%s' % (baseurl, name),
    license='GPL',
    namespace_packages=namespace,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
        'collective.folderishtraverse',
        'collective.folderishtypes',
        'collective.folderorder',
        'plone.app.theming',
        'plone.resource',
        'z3c.jbot',
    ],
    extras_require=dict(
        live=[
            'plone.app.caching',
        ],
        test=[
            'plone.app.robotframework',
            'plone.app.testing',
        ]
    ),
)
