#!/user/bin/env python
import click

@click.command()
def hello():
    click.echo('Hello Earth!')

if __name__ == '__main__':
    hello()