from pyramid.config import Configurator
from pyramid.traversal import DefaultRootFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=DefaultRootFactory)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.security')
    config.include('.admin')
    config.scan()
    return config.make_wsgi_app()
