# (c) Yasuhiro Fujii <http://mimosa-pudica.net>, under MIT License.
from numpy import *
from matplotlib import pyplot


def plot(xs, tss, fn):
    pyplot.figure(figsize = (9.0, 6.0))
    pyplot.xlim(min(xs), max(xs))
    pyplot.ylim(0.0, max(max(ts) for ts in tss))
    for i, ts in enumerate(tss):
        pyplot.plot(xs, ts, ["--", "-.", ":"][i % 3], label = "%d" % i, linewidth = 1.0)
    pyplot.legend()
    pyplot.savefig(fn, format = "svg", bbox_inches = "tight")

def plot_variance_normalized():
    xs = linspace(-6.0, 3.0, 256)
    gs = (1.0 / sqrt(2.0 * pi)) * exp(-0.5 * xs * xs)
    ss = 0.5 / cosh((pi / 2.0) * xs)
    a = pi / (2.0 * sqrt(3.0))
    fs = (a / 2.0) / cosh(a * xs) ** 2
    a = sqrt((pi * pi - 6.0) / 3.0)
    hs = where(abs(xs) < pi / a, (a / (2.0 * pi)) * (1.0 + cos(a * xs)), 0.0)
    ts = (2.0 / pi) / (1.0 + xs * xs) ** 2
    plot(xs, [ts, ss, fs, gs, hs], "variance.svg")

def plot_normalized_at_zero():
    xs = linspace(-8.0, 4.0, 256)
    gs = exp(-0.5 * xs * xs)
    ss = 1.0 / cosh(xs)
    fs = 1.0 / cosh(xs / sqrt(2)) ** 2
    hs = where(abs(xs) < 2.0, 0.5 + 0.5 * cos((pi / 2.0) * xs), 0.0)
    cs = 1.0 / (1.0 + 0.5 * xs * xs)
    plot(xs, [cs, ss, fs, gs, hs], "at_zero.svg")

plot_variance_normalized()
plot_normalized_at_zero()
