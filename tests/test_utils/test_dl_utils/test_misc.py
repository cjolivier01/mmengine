# Copyright (c) OpenMMLab. All rights reserved.
from importlib.machinery import ModuleSpec

from mmengine.utils.dl_utils import misc


def test_mmcv_full_available(monkeypatch):
    monkeypatch.setattr(
        misc.importlib.util,
        "find_spec",
        lambda name: ModuleSpec(name, loader=None),
    )
    assert misc.mmcv_full_available()

    monkeypatch.setattr(misc.importlib.util, "find_spec", lambda name: None)
    assert not misc.mmcv_full_available()
