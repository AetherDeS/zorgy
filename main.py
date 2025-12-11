#!/usr/bin/env python3
"""
Утилита для создания резервных копий файлов и каталогов.
Поддерживает сжатие в формат .tar.gz.
"""

import os
import shutil
import click
from datetime import datetime


@click.group()
@click.version_option("1.0.0")
def cli():
    pass


@cli.command("backup")
@click.option(
    "--source",
    "-s",
    required=True,
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True, resolve_path=True),
    help="Исходный файл или каталог для резервного копирования.",
)
@click.option(
    "--destination",
    "-d",
    type=click.Path(file_okay=False, writable=True, resolve_path=True),
    default="/var/zorgy/backups",
    show_default=True,
    help="Каталог для сохранения резервных копий.",
)
@click.option(
    "--compress",
    is_flag=True,
    help="Архивировать резервную копию в формат .tar.gz.",
)
def backup(source, destination, compress):
    """Выполняет резервное копирование указанного файла или каталога."""
    # Создаём директорию назначения, если её нет
    os.makedirs(destination, exist_ok=True)

    # Формируем имя резервной копии с отметкой времени
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    basename = os.path.basename(source.rstrip(os.sep))  # убираем завершающий слэш для каталогов
    filename = f"{basename}_{timestamp}"

    target_path = os.path.join(destination, filename)

    try:
        if compress:
            click.echo(f"Создаём архив: {target_path}.tar.gz")
            shutil.make_archive(target_path, "gztar", root_dir=os.path.dirname(source), base_dir=os.path.basename(source))
            click.secho("Архивация успешно завершена.", fg="green")
        else:
            click.echo(f"Копируем '{source}' в '{target_path}'")
            if os.path.isdir(source):
                shutil.copytree(source, target_path)
            else:
                shutil.copy2(source, target_path)
            click.secho("Резервное копирование успешно завершено.", fg="green")

    except Exception as e:
        click.secho(f"Ошибка: {e}", fg="red", err=True)
        raise click.Abort()


if __name__ == "__main__":
    cli()
