import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    'bcrypt',
    'alembic',
    'docutils',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_sacrud',
    'ps_alchemy',
    'ziggurat_foundations',
    'pyramid_redis_sessions',
    'pyramid_mailer',
    'deform>=2.0a2',
    'colander',
    'ColanderAlchemy',
    'pyramid_storage',
    'cornice',
    'pyramid_services',
    'pyramid_celery',
    'pyramid_layout',
    'paginate',
    'repoze.zcml >= 1.0b1',
    'repoze.workflow >= 1.0b1',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
]

setup(name='bluehourse',
      version='0.0',
      description='bluehourse',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = bluehourse:main
      [console_scripts]
      initialize_bluehourse_db = bluehourse.scripts.initializedb:main
      """,
      )
