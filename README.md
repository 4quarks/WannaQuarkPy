# WannaQuarkPy

```
               /'.    .'\
               \( \__/ )/
         ___   / (.)(.) \   ___
    _.-"`_  `-.|  ____  |.-`  _`"-._
 .-'.-'//||`'-.\  V--V  /.-'`||\\'-.'-.
`'-'-.// ||    / .___.  \    || \\.-'-'`
      `-.||_.._|        |_.._||.-'
               \ ((  )) /
                '.    .'
                  `\/`
```

In order to explore the soul of the ransomware attacks we have developed a basic ransomware using python that can be used to encrypt and decrypt any type of files.
<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3
  ```sh
  python --version
  sudo apt install python3
  ```
  
### Installation

1. Clone the repo:
   ```
   $ git clone https://github.com/4quarks/WannaQuarkPy.git
   ```
2. Setup virtual environment:
    ```
    $ cd WannaQuarkPy
    $ sudo apt-get install python3-venv
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
3. Install Python libraries listed on the `requirements.txt`:
   ```
   $ pip install -r requirements.txt
   ```
   
<!-- USAGE EXAMPLES -->
## Usage
You can explore the functionalities:
```bash
$ python -m wannaquark -h
```
The command generates a logfile (`wannaquark.log`) where you can see further details.

### Encrypt

1) Encrypt all files inside a folder
```bash
python3 -m wannaquark encrypt folder_to_encrypt
```

2) Encrypt all files with certain extension
```bash
python3 -m wannaquark encrypt folder_to_encrypt -e ".txt,.png"
```

3) Create a document with the key of encryption
```bash
python3 -m wannaquark encrypt folder_to_encrypt -k
```

4) Create a document with the list of target files
```bash
python3 -m wannaquark encrypt folder_to_encrypt -t
```
4) Encrypt and decrypt the file
```bash
python3 -m wannaquark encrypt folder_to_encrypt -d
```

### Decrypt
1) Decrypt all documents encrypted in a certain folder using the given key
```bash
python3 -m wannaquark decrypt folder_to_decrypt "key-of-decryption"
```

### Example
```bash
$ cat test/test.txt 
hello
$ python -m wannaquark encrypt test
The key generated is b';\x7fR0\x13\x0eeR'
$ python -m wannaquark decrypt test "b';\x7fR0\x13\x0eeR'"
$ cat test/test_decry.txt 
hello
```