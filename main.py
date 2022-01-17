#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 12:50:53 2022

@author: cloture
"""
import numpy

seq_a = "GCATGCG"
seq_b = "GATTACA"

match = 1
penalty = -1


def build_mat(n, m):
    return numpy.zeros(shape=(n + 1, m + 1))

def score(a, b):
    if (a == b):
        return match
    else:
        return penalty

def fill_cell(mat, i, j):
        match = mat[i - 1][j - 1] + score(seq_a[i - 1], seq_b[j - 1])
        delete = mat[i - 1][j] + penalty
        insert = mat[i][j - 1] + penalty
        mat[i][j] = max(match, delete, insert)

def fill_mat(mat):
    for i in range (0, len(mat)):
        for j in range (0, len(mat[0])):
            if (j < 1):
                mat[i][j] = i * penalty
            elif (i < 1):
                mat[i][j] = j * penalty
            else:
                fill_cell(mat, i, j)

def traceback(mat):
    print(mat)
    
    align_a = ""
    align_b = ""
    
    i = len(seq_a)
    j = len(seq_b)
    
    while(i > 0 or j > 0):
        if (mat[i][j] == mat[i - 1][j - 1] + score(seq_a[i - 1], seq_b[j - 1])):
            align_a += seq_a[i - 1]
            align_b += seq_b[j - 1]
            i -= 1
            j -= 1
        elif (mat[i][j] == mat[i - 1][j] + penalty):
            align_a += seq_a[i - 1]
            align_b += "-"
            i -= 1
        else:
            align_a += "-"
            align_b += seq_b[i - 1]
            j -= 1
    return align_a[::-1], align_b[::-1]


def needleman_wunsch():
    mat = build_mat(len(seq_a), len(seq_b))
    fill_mat(mat)
    align_a, align_b = traceback(mat)
    
    print("ALIGNEMENT A : " + align_a)
    print("ALIGNEMENT_B : " + align_b)
            
    
    
    
    
    
    
    
    
    
    