#!/usr/bin/env python3

def pytest_itemcollected(item):
    try:
        par = item.parent.obj
        node = item.obj
        pref = par.__doc__.strip() if getattr(par, '__doc__', None) else par.__class__.__name__
        suf = node.__doc__.strip() if getattr(node, '__doc__', None) else node.__name__
        if pref or suf:
            item._nodeid = ' '.join((pref, suf))
    except Exception:
        # Avoid breaking pytest if something unexpected happens
        pass
