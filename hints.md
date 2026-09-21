# GitHub Markdown and Mathematics Rendering Hints

This file defines the formatting rules to use when creating or editing mathematical exercise sheets in this repository.

The main goal is simple: **the raw Markdown must render correctly on GitHub without broken LaTeX, red error messages, or formulas displayed as literal source code.**

---

## 1. Writing style

Write like a technical notebook or exercise sheet, not like a conversation.

Use normal Markdown headings:

```markdown
# Main title
## Section
### Exercise 1. Title
```

Prefer neutral academic phrasing. Avoid conversational filler such as:

- "Let's solve this"
- "Now we compute"
- "As you can see"

Keep explanatory text outside mathematical environments whenever possible.

---

## 2. Use only dollar delimiters for mathematics

Use:

- `$...$` for short inline mathematics,
- `$$...$$` for display mathematics.

Correct:

```markdown
The function is $f(x)=x^2+1$.

$$
f'(x)=2x
$$
```

Do **not** use:

```text
\( ... \)
\[ ... \]
```

Do not use display-style environments between single dollar signs.

Incorrect:

```markdown
$\begin{cases}
x+y=2, \\
x-y=0
\end{cases}$
```

Correct:

```markdown
$$
\begin{cases}
x+y=2, \\
x-y=0
\end{cases}
$$
```

---

## 3. Display mathematics must be separated from text

Every display formula must have:

1. one empty line before the opening `$$`,
2. the opening `$$` on its own line,
3. the formula on separate line(s),
4. the closing `$$` on its own line,
5. one empty line after the block.

Correct:

```markdown
The determinant is

$$
\det A = -2
$$

Therefore the matrix is invertible.
```

Incorrect:

```markdown
The determinant is $$\det A=-2$$, so the matrix is invertible.
```

Also avoid consecutive display blocks without an empty line between them.

---

## 4. Matrices: always use `pmatrix`

Use `pmatrix` for matrices.

Each matrix row must be written on a separate Markdown line and must end with `\\`.

Correct:

```markdown
$$
A=
\begin{pmatrix}
2 & 1 & 0 \\
0 & 1 & -1 \\
1 & 0 & 1 \\
\end{pmatrix}
$$
```

Do not compress a matrix into one line.

Avoid:

```text
\begin{matrix}...\end{matrix}
\begin{bmatrix}...\end{bmatrix}
\begin{array}...\end{array}
```

For an augmented matrix, keep `pmatrix` and use `\mid` explicitly:

```markdown
$$
\begin{pmatrix}
1 & 2 & \mid & 3 \\
0 & 1 & \mid & 4 \\
\end{pmatrix}
$$
```

---

## 5. Systems and piecewise functions: never glue rows together

For `cases`, every row must be placed on a new source line.

Correct:

```markdown
$$
f(x)=
\begin{cases}
x+1, & -1 \le x < 1, \\
2, & 1 \le x \le 3.
\end{cases}
$$
```

Incorrect:

```text
$$
f(x)=\begin{cases}x+1,&-1\le x<1,\\2,&1\le x\le3.\end{cases}
$$
```

The second version can make GitHub interpret fragments such as `\\2`, `\\x`, `\\ax`, or `\\k` as malformed commands.

**Rule:** after a row separator `\\`, insert a newline before the next row begins.

The same rule applies to matrices and other multiline environments.

---

## 6. Long derivations: use a multiline alignment block

For long derivations, use a multiline alignment environment only inside display mathematics.

Prefer:

```markdown
$$
\begin{aligned}
v(t) &= \frac{dx}{dt} \\
     &= v_0 + at
\end{aligned}
$$
```

Do not place `aligned`, `align`, `cases`, or matrix environments inside single-dollar inline math.

Use multiline environments only when they improve readability.

---

## 7. Avoid macros that GitHub rejects in this repository

The GitHub renderer used here has rejected some otherwise valid LaTeX/KaTeX commands.

Avoid:

```text
\operatorname{...}
\text{...}
\boxed{...}
\color{...}
```

Use simpler alternatives.

Instead of:

```text
\operatorname{proj}_v u
```

use:

```text
\mathrm{proj}_v\,u
```

Instead of:

```text
30\text{ cm}
```

use:

```text
30\,\mathrm{cm}
```

Instead of:

```text
z=\text{const}
```

