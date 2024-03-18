import asyncio
import discord
from discord import app_commands
from discord.ext import commands, tasks
from concurrent.futures import ThreadPoolExecutor
import requests
import re
import xml.etree.ElementTree as ET

class AzerothCore(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.executor = ThreadPoolExecutor(max_workers=2)


    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        self.soap_command = f".server info"
        print("AzerothCore Online")
        self.update_status.start()  # Start the background task


    def cog_unload(self):
        self.update_status.cancel()  # Stop the task when the cog is unloaded


    @tasks.loop(seconds=60)
    async def update_status(self):
        # Execute the SOAP command and get the result
        result = await self.execute_soap_command(self.soap_command)
        server_info = self.parse_server_info(result)
        await self.client.change_presence(activity=discord.Game(name=server_info)) # Update the client's status with the result


    def parse_server_info(self, soap_response):
        # Extract and format the server info from the SOAP response
        # connected_players = re.search(r"Connected players: (\d+)", soap_response).group(1)
        # connection_peak = re.search(r"Connection peak: (\d+)", soap_response).group(1)
        # update_time_diff = re.search(r"Update time diff: ([\dms, average: \dms]+)", soap_response).group(1)
        server_uptime = re.search(r"Server uptime: ([\d hour(s) minute(s) second(s)]+)", soap_response).group(1)
        server_status = "Online" if soap_response else "Offline"
        formatted_status = f"WOTLK Server: {server_status}\n\nServer uptime: {server_uptime}"
        return formatted_status


    @update_status.before_loop
    async def before_update_status(self):
        await self.client.wait_until_ready()  # Wait until the bot is ready


    async def execute_soap_command(self, soap_command):
        host = "xanmal.zapto.org"
        port = "7878"
        url = f'http://{host}:{port}/' # SOAP URL and Authentication
        soap_body = self.construct_soap_body(soap_command)
        auth = ('Xanmal', 'K1347334F!King!')  # Replace with your actual credentials
        response = await asyncio.get_event_loop().run_in_executor(self.executor, self.send_soap_request, url, auth, soap_body) # Sending the POST request to the SOAP service in a separate thread
        return response


    def construct_soap_body(self, command):
        # Construct SOAP XML Body
        return f'''<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                    xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                    xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
                    xmlns:xsd="http://www.w3.org/1999/XMLSchema"
                    xmlns:ns1="urn:AC">
                <SOAP-ENV:Body>
                    <ns1:executeCommand>
                        <command>{command}</command>
                    </ns1:executeCommand>
                </SOAP-ENV:Body>
            </SOAP-ENV:Envelope>'''


    def send_soap_request(self, url, auth, soap_body):
        headers = {'Content-Type': 'application/xml'}
        try:
            response = requests.post(url, auth=auth, data=soap_body, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as e:
            return f"Error occurred: {e}"


    @app_commands.command(name="create_account", description="Create a new game account")
    async def create_account(self, interaction: discord.Interaction, username: str, password: str):
        soap_command = f".account create {username} {password}"
        result = await self.execute_soap_command(soap_command)
        
        # Extract the name of the created account
        start_index = result.find("Account created: ") + len("Account created: ")
        end_index = result.find("&#xD;")
        account_name = result[start_index:end_index]
        
        extracted_part = f"Account created: {account_name}"
        await interaction.response.send_message(extracted_part)


    @app_commands.command(name="delete_account", description="Delete a game account")
    async def delete_account(self, interaction: discord.Interaction, account: str):
        soap_command = f".account delete {account}"
        result = await self.execute_soap_command(soap_command)
        
        # Extract the name of the deleted account
        start_index = result.find("Account deleted: ") + len("Account deleted: ")
        end_index = result.find("&#xD;")
        account_name = result[start_index:end_index]
        
        extracted_part = f"Account deleted: {account_name}"
        await interaction.response.send_message(extracted_part)


    @app_commands.command(name="olist", description="See who is online")
    async def olist(self, interaction: discord.Interaction):
        soap_command = ".account onlinelist"
        result = await self.execute_soap_command(soap_command)
        extracted_part = self.extract_response_part(result)
        await interaction.response.send_message(extracted_part)


    @app_commands.command(name="change_faction", description="Change character's faction")
    async def change_faction(self, interaction: discord.Interaction, name: str):
        soap_command = f".character changefaction {name}"
        result = await self.execute_soap_command(soap_command)
        extracted_part = self.extract_response_part(result)
        await interaction.response.send_message(extracted_part)


    def extract_response_part(self, result):
        start_index = result.find("<result>") + len("<result>")
        end_index = result.find("</result>")
        extracted_part = result[start_index:end_index]
        return extracted_part


async def setup(client):
    await client.add_cog(AzerothCore(client))
