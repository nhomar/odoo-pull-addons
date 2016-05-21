#!/usr/bin/env python
# -*- coding: utf-8 -*

import click
import ConfigParser
import subprocess


__version__ = '1.0.1'


def git(repo_list, cmd):
    for repo in repo_list:
        cmd_new = ['git'] + cmd
        click.echo('--'*10)
        click.echo(repo)
        subprocess.call(cmd_new, cwd=repo)


def update(config_file, version='8.0'):
    config = ConfigParser.ConfigParser()
    config.readfp(open(config_file))
    ap = config.get('options', 'addons_path')
    repo_list = ap.split(',')
    check_branch = ['branch']
    update_cmd = ['pull', 'origin', version]
    git(repo_list, update_cmd)
    git(repo_list, check_branch)


@click.command()
@click.option('--odoo-config', '-c',
              type=click.Path(exists=True),
              help="A existent config file.")
@click.option('--odoo-version', '-vv', default='8.0',
              help="Force check the version")
@click.option('--version', '-v', is_flag=True,
              help="Show Version and exit.")
def cli(odoo_config, odoo_version, version):
    if version:
        click.echo(__version__)
        exit()
    if not odoo_config:
        click.echo("Provide a valid Odoo's config file")
        exit()
    update(click.format_filename(odoo_config),
           odoo_version)
