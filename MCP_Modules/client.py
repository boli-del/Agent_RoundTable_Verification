from openai import OpenAI
import os
import asyncio
from mcp import ClientSession
from contextlib import AsyncExitStack
import openai

class MCPClient:
    def __init__(self):
        self.api_key = os.get_env('OPENAI_API_KEY')
        self.model = os.get_env('MODEL')
        self.base_url = os.get_env('BASE_URL')

        #fill in session upon server code finish
        self.session = ''
        self.client = OpenAI(api_key = self.api_key, base_url = self.base_url)
        self.exit_stack = AsyncExitStack()
        #checking for api_keys
        if not os.get_env('OPENAI_API_KEY'):
            raise ValueError ('Warning, missing API key, to continue using the service, please provide an API key')
        
    async def process_user_response(self, prompt : str) -> str:
        return 

    def Connect_To_Server(self, server_path : str) -> str:

        #checking whether the server script is either a .py or .js file
        if not ((is_py := server_path.endswith('.py')) or (is_js := server_path.endswith('.js'))):
            raise ValueError('Warning, server script must be .py or .js file')
        
        #depending on the is_py or is_js, path in the command and start the script
        #for future developments if using node and js
        command = 'python' if is_py else 'node'
    
    async def clean_up(self):
        await self.exit_stack.aclose()

async def main():
    return None
        