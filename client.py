# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import requests
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Send a query to the server.")
parser.add_argument("query", type=str, help="The query to send to the server")

# Parse arguments
args = parser.parse_args()

# Make the POST request with the query argument
response = requests.post("http://127.0.0.1:8000/predict", json={"query": args.query})
print(f"Status: {response.status_code}\nResponse:\n {response.text}")
