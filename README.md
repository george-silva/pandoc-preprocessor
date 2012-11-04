pandoc-preprocessor
===================

# Why?

I needed a preprocessor that could navigate into markdown/latex ```\include``` instruction and would concatenate all
of them in a single document, that would be then, generated to latex/pdf using pandoc.

# Features

At the time, I only have one preprocessor routine, that is the \include command in latex.

# How to use

```bash
python preprocessor.py "path_to_origin_file" ["path_to_destination_file"]
```

# Example

Imagine that you have the following markdown file, called index.md:

```
Title
=====

Some text here

\include{chapter01.md}

\include{chapter02.md}
```

And, chapter01.md:

```
Chapter 01
==========

Here's the lovely story of the snow-white.
```

And, chapter02.md:

```
Chapter 02
==========

Here's the chapter 2.
```

If you use the preprocessor, like this:

```bash
python preprocessor.py home/your_user/book/index.md
```

The preprocessor will produce the following file, named acumulado.md:

```
Title
=====

Some text here

Chapter 01
==========

Here's the lovely story of the snow-white.

Chapter 02
==========

Here's the chapter 2.
```