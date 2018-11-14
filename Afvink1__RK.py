# Naam: Rutger Kemperman
# Datum: 14-11-2018
# Versie: 2

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.



def main():
    """roept de main functie aan, itereert over de andere functies, en vraagt om een zoekwoord.
    Op dit zoekwoord wordt gezocht in het bestand, en print het gevonden antwoord.
    Input:
    zoekwoord - string, opgegeven woord wordt doorzocht in het bestand.
    Output:
    gevonden data - string, alle lines die met het zoekwoord verband hebben.
    """
    bestand = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"
    headers, seqs = lees_inhoud(bestand)
    zoekwoord = input("Geef een zoekwoord op: ")
    try:
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:", headers[i])
                check_is_dna = is_dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")
    except FileNotFoundError:
        print("there is no file to be found")
    except IOError:
        print("there is a problem with the selected file")
    except UnicodeDecodeError:
        print("an unexpected error has occurred")


def lees_inhoud(bestands_naam):
    """opent het hele bestand en leest deze. Headers en sequenties worden in aparte lijsten gezet.

    Input:
    bestands_naam - string, de naam van het in te lezen bestand

    Output:
    headers - list, lijst met alle headers uit het bestand
    seqs - list, lijst met alle sequences uit het bestand
    """
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs



def is_dna(seq):
    """bepaalt of de inhoud DNA is aan de hand van de lengte van het bestand.
    Output:
    dna - bool, geeft aan of het bestand wel of niet uit alleen DNA bestaat.
    """
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g

    if total == len(seq):
        dna = True
    return dna


def knipt(alpaca_seq):
    """
    """
    try:
        bestand = open("enzymen.txt")
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^", "")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")
    except FileNotFoundError:
        print("oi where dat file @?")
    except IOError:
        print("File cant be opened, get a crowbar")
    except:
        print("not sure what happened, but something happened for sure")


main()

