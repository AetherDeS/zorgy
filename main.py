import click


@click.command()
@click.option(
    "--directories",
    "-d",
    default="/home",
    show_default="True",
    help="Available directories /home, /etc, /var, /srv, /opt",
)
@click.option(
    "--path",
    default="/var/zorgy/backups/",
    help="Directory to save backups, by default=/var/zorgy/backups",
)
@click.option("--compress", is_flag=True, help="Архивировать резервную копию")
def main():
    click.echo("Some description of this util")


if __name__ == "__main__":
    main()


"""
click.group()
def cli():
    pass


@cli.command('backup')
@click.option('--source', '-s', required=True, help='Источник (каталог или файл)')
@click.option('--destination', '-d', default=None, help='Каталог назначения')
@click.option('--compress', is_flag=True, help='Архивировать резервную копию')
def backup(source, destination, compress):
    "
    Выполняет резервное копирование каталога или файла
    "
    if not os.path.exists(source):
        raise FileNotFoundError(f'Исходный путь "{source}" не существует.')

    # По умолчанию сохранить в родительской директории текущего рабочего каталога
    if not destination:
        parent_dir = os.getcwd() + '/backups'
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        destination = parent_dir

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{os.path.basename(source)}_{timestamp}'


    target_path = os.path.join(destination, filename)

    try:
        if compress:
            print(f'Создаем архив {target_path}.tar.gz...')
            shutil.make_archive(target_path, 'gztar', source)
        else:
            print(f'Копируем {source} в {target_path}')
            if os.path.isdir(source):
                shutil.copytree(source, target_path)
            else:
                shutil.copy(source, target_path)

        print("Резервное копирование успешно завершилось.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    cli()
"""
