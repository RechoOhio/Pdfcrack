## Pdfcrack 
```
This tool is legitimate 
```
## Install Requirements (Termux)
```
pkg install python python2 python3
```
## Run commands 
```
git clone https://github.com/RechoOhio/Pdfcrack
cd Pdfcrack
pip install PyPDF2 tqdm
```
## Dictionary attack, password if faster common
```
python pdfcrack.py encrypted.pdf -w wordlist.txt
```
## Brute force attack, slower but more thorough 
```
python pdfcrack.py encrypted.pdf -b -l 5
```
## Don't forget thanks me Later
