import logging
import subprocess

from vdt.versionplugin.gitchain.shared import parse_version_extra_args

log = logging.getLogger(__name__)


def build_package(version):
    """
    Build package with debianize.
    """
    args = parse_version_extra_args(version.extra_args)

    log.debug("Building version {0} with gitchain.".format(version))
    with version.checkout_tag:
        cmd = ['git', 'status'] 
        log.debug("Running command {0}".format(" ".join(cmd)))
        log.debug(subprocess.check_output(cmd))

    return 0
