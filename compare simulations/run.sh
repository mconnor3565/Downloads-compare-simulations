#!/bin/bash

mkdir -p plots
python3 plot_davg.py &
python3 plot_dperp.py &
python3 plot_drot.py &
python3 plot_dpara.py &

it config --global user.email "you@example.com"
  git config --global user.name "Your Name"