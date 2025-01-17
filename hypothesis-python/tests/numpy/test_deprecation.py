# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Most of this work is copyright (C) 2013-2021 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.
#
# END HEADER

from warnings import catch_warnings

import pytest

from hypothesis.errors import HypothesisDeprecationWarning, InvalidArgument
from hypothesis.extra import numpy as nps


def test_basic_indices_bad_min_dims_warns():
    with pytest.warns(HypothesisDeprecationWarning):
        with pytest.raises(InvalidArgument):
            nps.basic_indices((3, 3, 3), min_dims=4).example()


def test_basic_indices_bad_max_dims_warns():
    with pytest.warns(HypothesisDeprecationWarning):
        nps.basic_indices((3, 3, 3), max_dims=4).example()


def test_basic_indices_default_max_dims_does_not_warn():
    with catch_warnings(record=True) as record:
        nps.basic_indices((3, 3, 3)).example()
        nps.basic_indices((3, 3, 3), allow_newaxis=True).example()
        assert len(record) == 0
