import json
import httpx
from mcp.server.fastmcp import FastMCP
import pandas as pd
from typing import Union, Dict
import datetime

#initializing mcp server
Server = FastMCP(name = 'Orchestrator_Network')
USER_AGENT = 'Orchestrator'

async def plan_calendar(input: Union[str, Dict], output_path = None ) -> str:
    if isinstance(input, Dict):
        for key in input['plan']:
            