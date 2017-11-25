# Primitive

> A primitive news feed is very simple application that allows users to post information to a feed and also view information on the feed


## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [License](#license)


## Install

1. Clone the repo
```
$ git clone [URL]
```

2. Create a virtual environment
```
virtualenv venv
```

3. Install dependencies
```
pip install --editable .
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

- Access the help menu:
```
$ primefeed --help
```

## Maintainers

[@joewachira](https://github.com/joewachira) [@Kalela](https://github.com/Kalela) [@paulkariukirimiru](https://github.com/PaulKariukiRimiru) [@edwardmudaida](https://github.com/EdwardMudaida)

PRs accepted.

## License

MIT © 2017 Joe Wachira