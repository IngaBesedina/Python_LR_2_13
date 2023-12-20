#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tag


if __name__ == "__main__":
    t = input('тег - ')
    s = input('строка - ')

    tag_wrapp = tag.tag_wrapper(t)
    print(tag_wrapp(s))