use:

```text
z=\mathrm{const}
```

When ordinary prose is sufficient, move the words outside the mathematical environment rather than forcing them into LaTeX.

---

## 8. Do not use multiline environments inside inline math

This is a common GitHub rendering failure.

Incorrect:

```markdown
1. $\begin{cases}x+y=2,\\x-y=0\end{cases}$
```

Correct:

```markdown
**System 1**

$$
\begin{cases}
x+y=2, \\
x-y=0.
\end{cases}
$$
```

The same rule applies to:

- `cases`,
- `pmatrix`,
- `aligned` / `align`,
- other multiline environments.

---

## 9. Keep LaTeX commands visually separated from following content

A double backslash is a row separator. It must not accidentally become the beginning of another command.

Risky source:

```text
...,\\2,...
...,\\x,...
...,\\ax,...
...,\\k,...
```

Safe source:

```text
..., \\
2, ...

..., \\
x+1, ...
```

This rule is especially important in `cases`, matrices, and equation systems.

---

## 10. Recommended safe patterns

### Short inline expression

```markdown
Let $x\neq 0$.
```

### Display equation

```markdown
$$
\lim_{x\to0}\frac{\sin x}{x}=1
$$
```

### Matrix

```markdown
$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}
$$
```

### Piecewise function

```markdown
$$
f(x)=
\begin{cases}
x^2, & x\ge0, \\
ax, & x<0.
\end{cases}
$$
```

### Several systems in one exercise

Do not put them into numbered-list items as inline formulas. Give each system a short text label and a separate display block:

```markdown
**System 1**

$$
\begin{cases}
x+y=2, \\
x-y=0.
\end{cases}
$$

**System 2**

$$
\begin{cases}
x+y=2, \\
2x+2y=4.
\end{cases}
$$
```

---

## 11. Final rendering checklist

Before committing a Markdown exercise sheet, check all of the following:

- [ ] Inline mathematics uses only `$...$`.
- [ ] Display mathematics uses only `$$...$$`.
- [ ] Every `$$` delimiter is on its own line.
- [ ] There is an empty line before and after every display block.
- [ ] No `\\(...\\)` or `\\[...\\]` remains.
- [ ] Matrices use `pmatrix`.
- [ ] Matrix rows are written on separate lines and end with `\\`.
- [ ] `cases` rows are written on separate lines and end with `\\`.
- [ ] No multiline environment is placed inside single-dollar inline math.
- [ ] No row separator is glued to the next token, such as `\\2`, `\\x`, `\\ax`, or `\\k`.
- [ ] No `\operatorname`, `\text`, `\boxed`, or `\color` remains.
- [ ] Units and short labels inside formulas use simple forms such as `\mathrm{cm}`.
- [ ] The final file has been visually checked in GitHub's rendered view.

If a formula renders correctly in another editor but GitHub displays red text or literal LaTeX source, simplify the syntax and follow the safe patterns above rather than relying on editor-specific LaTeX support.

---

## 12. Never put a bare equals sign on its own Markdown line

Inside a display-math block, avoid writing a derivation like this:

```markdown
$$
\det A
=
ad-bc
=
1
$$
```

A line containing only `=` can be interpreted by GitHub's Markdown parser as Setext-heading syntax and may break the surrounding math block.

Use one of these safer forms instead:

```markdown
$$
\det A = ad-bc = 1
$$
```

or, for a longer derivation:

```markdown
$$
\begin{aligned}
\det A &= ad-bc \\
       &= 1
\end{aligned}
$$
```

**Rule:** never leave `=`, `-`, or similar Markdown-significant punctuation alone on a line inside a display-math block.

Add this to the pre-commit check:

- [ ] No line inside a `$$...$$` block consists only of `=`.

---

## 13. Never use a single `$` as a block delimiter

A display block must start and end with exactly `$$`.

Incorrect:

```markdown
$
A^{-1}=
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$
```

Incorrect:

```markdown
$
\det A=1
$
```

Correct:

```markdown
$$
A^{-1}=
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$
```

A line containing only one dollar sign is never valid for display mathematics in these repository notes.

Add these checks before every commit:

- [ ] There is no line containing only a single `$`.
- [ ] The number of standalone `$$` delimiter lines is even.
- [ ] Every display block opens with `$$` and closes with `$$`.
