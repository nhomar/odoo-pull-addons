#!/usr/bin/env python
# -*- coding: utf-8 -*

import click
import ConfigParser
import subprocess


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
    update_cmd = ['pull', 'origin', version]
    git(repo_list, update_cmd)


@click.command()
@click.argument('odoo-config', type=click.Path(exists=True))
def cli(odoo_config):
    update(click.format_filename(odoo_config))
