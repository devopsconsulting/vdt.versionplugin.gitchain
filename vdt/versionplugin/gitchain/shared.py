import argparse

def parse_version_extra_args(version_args):
    p = argparse.ArgumentParser(description="Instead of building packages as a freezed state, propagate tags between git repositories.")
    p.add_argument('--target-repo', help="The full url to the target repository, the tag will be pushed there", nargs=1)
    p.add_argument('--target-branch', help="The name of the branch to push to.", nargs=1)
    p.add_argument('--force', '-f', help="Push with --force.")

    return p.parse_args(version_args)
