# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= checking a gitGroup's member repos against its rules.
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
** This File: /bisos/git/bxRepos/bisos-pip/gitist/py3/bisos/gitist/gitGroup_csu.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/gitist/py3/bisos/gitist/gitGroup_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
if 'csInfo' not in globals(): import typing ; csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['loadAs'], }
csInfo['version'] = '202606053019'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'gitGroup_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
The =gitGroup_*= Cmnds of a gitGroup plant (=<gitGroup>_gitGroup.pcs= on =gitGroup-seed.cs=): its
members, a read-only status of every member against every rule, a diff for a file that drifted,
and an update that applies only the safe actions. Never stages or commits. bisos-pip/gitist
WorkPlan Stage 7; =bx-gitRepos= (=baseUpdateDotIgnore=, =baseVerifyDotIgnore=) stays beside it.

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

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= "  :title "*Py Library IMPORTS*" :comment "-- Framework and External Packages Imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- Framework and External Packages Imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# import os
import collections
# import pathlib
# import invoke

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
import difflib
import functools
import hashlib
import pathlib
import shutil
import subprocess
import typing

from bisos.gitist import gitGroup_seedInfo
from bisos.csSeed import seedsLib

import logging
log = logging.getLogger(__name__)

####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    csParams.parDictAdd(
        parName='replaceDrift',
        parDescription="gitGroup_update: also replace files that drifted (differ, not declared custom).",
        parDataType=None,
        parDefault=None,
        parChoices=['true', 'false'],
        argparseShortOpt=None,
        argparseLongOpt='--replaceDrift',
    )


####+BEGIN: b:py3:cs:orgItem/section :title "Rules Evaluation" :comment "members, template versions, statuses"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Rules Evaluation* members, template versions, statuses  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# Statuses, by rule kind. fileFromTemplate: ok missing stale drift custom. notTracked: ok tracked.
safeStatuses = ("missing", "stale")


@dataclasses.dataclass
class Finding:
    """One member against one rule."""
    repo: str
    rule: str
    status: str
    detail: str = ""


def plantBaseRepo() -> pathlib.Path | None:
    """The repo holding the plant (the gitGroup's base repo): the nearest ancestor with a =.git=, of
    the plant's *real* path.
    Resolved on purpose: run from PATH, the plant is a symlink (e.g. in =/bisos/core/bsip/bin=) and its
    parameters come from where the file really lives --- unlike a CBM leaf (bisos.capability's
    =resolveCbsSpec()=), whose parameters come from where its symlink is planted."""
    plant = seedsLib.seededCsxuInfo.plantOfThisSeed
    if plant is None:
        return None
    for each in pathlib.Path(plant).resolve().parents:
        if (each / ".git").exists():
            return each
    return None


def _info() -> gitGroup_seedInfo.GitGroupSeedInfo:
    """The plant's declaration; a =.spcs= plant's name and gitGroup directory filled in from where it
    lives (the directory is its base repo's parent)."""
    info = gitGroup_seedInfo.gitGroupSeedInfo
    if info.gitGroupDir is None and info.rules:
        baseRepo = plantBaseRepo()
        if baseRepo is not None:
            info.gitGroupDir = baseRepo.parent
            info.gitGroupName = info.gitGroupName or baseRepo.parent.name
    if info.gitGroupDir is None:
        raise ValueError("no gitGroup declared: run this through a <gitGroup>_gitGroup.pcs/.spcs plant")
    info.gitGroupName = info.gitGroupName or info.gitGroupDir.name
    return info


def _git(repo: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=False)


