[![Build Status](https://travis-ci.org/RobDWaller/html_parse.svg?branch=master)](https://travis-ci.org/RobDWaller/html_parse) [![codecov](https://codecov.io/gh/RobDWaller/html_parse/branch/master/graph/badge.svg)](https://codecov.io/gh/RobDWaller/html_parse) [![Maintainability](https://api.codeclimate.com/v1/badges/d43c3780ccf78820c5b7/maintainability)](https://codeclimate.com/github/RobDWaller/gingerfy/maintainability)
# Python HTML Parse

Parse HTML strings in to a value object that can output JSON and offers a number of helper methods.

## Usage

```python
import html_parse

result = html_parse.parse('<html><title>Hello World</title></html>')

print(result.get_title())
# Output: Hello World

print(result.get_json())
# Output: {['title': 'Hello World']}
```

### Methods available on Parse object

```python
get_title() -> str

get_html_data() -> array

get_json() -> str
```

## Author

[RobDWaller](https://twitter.com/RobDWaller)
