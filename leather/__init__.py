import click

from leather import wetmold


@click.group
def leather():
    """
    Making models for leatherworking
    """
    pass


leather.add_command(wetmold.create_wetmold)