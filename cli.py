import click
import sentry_sdk

from leather import leather


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--sentry-dsn', envvar='SENTRY_DSN')
def cli(sentry_dsn):
    """
    ZCAD - CadQuery cli tools
    """
    if sentry_dsn:
        sentry_sdk.init(dsn=sentry_dsn)


cli.add_command(leather)


if __name__ == '__main__':
    cli()