def members(info: gitGroup_seedInfo.GitGroupSeedInfo | None = None) -> list[pathlib.Path]:
    """The git repos directly under the gitGroup directory, minus exclude. Symlinks are left out:
    =gitGroup= is a symlink to =.github=, which would otherwise be counted twice."""
    info = info or _info()
    assert info.gitGroupDir is not None
    return [each for each in sorted(info.gitGroupDir.iterdir())
            if not each.is_symlink() and (each / ".git").exists() and each.name not in info.exclude]


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@functools.lru_cache(maxsize=None)
def templateVersions(template: str) -> tuple[bytes, dict[str, str]]:
    """The template's current content, and {sha256: "<commit> <date>"} of every earlier version in
    the git history of the repo it lives in (resolving symlinks); no history if it is not in one."""
    real = pathlib.Path(template).resolve()
    current = real.read_bytes()
    versions: dict[str, str] = {}
    top = _git(real.parent, "rev-parse", "--show-toplevel").stdout.decode().strip()
    if top:
        rel = real.relative_to(pathlib.Path(top).resolve()).as_posix()
        log = _git(pathlib.Path(top), "log", "--format=%h %cs", "--", rel).stdout.decode().splitlines()
        for line in log:
            commit = line.split()[0]
            shown = _git(pathlib.Path(top), "show", f"{commit}:{rel}")
            if shown.returncode == 0:
                versions.setdefault(_sha(shown.stdout), line)
    versions.pop(_sha(current), None)
    return current, versions


def checkRule(repo: pathlib.Path, rule: gitGroup_seedInfo.Rule) -> Finding:
    """The status of one member against one rule."""
    if isinstance(rule, gitGroup_seedInfo.FileFromTemplate):
        target = repo / rule.path
        if not target.is_file():
            return Finding(repo.name, rule.name, "missing")
        current, versions = templateVersions(rule.template)
        data = target.read_bytes()
        if data == current:
            return Finding(repo.name, rule.name, "ok")
        if _sha(data) in versions:
            return Finding(repo.name, rule.name, "stale", f"template as of {versions[_sha(data)]}")
        if repo.name in rule.customRepos:
            return Finding(repo.name, rule.name, "custom", "declared in the plant")
        return Finding(repo.name, rule.name, "drift", "differs from every template version")
    tracked = _git(repo, "ls-files", "--", *rule.paths).stdout.decode().split()
    if tracked:
        return Finding(repo.name, rule.name, "tracked", " ".join(tracked))
    return Finding(repo.name, rule.name, "ok")


def statusAll(repoNames: list[str] | None = None) -> list[Finding]:
    """Every member (or the named ones) against every rule."""
    info = _info()
    repos = members(info)
    if repoNames:
        unknown = set(repoNames) - {each.name for each in repos}
        if unknown:
            raise ValueError(f"not members of {info.gitGroupName}: {' '.join(sorted(unknown))}")
        repos = [each for each in repos if each.name in repoNames]
    return [checkRule(repo, rule) for repo in repos for rule in info.rules]


def summary(findings: list[Finding]) -> str:
    """Per rule, how many members are in each status other than ok."""
    parts = []
    for ruleName in dict.fromkeys(each.rule for each in findings):
        counts = collections.Counter(each.status for each in findings if each.rule == ruleName)
        notOk = ", ".join(f"{status} {count}" for status, count in sorted(counts.items()) if status != "ok")
        parts.append(f"{ruleName}: {notOk or 'all ok'}")
    repos = len({each.repo for each in findings})
    return f"{repos} members --- " + " --- ".join(parts)


def _rule(name: str) -> gitGroup_seedInfo.Rule:
    for rule in _info().rules:
        if rule.name == name:
            return rule
    raise ValueError(f"no rule named {name}: {' '.join(rule.name for rule in _info().rules)}")


def fileDiff(repoName: str, ruleName: str) -> str:
    """A unified diff from the template to the member's file."""
    rule = _rule(ruleName)
    if not isinstance(rule, gitGroup_seedInfo.FileFromTemplate):
        raise ValueError(f"{ruleName} is not a file rule")
    target = _info().gitGroupDir / repoName / rule.path  # type: ignore[operator]
    theirs = target.read_text().splitlines(keepends=True) if target.is_file() else []
    current, _ = templateVersions(rule.template)
    return "".join(difflib.unified_diff(current.decode().splitlines(keepends=True), theirs,
                                        fromfile=f"template ({rule.template})", tofile=str(target)))


