import PyPDF2
import itertools
import string
import time
from tqdm import tqdm

def dictionary_attack(pdf_path, wordlist_path):
    """
    Attempt to open a PDF using passwords from a wordlist
    """
    with open(wordlist_path, 'r', errors='ignore') as wordlist:
        words = [line.strip() for line in wordlist]
    
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    
    for word in tqdm(words, desc="Trying passwords"):
        try:
            if pdf_reader.decrypt(word):
                print(f"\nSuccess! Password found: {word}")
                return word
        except:
            continue
    
    print("\nPassword not found in wordlist.")
    return None

def brute_force_attack(pdf_path, max_length=4, chars=string.printable.strip()):
    """
    Attempt to open a PDF by trying all possible character combinations
    """
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    
    for length in range(1, max_length + 1):
        print(f"Trying passwords with length {length}...")
        for attempt in tqdm(itertools.product(chars, repeat=length), 
                           desc=f"Length {length}", 
                           total=len(chars)**length):
            password = ''.join(attempt)
            try:
                if pdf_reader.decrypt(password):
                    print(f"\nSuccess! Password found: {password}")
                    return password
            except:
                continue
    
    print("\nBrute force attack completed. Password not found.")
    return None

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='PDF Password Cracker')
    parser.add_argument('pdf_file', help='Path to the encrypted PDF file')
    parser.add_argument('-w', '--wordlist', help='Path to wordlist file for dictionary attack')
    parser.add_argument('-b', '--bruteforce', action='store_true', 
                       help='Use brute force attack (warning: can be very slow)')
    parser.add_argument('-l', '--max-length', type=int, default=4,
                       help='Maximum password length for brute force attack (default: 4)')
    
    args = parser.parse_args()
    
    start_time = time.time()
    
    if args.wordlist:
        print("Starting dictionary attack...")
        password = dictionary_attack(args.pdf_file, args.wordlist)
    elif args.bruteforce:
        print("Starting brute force attack...")
        print("Warning: This may take a very long time!")
        password = brute_force_attack(args.pdf_file, args.max_length)
    else:
        print("Please specify either --wordlist or --bruteforce option")
        return
    
    if password:
        print(f"Password cracked in {time.time() - start_time:.2f} seconds")
    else:
        print("Failed to crack the password")

if __name__ == '__main__':
    main()