#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

"""Add custom configs and default values"""
from fvcore.common.config import CfgNode

def add_custom_config(_C):
    # Add your own customized configs.
    _C.TL = CfgNode()
    _C.TL.METHOD = "ft"
    _C.TL.LR_MULTIPLIER = 1e-1
    _C.TL.EXCLUDE_FREEZE = []
