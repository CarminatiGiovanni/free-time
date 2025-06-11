#include <pybind11/pybind11.h>
#include <cmath>

// z = re + im * i
// z^2 = (re^2 - im^2) + (2 * re * im) * i

int mendelbrot_point(double c_re, double c_im,const int MAX_ITER,const unsigned long long int LIMIT) {
    int n = 0;
    double z_re = 0;
    double z_im = 0;
    double new_re = 0;
    double new_im = 0;
    double mod = 0; // module of z
    while (mod < LIMIT && n < MAX_ITER) {
        new_re = z_re * z_re - z_im * z_im + c_re;
        new_im = 2 * z_re * z_im + c_im;
        z_re = new_re;
        z_im = new_im;
        mod = sqrt(z_re * z_re + z_im * z_im);
        n++;
    }
    return n;
}


PYBIND11_MODULE(mendelbrot, m) {
    m.doc() = "pybind11 module for mendelbrotset calculation"; // Optional module docstring

    m.def("mendelbrot_point", &mendelbrot_point, "A function that executes the mendelbrot calculation for a given complex number c",
          pybind11::arg("c_re"), pybind11::arg("c_im"), pybind11::arg("MAX_ITER"), pybind11::arg("LIMIT"));
}