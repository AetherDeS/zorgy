import click


@click.command()
@click.option('--directories', prompt="Choose directories", help='Available directories /home, /etc, /var, /srv, /opt')
def main():
    click.echo("Some description of this util")





if __name__ == "__main__":
    main()
