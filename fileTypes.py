from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PDFMinerLoader,
    TextLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredXMLLoader,
    TextLoader,  
)
import os
import glob
import re

# Define a dictionary mapping file extensions to their respective loaders
LOADER_MAPPING = {
    ".csv": (CSVLoader, {}),
    ".doc": (UnstructuredWordDocumentLoader, {}),
    ".docx": (UnstructuredWordDocumentLoader, {}),
    ".enex": (EverNoteLoader, {}),
    ".eml": (UnstructuredEmailLoader, {}),
    ".epub": (UnstructuredEPubLoader, {}),
    ".html": (UnstructuredHTMLLoader, {}),
    ".md": (UnstructuredMarkdownLoader, {}),
    ".odt": (UnstructuredODTLoader, {}),
    ".pdf": (PDFMinerLoader, {}),
    ".ppt": (UnstructuredPowerPointLoader, {}),
    ".pptx": (UnstructuredPowerPointLoader, {}),
    ".txt": (TextLoader, {"encoding": "utf8"}),
}

def clean_files(dir_path):
    # Set the directory path
    # dir_path = '/data'

    # Compile a regular expression pattern to match whitespace or irregular characters
    pattern = re.compile(r'\s+')

    # Loop through each file in the directory
    for filename in os.listdir(dir_path):
        # Clean up the file name by replacing whitespace and irregular characters with an underscore
        cleaned_filename = re.sub(pattern, '_', filename)

        # Get the original file path
        original_file_path = os.path.join(dir_path, filename)

        # Get the new file path with the cleaned-up name
        new_file_path = os.path.join(dir_path, cleaned_filename)

        # Check if the file exists and is not a directory
        if os.path.exists(original_file_path) and not os.path.isdir(original_file_path):
            # Rename the file to its cleaned-up name
            os.rename(original_file_path, new_file_path)

def load_documents_cls(directory, itemType:str):
    file_list = glob.glob(directory + f"/*{itemType}") # Include slash or it will search in the wrong directory!!
    loader = DirectoryLoader(directory, glob=f"**/*{itemType}", show_progress=True, use_multithreading=True, loader_cls=LOADER_MAPPING[itemType][0])
    documents = loader.load()
    return documents

# Usage
def load_all_docs(directory_path):
    directory_path = "/data"
    clean_files(directory_path)
    loaded_documents=[]
    for itemType in LOADER_MAPPING.keys():
        # print(itemType)
        loaded_documents.append(load_documents_cls(directory_path,itemType))

    return loaded_documents
