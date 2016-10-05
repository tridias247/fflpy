import click

class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    config.verbose = verbose
    pass

@cli.group()
@pass_config
def fetch(config):
    """ Commands to fetch data from a remote or local source. """

@fetch.command('projections')
@pass_config
def fetch_projections(config):
    """ Command to fetch player projection data. """
    click.echo("Fetching projection data.")
    fetch_espn_projections(config)