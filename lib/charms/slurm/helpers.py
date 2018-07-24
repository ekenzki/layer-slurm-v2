import os

from charmhelpers.core.host import mkdir
from charmhelpers.core.templating import render

SLURMD_SERVICE = 'slurmd'
SLURMCTLD_SERVICE = 'slurmctld'
SLURM_CONFIG_TEMPLATE = 'slurm.conf'
SLURM_CONFIG_PATH = '/etc/slurm-llnl/slurm.conf'

MUNGE_SERVICE = 'munge'
MUNGE_KEY_TEMPLATE = 'munge.key'
MUNGE_KEY_PATH = '/etc/munge/munge.key'

GRES_CONFIG_TEMPLATE = 'gres.conf'
GRES_CONFIG_PATH = '/etc/slurm-llnl/gres.conf'

def render_gres_config(context):
    render(source=GRES_CONFIG_TEMPLATE,
           target=GRES_CONFIG_PATH,
           context=context,
           owner=context.get('slurm_user'),
           group=context.get('slurm_user'),
           perms=0o644)


def render_slurm_config(context):
    render(source=SLURM_CONFIG_TEMPLATE,
           target=SLURM_CONFIG_PATH,
           context=context,
           owner=context.get('slurm_user'),
           group=context.get('slurm_user'),
           perms=0o644)


def render_munge_key(context):
    render(source=MUNGE_KEY_TEMPLATE,
           target=MUNGE_KEY_PATH,
           context=context,
           owner='munge',
           group='munge',
           perms=0o400)


def create_spool_dir(context):
    if not os.path.isdir(context.get('slurmd_spool_dir')):
        mkdir(path=context.get('slurmd_spool_dir'),
              owner=context.get('slurm_user'),
              group=context.get('slurm_user'),
              perms=0o750)


def create_state_save_location(context):
    if not os.path.isdir(context.get('state_save_location')):
        mkdir(path=context.get('state_save_location'),
              owner=context.get('slurm_user'),
              group=context.get('slurm_user'),
              perms=0o750)
