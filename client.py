from openai import OpenAI
import os

class MCPClient:
    def __init__(self):
        self.api_key = os.get_env('DASHSCOPE_API_KEY')
        self.model = os.get_env('MODEL')
        self.base_url = os.get_env('BASE_URL')
        #fill in session upon server code finish
        self.session = ''
        #checking for api_keys
        if not os.get_env('DASHSCOPE_API_KEY'):
            raise ValueError ('Warning, missing API key, to continue using the service, please provide an API key')
        
    def Connect_To_Server(self, server_path : str) -> str:

        #checking whether the server script is either a .py or .js file
        if not ((is_py := server_path.endswith('.py')) or (is_js := server_path.endswith('.js'))):
            raise ValueError('Warning, server script must be .py or .js file')
        
        #depending on the is_py or is_js, path in the command and start the script
        command = 'python' if is_py else 'node'
        

        