def update(repoNames: list[str] | None = None, replaceDrift: bool = False) -> list[str]:
    """Apply the safe actions: write the template over =missing= and =stale= files (and =drift= ones
    when replaceDrift). Never =custom=, never stages: for =tracked= it returns the git line to run."""
    info = _info()
    assert info.gitGroupDir is not None
    done = []
    for finding in statusAll(repoNames):
        rule = _rule(finding.rule)
        if isinstance(rule, gitGroup_seedInfo.FileFromTemplate):
            if finding.status in safeStatuses or (replaceDrift and finding.status == "drift"):
                shutil.copyfile(pathlib.Path(rule.template).resolve(), info.gitGroupDir / finding.repo / rule.path)
                done.append(f"{finding.repo}: {rule.path} written ({finding.status})")
        elif finding.status == "tracked":
            done.append(f"{finding.repo}: run: git -C {info.gitGroupDir / finding.repo} rm --cached {finding.detail}")
    return done


def untrack(repoNames: list[str] | None = None) -> list[str]:
    """For every =tracked= notTracked finding, =git rm --cached= its paths: the files stay on disk, the
    deletion is staged (only that), and the commit stays the user's. The one place that stages."""
    info = _info()
    assert info.gitGroupDir is not None
    done = []
    for finding in statusAll(repoNames):
        if finding.status != "tracked":
            continue
        repo = info.gitGroupDir / finding.repo
        result = _git(repo, "rm", "--cached", "--quiet", "--", *finding.detail.split())
        if result.returncode != 0:
            raise ValueError(f"{finding.repo}: git rm --cached failed: {result.stderr.decode().strip()}")
        done.append(f"{finding.repo}: untracked (staged): {finding.detail}")
    return done


####+BEGIN: b:py3:cs:orgItem/section :title "Cached Lists" :comment "for Blee's Magit menus"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Cached Lists* for Blee's Magit menus  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# /bisos/var/gitGroup/<gitGroup>/cachedList.<vcMode>: the real paths of the gitGroup directory (when it
# is itself a git repo, as before the base/.github layout) and of the members, one per line. Read by
# Blee's Magit menus (bap:magit:gitGroup/visit).
cachedListsBase = pathlib.Path("/bisos/var/gitGroup")


def vcModeOf(path: pathlib.Path) -> str:
    """=auth= or =anon= from the real path (/bisos/git/auth/... or /bisos/git/anon/...), else =other=."""
    parts = path.resolve().parts
    for mode in ("auth", "anon"):
        if mode in parts:
            return mode
    return "other"


def cachedListPath(info: gitGroup_seedInfo.GitGroupSeedInfo | None = None) -> pathlib.Path:
    info = info or _info()
    assert info.gitGroupDir is not None
    return cachedListsBase / str(info.gitGroupName) / f"cachedList.{vcModeOf(info.gitGroupDir)}"


def cachedListLines(info: gitGroup_seedInfo.GitGroupSeedInfo | None = None) -> list[str]:
    """The gitGroup directory (if it is a git repo), then the members, as real paths."""
    info = info or _info()
    assert info.gitGroupDir is not None
    repos = ([info.gitGroupDir] if (info.gitGroupDir / ".git").exists() else []) + members(info)
    return [str(repo.resolve()) for repo in repos]


