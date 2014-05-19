vdt.versionplugin.gitchain
==========================

Instead of building packages as a freezed state, propagate tags between git repositories.

Example::

    version --plugin=gitchain --target-repo=file:///tmp/vdt.versionplugin.gitchain --target-ref=refs/heads/kakalkal --force -v
    DEBUG:vdt.versionplugin.default:Extra argument are ['--target-repo=file:///tmp/vdt.versionplugin.gitchain', '--target-ref=refs/heads/kakalkal', '--force']
    WARNING:vdt.versionplugin.default:Not tagging, this revision is already tagged as: 0.0.1

    DEBUG:vdt.versionplugin.gitchain.freeze:Arguments are Namespace(force=True, target_ref='refs/heads/kakalkal', target_repo='file:///tmp/vdt.versionplugin.gitchain')
    DEBUG:vdt.versionplugin.gitchain.freeze:Building version 0.0.1 with gitchain.
    Note: checking out '0.0.1'.

    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by performing another checkout.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -b with the checkout command again. Example:

      git checkout -b new_branch_name

    HEAD is now at a3b304b... Parse arguments.
    DEBUG:vdt.version.shared:M	vdt/versionplugin/gitchain/freeze.py
    M	vdt/versionplugin/gitchain/shared.py
