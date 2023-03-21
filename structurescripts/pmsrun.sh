#!/bin/bash
pymol -cq $1 -- ${@:2}
