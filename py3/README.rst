=======================================
bisos.gitist: Git Mass Cloning and More
=======================================

.. contents::
   :depth: 3
..

Overview
========

*bisos.gitist* provides general facilities for mass cloning of public
github and gitlab and also private gitlab instances.

bisos.gitist is a python package that uses the
`PyCS-Framework <https://github.com/bisos-pip/pycs>`__.

gitist.cs is a seed. Common usages of gitist take the form of a
gitistProc.pcs.

.. _table-of-contents:

Table of Contents TOC
=====================

-  `Overview <#overview>`__
-  `Gitist Layers <#gitist-layers>`__
-  `Post-Installation Setup <#post-installation-setup>`__
-  `Installation <#installation>`__

   -  `Installation With pip <#installation-with-pip>`__
   -  `Installation With pipx <#installation-with-pipx>`__

-  `Usage <#usage>`__

   -  `Local Usage (system
      command-line) <#local-usage-system-command-line>`__

-  `Documentation and Blee-Panels <#documentation-and-blee-panels>`__

   -  `bisos.gitist Blee-Panels <#bisosgitist-blee-panels>`__

-  `Support <#support>`__
-  `Planned Improvements <#planned-improvements>`__

Gitist Layers
=============

#. PyCS Framework
#. Seeded/Planted PyCS Framework (gitist.cs)
#. Common csCmndsList (bisos.csSeed)
#. Gitist Commands CSUs

Post-Installation Setup
=======================

After installing, run the provisioning script to create the credentials
directory and place the configuration templates:

.. code:: bash

   config/provision.pcs -i credsSetup

This creates ``~/credentials/git/`` and copies two config files there if
they do not already exist:

-  ``~/credentials/git/githubHosts.cfg`` — GitHub configuration; insert
   your GitHub PAT (Personal Access Token) here.
-  ``~/credentials/git/gitlabHosts.cfg`` — GitLab configuration; insert
   your GitLab PAT here.

Once the PATs are in place, you can run the gitist proc scripts, e.g.:

.. code:: bash

   bin/github-pub-gitist.pcs
   bin/gitlab-pub-gitist.pcs

Installation
============

The sources for the bisos.gitist pip package are maintained at:
https://github.com/bisos-pip/gitist.

The bisos.gitist pip package is available at PYPI as
https://pypi.org/project/bisos.gitist

You can install bisos.gitist with pip or pipx.

Installation With pip
---------------------

If you need access to bisos.gitist as a python module, you can install
it with pip:

.. code:: bash

   pip install bisos.gitist

Installation With pipx
----------------------

If you only need access to bisos.gitist on command-line, you can install
it with pipx:

.. code:: bash

   pipx install bisos.gitist

Usage
=====

Local Usage (system command-line)
---------------------------------

``gitist.cs`` does the equivalent of gitist.

.. code:: bash

   bin/gitist.cs
   bin/gitistProc.pcs

Documentation and Blee-Panels
=============================

bisos.gitist is part of ByStar Digital Ecosystem http://www.by-star.net.

This module's primary documentation is in the form of Blee-Panels.
Additional information is also available in:
http://www.by-star.net/PLPC/180047

bisos.gitist Blee-Panels
------------------------

bisos.gitist Blee-Panles are in ./panels directory. From within Blee and
BISOS these panles are accessible under the Blee "Panels" menu.

See
`file:./panels/_nodeBase_/fullUsagePanel-en.org <./panels/_nodeBase_/fullUsagePanel-en.org>`__
for a starting point.

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact

Planned Improvements
====================

-  Enumerate applicabilities: telecom/SON, datacenter, CMIP-MOs
-  py3/bisos/gitist/tocsModule\ :sub:`csu`.py
