#!/usr/bin/env python3
# Regenerates blocklists/pl-dno.jsonl from the Polish regulator's register of
# numbers that never make outgoing calls (UKE "DNO"): a call showing one of
# them is spoofed.
import csv, io, json, urllib.request

URL = "https://numeracja.uke.gov.pl/pl/orvc_tables/export.csv"

data = urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "hookline-sources"})).read().decode("utf-8")
rows = csv.DictReader(io.StringIO(data), delimiter=";")
numbers = sorted({r["numer_telefonu"].strip() for r in rows if r["numer_telefonu"].strip().isdigit() and not r["data_wykreslenia"].strip()})

with open("blocklists/pl-dno.jsonl", "w") as out:
    for number in numbers:
        out.write(json.dumps({"name": "Do Not Originate (UKE)", "pattern": "48" + number}) + "\n")
print(len(numbers), "numbers")
