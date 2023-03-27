import raspberry_pi_website
import kabbes_repository_generator
import kabbes_user_client
import py_starter as ps

class Client( raspberry_pi_website.Website, kabbes_repository_generator.Client ):

    BASE_CONFIG_DICT = {
        "_Dir": raspberry_pi_website._Dir,
    }

    def __init__( self, dict={}, **kwargs ):

        kabbes_repository_generator.Client.__init__( self )
        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        overwrite_cfg = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        self.cfg.merge(overwrite_cfg)

        raspberry_pi_website.Website.__init__( self )
