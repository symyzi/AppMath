#include <fstream>
#include <vector>
#include "constants.h"
#include "methods.h"

int ITERATION_COUNT_D = 0;
int FUNCTION_CALLS_D = 0;

void Dichotomy() {
    double mid;
    double a = A0;
    double b = B0;
    std::vector<double> section;
    while (b - a > EPS) {
        ITERATION_COUNT_D++;
        mid = (b + a) / 2;

        double y1 = objectiveFunction(mid - D);
        double y2 = objectiveFunction(mid + D);

        FUNCTION_CALLS_D += 2;

        if (y1 <= y2) {
            b = mid + D;
        } else if (y1 > y2) {
            a = mid - D;
        }
        section.push_back(b - a);
    }

    std::ofstream fout(PATH);
    fout << "Dichotomy Result: " << (a + b) / 2 << '\n';
    fout << "Iterations: " << ITERATION_COUNT_D << " Function calls: " << FUNCTION_CALLS_D << '\n';
    fout.close();

    std::ofstream fout1(DICHOTOMYOUT);
    fout1 << "Section:" << '\n';
    for (double i: section)
        fout1 << i << '\n';
    fout1.close();
}