def cachedListWrite(info: gitGroup_seedInfo.GitGroupSeedInfo | None = None) -> pathlib.Path:
    """Write the cached list: a temporary file renamed into place, so a reader never sees half of it."""
    info = info or _info()
    target = cachedListPath(info)
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_name(f".{target.name}.tmp")
    temp.write_text("".join(f"{line}\n" for line in cachedListLines(info)))
    temp.replace(target)
    return target


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Direct Command Services" :anchor ""  :extraInfo "Examples and CSs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Direct Command Services_: |]]  Examples and CSs  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "pyKwArgs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_csu>>  =verify= ro=cli pyInv=pyKwArgs   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             pyKwArgs: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  The gitGroup Cmnds, for the plant's gitGroup.
        #+end_org """)

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        try:
            info = _info()
        except ValueError:
            cs.examples.menuChapter('=gitGroup: run through a <gitGroup>_gitGroup.pcs/.spcs plant=')
            literal("bisos-pip_gitGroup.spcs  # bisos-pip/base/py3/bin, name and directory from where it lives")
            literal("blee_gitGroup.spcs       # blee/base/py3/bin, name and directory from where it lives")
            return(cmndOutcome)

        repos = members(info)
        firstRepo = repos[0].name if repos else "<repo>"
        fileRules = [rule.name for rule in info.rules if isinstance(rule, gitGroup_seedInfo.FileFromTemplate)]

        cs.examples.menuChapter(f'=gitGroup {info.gitGroupName}: {info.gitGroupDir} ({len(repos)} members)=')
        cmnd('gitGroup_members', comment=" # the member repos")
        cmnd('gitGroup_status', comment=" # read-only: every member against every rule")
        cmnd('gitGroup_status', args=firstRepo, comment=" # one member")
        if fileRules:
            cmnd('gitGroup_diff', args=f"{firstRepo} {fileRules[0]}", comment=" # template -> member's file")

        cs.examples.menuChapter('=Update: writes files only; never stages or commits=')
        cmnd('gitGroup_update', comment=" # missing and stale files; prints git rm --cached lines")
        cmnd('gitGroup_update', pars=od([('replaceDrift', 'true')]), comment=" # drift too (after gitGroup_diff)")
        cmnd('gitGroup_update', args=firstRepo, comment=" # one member")

        cs.examples.menuChapter('=Untrack: stages only the git rm --cached of notTracked paths; never commits=')
        cmnd('gitGroup_untrack', comment=" # every member whose notTracked paths are tracked")
        cmnd('gitGroup_untrack', args=firstRepo, comment=" # one member")

        cs.examples.menuChapter("=Cached list, for Blee's Magit menus=")
        cmnd('gitGroup_cachedListUpdate', comment=f" # writes {cachedListPath(info)}")
        cmnd('gitGroup_cachedList', comment=" # prints it (writes it first if absent)")

        cs.examples.menuChapter('=The rules=')
        for rule in info.rules:
            if isinstance(rule, gitGroup_seedInfo.FileFromTemplate):
                literal(f"# {rule.name}: = {rule.template}" + (f" (custom: {' '.join(rule.customRepos)})" if rule.customRepos else ""))
            else:
                literal(f"# {rule.name}: not tracked: {' '.join(rule.paths)}")

        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitGroup_members" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitGroup_members>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitGroup_members(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] The member repos: git repos directly under the gitGroup directory, minus exclude.
        #+end_org """)
        try:
            repos = members()
        except ValueError as err:
            return failed(cmndOutcome.set(opError=b.OpError.Failure, opErrInfo=str(err)))
        if rtInv.outs:
            for repo in repos:
                print(repo)
        return cmndOutcome.set(opError=b.OpError.Success, opResults=[repo.name for repo in repos])


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitGroup_status" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitGroup_status>>  =verify= argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitGroup_status(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Read-only: every member (or the named ones) against every rule; then counts.
        #+end_org """)
        repoNames = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)
        try:
            findings = statusAll(repoNames or None)
        except ValueError as err:
            return failed(cmndOutcome.set(opError=b.OpError.Failure, opErrInfo=str(err)))
        if rtInv.outs:
            for finding in findings:
                print(f"{finding.repo:28} {finding.rule:16} {finding.status:8} {finding.detail}")
        return cmndOutcome.set(opError=b.OpError.Success, opResults=summary(findings))

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="repoNames",
            argDefault='',
            argChoices=[],
            argDescription="Member repo names; none: all members"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitGroup_diff" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 2 :argsMax 2 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitGroup_diff>>  =verify= argsMin=2 argsMax=2 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitGroup_diff(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 2, 'Max': 2,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] A unified diff from a file rule's template to the member's file.
        #+end_org """)
        repoName = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        ruleName = self.cmndArgsGet("1", cmndArgsSpecDict, argsList)
        try:
            diff = fileDiff(repoName, ruleName)
        except ValueError as err:
            return failed(cmndOutcome.set(opError=b.OpError.Failure, opErrInfo=str(err)))
        if rtInv.outs:
            print(diff or f"{repoName}: {ruleName} equals the template")
        return cmndOutcome.set(opError=b.OpError.Success, opResults=f"{len(diff.splitlines())} diff lines")

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repoName",
            argDefault='',
            argChoices=[],
            argDescription="A member repo name"
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="ruleName",
            argDefault='',
            argChoices=[],
            argDescription="A file rule's name (its path, e.g. .gitignore)"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitGroup_update" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "replaceDrift" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitGroup_update>>  =verify= parsOpt=replaceDrift argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitGroup_update(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'replaceDrift', ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             replaceDrift: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'replaceDrift': replaceDrift, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Write the template over missing and stale files (drift too with
