#!/bin/bash
#SBATCH --partition=small
#SBATCH --mem=128GB

hostname
module load pytorch
cd ~/slurm_tutorials
echo python $*
python $*
