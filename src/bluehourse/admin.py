from bluehourse.models import Page, User

from pyramid.security import Allow, Everyone
from pyramid_sacrud import PYRAMID_SACRUD_HOME
from pyramid.interfaces import IRootFactory


def pach_root_acl_factory(root_factory):
    root_factory.__acl__ = [
        (Allow, Everyone, PYRAMID_SACRUD_HOME),
    ]


def includeme(config):
    config.commit()
    pach_root_acl_factory(config.registry.getUtility(IRootFactory))
    config.include('ps_alchemy')
    config.include('pyramid_sacrud')
    settings = config.registry.settings
    settings['pyramid_sacrud.models'] = (('Users', [User, Page]),
                                         ('Pages', [Page]))
