#!/usr/bin/env python3

from py3dot import Graph

hello = Graph()
hello.add_edge('Hello', 'World')
hello.save_fig('hello.png')
