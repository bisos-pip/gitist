# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: What a gitGroup plant declares: its rules, members to leave out, its name and directory.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/gitist/py3/bisos/gitist/gitGroup_seedInfo.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/gitist/py3/bisos/gitist/gitGroup_seedInfo.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
if 'csInfo' not in globals(): import typing ; csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['loadAs'], }
csInfo['version'] = '202606051742'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'gitGroup_seedInfo-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
A gitGroup is a directory of git repos (its members) that follow the same rules. Its plant,
=<gitGroup>_gitGroup.spcs= in the gitGroup's base repo, calls =setup()= here with the rule
factories below; =gitGroup_csu= checks the members against the rules.
** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] *Imports* =Based on Classification=cs-u=
#+end_org """
from bisos import b  # noqa: E402
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import dataclasses
import pathlib
import typing


@dataclasses.dataclass
class FileFromTemplate:
    """Rule: the member's =path= is a copy of =template=, except in =customRepos= (declared exceptions)."""
    path: str
    template: str
    customRepos: list[str] = dataclasses.field(default_factory=list)
    name: str = ""

    def __post_init__(self) -> None:
        self.name = self.name or self.path


@dataclasses.dataclass
class NotTracked:
    """Rule: none of =paths= is tracked by git in the member (generated files, for example)."""
    paths: list[str]
    name: str = "notTracked"


Rule = typing.Union[FileFromTemplate, NotTracked]


def fileFromTemplate(
        path: str,
        template: str,
        customRepos: list[str] | None = None,
        name: str = "",
) -> FileFromTemplate:
    """The member's =path= (relative to the repo) must equal =template= (an absolute path)."""
    return FileFromTemplate(path, template, list(customRepos or []), name)


def notTracked(
        paths: list[str],
        name: str = "notTracked",
) -> NotTracked:
    """None of =paths= (relative to the repo) may be tracked by git."""
    return NotTracked(list(paths), name)


@dataclasses.dataclass
class GitGroupSeedInfo:
    """What the plant declared (singleton =gitGroupSeedInfo=)."""
    gitGroupName: str | None = None
    gitGroupDir: pathlib.Path | None = None
    exclude: list[str] = dataclasses.field(default_factory=list)
    rules: list[Rule] = dataclasses.field(default_factory=list)
    examplesFuncsList: list[typing.Callable] | None = None


gitGroupSeedInfo = GitGroupSeedInfo()


def setup(
        rules: list[Rule],
        gitGroupName: str | None = None,
        gitGroupDir: str | None = None,
        exclude: list[str] | None = None,
        examplesFuncsList: list[typing.Callable] | None = None,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Called by a gitGroup plant: its rules, member names to leave out, and the
gitGroup's name and directory (the one holding its member repos). A =<gitGroup>_gitGroup.spcs= plant
in the base repo leaves name and directory out: they come from where it really lives
(=gitGroup_csu._info()=: the directory is its base repo's parent, the name is the directory's name).
A plant kept elsewhere passes both.
    #+end_org """
    gitGroupSeedInfo.gitGroupName = gitGroupName
    gitGroupSeedInfo.gitGroupDir = pathlib.Path(gitGroupDir).expanduser() if gitGroupDir else None
    gitGroupSeedInfo.rules = list(rules)
    gitGroupSeedInfo.exclude = list(exclude or [])
    gitGroupSeedInfo.examplesFuncsList = examplesFuncsList


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
