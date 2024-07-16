# Intro

Introduction of Convolve operation.

---

[toc]

## Wikipedia

> In mathematics (in particular, functional analysis), convolution is a mathematical operation on two functions (${f}$ and ${g}$) that produces a third function
>
> $${f \ast g}$$
>
> The term convolution refers to both the result function and to the process of computing it. It is defined as the integral of the product of the two functions after one is reflected about the y-axis and shifted. The integral is evaluated for all values of shift, producing the convolution function. The choice of which function is reflected and shifted before the integral does not change the integral result (see commutativity). Graphically, it expresses how the 'shape' of one function is modified by the other. [wikipedia](https://en.wikipedia.org/wiki/Asterisk).

![example1](./asset/Convolution_of_box_signal_with_itself2.gif "example1")
![example2](./asset/Convolution_of_spiky_function_with_box2.gif "example2")

## Compare Convolve with Cross- and Auto-Correlation

![compare](./asset/Comparison_convolution_correlation.svg.png)

## Definition

The convolution of ${f}$ and ${g}$ is written ${f \ast g}$, denoting the operator with the symbol ${\ast}$.
In latex, you can use `\ast` function to write convolution symbol

$$\begin{cases}
(f \ast g)(t) \\
(f \circledast g)(t)
\end{cases}:=\int_{-\infty}^{\infty} f(\tau) g(t-\tau) d \tau$$

In discrete convolution

$$(f \ast g)[n]=\sum_{m=-\infty}^{\infty} f[m] g[n-m]$$

```latex
% Latex equation written by
% https://www.math-linux.com/latex/faq/latex-faq/article/latex-convolution-symbol

% With circle
$$(f \circledast g)(t):=\int_{-\infty}^{\infty} f(\tau) g(t-\tau) d \tau$$

% Without circle
$$(f \ast g)(t):=\int_{-\infty}^{\infty} f(\tau) g(t-\tau) d \tau$$
```

## Appendix

> The symbol U+2217 ∗ ASTERISK OPERATOR is different than U+002A * ASTERISK, which is often used to denote complex conjugation. See Asterisk § Mathematical typography.
> The asterisk (/ˈæstərɪsk/ *), from Late Latin asteriscus, from Ancient Greek ἀστερίσκος, asteriskos, "little star", is a typographical symbol. It is so called because it resembles a conventional image of a heraldic star. [wikipedia](https://en.wikipedia.org/wiki/Asterisk).
