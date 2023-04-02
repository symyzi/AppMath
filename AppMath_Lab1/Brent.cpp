#include <vector>
#include "methods.h"
#include "constants.h"

int ITERATION_COUNT_B = 0;
int FUNCTION_CALLS_B = 0;

const double GR_REV = (3 - std::sqrt(5)) / 2;

void Brent() {
    double a = A0;
    double b = B0;
    double w = b - (b - a) / GR;
    double x = b - (b - a) / GR;
    double v = b - (b - a) / GR;
    double u;
    double yw = objectiveFunction(w);
    double yx = objectiveFunction(x);
    double yv = objectiveFunction(v);

    FUNCTION_CALLS_B += 3;

    double d = b - a;
    double e = b - a;

    std::vector<double> section;

    while (b - a > EPS) {
        ITERATION_COUNT_B++;

        double g = e;
        e = d;

        double uTemp;
        if (x != w && w != v && x != v && yx != yw && yw != yv && yx != yv) {
            uTemp = std::abs(v - (pow((v - w), 2) * ((yx - yv) - pow((v - x), 2) * (yv - yw)) /
                                  (2 * ((v - w) * (yx - yv) - (v - x) * (yx - yw)))));

            if (uTemp >= a + EPS && a <= b - EPS && std::abs(uTemp - x) < g / 2) {
                u = uTemp;
                d = std::abs(u - x);
            } else {
                if (x < (b + a) / 2) {
                    u = x + GR_REV * (b - x);
                    d = b - x;
                } else {
                    u = x - GR_REV * (x - a);
                    d = x - a;
                }
            }
        } else {
            if (x < (b + a) / 2) {
                u = x + GR_REV * (b - x);
                d = b - x;
            } else {
                u = x - GR_REV * (x - a);
                d = x - a;
            }
        }

        double yu = objectiveFunction(u);
        FUNCTION_CALLS_B++;

        // Change boundaries
        if (yu <= yx) {
            if (u >= x) {
                a = x;
            } else {
                b = x;
            }
            v = w;
            w = x;
            x = u;
            yv = yw;
            yw = yx;
            yx = yu;
        } else {
            if (u >= x) {
                b = u;
            } else {
                a = u;
            }

            if (yu <= yw || w == x) {
                v = w;
                w = u;
                yv = yw;
                yw = yu;
            } else if (yu <= yv || v == x || v == w) {
                v = u;
                yv = yu;
            }
        }
        section.push_back(b - a);
    }

    std::ofstream fout(PATH, std::fstream::app);
    fout << "Brent Result: " << (a + b) / 2 << '\n';
    fout << "Iterations: " << ITERATION_COUNT_B << " Function calls: " << FUNCTION_CALLS_B << '\n';
    fout.close();

    std::ofstream fout1(BRENTOUT);
    fout1 << "Section:" << '\n';
    for (double i: section)
        fout1 << i << '\n';
    fout1.close();
}