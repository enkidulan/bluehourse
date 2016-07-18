from bluehourse.models import Page, User


def includeme(config):
    # import pdb; pdb.set_trace()
    config.include('ps_alchemy')
    config.include('pyramid_sacrud')
    settings = config.registry.settings
    settings['pyramid_sacrud.models'] = (('Users', [User, Page]),
                                         ('Pages', [Page]))
