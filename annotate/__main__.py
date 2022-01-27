import sys
import argparse
from .program import run
from .args import args_setup

parser = args_setup()
pargs = parser.parse_args()
kwargs = {"archive": pargs.a, "classifier": pargs.c, "days_ago": pargs.d, "novel_objects": bool(pargs.n)}

run(**kwargs)
