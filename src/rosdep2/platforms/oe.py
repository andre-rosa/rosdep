from __future__ import print_function
import subprocess, sys
from rospkg.os_detect import OS_OPENEMBEDDED, OsDetect
from ..installers import PackageManagerInstaller
from ..shell_utils import read_stdout
OPKG_INSTALLER = 'opkg'

def register_installers(context):
    context.set_installer(OPKG_INSTALLER, OpkgInstaller())


def register_platforms(context):
    register_oe(context)


def register_oe(context):
    context.add_os_installer_key(OS_OPENEMBEDDED, OPKG_INSTALLER)
    context.set_default_os_installer_key(OS_OPENEMBEDDED, lambda self: OPKG_INSTALLER)
    context.set_os_version_type(OS_OPENEMBEDDED, OsDetect.get_codename)


def opkg_detect(pkgs, exec_fn=None):
    """
    Given a list of package, return the list of installed packages.

    :param pkgs: list of package names, optionally followed by a fixed version (`foo=3.0`)
    :param exec_fn: function to execute Popen and read stdout (for testing)
    :return: list elements in *pkgs* that were found installed on the system
    """
    print('TBD: opkg_detect')
    return []


class OpkgInstaller(PackageManagerInstaller):
    """
    An implementation of the Installer for use on oe systems.
    """

    def __init__(self):
        super(OpkgInstaller, self).__init__(opkg_detect)

    def get_version_strings(self):
        print('TBD OpkgInstaller::get_version_strings')
        output = subprocess.check_output(['opkg', '--version'])
        version = output.splitlines()[0].split(' ')[2]
        return [
         ('opkg {}').format(version)]

    def get_install_command(self, resolved, interactive=True, reinstall=False, quiet=False):
        print('TBD OpkgInstaller::_get_install_command')
        packages = self.get_packages_to_install(resolved, reinstall=reinstall)
        if not packages:
            return []
            base_cmd = ['opkg', 'install']
            if quiet:
                base_cmd.append('-V')
            return []

