# intent_generator.py
Used to generate DialogFlow intent in json format from text file source

### Requirements
python 3.5.0 +
python-dateutil==2.7.5

### Usage
python intent_generator.py -i INPUT_FILE_PATH -o OUTPUT_FILE_PATH

### Example:
python intent_generator.py -i "C:\hello.txt" -o "F:\hello.json"

### Txt File Description:
Should be a basic txt file.
Each row is a single training example.
UTF-8 encoded.

### Output:
Valid json file for uploading to DialogFlow