--replaceDrift=true); never custom; never stages or commits: prints the git rm --cached lines.
        #+end_org """)
        repoNames = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)
        try:
            done = update(repoNames or None, replaceDrift=(replaceDrift == 'true'))
        except ValueError as err:
            return failed(cmndOutcome.set(opError=b.OpError.Failure, opErrInfo=str(err)))
        if rtInv.outs:
            for line in done:
                print(line)
        return cmndOutcome.set(opError=b.OpError.Success, opResults=f"{len(done)} actions")

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="repoNames",
            argDefault='',
            argChoices=[],
            argDescription="Member repo names; none: all members"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitGroup_untrack" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitGroup_untrack>>  =verify= argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitGroup_untrack(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] git rm --cached the notTracked paths a member (or every member) still
tracks: the files stay on disk and only that deletion is staged; the commit is the user's.
        #+end_org """)
        repoNames = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)
        try:
            done = untrack(repoNames or None)
        except ValueError as err:
            return failed(cmndOutcome.set(opError=b.OpError.Failure, opErrInfo=str(err)))
        if rtInv.outs:
            for line in done:
                print(line)
        return cmndOutcome.set(opError=b.OpError.Success, opResults=f"{len(done)} members untracked")

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="repoNames",
            argDefault='',
            argChoices=[],
            argDescription="Member repo names; none: all members"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitGroup_cachedListUpdate" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitGroup_cachedListUpdate>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitGroup_cachedListUpdate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Write /bisos/var/gitGroup/<gitGroup>/cachedList.<vcMode>: the gitGroup
directory (when it is a git repo) and the members (real paths), for Blee's Magit menus.
        #+end_org """)
        try:
            target = cachedListWrite()
        except (ValueError, OSError) as err:
            return failed(cmndOutcome.set(opError=b.OpError.Failure, opErrInfo=str(err)))
        lines = len(target.read_text().splitlines())
        return cmndOutcome.set(opError=b.OpError.Success, opResults=f"{target}: {lines} repos")


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "gitGroup_cachedList" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<gitGroup_cachedList>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class gitGroup_cachedList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Print the cached list; write it first if it is absent.
        #+end_org """)
        try:
            target = cachedListPath()
            if not target.is_file():
                cachedListWrite()
            lines = target.read_text().splitlines()
        except (ValueError, OSError) as err:
            return failed(cmndOutcome.set(opError=b.OpError.Failure, opErrInfo=str(err)))
        if rtInv.outs:
            for line in lines:
                print(line)
        return cmndOutcome.set(opError=b.OpError.Success, opResults=f"{target}: {len(lines)} repos")


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
