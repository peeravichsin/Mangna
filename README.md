# Mangna (มั้งนะ)
Mangna is a tool that makes lists of possible passwords for Brute Force Attacks. It takes an input and changes it based on methods like Munge by Th3S3cr3tAg3nt to generate different potential passwords.

Reference https://github.com/Th3S3cr3tAg3nt/Munge

```
usage: mangna.py [-h] -i INPUT_FILE [-o OUTPUT_FILE] [-c] [-s] [-y]

Generate concatenated words and variants

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        Text file containing words (one per line)
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output file to save generated lines (default: output.txt)
  -c, --connect         Connect generated words first
  -s, --suffixes        Include suffix variants (Default)
  -y, --years           Include year variants
```

```bash
git clone https://github.com/peeravichsin/Mangna
```
