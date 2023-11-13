# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#import random
import pprint
import google.generativeai as palm
import argparse
import sys
import os


#import vertexai
#from vertexai.language_models import TextGenerationModel

#temperature = 0.0
#project_id = 'mgcp-1192365-transcription-poc'
#location = 'us-central1'
#vertexai.init(project=project_id, location=location)

#parameters = {
#        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
#        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
#        "top_p": 0.8,
#        # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
#        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
#}
# promptStr = "Name the first ten USA Presidents."
#model = TextGenerationModel.from_pretrained("text-bison@001")

palm.configure()

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
def communicateWithChatGPT(str):
        prompt = str
        completion = palm.generate_text(
                model=model,
                prompt=str,
                temperature=0,
                max_output_tokens=1000000,
        )
        return completion.result
