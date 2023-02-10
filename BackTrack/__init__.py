#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根结点出发深度探索解空间树。
当探索到某一结点时，要先判断该结点是否包含问题的解，
如果包含，就从该结点出发继续探索下去，如果该结点不包含问题的解，则逐层向其祖先结点回溯。（其实回溯法就是对隐式图的深度优先搜索算法）。
若用回溯法求问题的所有解时，要回溯到根，且根结点的所有可行的子树都要已被搜索遍才结束。
而若使用回溯法求任一个解时，只要搜索到问题的一个解就可以结束。
"""
