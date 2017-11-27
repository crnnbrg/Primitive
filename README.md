# Primitive

> A primitive news feed is very simple application that allows users to post information to a feed and also view information on the feed


## Table of Contents

- [Demo](#demo)
- [Technologies used](#technologies-used)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [License](#license)


## Demo

[Showterm](http://showterm.io/ccb1d56f02e8ffec5143a#fast)

## Technologies used

`Python` `Click` `Requests`

## Install

1. Clone the repo
```
$ git clone [URL]
```

2. Create a virtual environment and activate it
```
$ virtualenv venv && source ./venv/bin/activate
```

3. Install dependencies
```
$ pip install --editable .
$ pip install requests
```

## Usage

- Creating a new post:
```
$ primefeed post <title> <body>
```

- Viewing posts from the feed:
```
$ primefeed view_feed
```

- Viewing a post's comments:
```
$ primefeed view_comments <postId>
```

- Submitting a comment to a post.
```
$ primefeed comment <postId> <title> <body>
```

- Access the help menu:
```
$ primefeed --help
```

## Maintainers

[@joewachira](https://github.com/joewachira) [@dorismugah](https://github.com/daurice) [@Kalela](https://github.com/Kalela) [@paulkariukirimiru](https://github.com/PaulKariukiRimiru) [@edwardmudaida](https://github.com/EdwardMudaida)

PRs accepted.

## License

MIT © 2017 Joe Wachira
