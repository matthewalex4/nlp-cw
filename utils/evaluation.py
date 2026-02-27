#!/usr/bin/env python
import sys
import os
import os.path
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
import numpy as np

# as per the metadata file, input and output directories are the arguments
[_, input_dir, output_dir, file_name] = sys.argv

# unzipped submission data is always in the 'res' subdirectory
# https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions

# define gold data path
ref_dir = os.path.join(input_dir, 'ref')

# define submission data path
submission_dir = os.path.join(input_dir, 'res')
files = os.listdir(submission_dir)

# define path for scores file
outf = open(os.path.join(output_dir,'scores.txt'),'w')

# evaluating on task 1
if file_name in files:
    task1_res = []
    task1_gold = []
    with open(os.path.join(submission_dir, file_name)) as f:
        for line in f:
            task1_res.append(int(line.strip()))
    with open(os.path.join(ref_dir, file_name)) as f:
        for line in f:
            task1_gold.append(int(line.strip()))
    # task 1 scores
    t1p = precision_score(task1_gold, task1_res)
    t1r = recall_score(task1_gold, task1_res)
    t1f = f1_score(task1_gold, task1_res)
    # task1
    outf.write('task1_precision:'+str(t1p)+'\n')
    outf.write('task1_recall:'+str(t1r)+'\n')
    outf.write('task1_f1:'+str(t1f)+'\n')    
