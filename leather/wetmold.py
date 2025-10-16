import click


@click.command
@click.option('-l', '--length', type=float, required=True,
    help='Length of the wetmold')
def create_wetmold(length):
    """
    Makes a wetmold with the given dimensions
    """

    print(f"Creating wetmold with length: {length}")