## Custom Div Class Markdown Extension

FORKED WITH <3 from https://github.com/exaroth/mdx_custom_span_class

This is a simple extension for Python-Markdown library, which allows adding div elements with custom class. Great for alert boxes and such.

The syntax is:
```
!!!<class name>
<text to be wrapped>
!!!
```
For instance:

```shell
!!!alert-info
This is some things about stuff
!!!
```
will return

```html
<div class="alert-info">This is some things about stuff</div>
```


### Installation

```shell
pip install git+git://github.com/trek10inc/mdx_custom_div_class.git
```

### Usage

```python
import markdown

md = markdown.Markdown(extensions=["custom_div_class"])
md.convert("!!!<class name>
              <text to be wrapped>
            !!!")

```

