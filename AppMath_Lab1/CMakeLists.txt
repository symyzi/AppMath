cmake_minimum_required(VERSION 3.21)
project(AppMath_Lab1)

set(CMAKE_CXX_STANDARD 14)

add_executable(AppMath_Lab1
        main.cpp
        constants.h
        methods.h

        Dichotomy.cpp
        GoldenRatio.cpp
        Fibonacci.cpp
        Parabola.cpp
        Brent.cpp

        objectiveFunction.cpp
        fibonacciNumberFunction.cpp)
