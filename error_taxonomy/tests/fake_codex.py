#!/usr/bin/env python3
"""Offline subprocess fixture: it never contacts a model or reads credentials."""
import json
import os
from pathlib import Path
import sys

args=sys.argv[1:]
if '--output-schema' not in args:
    raise SystemExit('test request omitted --output-schema')
schema=Path(args[args.index('--output-schema')+1])
json.loads(schema.read_text())
out=Path(args[args.index('--output-last-message')+1])
state=Path(os.environ['TAXONOMY_TEST_STATE'])
count=int(state.read_text()) if state.exists() else 0
values=json.loads(Path(os.environ['TAXONOMY_TEST_RESPONSES']).read_text())
state.write_text(str(count+1))
value=values[count]
out.write_text(value if isinstance(value,str) else json.dumps(value))
sys.stdin.read()
print(json.dumps({'type':'thread.started','thread_id':'test-isolated-session'}))
print(json.dumps({'type':'turn.completed','usage':{'input_tokens':(count+1)*100,'output_tokens':(count+1)*10}}))
