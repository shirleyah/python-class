#!/usr/bin/env python3
"""
nucleotide_frequency.py - Calculate nucleotide frequencies in a DNA sequence.

Author: <heladia@ccg.unam.mx>
Date: 2023-10-10
Version: 1.0

Usage:
    python nucleotide_frequency.py --file <archivo_dna.txt>

Options:
    --file : Specify the path to a text file containing the DNA sequence.

Description:
    This program reads a DNA sequence from a specified file, calculates the frequency
    of nucleotides (A, T, C, G), and displays the count and percentage of each nucleotide.

Example:
    python nucleotide_frequency.py --file my_dna_sequence.txt

Notes:
    Ensure that the input file contains a valid DNA sequence consisting only of characters A, T, C, and G.
"""

import argparse


def calcular_frecuencias(secuencia):
    """
    Calculate the absolute and percentage frequencies of each nucleotide in the given DNA sequence.

    Args:
        secuencia (str): A string representing the DNA sequence.

    Returns:
        dict: A dictionary with nucleotides as keys and a tuple of count and percentage as values.
    """

    # Dictionary to hold the count of each nucleotide
    conteo = {
        'A': secuencia.count('A'),
        'T': secuencia.count('T'),
        'C': secuencia.count('C'),
        'G': secuencia.count('G')
    }

    # Sum the total number of nucleotides counted
    total_nucleotidos = sum(conteo.values())

    # Calculate percentage frequencies for each nucleotide
    frecuencias = {key: (value, (value / total_nucleotidos) * 100) for key, value in conteo.items()}

    return frecuencias


def main():

    # Create an argument parser for command line options
    parser = argparse.ArgumentParser(
        description='Calcula la frecuencia de nucleótidos en una secuencia de DNA proporcionada en un archivo.'
    )
    parser.add_argument('--file', type=str, required=True, help='Archivo de texto que contiene la secuencia de DNA.')

    args = parser.parse_args()

    filename = args.file

    try:
        # Open the file and read the DNA sequence
        with open(filename, 'r') as file:
            secuencia = file.read().strip().upper()

        # Calculate the nucleotide frequencies
        frecuencias = calcular_frecuencias(secuencia)

        # Output the frequencies to the console
        for nucleotido, (conteo, porcentaje) in frecuencias.items():
            print(f"Nucleótido: {nucleotido}, Conteo: {conteo}, Porcentaje: {porcentaje:.2f}%")

    # Handle the case where the file is not found
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no fue encontrado.")
        
    # Handle any other exceptions that might occur
    except Exception as e:
        print(f"Se produjo un error: {e}")


if __name__ == '__main__':
    main()
