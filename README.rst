crr_labels
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Python package wrapping over FANTOM and ENCODE labels for cis regulatory regions.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install crr_labels

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Python package wrapping over FANTOM and ENCODE labels for cis regulatory regions.



## Project data

- [Link to FANTOM cell_line to FANTOM code map](http://fantom.gsc.riken.jp/5/datafiles/latest/extra/Enhancers/Human.sample_name2library_id.txt)
- [Link to roadmap dataset](https://egg2.wustl.edu/roadmap/web_portal/chr_state_learning.html)
- [Link to roadmap cell_line to roadmap code map](https://egg2.wustl.edu/roadmap/data/byFileType/metadata/EID_metadata.tab)
- [Link to old ENCODE segmentation tracks](http://hgsv.washington.edu/cgi-bin/hgTrackUi?hgsid=2654871_pjNn3UAIBZ4mP640eon9AekZYGY2&g=hub_4_genomeSegmentation&hgTracksConfigPage=configure)
- [Link to download paths for old ENCODE segmentation tracks](http://ftp.ebi.ac.uk/pub/databases/ensembl/encode/integration_data_jan2011/byDataType/segmentations/jan2011/)
- [Link to Fantom Promoters](http://slidebase.binf.ku.dk/human_promoters/results)
- [Link to Fantom Enhancers](http://slidebase.binf.ku.dk/human_enhancers/results)


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