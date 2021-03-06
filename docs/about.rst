Getting Start
=============

Link
----
    * GitHub: `   https://github.com/Mirio/psnstoreprice/tree/master <https://github.com/Mirio/psnstoreprice/tree/master>`_
    * Documentation: `http://psnstoreprice.readthedocs.org/ <http://psnstoreprice.readthedocs.org/>`_
    * PYPI: `https://pypi.python.org/pypi/psnstoreprice <https://pypi.python.org/pypi/psnstoreprice>`_


Badge
-----

.. image:: https://travis-ci.org/Mirio/psnstoreprice.svg?branch=0.1
    :target: https://travis-ci.org/Mirio/psnstoreprice

.. image:: https://img.shields.io/pypi/dm/psnstoreprice.svg
    :target: https://pypi.python.org/pypi/psnstoreprice

.. image:: https://img.shields.io/github/downloads/mirio/psnstoreprice/total.svg
    :target: https://github.com/Mirio/psnstoreprice/tree/0.1

.. image:: https://readthedocs.org/projects/psnstoreprice/badge/?version=0.1
    :target: http://psnstoreprice.readthedocs.org/en/latest/?badge=0.1
    :alt: Documentation Status

Features
--------
    * Easy to find the price without using the Amazon API
    * Easy to use
    * Python 3.x +
    * Unittest
    * Custom Errors


Installation via Pip
--------------------

.. code-block:: bash
    :name: installation

    pip install psnstoreprice


Installation from Source
------------------------

.. code-block:: bash
    :name: installation_source

    git clone https://github.com/Mirio/psnstoreprice.git
    cd psnstoreprice
    python setup.py install


Uninstall via Pip
-----------------

.. code-block:: bash
    :name: installation

    pip uninstall psnstoreprice


Basic usage
-----------

Code:

.. code-block:: python
    :name: code

    from psnstoreprice import PsnStorePrice

    url = "https://store.playstation.com/#!/en-ie/games/earth-defense-force-41-the-shadow-of-new-despair/" \
          "cid=EP4293-CUSA03467_00-EARTHDEFENSEFO41"
    pricelib = PsnStorePrice()
    print(pricelib.getprice(url))


Output:

.. code-block:: bash
    :name: code

    $ python example_getprice.py
    64.99

