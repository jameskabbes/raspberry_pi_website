import kabbes_repository_generator
import raspberry_pi_website

class Website( kabbes_repository_generator.RepositoryGenerator ):

    def __init__( self ):
        kabbes_repository_generator.RepositoryGenerator.__init__( self )

        """
        import subprocess

        bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        """

        "subprocess.Popen(..., cwd='path\to\somewhere')"