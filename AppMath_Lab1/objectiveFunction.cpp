#include <cmath>
#include "methods.h"

double objectiveFunction(double x) {
    return std::exp(std::sin(x) * std::log(x));
}