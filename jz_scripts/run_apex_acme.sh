#!/bin/bash
#SBATCH -J beamrdiderapexacme
#SBATCH --cpus-per-task 64
#SBATCH -t 24:00:00
#SBATCH --output=/scratch/enisioti/acme_log/jz_logs/%j.out
#SBATCH --error=/scratch/enisioti/acme_log/jz_logs/%j.err
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/gpfs/home/enisioti/anaconda3/envs/acme/lib
python examples/baselines/rl_discrete/run_dqn_custom.py