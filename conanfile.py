#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostIclConan(base.BoostBaseConan):
    name = "boost_icl"
    url = "https://github.com/bincrafters/conan-boost_icl"
    lib_short_names = ["icl"]
    header_only_libs = ["icl"]
    b2_requires = [
        "boost_assert",
        "boost_concept_check",
        "boost_config",
        "boost_container",
        "boost_core",
        "boost_date_time",
        "boost_detail",
        "boost_iterator",
        "boost_move",
        "boost_mpl",
        "boost_rational",
        "boost_static_assert",
        "boost_type_traits",
        "boost_utility"
    ]


