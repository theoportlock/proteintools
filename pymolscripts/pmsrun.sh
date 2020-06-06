#!/bin/bash
pymol -cq ~/proteintools/scripts/$1 -- ${@:2}
