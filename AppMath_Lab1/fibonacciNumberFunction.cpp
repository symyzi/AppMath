#include <cmath>
#include "methods.h"

double fibonacciNumberFunction(double n) {
    return 1 / std::sqrt(5) * (pow(((1 + std::sqrt(5)) / 2), n) - pow(((1 - std::sqrt(5)) / 2), n));
}
