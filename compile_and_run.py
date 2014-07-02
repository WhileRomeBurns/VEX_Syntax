# http://www.sidefx.com/docs/houdini13.0/vex/vcc
#   vcc <program.vfl> <program.vex>

# http://www.sidefx.com/docs/houdini13.0/ref/utils/vexexec
#   vexexec [-p nproc] [-t] <program.vex> <program arguments> ...

import os
import re
import sys
import platform
import subprocess


LIN_DEFAULT = '/opt'
OSX_DEFAULT = '/Applications'
WIN_DEFAULT = 'C:/Program Files/Side Effects Software'


def version_tuple(name):
    """Given 'Houdini 13.0.376', returns the tuple (13, 0, 376)."""
    return tuple([int(d) for d in re.findall('[0-9]{1,4}', name)])


def common_install():
    """Returns the common houdini install parent directory based on the
    platform as well as the regex for the install name pattern."""
    plat = platform.platform(terse=True)

    if plat.startswith('Win'):
        install = WIN_DEFAULT
        regex = '^Houdini.*'      # Houdini 13.0.376

    elif plat.startswith('Dar'):
        install = OSX_DEFAULT
        regex = '^Houdini.*'      # Houdini 13.0.376

    elif plat.startswith('Lin'):
        install = LIN_DEFAULT
        regex = '^hfs.*'          # hfs13.0.376

    else:
        raise Exception('Unknown platform, cannot find Houdini.')

    return (os.path.normpath(install), regex)


def find_latest_houdini():
    """Searches the default sidefx install locations for the most up to date
    install of houdini and returns the normalized path and version as a tuple.

    Example return:
        ( '/Applications/Houdini 13.0.376', (13, 0, 376) )."""
    install, regex = common_install()

    # find all the houdini directories in the install parent directory
    versions = []
    for folder in os.listdir(install):
        if re.match(regex, folder):
            versions.append(folder)

    # find the most up to date version in the install path by comparing the
    # major, minor and bug release numbers
    current_name = 'Houdini 0.0.0'
    current_mmb = (0, 0, 0)

    for ver in versions:
        # find groups of digits of min length 1, max length 4, and cast to int
        mmb = version_tuple(ver)

        if len(mmb) < 3:
            raise Exception('Unexpected version format.')

        # compare major
        newer = False
        if mmb[0] > current_mmb[0]:
            newer = True
        elif mmb[0] == current_mmb[0]:
            # same major, so compare minor version
            if mmb[1] > current_mmb[1]:
                newer = True
            elif mmb[1] == current_mmb[1]:
                # same minor, so compare bug version
                if mmb[2] > current_mmb[2]:
                    newer = True

        if newer:
            current_name = ver
            current_mmb  = mmb

    # we should now have the most current houdini install
    return (os.path.join(install, current_name), current_mmb)


def find_houdini():
    """Returns the version of Houdini specified by the hfs environment
    variable and failing that calls find_latest_houdini() which will search
    commmon default install locations.

    Example return:
        ( '/Applications/Houdini 13.0.376', (13, 0, 376) )."""
    try:
        hfs = os.environ['HFS']
        head, tail = os.path.split(hfs)
        return (hfs, version_tuple(tail))

    except:
        return find_latest_houdini()


def execute(bin, vex, threads=1, time=True):
    """Uses vexexec to run simple vex programs. Not incredibly useful."""
    vexexec = os.path.normpath(os.path.join(bin, 'vexexec'))

    # execute vex
    if time:
        subprocess.call([vexexec, '-p', str(threads), '-t', vex], shell=True)
    else:
        subprocess.call([vexexec, '-p', str(threads), vex], shell=True)


def build(bin, vfl):
    """Builds the vfl path. Compilation name is the same but with the vex
    extension."""
    vcc = os.path.normpath(os.path.join(bin, 'vcc'))

    # compile vfl to vex
    vex = vfl.replace('.vfl', '.vex')
    subprocess.call([vcc, vfl, '-o', vex], shell=True)

    return vex


def main(vfl, run=False, version=True, threads=1, time=True):
    """Compiles and optionally runs vex code. Arguments:
            vfl:     the path to compile '/some/code.vlf'
            run:     if this is true, we call execute() and thus vexexec
            version: print the houdini version called for compiling and running
            threads: number of threads when run is true
            time:    print the execution time when running
    """
    hfs, version = find_houdini()
    if version:
        print('Using houdini path:\n\t%s' % hfs)

    # compile
    print('Compiling:\n\t%s' % vfl)
    bin = os.path.join(hfs, 'bin')
    vex = build(bin, vfl)

    # execute
    if run:
        print('Executing:\n\t%s' % vex)
        execute(bin, vex, threads, time)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('No vfl specified for compilation.')

    elif len(sys.argv) == 2:
        # build
        main(sys.argv[1])

    elif len(sys.argv) == 3:
        # build and run
        main(sys.argv[1], sys.argv[2])

    else:
        raise Exception('To many arguments.')
