#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A plugin for Autobot that rolls a dice of variable sides"""

import random


def rollDie(sides):
    """Get a random number between 1 and N"""
    try:
        if int(sides) >= 2:
            count = int(sides) + 1
            roll = random.randrange(1,count)
            return roll
        else:
            return "Please use a number greater than one"
    except ValueError:
        message = "I'm sorry, I can't use that, please tell me the number of sides you want using whole positive integers. dice <num>"
        return message
    except:
        return
