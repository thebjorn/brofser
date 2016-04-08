# -*- coding: utf-8 -*-
from invoke import collection
from dktasklib import docs, publish, Package, version, upversion

ns = collection.Collection(
    docs, publish, version, upversion
)
ns.configure({
    'pkg': Package()
})
