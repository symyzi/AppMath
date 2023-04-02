#ifndef LAB_1_CONSTANTS_H
#define LAB_1_CONSTANTS_H

#include <string>
#include <cmath>

const double EPS = 0.001;
const double D = 0.00000005; // Delta for Dichotomy method
const double A0 = 9;
const double B0 = 12;
const double GR = (1 + std::sqrt(5)) / 2; // Golden Ratio

const std::string PATH{
        "D:\\clion projects\\AppMath_Lab1\\output\\lab1out.txt"}; // Insert your path to lab1out.txt
const std::string DICHOTOMYOUT{"D:\\clion projects\\AppMath_Lab1\\output\\DichotomySection.txt"};
const std::string GOLDENRATIOOUT{"D:\\clion projects\\AppMath_Lab1\\output\\GoldenRatioSection.txt"};
const std::string FIBONACCIOUT{"D:\\clion projects\\AppMath_Lab1\\output\\FibonacciSection.txt"};
const std::string PARABOLAOUT{"D:\\clion projects\\AppMath_Lab1\\output\\ParabolaSection.txt"};
const std::string BRENTOUT{"D:\\clion projects\\AppMath_Lab1\\output\\BrentSection.txt"};

#endif //LAB_1_CONSTANTS_H
