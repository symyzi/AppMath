#include <fstream>
#include <vector>
#include <iostream>
#include "methods.h"
#include "constants.h"

int ITERATION_COUNT_F = 0;
int FUNCTION_CALLS_F = 0;

void Fibonacci() {
    double a = A0, b = B0;
    double n = (b - a) * 10;
    double x1 = a + (fibonacciNumberFunction(n) / fibonacciNumberFunction(n + 2)) * (b - a);
    double x2 = a + (fibonacciNumberFunction(n + 1) / fibonacciNumberFunction(n + 2)) * (b - a);
    double y1 = objectiveFunction(x1);
    double y2 = objectiveFunction(x2);
    FUNCTION_CALLS_F += 2;
    std::vector<double> section;
    while (b - a > EPS) {
        ITERATION_COUNT_F++;
        if (y1 <= y2) {
            b = x2;
            x2 = x1;
            y2 = y1;
            x1 = a + (fibonacciNumberFunction(n) / fibonacciNumberFunction(n + 2)) * (b - a);
            y1 = objectiveFunction(x1);
            FUNCTION_CALLS_F++;
        } else {
            a = x1;
            x1 = x2;
            y1 = y2;
            x2 = a + (fibonacciNumberFunction(n + 1) / fibonacciNumberFunction(n + 2)) * (b - a);
            y2 = objectiveFunction(x2);
            FUNCTION_CALLS_F++;
        }
        section.push_back(b - a);
    }
    std::ofstream fout(PATH, std::fstream::app);
    fout << "Fibonacci Result: " << (a + b) / 2 << '\n';
    fout << "Iterations: " << ITERATION_COUNT_F << " Function calls: " << FUNCTION_CALLS_F << '\n';
    fout.close();

    std::ofstream fout1(FIBONACCIOUT);
    fout1 << "Section:" << '\n';
    for (double i: section)
        fout1 << i << '\n';
    fout1.close();
}

