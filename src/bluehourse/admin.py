from bluehourse.models import Page, User

from pyramid.security import Allow
from pyramid_sacrud import PYRAMID_SACRUD_HOME, PYRAMID_SACRUD_VIEW
from pyramid.interfaces import IRootFactory
from ps_alchemy.resources import ListResource


class EditorResource(ListResource):
    __acl__ = [(Allow, 'editor', PYRAMID_SACRUD_VIEW), ]


def pach_root_acl_factory(root_factory):
    root_factory.__acl__ = [
        (Allow, 'editor', PYRAMID_SACRUD_HOME),
    ]


def includeme(config):
    config.commit()
    pach_root_acl_factory(config.registry.getUtility(IRootFactory))
    config.include('ps_alchemy')
    config.include('pyramid_sacrud')
    settings = config.registry.settings
    settings['pyramid_sacrud.models'] = (('Users', [EditorResource(User), EditorResource(Page)]),
                                         ('Pages', [EditorResource(Page)]))
