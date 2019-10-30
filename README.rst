crr_labels
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Python package wrapping over FANTOM labels for cis regulatory regions.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install crr_labels

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Usage examples
-----------------------------------------------
Currently we support only `FANTOM CAGE data <http://fantom.gsc.riken.jp/5/data/>`_,
but in the future also `Roadmap <https://egg2.wustl.edu/roadmap/web_portal/chr_state_learning.html>`_
will be included.

FANTOM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To retrieve the FANTOM promoters you can proceed as follows:

.. code:: python

    from crr_labels import fantom

    enhancers, promoters = fantom(
        cell_lines=["HelaS3", "GM12878"],
        window_size=200,
        genome = "hg19",
        center_enhancers = "peak",
        enhancers_threshold = 0,
        promoters_threshold = 5,
        drop_always_inactive_rows = True
    )

The library will download and parse the fantom project raw data and return two dataframes for the required cell lines.
Consider reading the method docstring for more id-depth informations about the method.

The main steps are the following:

- The raw files are retrieved from the fantom dataset from the link specified in the `fantom_data.json file <add link>`_
- The window for the enhancers and promoters are expanded or compressed to the given window size. In particular:
    - The enhancers window can either be centered on the region center with the "center" mode or around the "peak" with the "peak" mode.
    - The promoters window is upstream in the positive strand from the end of the promoter and downstream on the negative strand from the start of the promoter.
- When multiple experiments are present for a cell line, for instance for "HelaS3", an average of the activation peaks is executed.
- Optionally (and by default) the rows that are always inactive for the chosen cell lines are dropped. You can specify this behaviour using the parameter "drop_always_inactive_rows".

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/crr_labels.png
   :target: https://travis-ci.org/LucaCappelletti94/crr_labels
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_crr_labels&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_crr_labels
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_crr_labels&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_crr_labels
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_crr_labels&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_crr_labels
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/crr_labels/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/crr_labels?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/crr_labels.svg
    :target: https://badge.fury.io/py/crr_labels
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/crr_labels
    :target: https://pepy.tech/badge/crr_labels
    :alt: Pypi total project downloads 

.. |codacy|  image:: https://api.codacy.com/project/badge/Grade/c0a7e110045a4d25933c65fe2014a33c
    :target: https://www.codacy.com/manual/LucaCappelletti94/crr_labels?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/crr_labels&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/7c18ec5176f2ebebef96/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/crr_labels/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/7c18ec5176f2ebebef96/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/crr_labels/test_coverage
    :alt: Code Climate Coverate