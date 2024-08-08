# Markdown footnote support

It is actually one of the markdown extra feature [^markdownExtraFeature]
[^markdownExtraFeature]: <https://en.wikipedia.org/wiki/Markdown#Markdown_Extra>

> Markdown Extra is a lightweight markup language based on Markdown implemented in PHP (originally), Python and Ruby. It adds the following features that are not available with regular Markdown:
>
> - Markdown markup inside HTML blocks
> - Elements with id/class attribute
> - "Fenced code blocks" that span multiple lines of code
> - Tables
> - Definition lists
> - Footnotes
> - Abbreviations
>
> Markdown Extra is supported in some content management systems such as Drupal, Grav (CMS) and TYPO3.

---

[toc]

## Better reference

It is the footnotes supporting in Markdown fields [^footnotesInMarkdownFields]
It gives the markdown a better reference option, the official example is
[^footnotesInMarkdownFields]: <https://github.blog/changelog/2021-09-30-footnotes-now-supported-in-markdown-fields/>

```markdown
Footnotes let you reference relevant information without disrupting the flow of what you're trying to say:
Here is a simple footnote[^1]. With some additional text after it.

[^1]: some-reference-url

You can now use footnote syntax in any Markdown field!
Footnotes are displayed as superscript links.
Click them to jump to their referenced information, displayed in a new section at the bottom of the document.
```

Moreover, it supports defining the label for longer notes other than numbers.
In the following example, the `footnotesInMarkdownFields` plays as the long note.

```markdown
Footnotes now supported in Markdown fields [^footnotesInMarkdownFields]
[^footnotesInMarkdownFields]: <https://github.blog/changelog/2021-09-30-footnotes-now-supported-in-markdown-fields/>
```

![footnotes_in_markdown](./asset/footnotes_in_markdown.gif)

## Easier for summary

Think about it, if my writing contains several markdown files.
I can walk through them and fetch out the reference marks for summary.
For the purpose, I have to carefully assign the note for the reference to make them readable in the summary.
Maybe, some LLM AI can do it better for me.
